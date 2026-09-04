# Implementation Guide

## Fresh-agent procedure

A fresh architect/coding agent must be able to implement the repository without any conversation history.

1. Read `AGENTS.md`.
2. Read `spec/implementation-roadmap.md` — the frozen human-readable roadmap/progress authority.
3. Read `spec/development-state/program-state.json` — the machine-readable progress authority.
4. Read `spec/architecture-lock.md`.
5. Read `spec/architecture.md`, `spec/requirements.md`, `spec/work-items.md`, `spec/dependency-graph.md`.
6. Select the first dependency-eligible FZ item; never start a blocked item.
7. Read `spec/work-orders.md` and all referenced integration/device contracts.
8. Inspect the current repository/code before designing changes.
9. Implement the smallest conforming change for exactly that FZ item.
10. Run objective verification.
11. Record acceptance evidence.
12. Update both `spec/development-state/program-state.json` and `spec/implementation-roadmap.md` in the same governed change when status changes.
13. Open/update the PR with requirement -> work item -> tests/evidence mapping.

## Authority hierarchy

Architecture invariants: `spec/architecture-lock.md`.

Requirements: `spec/requirements.md`.

Scope: `spec/work-items.md` + selected work order.

Dependencies: `spec/dependency-graph.md`.

Implementation sequencing/progress: `spec/implementation-roadmap.md` + synchronized `spec/development-state/program-state.json`.

Workflow execution authority: WorkflowOS, outside this repository.

If these artifacts disagree, stop implementation and resolve the repository inconsistency through the governed change process.

## Non-negotiable engineering rules

- No implementation behavior without a repository requirement/work item/contract or governed change.
- LLM output is never authority.
- Every side effect passes through capability + policy.
- No duplicated WorkflowOS execution/state authority.
- Use idempotency keys for externally visible mutations.
- Preserve correlation IDs across async boundaries.
- Raw media stays local by default.
- Secrets use the secret abstraction and never ordinary domain records/logs.
- Device clients are not backend authority.
- Realtime session state is ephemeral.
- Semantic device/embodiment APIs are preferred over pixel/renderer-specific APIs.
- Extensions are least-privileged and sandboxed.

## Android-specific execution

Android Studio Gemini agents must also read `GEMINI.md`, `docs/android/ANDROID-IMPLEMENTATION.md`, and `docs/android/FZ-ANDROID-WORKSTREAM.md`. Android must implement only the Android-facing portion of an eligible FZ item; it must not invent a parallel Android roadmap.

## Definition of done

Code, tests, architecture checks, security/privacy checks, and acceptance evidence must all satisfy the selected work order. An agent's statement that an item is complete is never evidence by itself.
