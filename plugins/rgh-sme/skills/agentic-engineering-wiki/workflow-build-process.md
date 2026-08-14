---
type: concept
title: Workflow Build Process
description: >
  Build an LLM workflow in five ordered steps — define the goal, specify
  tasks, implement tasks, wire the workflow, then optimize — for modularity.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
---

A basic LLM workflow — individual tasks may use an LLM, but routing between
tasks is a traditional fixed pipeline, distinct from
[LLM-driven workflow routing](llm-driven-workflow-routing.md) — trades
generality for strength on complicated, multi-step work where a
conversational agent runs into
[structural limitations](conversational-agent-structural-limitations.md); see
[generality-strength tradeoff](generality-strength-tradeoff.md) for when that
tradeoff is worth making. It is best built in five ordered steps:

1. **Define goal** — identify the purpose: what output or change should the
   workflow accomplish?
2. **Specify tasks** — break the workflow into tasks that, executed in order,
   achieve the goal. For LLM-based tasks, identify needed tools plus each
   task's inputs and outputs (see
   [task I/O schema design](task-io-schema-design.md)).
3. **Implement tasks** — build tasks as specified, with clearly defined I/O,
   each verified to work correctly in isolation.
4. **Implement workflow** — connect tasks into a complete workflow, adjusting
   individual tasks as needed so they function correctly in the full context.
5. **Optimize workflow** — improve quality, performance, and cost.

Workflows earn their appeal through modularity: breaking a complex problem
into components makes it easier to build, and when something breaks it's
easier to reason about and isolate the failing piece — the same isolation
benefit named generally by
[task decomposition prompting](task-decomposition-prompting.md) and by
[AI pipeline orchestration](ai-pipeline-orchestration.md)'s step-to-step
format checks. This modularity is why fixed workflows are the shape to prefer
under [progressive agent architecture](progressive-agent-architecture.md);
reach for [LLM-driven workflow routing](llm-driven-workflow-routing.md) only
once that strength genuinely still needs open-ended agency.
