---
type: concept
title: Natural Language Action Plans
description: >
  Express agent plans in natural language then translate to tool calls, which
  is more robust to API churn than planning directly in exact function names.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

Planning with exact function names is brittle. Tool APIs rename and reshape
over time, forcing prompt and few-shot updates — and a finetuned planner would
need refinetuning. Cross-use-case reuse also suffers when each environment has
different APIs.

An alternative is to generate plans in natural language ("get current date /
retrieve best-selling product last week / …"). Models trained mostly on natural
language handle this better and hallucinate less on the plan itself. The cost
is a **translator** (sometimes called a program generator) that converts each
NL action into an executable command from the
[tool inventory](tool-inventory.md).

Translation is usually simpler than planning and can run on a weaker model with
lower hallucination risk — but the translator itself becomes a failure point
and needs its own checks under
[agent planning failure modes](agent-planning-failure-modes.md) and
[agent tool failure modes](agent-tool-failure-modes.md).
