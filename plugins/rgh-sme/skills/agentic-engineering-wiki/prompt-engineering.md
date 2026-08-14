---
type: concept
title: Prompt Engineering
description: >
  Crafting instructions that elicit a desired model outcome without changing
  weights — the first adaptation lever before heavier techniques like finetuning.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 4"
---

Prompt engineering crafts an instruction that gets a model to generate a desired
outcome without updating weights. It is usually the easiest adaptation technique
and should be exhausted with experimental rigor before moving to finetuning.

A prompt generally has a [prompt anatomy](prompt-anatomy.md): task description
(including role and output format), optional few-shot examples from
[in-context learning](in-context-learning.md), and the concrete task. Prompting
only works if the model can follow instructions; weaker models need more
fiddling because they are less robust to small perturbations ("5" vs "five",
newlines, capitalization).

Treat prompt changes like ML experiments: version them, track evaluations, and
judge each change in the context of the whole system — a subtask win can be a
system loss. Separate prompts from application code and prefer a
[prompt catalog](prompt-catalog.md) when many apps share prompts. Frame the
work as the inbound half of the [LLM application loop](llm-application-loop.md):
stay on the [Little Red Riding Hood principle](little-red-riding-hood-principle.md),
run a [feedforward pass](llm-application-feedforward-pass.md), and gate changes with
[offline prompt evaluation](offline-prompt-evaluation.md). Rank harness ambition
with [prompt engineering sophistication levels](prompt-engineering-sophistication-levels.md)
before inventing agent loops for problems a thin wrapper or context injection
would solve.
