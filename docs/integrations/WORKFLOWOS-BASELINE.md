# WorkflowOS Baseline

Integration assumptions must be pinned to an explicit WorkflowOS commit/release when implementation begins.

Floooz can discover workflows, show metadata, bind/install workflow references, invoke executions, observe execution state/events, and present authoritative results/evidence.

Floooz cannot duplicate workflow state, transition semantics, criterion evaluation, execution orchestration, or completion authority.

The WorkflowOS repository and its implementation plan are the authority for WorkflowOS internals. Any missing integration primitive must be added there first through its governed process.

Implementation agents should inspect the current WorkflowOS repository and pin the exact compatible revision in Floooz configuration rather than relying on an unpinned `main` branch.