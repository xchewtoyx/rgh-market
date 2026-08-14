---
type: concept
title: Agent-Computer Interface
description: >
  Design the commands, observations, and history formatting an LM agent uses to
  operate a computer so digital work matches model limits, not human GUIs.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 1–30"
---

An agent-computer interface (ACI) is the moldable digital surface between an
[LLM agent](llm-agent.md) and a computer — available commands, how state is
communicated back, how command/observation history is tracked, and how that
history is formatted with high-level instructions into each LM input. Digital
environments can be reshaped via APIs; historically they were built for
software or humans, not LMs. An ACI is the IDE analogy for agents: specialized
interfaces raise effectiveness without changing model weights.

Humans ignore unused UI chrome; LMs pay a fixed token cost for every character
and suffer distracting context ([lost in the middle](lost-in-the-middle.md)).
A well-designed ACI helps the agent understand application state given prior
changes, manage history to drop stale observations, and take actions
efficiently and reliably. Follow
[ACI design principles](aci-design-principles.md). For software engineering,
fundamental subtasks are localization, editing, and testing — typically via a
[stateful file viewer](stateful-file-viewer.md),
[guardrailed edits](guardrailed-edit-tool.md),
[bounded search](bounded-search-observations.md), and
[collapsed observations](collapsed-observations.md).

Interaction style is usually [ReAct](react-loop.md): thought + one command,
then incorporate execution feedback. Document custom commands with usage plus
docstring in the [agent episode prompt stack](agent-episode-prompt-stack.md)
system template. Prefer this abstraction over a raw Linux shell when the shell
lacks segment edits, silent failures hide mistakes, or verbose dumps starve
the context budget under [tool definition design](tool-definition-design.md).
Ship the interface as a [configurable ACI harness](configurable-aci-harness.md)
so templates, commands, and history processors stay experimentable without
rewriting the agent loop.
