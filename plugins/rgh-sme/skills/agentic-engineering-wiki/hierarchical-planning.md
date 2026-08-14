---
type: concept
title: Hierarchical Planning
description: >
  Generate a high-level plan first, then expand each step into a detailed
  sub-plan, avoiding the generate-hard versus execute-hard granularity bind.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Generative Agents: Interactive Simulacra of Human Behavior"
    resource: "Generative Agents (Park et al.), pp. 1–22"
---

Plan granularity is a design choice. Detailed plans are hard to generate and
easier to execute; high-level plans are easier to generate and harder to
execute. Hierarchical planning sidesteps the bind: produce a coarse roadmap
first, then expand each step into a finer sub-plan — possibly with the same
planner or a different one.

This pairs with [plan-validate-execute](plan-validate-execute.md): validate the
high-level plan before expensive expansion, and validate each sub-plan before
tool calls. For [LLM agents](llm-agent.md), hierarchy also helps humans supply
a coarse plan the agent elaborates, which is a common
[human approval gates](human-approval-gates.md) pattern for complex tasks.

[Generative agent architecture](generative-agent-architecture.md) pushes the
same idea into daily life simulation: sketch a day in broad strokes, decompose
into hour chunks, then into 5–15 minute actions, store plans in the
[memory stream](memory-stream.md), and replan from the reaction point when
perception interrupts the agenda — generate only near-horizon detail just in
time when plans change often.
