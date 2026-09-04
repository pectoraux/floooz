# Floooz Agent Operating Contract

This repository is the sole source of truth for implementation. Assume no access to prior conversations.

## Mandatory reading order

1. `README.md`
2. `spec/implementation-roadmap.md` — frozen visual roadmap and progress authority
3. `spec/implementation-map.md` — detailed roadmap/contracts map
4. `spec/development-state/program-state.json` — canonical machine state
5. `spec/architecture-lock.md`
6. `spec/architecture.md`
7. `spec/requirements.md`
8. `spec/work-items.md`
9. `spec/work-orders.md`
10. `spec/dependency-graph.md`
11. `docs/implementation/IMPLEMENTATION-GUIDE.md`

Then read the specialist contract for the surface being changed:

- WorkflowOS: `docs/integrations/WORKFLOWOS.md` and `docs/integrations/WORKFLOWOS-BASELINE.md`
- Android/Gemini: `GEMINI.md`, `docs/android/ANDROID-IMPLEMENTATION.md`, and `docs/android/FZ-ANDROID-WORKSTREAM.md`
- Z.ai: `ZAI.md`

## Frozen architecture

Do not change frozen invariants in an implementation PR. Architecture changes require the documented architecture-change process and a new immutable architecture-lock version.

## Roadmap authority

`spec/implementation-roadmap.md` is the frozen human-readable roadmap and progress authority. `spec/development-state/program-state.json` is its machine-readable counterpart. `spec/implementation-map.md` is the detailed supporting map. Every completed, reverted, or blocked work item must update the machine state and the roadmap consistently. A mismatch is an invalid governed repository state.

The roadmap controls implementation sequencing/progress only. It does not override architecture invariants, requirements, dependency rules, or WorkflowOS authority.

## Work discipline

Implement one FZ work item per branch/PR. Do not start blocked work. Read the selected work order, inspect current code, implement the smallest conforming change, run objective verification, record evidence, update durable program state and roadmap, then open/update the PR.

## Authority

- PostgreSQL is authoritative Floooz application state.
- Redis/cache/process memory is never authoritative.
- LLM output is advisory, never permission authority, workflow-completion authority, or durable-state authority.
- WorkflowOS owns workflow definitions, workflow state, execution, verification, and workflow artifacts.
- Every side effect passes through the policy/capability execution boundary.
- Extensions are sandboxed and least-privileged.

## WorkflowOS boundary

Floooz may discover, bind/install, invoke, observe, and present WorkflowOS workflows. It must not implement a second WorkflowOS executor, state machine, criterion evaluator, or authoritative workflow database. If an integration primitive is missing, fix WorkflowOS through its own governed implementation process.

## Privacy

Camera, microphone, gaze, presence, and screen perception are local-first. Raw media must not leave the device by default. Cloud analysis requires an explicit policy path.

## Realtime

Agents are durable; sessions are ephemeral. Long-term identity and memory must never depend solely on process memory or conversation context.

## Engineering invariants

Use typed contracts, idempotency for side effects, correlation IDs across async boundaries, explicit authorization, secure secret abstraction, structured observability, and objective acceptance evidence.

## Required loop

```text
roadmap/program state -> eligible FZ item -> work order/contracts -> inspect code -> implement -> verify -> evidence -> synchronized state/map update -> PR
```

## No-chat-history rule

If a design detail is not discoverable from repository artifacts, do not invent it from assumed prior conversation. Record the ambiguity as a repository issue/change proposal and follow the architecture-change/governance process where required.
