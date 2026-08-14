---
type: concept
title: Multi-Agent Architecture
description: >
  Split agent work across specialized roles — planner, validator, executor,
  critic — so each component has a narrower job than a single monolithic agent.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

A multi-agent system assigns distinct agent roles to stages of the loop. A
minimal split is plan generation, plan validation, and plan execution under
[plan-validate-execute](plan-validate-execute.md). Reflection setups often add
a separate critic: one agent plans and acts, another evaluates after each step
or batch ([Reflexion](reflexion.md)).

Specialization helps because each role can use different prompts, models, or
tool subsets from the shared [tool inventory](tool-inventory.md). Parallel
candidate-plan generation with an evaluator is another multi-agent latency/cost
tradeoff. Treat role boundaries as harness design: clear inputs/outputs between
agents matter as much as each agent's internal
[ReAct](react-loop.md)-style loop.

**Roles and delegation** frameworks (AutoGen, CrewAI, and similar) push the same
idea further: assemble agents each with role, goal, backstory, and tools, then
delegate toward an overall goal. Process shapes include sequential pipelines,
hierarchical directors (a manager routes among specialists — AutoGen's group
chat manager is this pattern), and consensual collaboration where agents jointly
decide how work proceeds. A minimal unit is the
[Assistant–UserProxy pair](assistant-userproxy-pair.md). When agents own durable
assets rather than one-shot tasks, see
[stateful task agents](stateful-task-agents.md); when the model chooses the next
task rather than a fixed graph, see
[LLM-driven workflow routing](llm-driven-workflow-routing.md).
