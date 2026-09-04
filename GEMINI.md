# Android Studio Gemini Agent Entry Point

Treat this GitHub repository as the only source of truth. No prior chat or product discussion is required.

## Read in this order

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
11. `docs/android/ANDROID-IMPLEMENTATION.md`

## Android authority boundary

Android is a device runtime, not authoritative agent infrastructure. It owns device registration, local perception, realtime connectivity, rendering and policy-authorized device capabilities. It does not own durable agent identity, personality, memory, policy, permissions, WorkflowOS workflow state, or WorkflowOS execution.

## Selecting Android work

Do not invent an Android backlog. Use the frozen FZ roadmap. Android-related work becomes eligible only when its FZ dependencies are satisfied. In particular, device/runtime work follows the capability/policy foundation and must not bypass the server-side authority model.

## Implementation expectations

- Kotlin + coroutines/Flow + structured concurrency.
- Secure local storage for device/session credentials.
- Android runtime permissions are mandatory for camera/microphone.
- Prefer local ML for presence, gaze, VAD and other lightweight perception.
- Raw media stays local by default; cloud media requires an explicit policy path.
- Client authorization is defense in depth; server policy is authoritative.
- Use semantic device/UI capability contracts rather than pixel-specific assumptions.
- Preserve correlation IDs and idempotency across reconnects and side effects.

## Completion

A Gemini agent must produce objective acceptance evidence, update `spec/development-state/program-state.json` and `spec/implementation-map.md` consistently, and follow the one-FZ-item-per-branch/PR rule.
