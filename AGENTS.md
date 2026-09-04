# Floooz Agent Operating Contract

This repository is the sole source of truth for implementation. Assume no access to prior conversations.

## Read first
1. `spec/development-state/program-state.json`
2. `spec/architecture-lock.md`
3. `spec/architecture.md`
4. `spec/requirements.md`
5. `spec/work-items.md`
6. `spec/dependency-graph.md`
7. `docs/implementation/IMPLEMENTATION-GUIDE.md`
8. For WorkflowOS: `docs/integrations/WORKFLOWOS.md` and `docs/integrations/WORKFLOWOS-BASELINE.md`
9. For Android: `docs/android/ANDROID-IMPLEMENTATION.md` and `GEMINI.md`

## Frozen architecture
Do not change frozen invariants in an implementation PR. Architecture changes require the documented architecture-change process and a new immutable lock version.

## Work discipline
Implement one FZ work item per branch/PR. Do not start blocked work. Read the work order, inspect current code, implement the smallest conforming change, run objective verification, record evidence, and update durable program state.

## Authority
- PostgreSQL is authoritative Floooz application state.
- Redis/cache/process memory is never authoritative.
- LLM output is advisory, never permission authority, workflow-completion authority, or durable-state authority.
- WorkflowOS owns workflow definitions, workflow state, execution, verification, and artifacts.
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
program state -> eligible FZ item -> work order/contracts -> inspect code -> implement -> verify -> evidence -> state update -> PR
```
