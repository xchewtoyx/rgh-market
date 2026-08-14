---
type: concept
title: Plan Validate Execute
description: >
  Decouple plan generation from execution so a bad plan can be rejected before
  it burns tool calls, tokens, and irreversible side effects.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6"
---

A task has a goal and constraints; a plan is the roadmap of steps to satisfy
them. Coupling planning and execution in one prompt (think-then-act in a single
pass) can let an unvalidated runaway plan consume time and money before anyone
notices.

Prefer three stages:

1. **Plan generation** (task decomposition into actions).
2. **Plan validation** — heuristics (tools must exist in the
   [tool inventory](tool-inventory.md); length caps) and/or an AI judge that
   regenerates unreasonable plans.
3. **Execution** — usually via [function calling](function-calling.md).

Plans need not cover the whole task; they can address a subtask.
[Hierarchical planning](hierarchical-planning.md) further separates high-level
roadmap from detailed expansion. Splitting generation, validation, and
execution into separate roles is already a simple
[multi-agent architecture](multi-agent-architecture.md). Parallel candidate
plans traded against an evaluator buy latency at higher cost.
