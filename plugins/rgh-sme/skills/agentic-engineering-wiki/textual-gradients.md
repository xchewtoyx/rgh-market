---
type: concept
title: Textual Gradients
description: >
  Natural-language criticisms of a variable’s role in a computation graph,
  produced by an LLM as the analogue of a numerical gradient.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), ch. 2; §4"
---

In TextGrad, a compound AI system is a **computation graph** whose nodes are
variables (prompts, predictions, code, plans) and whose edges are arbitrary
transforms — LLM calls, simulators, interpreters — that need not be
differentiable. A **textual gradient** on a variable is interpretable
natural-language feedback describing how to change that variable to improve
downstream evaluation, aggregated from every successor context where the
variable was used (chain-rule analogue through black-box ops). This is the
primitive behind [compound AI system optimization](compound-ai-system-optimization.md).

Unlike white-box numerical prompt gradients that need model parameters (unusable
for closed APIs), textual gradients work through black-box LLM calls and
simulators. Prompt-only precursors (e.g. ProTeGi-style NL feedback on task
mistakes) become full autodiff-style propagation across stacks — including
[instance vs prompt optimization](instance-vs-prompt-optimization.md), not only
instruction rewrite. DSPy-style program optimizers are complementary: they
structure layers and often bootstrap demos; TextGrad-style frameworks center
backward NL feedback as the update rule.

The operator is domain-independent once implemented: given conversation
context `{x|y}` and criticisms on `{y}`, an LLM explains how to improve `{x}`.
Use textual gradients when you want automated search over unstructured
artifacts (system prompts, solutions, tool schemas) without hand-tuning each
component — then apply [textual gradient descent](textual-gradient-descent.md)
to produce the update. Pair with
[prompt optimization tooling](prompt-optimization-tooling.md) and
[offline prompt evaluation](offline-prompt-evaluation.md) so feedback quality
is measured, not assumed.
