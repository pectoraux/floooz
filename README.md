# Floooz

Persistent personal AI agent platform.

## Repository authority

This GitHub repository is the sole source of truth. No prior conversation, chat export, or external planning artifact is required to implement the system.

### Read first — all agents

1. [`AGENTS.md`](AGENTS.md) — mandatory operating contract
2. [`spec/implementation-map.md`](spec/implementation-map.md) — frozen human-readable roadmap and progress authority
3. [`spec/development-state/program-state.json`](spec/development-state/program-state.json) — canonical machine-readable progress state
4. [`spec/architecture-lock.md`](spec/architecture-lock.md) — frozen architecture invariants
5. [`spec/architecture.md`](spec/architecture.md) — architecture description
6. [`spec/requirements.md`](spec/requirements.md) — requirements
7. [`spec/work-items.md`](spec/work-items.md) — work-item scope
8. [`spec/work-orders.md`](spec/work-orders.md) — work-item implementation instructions
9. [`spec/dependency-graph.md`](spec/dependency-graph.md) — dependency authority
10. [`docs/implementation/IMPLEMENTATION-GUIDE.md`](docs/implementation/IMPLEMENTATION-GUIDE.md) — implementation protocol

### Specialist entry points

Android Studio Gemini: [`GEMINI.md`](GEMINI.md) and [`docs/android/ANDROID-IMPLEMENTATION.md`](docs/android/ANDROID-IMPLEMENTATION.md)

Z.ai: [`ZAI.md`](ZAI.md)

WorkflowOS integration: [`docs/integrations/WORKFLOWOS.md`](docs/integrations/WORKFLOWOS.md) and [`docs/integrations/WORKFLOWOS-BASELINE.md`](docs/integrations/WORKFLOWOS-BASELINE.md)

## Implementation rule

Select work only from `spec/development-state/program-state.json` where all hard dependencies are satisfied. Read the corresponding work order and inspect the repository before coding. One FZ work item per branch/PR. Completion requires objective evidence and synchronized updates to program state and `spec/implementation-map.md`.

## Architecture

The durable product is the Agent: identity + personality + owner model + memory + capabilities + policies + relationships + accumulated behavior. Models, devices, renderers and external workflow systems are replaceable integrations.

WorkflowOS remains the workflow execution authority. Floooz is the agent-facing integration boundary and must not duplicate WorkflowOS internals.
