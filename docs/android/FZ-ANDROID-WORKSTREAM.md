# Android / Gemini FZ Workstream

This document is the Android-specific implementation index for fresh Android Studio Gemini agents. It does not create a separate Android roadmap. The authoritative order remains `spec/implementation-roadmap.md` + `spec/development-state/program-state.json`.

## Android-relevant work items

### Foundation consumed by Android

- `FZ-001` Repository/bootstrap contracts
- `FZ-002` Domain model and IDs
- `FZ-003` PostgreSQL persistence foundation (backend contract consumed by Android)
- `FZ-004` Event envelope and persistence
- `FZ-005` Configuration/secrets (backend boundary; mobile consumes scoped session credentials)
- `FZ-006` API foundation
- `FZ-007` Observability
- `FZ-008` Agent lifecycle

### Device/runtime implementation

- `FZ-033` Device registration — Android client participates in secure registration/revocation.
- `FZ-034` Device capability registry — Android advertises semantic capabilities.
- `FZ-035` Device execution gateway — Android executes only server-policy-authorized actions.
- `FZ-036` Realtime session lifecycle — Android creates/maintains/ends sessions.
- `FZ-037` Realtime transport — Android WebRTC/realtime transport implementation.
- `FZ-038` Local perception signal contract — Android local perception produces semantic signals.
- `FZ-039` Reflex engine — device-side low-latency presence/gaze/interruption behavior.
- `FZ-041` Voice/realtime interaction — microphone, audio playback, interruption and reconnect semantics.

### Embodiment implementation

- `FZ-042` Embodiment contract — Android renderer implementation(s).
- `FZ-043` Performance director — Android applies semantic performance directives.
- `FZ-044` Semantic animation SDK — Android exposes/consumes renderer-independent animation semantics.

## Android must not do

- become the source of truth for agent identity, memory, personality, autonomy policy, permissions, or WorkflowOS execution;
- maintain a competing WorkflowOS state machine;
- execute side effects solely because the client believes they are permitted;
- upload raw camera/microphone/screen media by default;
- bypass server policy with local-only permission checks;
- invent a separate Android feature backlog outside the frozen FZ program.

## Android build contract

Recommended project modules:

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

Use Kotlin, coroutines/Flow, structured concurrency, Android runtime permissions, secure credential storage, lifecycle-aware realtime connections, and tests for capability registration, policy-denied actions, reconnects and local-perception privacy behavior.

## Gemini workflow

1. Read `GEMINI.md` and `AGENTS.md`.
2. Read the frozen roadmap and machine state.
3. Identify an Android-relevant FZ item that is dependency-eligible.
4. Read its work order in `spec/work-orders.md`.
5. Inspect the current Android code before changing it.
6. Implement only that FZ item's scope.
7. Produce objective tests/evidence.
8. Update program state and roadmap only when acceptance criteria are actually met.

If the desired Android behavior is not defined by the repository, stop and use the repository's governed change process rather than relying on conversation context.
