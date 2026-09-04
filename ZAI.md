# Z.ai Agent Entry Point

Treat this GitHub repository as the only source of truth. No prior conversation is required.

## Mandatory first read

1. `AGENTS.md`
2. `spec/implementation-roadmap.md` — frozen roadmap/progress authority
3. `spec/implementation-map.md` — detailed roadmap/contracts map
4. `spec/development-state/program-state.json` — machine-readable progress state
5. `spec/architecture-lock.md`
6. `spec/architecture.md`
7. `spec/requirements.md`
8. `spec/work-items.md`
9. `spec/work-orders.md`
10. `spec/dependency-graph.md`
11. `docs/implementation/IMPLEMENTATION-GUIDE.md`

## WorkflowOS

WorkflowOS is an external execution authority. Floooz may discover, bind/install, invoke, observe and present WorkflowOS workflows. Never implement a competing WorkflowOS executor, state machine, verification authority, or workflow database inside Floooz.

## Work selection

Select only a dependency-eligible FZ work item from program state and confirm it against the frozen roadmap. Read the work order, inspect the repository, implement the smallest conforming change, and produce objective acceptance evidence.

## Authority and safety

LLM output is advisory. It cannot authorize side effects, declare workflow completion, or become authoritative durable state. Every side effect must pass the capability and policy boundary. PostgreSQL is authoritative application state; Redis/process memory is not.

## Completion protocol

Update `spec/development-state/program-state.json` and `spec/implementation-roadmap.md` together after acceptance. One FZ item per branch/PR. If the repository does not specify something needed for implementation, do not reconstruct it from prior conversation; use the repository's governed change process.
