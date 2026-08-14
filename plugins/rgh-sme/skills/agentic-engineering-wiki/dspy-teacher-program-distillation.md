---
type: concept
title: DSPy Teacher-Program Distillation
description: >
  Compile an expensive teacher program first, then bootstrap a cheap student
  program's demonstrations or finetuning data from the teacher's own traces —
  even when no labels exist for the student's intermediate steps.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §4"
---

DSPy's [compiler](dspy-compiler-three-stages.md) can sample demonstrations
from a separate, specified **teacher program** rather than only from the
program being compiled itself. This lets an expensive configuration —
a large-model ensemble, or a program with more pipeline stages — supervise a
cheap one: compile a retrieval-augmented pipeline with a large chat model,
then use *that already-compiled program* as the teacher to bootstrap
demonstrations for `BootstrapFinetune`-ing a much smaller, cheaper program
from a larger pool of otherwise-unlabeled questions — labels for every
intermediate step are derived from the teacher's traces, not hand-annotated.

This is DSPy's version of the same "spend once during search, then serve
cheap" trade [strong-to-weak prompt optimization](strong-to-weak-prompt-optimization.md)
makes with a critique-driven optimizer, but the mechanism differs: strong-to-
weak optimization uses a stronger model's *textual criticism* to rewrite a
cheap model's prompt, while teacher-program distillation uses a stronger
program's *execution traces* as bootstrapped training data — demonstrations
for few-shot prompting, or labels for finetuning — for a cheaper program.
Prefer teacher-program distillation specifically when the target program
needs [demonstration bootstrapping or finetuning](instruction-vs-demonstration-optimization.md)
rather than an instruction rewrite, and when a stronger *compiled program*,
not just a stronger base model, is available to generate the traces.
