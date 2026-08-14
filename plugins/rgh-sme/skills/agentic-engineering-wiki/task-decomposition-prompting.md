---
type: concept
title: Task Decomposition Prompting
description: >
  Split a complex job into chained simpler prompts for better control, cheaper
  models on easy steps, and inspectable intermediate outputs.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 9"
  - title: "Least-to-Most Prompting Enables Complex Reasoning in Large Language Models"
    resource: "Least-to-Most Prompting (Zhou et al.), pp. 1–15"
---

Multi-step work often performs better as a chain of simpler prompts than as one
giant prompt. Example: customer support as intent classification JSON, then a
per-intent response generator. Benefits go beyond raw accuracy:
[intent classification for routing](intent-classification-for-routing.md)
enables monitoring and debugging of intermediate outputs, parallelization of
independent steps, and easier prompt writing.

Costs: higher perceived latency to the *final* answer if intermediates are
hidden, and more model queries — though each prompt is often shorter and weak
models can handle easy subtasks. Bloated monolith prompts (thousands of tokens
after iteration) are a signal to decompose. In agent systems, decomposition
aligns with [plan-validate-execute](plan-validate-execute.md) and
[hierarchical planning](hierarchical-planning.md).

One recurring split: separate a
[chain-of-thought](chain-of-thought-prompting.md) step from the value that
gets retained downstream — steps that must *think* from steps whose output is
*retained*. A "generate a plug-in concept" task, for example, can decompose
into a brainstorming step (produce several options, pick the best) and a
separate elaboration step (write up the chosen idea in detail): emit only the
chosen concept for downstream tasks under
[task I/O schema design](task-io-schema-design.md), keeping the reasoning
trace from a [templated-prompt task](templated-prompt-task.md)
out of the output those tasks actually consume, rather than relying on
prefix/suffix extraction to strip it back out of one combined completion.
Keep local retries inside the task when possible rather than adding a cyclic
[workflow topology](workflow-topology.md). When subproblem answers must feed
the next prompt for harder-than-exemplar cases, use
[least-to-most prompting](least-to-most-prompting.md).
