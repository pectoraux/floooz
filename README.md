# Floooz

Persistent personal AI agent platform.

## Fresh-agent start

This repository is the source of truth. No prior conversation is required.

**Read first:**

1. [`AGENTS.md`](AGENTS.md)
2. [`spec/development-state/program-state.json`](spec/development-state/program-state.json)
3. [`spec/architecture-lock.md`](spec/architecture-lock.md)
4. [`spec/architecture.md`](spec/architecture.md)
5. [`spec/requirements.md`](spec/requirements.md)
6. [`spec/work-items.md`](spec/work-items.md)
7. [`spec/work-orders.md`](spec/work-orders.md)
8. [`spec/dependency-graph.md`](spec/dependency-graph.md)
9. [`docs/implementation/IMPLEMENTATION-GUIDE.md`](docs/implementation/IMPLEMENTATION-GUIDE.md)

For Android, also read [`GEMINI.md`](GEMINI.md) and [`docs/android/ANDROID-IMPLEMENTATION.md`](docs/android/ANDROID-IMPLEMENTATION.md).

For WorkflowOS, also read [`docs/integrations/WORKFLOWOS.md`](docs/integrations/WORKFLOWOS.md).

## Architecture

The durable product is the Agent: identity + personality + owner model + memory + capabilities + policies + relationships + accumulated behavior. Models, devices, renderers and external workflow systems are replaceable integrations.

WorkflowOS remains the workflow execution authority. Floooz is the agent-facing integration boundary and must not duplicate WorkflowOS internals.