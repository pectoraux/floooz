# Floooz Requirements

## Product

Floooz is a persistent personal AI agent that can appear across digital screens, remember its owner, develop a useful personality, invoke installed WorkflowOS workflows, operate permitted devices, and present itself through configurable embodiments.

## Functional requirements

- Persistent agent creation/lifecycle.
- Studio configuration for identity, values, personality, voice, embodiment and autonomy.
- Durable long-term memory with inspection, correction, retraction and historical validity.
- Owner model learned from explicit preferences, corrections, successful interactions and workflow outcomes.
- Tiered local/edge/cloud/frontier model routing.
- Phone/laptop/desktop/TV/tablet/smart-display device runtimes.
- Local-first presence/gaze/speech/interruption perception.
- WorkflowOS discovery, install/binding, invocation, observation and authoritative result presentation; no duplicated workflow execution authority.
- Policy-controlled device actions and autonomy rules.
- Sandboxed extension platform with semantic avatar/device APIs.
- Renderer-independent embodiment and developer animation controls.
- Agent-to-agent discovery/collaboration via A2A boundary.
- Evidence-backed, reversible personality evolution and personalization.

## Non-functional requirements

Security: least privilege, scoped credentials, policy mediation, auditability.
Privacy: local-first perception; raw media cloud transfer requires explicit policy.
Reliability: idempotent side effects, durable state, reconnect/recovery.
Observability: correlation IDs across interaction, planning, capability, workflow/device execution and result.
Portability: provider/device/renderer implementations behind interfaces.
Testability: objective acceptance evidence for every work item.
Maintainability: explicit ownership boundaries; no WorkflowOS reimplementation.