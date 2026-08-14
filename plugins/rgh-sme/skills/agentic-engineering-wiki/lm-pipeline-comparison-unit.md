---
type: concept
title: Compare (Model, Program, Strategy) Triples, Not Models Alone
description: >
  "How do models compare on this benchmark" is underspecified for LM
  pipelines — report accuracy against a fixed program and compiling/
  optimization strategy so the comparison is reproducible.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §5"
---

A question like "how do different LMs compare on GSM8K" hides an unstated
variable: which prompt, how many few-shot demonstrations, whether
chain-of-thought was used, how any of that was chosen. Two people running
"the same" comparison can get different rankings purely from undisclosed
prompt-engineering differences — the model wasn't the only thing that
varied.

Once prompts and demonstration selection are treated as an
[optimizable, compiled artifact](dspy-compiler-three-stages.md) rather than
hand-tuned once and forgotten, the fix becomes available: report accuracy
against the full **(model, program, compiling strategy)** triple — e.g. "GSM8K
accuracy with program `ChainOfThought` compiled with
`BootstrapFewShotWithRandomSearch`" — instead of "GSM8K accuracy with GPT-4."
This is a reproducible unit precisely because the program and strategy are
themselves versioned artifacts, the same way a model checkpoint is, so a
different team can rerun the identical configuration rather than
approximating an undocumented hand-tuned prompt. It also isolates *where* a
gain came from: a jump in accuracy might reflect a better base model, a
better-decomposed program, or a better compiling strategy, and reporting all
three separately (rather than crediting the model alone) is what makes it
possible to tell which one actually mattered — the same discipline
[component-level harness ablation](component-level-harness-ablation.md)
applies to a coding-agent harness, applied here to an LM pipeline's prompts
and few-shot strategy instead of its tools and middleware.
