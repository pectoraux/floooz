# Floooz Agent Platform Architecture

## System

```text
Device Runtime (Android/Desktop/TV/etc)
        |
Realtime Session Gateway
        |
Agent Runtime
 | Identity | Memory | Owner Model | Policy | Capability | Model Router |
        |
      Event Bus
   /      |       \
WorkflowOS Extensions  Devices

A2A = agent-to-agent interoperability
MCP = tool/data interoperability
```

## Services

Agent, Genome/Identity, Personality, Owner Model, Memory, Policy/Autonomy, Capability Resolver, WorkflowOS Adapter, Device Registry, Realtime Session Gateway, Model Router, Reflex Engine, Performance/Embodiment Director, Extension Runtime, Evolution Engine, Event/Audit, Social/A2A.

## Authority

```text
user intent -> model/planner -> capability -> policy -> adapter -> execution
```

No LLM, extension, or workflow result can bypass policy.

## Durable state

PostgreSQL stores authoritative Floooz state. Redis/cache/process memory are acceleration only. Agents persist; realtime sessions do not.

## Memory

Memory types: identity, semantic, episodic, procedural, relational, preference, goal. Records support confidence, importance, temporal validity, status, embeddings where useful, and relations for support/contradiction/supersession.

## Compute

T0 deterministic reflexes; T1 small local model; T2 local multimodal model; T3 cloud general model; T4 frontier reasoning. Model Router considers task type, complexity, context size, latency budget, privacy, device resources, historical success, cost, and owner preferences.

## Perception

Camera/microphone/screen inputs are local-first. Convert raw media to semantic signals on-device when possible. Raw media must not leave the device by default.

## Embodiment

Runtime emits semantic performance directives. A Behavior Director maps them to avatar-specific motion, gaze, expression, pose, animation, or effects. Avatars may be human, stylized, eyes-only, abstract, or non-human.

## Extensions

Extensions declare capabilities, permissions, event subscriptions, device/embodiment requirements, network policy, and data-access policy. They run sandboxed and cannot mutate authority directly.

## Social

A2A is the interoperability layer. Floooz adds identity, consent, trust, relationship, and privacy boundaries around it. Public agent identity never contains private memory, credentials, private files, or internal prompts.