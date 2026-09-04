# Floooz Implementation Work Items

One work item per branch/PR. Start only when dependencies are satisfied. Acceptance evidence is mandatory.

| ID | Work item | Depends on |
|---|---|---|
| FZ-001 | repository/bootstrap contracts | — |
| FZ-002 | domain model and IDs | FZ-001 |
| FZ-003 | PostgreSQL persistence foundation | FZ-002 |
| FZ-004 | event envelope and persistence | FZ-003 |
| FZ-005 | configuration and secret abstraction | FZ-001 |
| FZ-006 | API foundation | FZ-004 |
| FZ-007 | health/readiness/observability | FZ-006 |
| FZ-008 | agent lifecycle | FZ-003,FZ-006 |
| FZ-009 | genome/versioning | FZ-008 |
| FZ-010 | identity profile | FZ-008 |
| FZ-011 | personality profile | FZ-008 |
| FZ-012 | behavioral examples/rules | FZ-010,FZ-011 |
| FZ-013 | owner model | FZ-012 |
| FZ-014 | preference evidence | FZ-013 |
| FZ-015 | memory model | FZ-008 |
| FZ-016 | memory retrieval | FZ-015 |
| FZ-017 | memory write/consolidation | FZ-016 |
| FZ-018 | memory correction/supersession | FZ-017 |
| FZ-019 | memory observability/audit | FZ-018 |
| FZ-020 | permission model | FZ-001 |
| FZ-021 | autonomy policy | FZ-020 |
| FZ-022 | capability domain model | FZ-020 |
| FZ-023 | capability resolver | FZ-022 |
| FZ-024 | action planning | FZ-023 |
| FZ-025 | policy-enforced execution gateway | FZ-021,FZ-024 |
| FZ-026 | capability binding lifecycle | FZ-025 |
| FZ-027 | WorkflowOS adapter contract | FZ-006,FZ-020 |
| FZ-028 | WorkflowOS discovery | FZ-027 |
| FZ-029 | WorkflowOS binding/install | FZ-028,FZ-026 |
| FZ-030 | WorkflowOS invocation | FZ-029,FZ-025 |
| FZ-031 | WorkflowOS execution observation | FZ-030 |
| FZ-032 | WorkflowOS result/evidence presentation | FZ-031 |
| FZ-033 | device registration | FZ-006 |
| FZ-034 | device capability registry | FZ-033 |
| FZ-035 | device execution gateway | FZ-034,FZ-025 |
| FZ-036 | realtime session lifecycle | FZ-008 |
| FZ-037 | realtime transport | FZ-036 |
| FZ-038 | local perception signal contract | FZ-036 |
| FZ-039 | reflex engine | FZ-038 |
| FZ-040 | model router | FZ-006 |
| FZ-041 | voice/realtime interaction | FZ-037,FZ-040 |
| FZ-042 | embodiment contract | FZ-008 |
| FZ-043 | behavior/performance director | FZ-042 |
| FZ-044 | semantic animation SDK | FZ-043 |
| FZ-045 | extension manifest/runtime | FZ-022,FZ-020 |
| FZ-046 | extension capability/permission bridge | FZ-045,FZ-025 |
| FZ-047 | social identity/A2A boundary | FZ-008,FZ-006 |
| FZ-048 | agent relationship/session model | FZ-047 |
| FZ-049 | personality evolution | FZ-013,FZ-014 |
| FZ-050 | routing/personalization learning | FZ-040,FZ-049 |

Detailed work-order format is defined in `spec/work-orders.md`. A work item is complete only when implementation, tests, architecture checks, and objective acceptance evidence satisfy its work order.