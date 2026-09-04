# Floooz Work Orders

Every work order follows: objective, scope, non-goals, dependencies, contracts, implementation notes, tests, acceptance evidence, and state-update requirements. Do not expand scope without a governed architecture/requirements change.

## FZ-001 — Repository/bootstrap contracts
Objective: make repository self-describing and establish CI/governance. Acceptance: fresh agent finds source-of-truth docs and CI passes baseline checks.

## FZ-002 — Domain model and IDs
Objective: typed stable IDs for User, Agent, Device, Session, Memory, Capability, Binding, Workflow, Extension and Relationship. Acceptance: compile/serialization tests and no ambiguous string IDs at domain boundaries.

## FZ-003 — PostgreSQL persistence foundation
Objective: migrations, repositories, transactions, timestamps and concurrency primitives. Acceptance: clean bootstrap, migration test, repository integration tests.

## FZ-004 — Event envelope and persistence
Objective: durable event envelope with event ID, type, agent/session/device IDs, correlation/causation and timestamp. Acceptance: round-trip and correlation propagation tests.

## FZ-005 — Configuration and secrets
Objective: typed configuration and secret-provider abstraction. Acceptance: startup validation, missing-secret behavior, log redaction.

## FZ-006 — API foundation
Objective: versioned HTTP API, authentication boundary, validation and stable error envelope. Acceptance: contract/auth tests.

## FZ-007 — Health/readiness/observability
Objective: health/readiness, structured logs, metrics/tracing hooks. Acceptance: dependency failure/readiness tests and correlation IDs.

## FZ-008 — Agent lifecycle
Objective: create/read/update/pause/archive persistent agents. Acceptance: API/persistence lifecycle tests.

## FZ-009 — Genome/versioning
Objective: immutable agent genome snapshots and rollback. Acceptance: version history, rollback and immutability tests.

## FZ-010 — Identity profile
Objective: identity, values, boundaries and principles. Acceptance: schema/API persistence tests.

## FZ-011 — Personality profile
Objective: normalized traits, context profiles and evolution configuration. Acceptance: validation/version tests.

## FZ-012 — Behavioral examples/rules
Objective: explicit and learned behavioral exemplars with provenance/priority. Acceptance: CRUD, ordering and provenance tests.

## FZ-013 — Owner model
Objective: durable communication, decision, interaction and work preferences. Acceptance: persistence/retrieval tests.

## FZ-014 — Preference evidence
Objective: record explicit, correction, behavioral and workflow evidence with confidence. Acceptance: weighting/confidence tests.

## FZ-015 — Memory model
Objective: typed temporal confidence-aware memories and relations. Acceptance: schema/invariant tests.

## FZ-016 — Memory retrieval
Objective: semantic, structured and temporal retrieval interface. Acceptance: ranking/filtering tests.

## FZ-017 — Memory consolidation
Objective: candidate extraction, importance/confidence, deduplication and contradiction handling. Acceptance: consolidation tests.

## FZ-018 — Memory correction/supersession
Objective: user correction, retract, supersede and validity history. Acceptance: correction/history tests.

## FZ-019 — Memory audit
Objective: provenance and inspectable memory audit events. Acceptance: audit coverage tests.

## FZ-020 — Permission model
Objective: typed permission requirements and grants. Acceptance: least-privilege/denial matrix tests.

## FZ-021 — Autonomy policy
Objective: NEVER/ASK/ASK_ONCE/AUTONOMOUS modes and constraints. Acceptance: deterministic policy matrix.

## FZ-022 — Capability domain model
Objective: unified capability metadata for WorkflowOS, MCP, device, native, extension and A2A sources. Acceptance: schema/serialization tests.

## FZ-023 — Capability resolver
Objective: rank capabilities by semantic fit, installation, compatibility, permissions and owner history. Acceptance: deterministic ranking tests.

## FZ-024 — Action planning
Objective: side-effect plans with risk, approval and evidence requirements. Acceptance: planning contract tests.

## FZ-025 — Policy-enforced execution gateway
Objective: mandatory authorization boundary for all side effects. Acceptance: LLM/extension/workflow-result bypass attempts fail.

