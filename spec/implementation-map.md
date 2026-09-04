# Floooz Implementation Map

**Status:** FROZEN
**Role:** Human-readable implementation roadmap and progress authority
**Machine counterpart:** `spec/development-state/program-state.json`

This map is the canonical human-readable view of implementation progress. It MUST be updated after every completed, reverted, or blocked FZ work item. The machine-readable status in `spec/development-state/program-state.json` and this map must agree; disagreement is an invalid governed repository state and must be corrected before new work starts.

## Source-of-truth order

1. `spec/architecture-lock.md` — frozen architectural invariants
2. `spec/requirements.md` — product requirements
3. `spec/work-items.md` — work-item scope
4. `spec/dependency-graph.md` — dependency authority
5. `spec/development-state/program-state.json` — machine-readable work-item status
6. `spec/implementation-map.md` — human-readable roadmap/progress authority
7. `spec/work-orders.md` — implementation instructions for the selected work item

An implementation agent MUST NOT derive scope from chat history.

## Status legend

- `⬜ BLOCKED` — dependencies are incomplete
- `🟦 READY` — all hard dependencies satisfied; eligible to start
- `🔄 ACTIVE` — implementation in progress on an active branch/PR
- `✅ FINAL` — accepted, verified, and merged/finalized
- `⛔ BLOCKED` — blocked after starting due to an identified dependency or external condition
- `↩️ REWORK` — previously accepted work requires a governed corrective change

## Progress map

