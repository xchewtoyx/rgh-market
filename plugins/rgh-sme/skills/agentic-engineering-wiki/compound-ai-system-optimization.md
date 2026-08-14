---
type: concept
title: Compound AI System Optimization
description: >
  Treat multi-component LLM systems as optimizable computation graphs so
  prompts, solutions, and tools improve via automated feedback—not only craft.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), §1; §5"
---

Modern agent stacks are **compound systems**: multiple LLM calls plus tools,
simulators, search, and interpreters. Hand-crafting each component does not
scale; TextGrad frames the missing piece as **principled automated
optimization** analogous to what autodiff did for neural nets. Design goals
for such optimizers: **general** (not one-domain handcrafts), **easy to use**
(familiar autodiff-like abstractions), and inspectable/open so harness teams
can audit updates.

Represent the system as a graph, backpropagate
[textual gradients](textual-gradients.md), and update variables with
[textual gradient descent](textual-gradient-descent.md) under
[instance vs prompt optimization](instance-vs-prompt-optimization.md). Prefer
frameworks that work out-of-the-box once you supply an objective (unit tests,
LLM judges, simulators) rather than per-application gradient prompt rewrites —
then still gate ships with
[offline prompt evaluation](offline-prompt-evaluation.md). Extend the graph to
real agent surfaces ([tool use](agent-tool-categories.md),
[retriever–generator architectures](retriever-generator-architecture.md))
rather than optimizing isolated prompts. In-silico or judge-only wins are not enough when the objective is a
simulator — plan domain oracles before treating optimized plans/code as
production-ready. This sits above single-prompt
[prompt optimization tooling](prompt-optimization-tooling.md) and below runtime
orchestration concerns owned by [agent control flow](agent-control-flow.md).
