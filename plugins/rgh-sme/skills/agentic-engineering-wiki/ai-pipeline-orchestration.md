---
type: concept
title: AI Pipeline Orchestration
description: >
  Declare models, data sources, and tools, then chain them so formats match and
  failures surface across multi-step agent and RAG pipelines.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 10"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

An orchestrator specifies how components work together end to end:

1. **Define components** — models (via a [model gateway](model-gateway.md)),
   external data, tools, eval hooks.
2. **Chain** — compose the path from query to completion (preprocess → retrieve
   → prompt → generate → score → return or escalate).

It must enforce step-to-step format compatibility and surface component and data
mismatches instead of failing silently. Parallelize independent steps (routing
and PII scrub) when latency matters. This is distinct from general workflow
orchestrators (Airflow-style) and from the agent's internal
[ReAct](react-loop.md) / [agent control flow](agent-control-flow.md).

A **basic LLM workflow** keeps that chain as a fixed DAG or graph: tasks may
call LLMs, but routing between tasks is traditional software. That finite,
known communication pattern makes failures easy to isolate and tasks easy to
evaluate one at a time — the default before
[LLM-driven workflow routing](llm-driven-workflow-routing.md). Follow
[workflow build process](workflow-build-process.md) and
[task I/O schema design](task-io-schema-design.md) when constructing the
graph.

Tempting to adopt a framework immediately; building without one first often
preserves understanding. Evaluate tools on integration/extensibility, support
for branching/parallel/error handling, and whether they hide API calls or add
latency — criteria for [progressive agent architecture](progressive-agent-architecture.md)
maturity.
