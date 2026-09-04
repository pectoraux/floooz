# Floooz API Contracts

## Agent

```ts
POST /v1/agents
GET  /v1/agents/:id
PATCH /v1/agents/:id
GET  /v1/agents/:id/genome
POST /v1/agents/:id/genome/rollback
```

## Memory

```ts
GET    /v1/agents/:id/memory
POST   /v1/agents/:id/memory/search
POST   /v1/agents/:id/memory
PATCH  /v1/agents/:id/memory/:memoryId
DELETE /v1/agents/:id/memory/:memoryId
POST   /v1/agents/:id/memory/:memoryId/retract
POST   /v1/agents/:id/memory/:memoryId/supersede
```

## Capabilities/workflows

```ts
GET  /v1/capabilities/discover?q=...
GET  /v1/agents/:id/capabilities
POST /v1/agents/:id/capabilities/:capabilityId/install
DELETE /v1/agents/:id/capabilities/:bindingId
POST /v1/agents/:id/workflows/:workflowId/start
GET  /v1/agents/:id/workflows/executions/:executionId
```

## Devices/sessions

```ts
POST /v1/devices/register
GET  /v1/devices/:id/capabilities
POST /v1/devices/:id/actions
POST /v1/agents/:id/sessions
WS   /v1/sessions/:sessionId
```

All mutations accept an idempotency key. Side-effecting actions are rejected unless the policy engine authorizes the capability. Realtime messages carry correlation IDs.

## Domain interfaces

```ts
interface ModelRouter {
  route(request: ModelRoutingRequest): Promise<ModelDecision>
}

interface CapabilityResolver {
  resolve(request: CapabilityResolutionRequest): Promise<CapabilityCandidate[]>
}

interface DeviceRuntime {
  capabilities(): Promise<DeviceCapability[]>
  execute(capabilityId: string, input: unknown): Promise<DeviceActionResult>
}

interface Embodiment {
  capabilities(): EmbodimentCapability[]
  lookAt(target: LookTarget, options?: LookOptions): Promise<void>
  setExpression(expression: string, intensity?: number): Promise<void>
  playAnimation(animation: AnimationRequest): Promise<void>
}

interface MemoryService {
  retrieve(input: MemoryRetrievalRequest): Promise<MemoryResult[]>
  create(input: CreateMemoryRequest): Promise<Memory>
  update(id: MemoryId, patch: MemoryPatch): Promise<Memory>
  supersede(id: MemoryId, replacement: CreateMemoryRequest): Promise<Memory>
  retract(id: MemoryId): Promise<void>
}
```

Exact implementation types may evolve only within the frozen architecture boundary.