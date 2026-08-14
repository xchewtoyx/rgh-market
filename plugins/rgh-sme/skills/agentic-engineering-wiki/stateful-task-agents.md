---
type: concept
title: Stateful Task Agents
description: >
  Bind an agent permanently to one work item instead of restarting fresh each
  time, so it can track that item's state and notify dependents when it changes.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

Reframes a workflow task as an agent permanently associated with a work item
(a source file, ticket, or asset), responsible for modifying that item's state
as needed, rather than starting fresh with no memory each time new work
arrives. Example: building a website where each source file (say, one page's
JS) has its own persistent code-writing agent responsible for that file. When
a related file changes — e.g. a human requests a UI change — the relevant
task agent makes the edit and notifies dependent task agents, which update
their own files to stay consistent and in turn notify their own dependents.
Unlike stateless task invocations that begin with empty memory on each
arrival, the agent carries continuity for its asset — closer to long-lived
[agent memory tiers](agent-memory-tiers.md) than to one-shot tool calls.

Workflow-level interaction patterns built on stateful task agents:

- A workflow orchestrator sends requests to particular task agents to update
  the assets they own.
- The workflow maintains a **dependency graph** among task agents as work
  items are created; when one updates, its task agent notifies dependents
  directly. Circular dependencies must be avoided or explicitly handled, or the
  workflow may never reach a stopping point.
- Because agents are stateful, users can interact with them directly — e.g. a
  developer discusses a needed change with the agent that owns a given file
  rather than editing content directly; once that task agent updates, neighbors
  on the dependency graph are notified to react.

This is a persistence-and-identity variant of
[LLM-driven workflow routing](llm-driven-workflow-routing.md): instead of a
central agent dispatching stateless task invocations, each work item carries
its own long-lived agent and [memory management](memory-management.md) tied
to that item rather than to a single conversation. It sits above
[LLM-driven workflow routing](llm-driven-workflow-routing.md): routing chooses
*which* work runs; stateful task agents define *who owns* persistent
artifacts. Pair with clear ownership boundaries in a
[multi-agent architecture](multi-agent-architecture.md) so notifications do
not become unbounded fan-out.
