---
type: concept
title: DSPy Compiler Three Stages
description: >
  A teleprompter compiles a DSPy program through candidate generation,
  parameter selection, and optional program-structure search — discrete
  stages, not a single optimization pass.
sources:
  - title: "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines"
    resource: "DSPy (Khattab et al.), §2, §4"
---

A **teleprompter** optimizes every
[parameterized module](dspy-module-parameterization.md) in a DSPy program
against a metric, via prompting or finetuning under one unified abstraction.
While not enforced by the framework, a typical teleprompter proceeds through
three distinct stages:

1. **Candidate generation.** Find every unique `Predict` module in the
   program (including ones nested inside other modules), and for each, sample
   candidate parameter values — instructions, field prefixes, and especially
   demonstrations. The simplest non-trivial teleprompter, `BootstrapFewShot`,
   does this by rejection sampling: run a teacher program (or the program's
   own zero-shot version) on training inputs, sometimes at high temperature or
   multiple times, and keep only the traces whose *multi-stage* execution
   collectively passes the program's metric — those passing traces become
   candidate demonstrations for every signature in the pipeline. This exploits
   a specific finding: LMs are unreliable in general but efficient at
   *searching* a well-decomposed program's solution space, so a handful of
   training examples is often enough to bootstrap further demonstrations from.
2. **Parameter optimization.** Once each parameter has a discrete candidate
   set from stage 1, standard hyperparameter search selects among them —
   random search, or Tree-structured Parzen Estimators. A distinct branch here
   is **finetuning**: `BootstrapFinetune` uses the bootstrapped demonstrations
   to update the LM's weights for a given module's predictor directly, which
   works even with no labels for any pipeline stage, so long as the metric
   itself doesn't need them.
3. **Higher-order program optimization.** A different class of change edits
   the program's *control flow*, not its parameters — the simplest form,
   **ensembling**: bootstrap several copies of the same program and replace
   it with a wrapper that runs them all in parallel and reduces their outputs
   with a combining function (e.g. majority vote).

**Training data stays deliberately small and incomplete** — potentially a
handful of examples, with labels typically needed only for the pipeline's
*final* output, not every intermediate step, unless the metric specifically
requires them. This label-efficiency is what keeps the framework's
modularity real: building a new pipeline means recompiling new code against
existing data, not annotating a new dataset per pipeline shape.

Because compiling is itself a versioned, reproducible step, benchmark
comparisons should report the full
[(model, program, strategy) triple](lm-pipeline-comparison-unit.md) rather
than crediting a model alone for an accuracy figure.

Contrast this discrete bootstrap-and-search approach with
[TextGrad](textual-gradients.md)-style [textual gradient descent](textual-gradient-descent.md):
DSPy's teleprompters search over a *sampled candidate set* validated by a
program-level metric, while TextGrad computes a natural-language critique of
the current value and rewrites it directly — different mechanics for the same
underlying goal of [prompt optimization tooling](prompt-optimization-tooling.md)
replacing hand-written prompts with a searched or optimized artifact.
