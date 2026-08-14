---
type: concept
title: Progressive Agent Architecture
description: >
  Grow from a bare model API to a full agentic system in ordered steps —
  context, guardrails, routing/gateway, caching, then write-capable loops.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

Start with the simplest architecture that can face users, then add components as
challenges appear. A common production progression:

1. Enhance context — [RAG](retrieval-augmented-generation.md) and read tools.
2. Add [input and output guardrails](input-output-guardrails.md).
3. Add a [model router](model-router.md) and [model gateway](model-gateway.md).
4. Cut latency/cost with [response caching](response-caching.md).
5. Add complex control flow and [write actions](agent-tool-categories.md) —
   full [LLM agent](llm-agent.md) patterns.

Each step adds capability or safety and also failure surface and debugging
difficulty. Adapt the order to the product; do not jump to write-capable agents
before context and blast-radius controls exist. Cross-cutting
[AI pipeline orchestration](ai-pipeline-orchestration.md) wires the pieces;
runtime metrics and tracing for the running system belong to observability
practice, not to this design sequence itself.

Within orchestration, prefer a **basic** fixed task graph (LLM inside tasks,
deterministic routing between them) before
[LLM-driven workflow routing](llm-driven-workflow-routing.md), role crews, or
[stateful task agents](stateful-task-agents.md). Fixed graphs keep a finite,
a-priori-known task set and communication pattern, so failures isolate per task
and per-task optimization stays tractable. Avoid LLMs where traditional software
or classical ML is enough; when LLMs are required, confine them to tasks inside
a dependable graph until goals truly need open-ended agency. That progression
is the practical face of the
[generality–strength tradeoff](generality-strength-tradeoff.md): conversational
agents stay general-but-weak; workflows buy strength for one goal.
