# FLOOOZ IMPLEMENTATION ROADMAP

**Status:** FROZEN
**Authority:** human-readable implementation sequencing and progress
**Machine state:** `spec/development-state/program-state.json`
**Detailed contracts:** `spec/implementation-map.md`

```text
FLOOOZ AGENT ENGINEER
                    Reality → Evidence → Knowledge → Decision → Action → Presence → Evolution

                                      ┌──────────────────────────┐
                                      │        FZ-001            │
                                      │ Repo / Runtime Bootstrap │
                                      │         STANDARD         │
                                      │          🟦 READY       │
                                      └────────────┬─────────────┘
                                                   │
                       ┌───────────────────────────┼───────────────────────────┐
                       │                           │                           │
                       ▼                           ▼                           ▼
              ┌────────────────┐          ┌────────────────┐          ┌────────────────┐
              │   FZ-002/003   │          │    FZ-005      │          │    FZ-020      │
              │ Domain + DB    │          │ Config/Secrets│          │ Permission     │
              │   STANDARD     │          │   STANDARD     │          │    CRITICAL    │
              │   ⬜ BLOCKED   │          │   ⬜ BLOCKED   │          │   ⬜ BLOCKED   │
              └───────┬────────┘          └────────────────┘          └───────┬────────┘
                      │                                                        │
                      ▼                                                        ▼
              ┌────────────────┐                                      ┌────────────────┐
              │   FZ-004/006   │                                      │    FZ-021      │
              │ Events + API   │                                      │ Autonomy       │
              │   STANDARD     │                                      │    CRITICAL    │
              │   ⬜ BLOCKED   │                                      │   ⬜ BLOCKED   │
              └───────┬────────┘                                      └───────┬────────┘
                      │                                                        │
          ┌───────────┼───────────────┬──────────────────┐                    │
          ▼           ▼               ▼                  ▼                    │
   ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐                │
   │ FZ-007     │ │ FZ-008     │ │ FZ-033     │ │ FZ-040     │                │
   │ Observab.  │ │ Agent      │ │ Devices    │ │ Model      │                │
   │ STANDARD   │ │ Lifecycle  │ │ Registry   │ │ Router     │                │
   │ ⬜ BLOCKED │ │ STANDARD   │ │ STANDARD   │ │ CRITICAL   │                │
   └────────────┘ │ ⬜ BLOCKED │ │ ⬜ BLOCKED │ │ ⬜ BLOCKED │                │
                  └─────┬──────┘ └─────┬──────┘ └────────────┘                │
                        │              │                                      │
               ┌────────┼───────┐      ▼                                      │
               ▼        ▼       ▼  ┌────────────┐                             │
        ┌────────────┐ ┌────────────┐│ FZ-034     │                             │
        │ FZ-009     │ │ FZ-015     ││ Device Caps│                             │
        │ Genome     │ │ Memory     ││ STANDARD   │                             │
        │ CRITICAL   │ │ CRITICAL   ││ ⬜ BLOCKED │                             │
        │ ⬜ BLOCKED │ │ ⬜ BLOCKED │└─────┬──────┘                             │
        └──────┬─────┘ └──────┬─────┘      │                                  │
               │              ▼            ▼                                  │
        ┌──────┴─────┐ ┌────────────┐ ┌────────────┐                           │
        │ FZ-010/011 │ │ FZ-016     │ │ FZ-035     │                           │
        │ Identity + │ │ Memory     │ │ Device     │                           │
        │ Personality│ │ Retrieval  │ │ Execution  │                           │
        │ STANDARD   │ │ CRITICAL   │ │ CRITICAL   │                           │
        │ ⬜ BLOCKED │ │ ⬜ BLOCKED │ │ ⬜ BLOCKED │                           │
        └──────┬─────┘ └──────┬─────┘ └────────────┘                           │
               ▼              ▼                                               │
        ┌────────────┐ ┌────────────┐                                         │
        │ FZ-012     │ │ FZ-017     │                                         │
        │ Behavioral │ │ Memory     │                                         │
        │ Rules      │ │ Consolid.  │                                         │
        │ STANDARD   │ │ CRITICAL   │                                         │
        │ ⬜ BLOCKED │ │ ⬜ BLOCKED │                                         │
        └──────┬─────┘ └──────┬─────┘                                         │
               ▼              ▼                                               │
        ┌────────────┐ ┌────────────┐                                         │
        │ FZ-013     │ │ FZ-018/019 │                                         │
        │ Owner      │ │ Correction │                                         │
        │ Model      │ │ + Audit    │                                         │
        │ CRITICAL   │ │ CRITICAL   │                                         │
        │ ⬜ BLOCKED │ │ ⬜ BLOCKED │                                         │
        └──────┬─────┘ └────────────┘                                         │
               ▼                                                               │
        ┌────────────┐                                                         │
        │ FZ-014     │                                                         │
        │ Preference │                                                         │
        │ Evidence   │                                                         │
        │ CRITICAL   │                                                         │
        │ ⬜ BLOCKED │                                                         │
        └──────┬─────┘                                                         │
               └────────────────────┬──────────────────────────────────────────┘
                                    ▼
                           ┌──────────────────┐
                           │    FZ-022 →      │
                           │ Capability       │
                           │ Domain →         │
                           │ Resolver →       │
                           │ Planning         │
                           │ FZ-022/023/024   │
                           │ CRITICAL         │
                           │ ⬜ BLOCKED       │
                           └────────┬─────────┘
                                    │
                                    ▼
                           ┌──────────────────┐
                           │     FZ-025       │
                           │ Policy-Enforced  │
                           │ Execution Gateway│
                           │     CRITICAL     │
                           │   ⬜ BLOCKED     │
                           └────────┬─────────┘
                                    │
                                    ▼
                           ┌──────────────────┐
                           │     FZ-026       │
                           │ Capability       │
                           │ Bindings         │
                           │     STANDARD     │
                           │   ⬜ BLOCKED     │
                           └────────┬─────────┘
                                    │
                                    ▼
                     ┌──────── WORKFLOWOS INTEGRATION ────────┐
                     │                                         │
                     │ FZ-027 → FZ-028 → FZ-029 → FZ-030      │
                     │ adapter    discovery   install  invoke  │
                     │   ⬜          ⬜         ⬜       ⬜     │
                     │                      │                  │
                     │                      ▼                  │
                     │                  FZ-031 → FZ-032        │
                     │                  observe    evidence    │
                     │                     ⬜         ⬜         │
                     └─────────────────────┬───────────────────┘
                                           │
            ┌──────────────────────────────┼─────────────────────────────┐
            │                              │                             │
            ▼                              ▼                             ▼
   ┌─────────────────┐          ┌─────────────────┐            ┌─────────────────┐
   │ FZ-036 → FZ-037 │          │ FZ-038 → FZ-039 │            │ FZ-042 → FZ-043 │
   │ Sessions         │          │ Perception      │            │ Embodiment       │
   │ → Transport      │          │ → Reflex        │            │ → Performance   │
   │ STANDARD        │          │ CRITICAL        │            │ HIGH_ASSURANCE  │
   │ ⬜ → ⬜          │          │ ⬜ → ⬜          │            │ ⬜ → ⬜           │
   └────────┬────────┘          └─────────────────┘            └────────┬────────┘
            │                                                             ▼
            ▼                                                     ┌─────────────────┐
   ┌─────────────────┐                                          │    FZ-044       │
   │    FZ-041       │                                          │ Semantic Anim.  │
   │ Voice / Realtime │                                          │ SDK             │
   │    CRITICAL     │                                          │ HIGH_ASSURANCE  │
   │   ⬜ BLOCKED    │                                          │ ⬜ BLOCKED      │
   └─────────────────┘                                          └────────┬────────┘
                                                                         │
                                                                         ▼
                                                               ┌─────────────────┐
                                                               │    FZ-045       │
                                                               │ Extension       │
                                                               │ Runtime         │
                                                               │    CRITICAL     │
                                                               │  ⬜ BLOCKED      │
                                                               └────────┬────────┘
                                                                        ▼
                                                               ┌─────────────────┐
                                                               │    FZ-046       │
                                                               │ Extension       │
                                                               │ Policy Bridge   │
                                                               │    CRITICAL     │
                                                               │  ⬜ BLOCKED      │
                                                               └─────────────────┘

                             SOCIAL / EVOLUTION

                  ┌─────────────────┐              ┌─────────────────┐
                  │    FZ-047       │              │    FZ-049       │
                  │ Social Identity │              │ Personality     │
                  │ + A2A Boundary  │              │ Evolution       │
                  │    CRITICAL     │              │    CRITICAL     │
                  │  ⬜ BLOCKED     │              │  ⬜ BLOCKED     │
                  └────────┬────────┘              └────────┬────────┘
                           ▼                                ▼
                  ┌─────────────────┐              ┌─────────────────┐
                  │    FZ-048       │              │    FZ-050       │
                  │ Agent Relations │              │ Routing +       │
                  │ + Social Sess.  │              │ Personalization │
                  │ HIGH_ASSURANCE  │              │    CRITICAL     │
                  │  ⬜ BLOCKED     │              │  ⬜ BLOCKED     │
                  └─────────────────┘              └─────────────────┘
```

