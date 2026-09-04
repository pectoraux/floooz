# Floooz Frozen Architecture Lock

**Version:** 0.1
**Status:** FROZEN

1. Agent identity, personality, owner model, memory, autonomy policy, device bindings, capability bindings, sessions, embodiment configuration, relationships, and evolution state belong to Floooz.
2. WorkflowOS remains authoritative for workflow definitions, workflow state, execution, verification, and workflow artifacts.
3. Floooz may discover, install/bind, start, observe, and present WorkflowOS workflows, but must not reimplement WorkflowOS execution semantics.
4. Every side effect is mediated by an explicit capability and policy decision.
5. LLM output is advisory; it is never authority for permissions, workflow completion, or durable state.
6. Durable application state belongs in PostgreSQL. Redis/cache/process memory may accelerate but never become authority.
7. Realtime sessions are ephemeral. Agent identity and long-term memory are durable.
8. Device media/perception is local-first. Raw camera/microphone/screen media is not sent to the cloud by default.
9. Public agent-to-agent identity exposes only explicitly public capabilities/metadata. Private memory, credentials, private files, and internal prompts are never public.
10. Extensions are sandboxed and receive only declared capabilities/permissions.
11. Model selection is replaceable behind a Model Router. Local, edge, cloud, and frontier reasoning models may coexist.
12. Personality evolution is versioned, reversible, evidence-backed, and must not optimize raw engagement at the expense of trust, autonomy, privacy, or safety.
13. Semantic device and embodiment APIs are preferred over pixel- or renderer-specific APIs.
14. Architecture changes require an explicit architecture-change record and a new immutable architecture-lock version.

## Change rule
An implementation PR may not modify this file or silently weaken an invariant. Architecture changes require rationale, affected invariants, migration/compatibility analysis, security/privacy analysis, updated requirements/work items, a new lock version, and explicit approval.