---
type: concept
title: Textual Gradient Descent
description: >
  Update a graph variable by asking an LLM to incorporate textual-gradient
  criticisms — the natural-language analogue of an SGD step.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), ch. 2"
---

**Textual Gradient Descent (TGD)** replaces θ ← θ − ∂L/∂θ with
`v_new = TGD.step(v, ∂L/∂v)`: an LLM rewrites variable `v` in light of
aggregated [textual gradients](textual-gradients.md). Keep that rewrite behind
[critique–optimizer separation](critique-optimizer-separation.md) so the
backward pass criticizes without proposing, and steer *what* may change with
[optimization variable role descriptions](optimization-variable-role-description.md).
Optional harness knobs:
[natural-language optimizer constraints](natural-language-optimizer-constraints.md),
[textual optimizer momentum](textual-optimizer-momentum.md), and
[optimizer in-context examples](optimizer-in-context-examples.md).
The same step operator applies across prompts, code, molecules, and plans once
the graph and losses are defined. For a graph with *n* edges, each optimization
iteration costs at most *n* extra LM calls for gradients (one ∇ per edge), plus
the forward evaluations.

Objectives may be unstructured and nondifferentiable — LLM judges, unit tests,
simulators — so TGD is a general offline improvement loop for compound systems,
not only numeric loss minimization. Choose the optimization target with
[instance vs prompt optimization](instance-vs-prompt-optimization.md). Keep
accepted updates behind [offline prompt evaluation](offline-prompt-evaluation.md)
or [per-task offline harness tests](per-task-offline-harness-tests.md), and
version winning prompts under [harness drift awareness](harness-drift-awareness.md).
