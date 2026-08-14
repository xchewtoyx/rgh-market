---
type: concept
title: Assistant–UserProxy Pair
description: >
  Two-role micro-workflow where a tool-using Assistant acts and a UserProxy
  keeps it on the human goal, corrects drift, and declares completion.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

An Assistant–UserProxy pair is a minimal
[multi-agent architecture](multi-agent-architecture.md) used by frameworks such
as AutoGen:

- **Assistant** — a standard conversational [LLM agent](llm-agent.md) with a
  [ReAct](react-loop.md)-style loop and background tools.
- **UserProxy** — stands in for the human; system-messaged to pursue the stated
  goal, act as a corrective force (steer, recommend), and eventually declare
  the goal accomplished. Often tool-light or tool-less relative to the
  Assistant.

The pair itself is a small LLM workflow: dialogue between roles replaces a
single agent that must both act and self-correct. System messages and tool
allocation are the harness levers — a CodeAssistant with file/test tools and a
goal-bearing UserProxy with no tools will converge or loop depending on those
choices. Scale the same idea with a group chat manager or hierarchical
director that delegates among several role-specialized agents
([LLM-driven workflow routing](llm-driven-workflow-routing.md)).