```text
FLOOOZ AGENT PLATFORM
                  Reality → Perception → Memory → Decision → Action → Presence → Evolution

                                      ┌───────────────────────┐
                                      │       FZ-001          │
                                      │ Repository / Bootstrap│
                                      │       STANDARD        │
                                      │       🟦 READY        │
                                      └───────────┬───────────┘
                                                  │
                         ┌────────────────────────┼────────────────────────┐
                         │                        │                        │
                         ▼                        ▼                        ▼
                ┌────────────────┐      ┌────────────────┐       ┌────────────────┐
                │    FZ-002      │      │    FZ-005      │       │    FZ-020      │
                │ Domain IDs     │      │ Config/Secrets │       │ Permission     │
                │    STANDARD    │      │    STANDARD    │       │    CRITICAL    │
                │   ⬜ BLOCKED    │      │   ⬜ BLOCKED    │       │   ⬜ BLOCKED    │
                └───────┬────────┘      └────────────────┘       └───────┬────────┘
                        │                                                 │
                        ▼                                                 ▼
                ┌────────────────┐                              ┌────────────────┐
                │    FZ-003      │                              │    FZ-021      │
                │ PostgreSQL     │                              │ Autonomy       │
                │    STANDARD    │                              │ Policy         │
                │   ⬜ BLOCKED    │                              │    CRITICAL    │
                └───────┬────────┘                              │   ⬜ BLOCKED    │
                        │                                       └───────┬────────┘
                        ▼                                               │
                ┌────────────────┐                                     │
                │    FZ-004      │                                     │
                │ Event Envelope │                                     │
                │    STANDARD    │                                     │
                │   ⬜ BLOCKED    │                                     │
                └───────┬────────┘                                     │
                        │                                               │
                        ▼                                               │
                ┌────────────────┐                                     │
                │    FZ-006      │                                     │
                │ API Foundation │                                     │
                │    STANDARD    │                                     │
                │   ⬜ BLOCKED    │                                     │
                └───────┬────────┘                                     │
                        │                                               │
               ┌────────┼────────┬─────────────┐                       │
               │        │        │             │                       │
               ▼        ▼        ▼             ▼                       ▼
          ┌─────────┐ ┌───────┐ ┌─────────┐ ┌─────────┐          ┌────────────────┐
          │ FZ-007  │ │FZ-008  │ │ FZ-033  │ │ FZ-040  │          │    FZ-022      │
          │ Health  │ │ Agent  │ │ Devices │ │ Model   │          │ Capability     │
          │ Observ. │ │ Life   │ │ Registry│ │ Router  │          │ Domain         │
          │ STANDARD│ │STANDARD│ │STANDARD │ │CRITICAL │          │ HIGH_ASSURANCE │
          │ ⬜      │ │ ⬜     │ │ ⬜      │ │ ⬜      │          │ ⬜ BLOCKED    │
          └─────────┘ └───┬───┘ └────┬────┘ └─────────┘          └───────┬─────────┘
                           │           │                                   │
                           ▼           ▼                                   ▼
                     ┌──────────┐ ┌──────────┐                     ┌────────────────┐
                     │ FZ-009   │ │ FZ-034   │                     │    FZ-023      │
                     │ Genome   │ │ Device   │                     │ Capability     │
                     │ Version  │ │ Caps     │                     │ Resolver       │
                     │ CRITICAL │ │ STANDARD │                     │    CRITICAL    │
                     │ ⬜       │ │ ⬜       │                     │   ⬜ BLOCKED    │
                     └────┬─────┘ └────┬─────┘                     └───────┬─────────┘
                          │             │                                   │
              ┌───────────┼──────────┐  ▼                                   ▼
              │           │          │┌──────────┐                    ┌────────────────┐
              ▼           ▼          ▼│ FZ-035   │                    │    FZ-024      │
        ┌──────────┐ ┌──────────┐ ┌────┴─────┐ │ Device   │                    │ Action         │
        │ FZ-010   │ │ FZ-011   │ │ FZ-015   │ │ Execute  │                    │ Planning      │
        │ Identity │ │Personality│ │ Memory   │ │ CRITICAL │                    │ STANDARD      │
        │ STANDARD │ │STANDARD  │ │ CRITICAL │ │ ⬜      │                    │ ⬜ BLOCKED    │
        └────┬─────┘ └────┬─────┘ └────┬─────┘ └──────────┘                    └───────┬─────────┘
             │              │              │                                             │
             └───────┬──────┘              ▼                                             │
                     ▼              ┌──────────┐                                         │
              ┌────────────┐        │ FZ-016   │                                         │
              │ FZ-012     │        │ Memory   │                                         │
              │ Behavioral │        │ Retrieval │                                         │
              │ Rules      │        │ CRITICAL │                                         │
              │ STANDARD   │        │ ⬜       │                                         │
              └────┬───────┘        └────┬─────┘                                         │
                   ▼                     │                                               │
              ┌────────────┐             ▼                                               │
              │ FZ-013     │       ┌──────────┐                                          │
              │ Owner Model│       │ FZ-017   │                                          │
              │ CRITICAL   │       │Consolid. │                                          │
              │ ⬜         │       │ CRITICAL │                                          │
              └────┬───────┘       │ ⬜       │                                          │
                   ▼                └────┬─────┘                                          │
              ┌────────────┐             ▼                                               │
              │ FZ-014     │       ┌──────────┐                                           │
              │ Preference │       │ FZ-018   │                                           │
              │ Evidence   │       │Correction│                                           │
              │ CRITICAL   │       │ CRITICAL │                                           │
              │ ⬜         │       │ ⬜       │                                           │
              └────────────┘       └────┬─────┘                                           │
                                          ▼                                               │
                                    ┌──────────┐                                           │
                                    │ FZ-019   │                                           │
                                    │ Memory   │                                           │
                                    │ Audit    │                                           │
                                    │ HIGH_AS  │                                           │
                                    │ ⬜       │                                           │
                                    └──────────┘                                           │
                                                                                         │
                         ┌───────────────────────────────────────────────────────────────┘
                         │
                         ▼
                ┌────────────────┐
                │    FZ-025      │
                │ Policy Enforced│
                │ Execution GW   │
                │    CRITICAL    │
                │   ⬜ BLOCKED   │
                └───────┬────────┘
                        │
                        ▼
                ┌────────────────┐
                │    FZ-026      │
                │ Capability     │
                │ Bindings       │
                │    STANDARD    │
                │   ⬜ BLOCKED   │
                └────────┬───────┘
                         │
                         ▼
                 ┌─────────────────── WORKFLOWOS ───────────────────┐
                 │                                                   │
                 │  FZ-027 → FZ-028 → FZ-029 → FZ-030 → FZ-031     │
                 │ Adapter   Discovery  Install   Invoke   Observe   │
                 │   🔴→🟦     ⬜        ⬜        ⬜       ⬜       │
                 │                          │                        │
                 │                          ▼                        │
                 │                       FZ-032                     │
                 │                Evidence Presentation             │
                 │                    HIGH_ASSURANCE                 │
                 │                       ⬜                           │
                 └────────────────────────┬───────────────────────────┘
                                          │
                     ┌────────────────────┼────────────────────┐
                     │                    │                    │
                     ▼                    ▼                    ▼
              ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
              │    FZ-036    │    │    FZ-038    │    │    FZ-042    │
              │ Realtime     │    │ Local        │    │ Embodiment   │
              │ Sessions     │    │ Perception   │    │ Contract     │
              │ STANDARD     │    │ CRITICAL     │    │ HIGH_ASSUR.  │
              │ ⬜           │    │ ⬜           │    │ ⬜           │
              └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
                     │                   │                   │
                     ▼                   ▼                   ▼
              ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
              │    FZ-037    │    │    FZ-039    │    │    FZ-043    │
              │ Realtime     │    │ Reflex       │    │ Performance  │
              │ Transport    │    │ Engine       │    │ Director     │
              │ STANDARD     │    │ CRITICAL     │    │ HIGH_ASSUR.  │
              │ ⬜           │    │ ⬜           │    │ ⬜           │
              └──────┬───────┘    └──────────────┘    └──────┬───────┘
                     │                                        │
                     ▼                                        ▼
              ┌──────────────┐                        ┌──────────────┐
              │    FZ-041    │                        │    FZ-044    │
              │ Voice /      │                        │ Semantic     │
              │ Realtime     │                        │ Animation SDK│
              │ CRITICAL     │                        │ HIGH_ASSUR.  │
              │ ⬜           │                        │ ⬜           │
              └──────────────┘                        └──────┬───────┘
                                                             │
                                                             ▼
                                                     ┌──────────────┐
                                                     │    FZ-045    │
                                                     │ Extension    │
                                                     │ Runtime      │
                                                     │ CRITICAL     │
                                                     │ ⬜           │
                                                     └──────┬───────┘
                                                            │
                                                            ▼
                                                     ┌──────────────┐
                                                     │    FZ-046    │
                                                     │ Extension    │
                                                     │ Policy Bridge │
                                                     │ CRITICAL     │
                                                     │ ⬜           │
                                                     └──────────────┘

                                 SOCIAL / MULTI-AGENT / EVOLUTION

                ┌────────────────┐                           ┌────────────────┐
                │    FZ-047      │                           │    FZ-049      │
                │ Social Identity│                           │ Personality    │
                │ + A2A Boundary │                           │ Evolution      │
                │    CRITICAL    │                           │    CRITICAL    │
                │   ⬜ BLOCKED   │                           │   ⬜ BLOCKED   │
                └───────┬────────┘                           └───────┬────────┘
                        │                                           │
                        ▼                                           ▼
                ┌────────────────┐                           ┌────────────────┐
                │    FZ-048      │                           │    FZ-050      │
                │ Relationships  │                           │ Routing +      │
                │ + Social       │                           │ Personalization│
                │ Sessions       │                           │ Learning       │
                │ HIGH_ASSURANCE │                           │    CRITICAL    │
                │   ⬜ BLOCKED   │                           │   ⬜ BLOCKED   │
                └────────────────┘                           └────────────────┘
```

