# Floooz Detailed Implementation Map

**Status:** FROZEN SUPPORTING ARTIFACT
**Canonical roadmap:** `spec/implementation-roadmap.md`
**Machine progress authority:** `spec/development-state/program-state.json`

This document contains the detailed implementation mapping behind the canonical roadmap. It is not a second progress authority. Statuses are authoritative in `program-state.json`; the same statuses are rendered in `implementation-roadmap.md`.

## Product execution model

```text
Reality / user input
        ↓
Perception + device signals
        ↓
Evidence / durable events
        ↓
Memory + owner model
        ↓
Decision / model routing / capability resolution
        ↓
Policy
        ↓
Action / external capability
        ↓
Observable result / evidence
        ↓
Presence / user-facing presentation
        ↓
Feedback
        ↓
Memory + owner-model + evolution updates
```

## Authority map

| Concern | Authority |
|---|---|
| Frozen architecture invariants | `spec/architecture-lock.md` |
| Product requirements | `spec/requirements.md` |
| Work-item scope | `spec/work-items.md` + selected section of `spec/work-orders.md` |
| Dependency eligibility | `spec/dependency-graph.md` + `program-state.json` |
| Implementation sequencing/progress | `spec/implementation-roadmap.md` + synchronized `program-state.json` |
| Detailed API/domain contracts | `spec/api-contracts.md` + `spec/architecture.md` |
| Workflow definitions/state/execution/verification/artifacts | WorkflowOS |
| Device-local execution | device runtime, subject to server policy |
| Public agent interoperability | A2A boundary |
| Tool/data interoperability | MCP boundary |

## FZ implementation streams

### Foundation

`FZ-001` repository/bootstrap → `FZ-002` domain IDs → `FZ-003` persistence → `FZ-004` events → `FZ-006` API → `FZ-007` observability.

`FZ-005` configuration/secrets branches from FZ-001.

### Identity / memory

`FZ-008` agent lifecycle → `FZ-009` genome; FZ-008 also enables `FZ-010` identity, `FZ-011` personality, `FZ-015` memory, `FZ-036` sessions and `FZ-042` embodiment.

Identity/personality: `FZ-010 + FZ-011 → FZ-012 → FZ-013 → FZ-014`.

Memory: `FZ-015 → FZ-016 → FZ-017 → FZ-018 → FZ-019`.

### Policy / capabilities

`FZ-001 → FZ-020 → FZ-021`.

`FZ-020 → FZ-022 → FZ-023 → FZ-024`.

`FZ-021 + FZ-024 → FZ-025 → FZ-026`.

### WorkflowOS integration

`FZ-006 + FZ-020 → FZ-027 → FZ-028`.

`FZ-028 + FZ-026 → FZ-029 → FZ-030 → FZ-031 → FZ-032`.

Floooz only discovers, binds, invokes, observes and presents WorkflowOS. It never duplicates WorkflowOS workflow execution/state/verification authority.

### Devices / realtime

`FZ-006 → FZ-033 → FZ-034 → FZ-035`.

`FZ-008 → FZ-036 → FZ-037`.

`FZ-036 → FZ-038 → FZ-039`.

`FZ-006 → FZ-040`.

`FZ-037 + FZ-040 → FZ-041`.

### Embodiment / extensions

`FZ-008 → FZ-042 → FZ-043 → FZ-044`.

`FZ-020 + FZ-022 → FZ-045 → FZ-046`.

### Social / evolution

`FZ-008 + FZ-006 → FZ-047 → FZ-048`.

`FZ-013 + FZ-014 → FZ-049`.

`FZ-040 + FZ-049 → FZ-050`.

## Cross-cutting invariants

1. No production side effect before the capability/policy execution gateway exists and is enforced.
2. No LLM output is authoritative for permissions, durable state, or workflow completion.
3. WorkflowOS remains external execution authority.
4. PostgreSQL is authoritative Floooz state; Redis/cache/process memory is not.
5. Realtime sessions are ephemeral; agent identity and memory are durable.
6. Raw camera/microphone/screen media stays local by default.
7. Semantic device and embodiment APIs are preferred over pixel/renderer-specific contracts.
8. Extensions are sandboxed and least-privileged.
9. One FZ work item per branch/PR.
10. A work item is complete only with objective acceptance evidence.

## Fresh-agent completion loop

```text
read roadmap + program state
        ↓
choose dependency-eligible FZ item
        ↓
read work order + contracts
        ↓
inspect repository
        ↓
implement smallest conforming change
        ↓
run tests/static/security/privacy checks
        ↓
record acceptance evidence
        ↓
synchronize program state + implementation roadmap
        ↓
PR
```
