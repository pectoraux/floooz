# Implementation Guide

## Fresh-agent procedure

1. Read `AGENTS.md`.
2. Read `spec/development-state/program-state.json`.
3. Read `spec/architecture-lock.md`.
4. Read `spec/architecture.md`, `spec/requirements.md`, `spec/work-items.md`, and `spec/dependency-graph.md`.
5. Select the first dependency-eligible FZ item.
6. Read `spec/work-orders.md` and the affected integration/device contract.
7. Inspect existing code before designing changes.
8. Implement the smallest conforming change.
9. Run objective verification.
10. Record acceptance evidence and update durable program state.
11. Open a PR mapping requirements -> work item -> tests/evidence.

## Non-negotiable engineering rules

- No implementation behavior without a requirement/work item/contract or governed change.
- LLM output is never authority.
- Every side effect passes through capability + policy.
- No duplicated WorkflowOS execution/state authority.
- Use idempotency keys for externally visible mutations.
- Preserve correlation IDs across async boundaries.
- Raw media stays local by default.
- Secrets use the secret abstraction and never ordinary domain records/logs.
- Device clients are not backend authority.
- Realtime session state is ephemeral.

## Definition of done

Code, tests, architecture checks, security/privacy checks, and acceptance evidence must all satisfy the selected work order. A model's statement that an item is complete is not evidence.