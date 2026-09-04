# Z.ai Agent Entry Point

Treat this GitHub repository as the only source of truth. No prior conversation is required.

## Mandatory first read

1. `AGENTS.md`
2. `spec/implementation-map.md`
3. `spec/development-state/program-state.json`
4. `spec/architecture-lock.md`
5. `spec/architecture.md`
6. `spec/requirements.md`
7. `spec/work-items.md`
8. `spec/work-orders.md`
9. `spec/dependency-graph.md`
10. `docs/implementation/IMPLEMENTATION-GUIDE.md`

## WorkflowOS

WorkflowOS is an external execution authority. Floooz may discover, bind/install, invoke, observe and present WorkflowOS workflows. Never implement a competing WorkflowOS executor, state machine, verification authority, or workflow database inside Floooz.

## Work selection

Select only a dependency-eligible FZ work item from program state. Read the corresponding work-order section, inspect the repository, implement the smallest conforming change, verify it, and record objective evidence.

## Authority and safety

LLM output is advisory. It cannot authorize side effects, declare workflow completion, or become authoritative durable state. Every side effect must pass the capability and policy boundary. PostgreSQL is authoritative application state; Redis/process memory is not.

## Completion protocol

Update `spec/development-state/program-state.json` and the frozen human-readable roadmap `spec/implementation-map.md` together after acceptance. One FZ item per branch/PR. If the repository does not specify something needed for implementation, do not reconstruct it from memory of an earlier conversation; raise a repository-native change proposal instead.
