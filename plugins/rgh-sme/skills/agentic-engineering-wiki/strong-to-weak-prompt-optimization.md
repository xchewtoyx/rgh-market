---
type: concept
title: Strong-to-Weak Prompt Optimization
description: >
  Optimize prompts for a cheaper inference model with feedback from a stronger
  model so you pay a fixed optimization cost and keep inference cheap.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), ch. 3 §3.3; Appendix E"
---

When [prompt optimization tooling](prompt-optimization-tooling.md) can use a
separate “gradient” or critique model, run the **optimizer/feedback engine** on
a stronger model and the **forward reasoner** on the weaker/cheaper model you
will deploy. The TextGrad reasoning experiments optimized a
`gpt-3.5-turbo` system prompt with `gpt-4o` feedback over small
train/val/test splits (Object Counting, Word Sorting, GSM8k), keeping the
prompt only when validation improved after each minibatch step. Concrete
splits used there: BBH Word Sorting / Object Counting at **50/100/100**,
GSM8k (DSPy) at **200/300/1319**. Score Object Counting and GSM8k with
[gold-standard matching](gold-standard-matching.md) on the last numerical
value; use a structured LLM judge (binary 1/0 inside tagged fields) for
Word Sorting where exact string match is brittle.

This is a harness cost trade: spend tokens once during offline search, then
serve the cheaper model with an improved instruction (often still zero-shot —
see [instruction vs demonstration optimization](instruction-vs-demonstration-optimization.md)).
[DSPy teacher-program distillation](dspy-teacher-program-distillation.md) makes
the same trade a different way — a stronger *compiled program*'s execution
traces become bootstrapped demonstrations or finetuning data for the cheap
program, instead of a stronger model's textual criticism rewriting a prompt.
Gate acceptance with [offline prompt evaluation](offline-prompt-evaluation.md)
or [per-task offline harness tests](per-task-offline-harness-tests.md) so
optimizer noise does not ship. Pair with
[harness drift awareness](harness-drift-awareness.md): the optimized prompt is
a versioned artifact tied to a specific inference model.
