# WorkflowOS Integration Contract

WorkflowOS is an external execution system and remains authoritative for workflow definitions, workflow state, execution, verification and workflow artifacts.

Floooz owns only discovery UX, agent bindings, authorization/policy context, invocation requests, execution observation/presentation and agent-facing memory/context.

## Adapter

```ts
interface WorkflowOSAdapter {
  search(query: WorkflowDiscoveryQuery): Promise<WorkflowSummary[]>
  getWorkflow(workflowId: string, version?: string): Promise<WorkflowDefinition>
  bind(request: WorkflowBindingRequest): Promise<WorkflowBinding>
  start(request: WorkflowStartRequest): Promise<WorkflowExecutionRef>
  getExecution(executionId: string): Promise<WorkflowExecutionView>
  subscribe(executionId: string, handler: WorkflowEventHandler): Promise<Subscription>
}
```

## Forbidden

Do not create a second WorkflowOS executor, workflow state machine, criterion evaluator, authoritative workflow database, or completion semantics in Floooz.

Store WorkflowOS IDs/versions/references, not duplicated workflow state. User-visible completion must be backed by authoritative WorkflowOS evidence. Side effects initiated through Floooz still pass the Floooz capability/policy boundary.

If Floooz needs an execution primitive that WorkflowOS does not expose, change WorkflowOS through its own governed implementation plan first.