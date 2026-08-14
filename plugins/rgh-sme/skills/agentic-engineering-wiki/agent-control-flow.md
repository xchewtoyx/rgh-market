---
type: concept
title: Agent Control Flow
description: >
  The order planned actions execute — sequential, parallel, conditional, or
  looped — with the model itself often determining non-sequential branches.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 9"
---

Control flow is the order in which planned actions run. Simple agents stay
**sequential**: task B waits on task A (for example, SQL runs only after NL-to-
SQL translation). Richer flows include:

- **Parallel** — independent calls run together (fetch prices for many products
  concurrently), cutting user-perceived latency.
- **Conditionals** — branch on prior output (buy vs. sell after reading an
  earnings report).
- **Loops** — repeat until a condition holds.

Unlike traditional software, AI agents often let the **model** decide control
flow. That makes non-sequential plans harder to generate and harder to
translate into executable commands (especially with
[natural language action plans](natural-language-action-plans.md)). When
choosing an agent framework, check which control flows it supports — parallel
browse/fetch is a common latency win that sequential-only harnesses cannot
express.

Fixed [workflow topology](workflow-topology.md) (pipeline, DAG, optional
cycles) is the non-model-driven counterpart: routing is code, while individual
tasks may still use LLMs. Prefer that shape until goals need
[LLM-driven workflow routing](llm-driven-workflow-routing.md).
