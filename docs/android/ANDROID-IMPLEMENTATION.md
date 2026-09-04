# Android Implementation Contract

Android is a device runtime, not authoritative agent infrastructure.

## Responsibilities

- secure device registration/revocation
- realtime session connectivity
- microphone/camera access only with Android/user permission
- local-first perception
- avatar/agent rendering
- policy-authorized device capabilities
- semantic UI/device capabilities where supported
- minimal offline continuity cache

## Forbidden

Android must not become the source of truth for agent identity, memory, personality, policy, permissions, or WorkflowOS execution.

## Suggested modules

```text
app
core:model
core:network
core:realtime
core:perception
core:permissions
core:device-capabilities
core:agent-rendering
feature:agent
feature:studio
feature:settings
```

Use Kotlin, coroutines/Flow, structured concurrency, secure storage and Android permission APIs. Prefer on-device ML for presence/gaze/voice activity. Server policy remains authoritative; client permission checks are defense in depth.

## Fresh Android agent rule

Read `GEMINI.md` and `AGENTS.md` before coding. Select only dependency-eligible FZ work items. Do not invent Android requirements from conversation history.