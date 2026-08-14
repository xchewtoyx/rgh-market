---
type: concept
title: LLM Agent
description: >
  An LLM agent is a model that perceives an environment and acts on it through
  a tool inventory, with the model itself serving as the planner.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
    resource: "Toolformer (Schick et al.), pp. 1–17"
---

An agent is anything that can perceive its environment and act upon that
environment. In foundation-model systems, the model is the "brain": it
processes the task and environment feedback, plans a sequence of actions, and
decides when the task is done.

Two design axes define an agent:

1. Its **environment** — the use-case world it operates in (a codebase, the web,
   a database, a kitchen, a road system).
2. Its **set of actions**, augmented by its [tool inventory](tool-inventory.md).

Environment and tools are interdependent: the environment determines which
tools are possible, while the tool inventory restricts which environments the
agent can effectively operate in. Familiar products already fit this frame —
chat assistants with search and code execution, or RAG systems whose retrievers
and SQL executors are tools.

Agent success depends on tool inventory quality and planner strength. Agents
typically need stronger models than non-agentic flows because
[compound mistakes](compound-mistake-amplification.md) accumulate across steps
and tool access raises the stakes of each wrong action. Teaching *which*,
*when*, *what*, and *how* for tools can be prompted
([function calling](function-calling.md), [ReAct](react-loop.md)) or learned
via [Toolformer-style](toolformer-tool-use.md) self-supervision — either way,
the harness must execute calls safely and feed results back as observations.