## Work-item status ledger

The ledger below is the compact progress tracker. The machine state is canonical for status values; this ledger MUST be synchronized whenever a status changes.

| Work item | Status | Assurance | Primary surface |
|---|---|---|---|
| FZ-001 | 🟦 READY | STANDARD | repo/platform |
| FZ-002 | ⬜ BLOCKED | STANDARD | domain |
| FZ-003 | ⬜ BLOCKED | STANDARD | persistence |
| FZ-004 | ⬜ BLOCKED | STANDARD | events |
| FZ-005 | ⬜ BLOCKED | STANDARD | config/security |
| FZ-006 | ⬜ BLOCKED | STANDARD | API |
| FZ-007 | ⬜ BLOCKED | STANDARD | observability |
| FZ-008 | ⬜ BLOCKED | STANDARD | agent |
| FZ-009 | ⬜ BLOCKED | CRITICAL | genome |
| FZ-010 | ⬜ BLOCKED | STANDARD | identity |
| FZ-011 | ⬜ BLOCKED | STANDARD | personality |
| FZ-012 | ⬜ BLOCKED | STANDARD | behavior |
| FZ-013 | ⬜ BLOCKED | CRITICAL | owner model |
| FZ-014 | ⬜ BLOCKED | CRITICAL | preference evidence |
| FZ-015 | ⬜ BLOCKED | CRITICAL | memory |
| FZ-016 | ⬜ BLOCKED | CRITICAL | retrieval |
| FZ-017 | ⬜ BLOCKED | CRITICAL | consolidation |
| FZ-018 | ⬜ BLOCKED | CRITICAL | correction |
| FZ-019 | ⬜ BLOCKED | HIGH_ASSURANCE | memory audit |
| FZ-020 | ⬜ BLOCKED | CRITICAL | permissions |
| FZ-021 | ⬜ BLOCKED | CRITICAL | autonomy |
| FZ-022 | ⬜ BLOCKED | HIGH_ASSURANCE | capabilities |
| FZ-023 | ⬜ BLOCKED | CRITICAL | resolver |
| FZ-024 | ⬜ BLOCKED | STANDARD | planning |
| FZ-025 | ⬜ BLOCKED | CRITICAL | execution gateway |
| FZ-026 | ⬜ BLOCKED | STANDARD | bindings |
| FZ-027 | ⬜ BLOCKED | HIGH_ASSURANCE | WorkflowOS adapter |
| FZ-028 | ⬜ BLOCKED | STANDARD | WorkflowOS discovery |
| FZ-029 | ⬜ BLOCKED | STANDARD | WorkflowOS install |
| FZ-030 | ⬜ BLOCKED | CRITICAL | WorkflowOS invocation |
| FZ-031 | ⬜ BLOCKED | HIGH_ASSURANCE | WorkflowOS observation |
| FZ-032 | ⬜ BLOCKED | HIGH_ASSURANCE | evidence presentation |
| FZ-033 | ⬜ BLOCKED | STANDARD | device registry |
| FZ-034 | ⬜ BLOCKED | STANDARD | device capabilities |
| FZ-035 | ⬜ BLOCKED | CRITICAL | device execution |
| FZ-036 | ⬜ BLOCKED | STANDARD | realtime sessions |
| FZ-037 | ⬜ BLOCKED | STANDARD | realtime transport |
| FZ-038 | ⬜ BLOCKED | CRITICAL | local perception |
| FZ-039 | ⬜ BLOCKED | CRITICAL | reflexes |
| FZ-040 | ⬜ BLOCKED | CRITICAL | model routing |
| FZ-041 | ⬜ BLOCKED | CRITICAL | voice |
| FZ-042 | ⬜ BLOCKED | HIGH_ASSURANCE | embodiment |
| FZ-043 | ⬜ BLOCKED | HIGH_ASSURANCE | behavior director |
| FZ-044 | ⬜ BLOCKED | HIGH_ASSURANCE | animation SDK |
| FZ-045 | ⬜ BLOCKED | CRITICAL | extension runtime |
| FZ-046 | ⬜ BLOCKED | CRITICAL | extension policy |
| FZ-047 | ⬜ BLOCKED | CRITICAL | social/A2A |
| FZ-048 | ⬜ BLOCKED | HIGH_ASSURANCE | relationships |
| FZ-049 | ⬜ BLOCKED | CRITICAL | personality evolution |
| FZ-050 | ⬜ BLOCKED | CRITICAL | routing learning |

## Update protocol

After each work item is accepted, update the corresponding row in this ledger and the matching item in `spec/development-state/program-state.json` in the same change. Add PR/commit/evidence references to the program state. Recompute dependency eligibility before selecting the next item.

A status is not allowed to advance merely because an agent claims completion. `✅ FINAL` requires the work-order acceptance criteria and objective repository/CI evidence.

## Freeze rule

This roadmap is frozen as an implementation-governance artifact. It may only change through a governed roadmap/dependency update that preserves the architecture lock and records why sequencing or scope changed. It is authoritative for implementation progress and sequencing, but never overrides `spec/architecture-lock.md`, requirements, dependency rules, or WorkflowOS's external authority.