## FZ-026 — Capability binding lifecycle
Objective: install/disable/remove bindings and aliases. Acceptance: lifecycle and grant tests.

## FZ-027 — WorkflowOS adapter contract
Objective: external adapter only. Acceptance: mocked contract tests and architecture check proving no duplicated workflow authority.

## FZ-028 — WorkflowOS discovery
Objective: search/get workflow metadata. Acceptance: discovery contract tests.

## FZ-029 — WorkflowOS binding/install
Objective: persist workflow ID/version references, aliases and grants. Acceptance: binding/permission tests.

## FZ-030 — WorkflowOS invocation
Objective: start authoritative WorkflowOS executions with idempotency. Acceptance: invocation and evidence-reference tests.

## FZ-031 — WorkflowOS execution observation
Objective: observe execution state/events and reconcile only an ephemeral presentation view. Acceptance: reconnect/order/idempotency tests.

## FZ-032 — WorkflowOS evidence presentation
Objective: present authoritative completion/results; never infer completion from LLM text. Acceptance: claim/evidence tests.

## FZ-033 — Device registration
Objective: authenticated device runtime registration/revocation. Acceptance: registration security tests.

## FZ-034 — Device capability registry
Objective: register semantic device capabilities and schemas. Acceptance: discovery/compatibility tests.

## FZ-035 — Device execution gateway
Objective: policy-authorized semantic device actions. Acceptance: denial/idempotency tests.

## FZ-036 — Realtime session lifecycle
Objective: durable session metadata and ephemeral connection state. Acceptance: reconnect/end/expiry tests.

## FZ-037 — Realtime transport
Objective: secure transport for voice/perception/presence. Acceptance: auth, reconnect, ordering and backpressure tests.

## FZ-038 — Local perception signal contract
Objective: normalized semantic signals from local perception. Acceptance: schema/privacy tests; raw media remains local by default.

## FZ-039 — Reflex engine
Objective: deterministic low-latency gaze, interruption, presence and idle behavior. Acceptance: latency/precedence tests.

## FZ-040 — Model router
Objective: route across deterministic/local/multimodal/cloud/frontier tiers. Acceptance: privacy, latency, fallback and routing matrix tests.

## FZ-041 — Voice/realtime interaction
Objective: streaming speech input/output and interruption. Acceptance: latency, interruption and reconnect tests.

## FZ-042 — Embodiment contract
Objective: renderer-independent semantic embodiment API. Acceptance: capability discovery and fallback tests.

## FZ-043 — Behavior/performance director
Objective: map social/emotional intent to embodiment actions. Acceptance: deterministic mapping tests.

## FZ-044 — Semantic animation SDK
Objective: developer API for avatar movement/animation independent of renderer. Acceptance: cross-avatar semantic compatibility tests.

## FZ-045 — Extension manifest/runtime
Objective: sandboxed install/lifecycle with declared permissions/capabilities. Acceptance: manifest, sandbox and resource-limit tests.

## FZ-046 — Extension capability/permission bridge
Objective: force extension side effects through capability/policy gateway. Acceptance: bypass/sandbox escape tests.

## FZ-047 — Social identity/A2A boundary
Objective: public agent identity and A2A interoperability without private-state leakage. Acceptance: public/private serialization tests.

## FZ-048 — Agent relationships/social sessions
Objective: trust, relationships and scoped social permissions. Acceptance: authorization tests.

## FZ-049 — Personality evolution
Objective: evidence-backed experiments, versioning, rollback and safety constraints. Acceptance: experiment/rollback/non-manipulation tests.

## FZ-050 — Routing/personalization learning
Objective: learn model/capability routing from outcomes without making learned state authoritative. Acceptance: regression/privacy/learning tests.

## Universal completion evidence
Each PR must state: work item ID, dependencies satisfied, files/modules changed, tests run, architecture invariants checked, security/privacy checks, and objective acceptance evidence. Update `spec/development-state/program-state.json` only after acceptance criteria are actually met.