## Implementation order

### Stage A — Repository and platform substrate

`FZ-001 → FZ-002 → FZ-003 → FZ-004 → FZ-006 → FZ-007`

`FZ-005` is parallel after `FZ-001`.

### Stage B — Identity, personalization, memory

`FZ-008 → FZ-009 → FZ-010/FZ-011 → FZ-012 → FZ-013 → FZ-014`

Memory stream:

`FZ-008 → FZ-015 → FZ-016 → FZ-017 → FZ-018 → FZ-019`

The identity/personality and memory streams may proceed in parallel where dependencies permit.

### Stage C — Authority and capabilities

`FZ-020 → FZ-021`

`FZ-020 → FZ-022 → FZ-023 → FZ-024`

`FZ-021 + FZ-024 → FZ-025 → FZ-026`

### Stage D — WorkflowOS integration

`FZ-027 → FZ-028 → FZ-029 → FZ-030 → FZ-031 → FZ-032`

No WorkflowOS workflow execution semantics are implemented locally.

### Stage E — Device and realtime presence

`FZ-006 → FZ-033 → FZ-034 → FZ-035`

`FZ-008 → FZ-036 → FZ-037 → FZ-041`

`FZ-036 → FZ-038 → FZ-039`

`FZ-006 → FZ-040`

`FZ-037 + FZ-040 → FZ-041`

### Stage F — Embodiment and developer platform

`FZ-008 → FZ-042 → FZ-043 → FZ-044`

`FZ-020 + FZ-022 → FZ-045 → FZ-046`

### Stage G — Agent network and evolution

`FZ-008 + FZ-006 → FZ-047 → FZ-048`

`FZ-013 + FZ-014 → FZ-049`

`FZ-040 + FZ-049 → FZ-050`

## Progress-update protocol

After a work item reaches `✅ FINAL`, the implementing agent MUST update both:

1. `spec/development-state/program-state.json`
2. this file's status marker for that work item

The update MUST include, where applicable:

- branch
- PR
- merge commit
- verification command(s)
- acceptance evidence location
- implementation notes affecting downstream work

A work item may not be marked `✅ FINAL` because an agent claims completion. Acceptance evidence must exist in the repository/CI or in the authoritative external system boundary.

## Authority rule

Once this roadmap is frozen, it is authoritative for implementation progress and sequencing. It does not override `spec/architecture-lock.md`, requirements, or WorkflowOS's own authority. If progress sequencing must change, the dependency graph and program state must be updated together and the reason recorded as a governed repository change.
