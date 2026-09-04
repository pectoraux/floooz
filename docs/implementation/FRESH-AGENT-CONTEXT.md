# Fresh Agent Context

A fresh architect or coding agent must be able to implement Floooz without conversation history.

## Product identity
Floooz is a persistent personal AI agent. The durable product is the agent identity plus personality, owner model, memory, capabilities, policies, relationships, and accumulated behavior—not a specific LLM, device, avatar, or workflow engine.

## Implementation strategy
Build in dependency order: foundation -> identity/personalization -> policy/capabilities -> WorkflowOS -> devices/realtime -> embodiment/extensions -> social/evolution.

## Critical ownership boundary
WorkflowOS is external authority for workflow definitions, execution, state, verification and artifacts. Floooz integrates with it and presents it through the agent. Never duplicate WorkflowOS internals.

## Runtime principle
Use deterministic reflexes for low-latency behaviors, local models for lightweight/private tasks, and larger cloud/frontier models only when complexity, context or quality requires them and policy permits.

## Device principle
Devices are clients/runtimes. They register capabilities and execute authorized actions. They are never authoritative for agent identity, memory, personality, permissions or workflow state.

## Developer platform principle
Extensions and avatar controls use semantic capability contracts. Renderer-specific details remain behind adapters.

## Fresh-agent rule
If a requirement is absent from this repository, do not invent it from memory or conversation. Identify the ambiguity and use the architecture-change process rather than silently changing architecture.