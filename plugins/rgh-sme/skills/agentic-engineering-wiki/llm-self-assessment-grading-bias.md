---
type: concept
title: LLM Self-Assessment Grading Bias
description: >
  An LLM judging its own model family's output grades less accurately unless
  it's framed as reviewing a third party's work, not its own.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 10"
---

For free-form textual quality (friendliness, helpfulness) that resists direct
comparison to a [gold standard](gold-standard-matching.md), LLMs can assess
their own domain despite the apparent conflict of a model grading work it (or
a close relative of it) produced — the "grade your own essay" problem. It
works, but only if done right.

A first warning applies regardless of framing: even though assessment
questions are often phrased as absolute quality questions ("Is this
correct?"), an LLM's assessment is a priori only a *relative* quality
judgment — "version A is judged right more often than version B." A
standalone score like "81% correct" carries little meaning on its own without
a comparison point.

The framing itself matters a great deal: don't let the model think it's
grading its own work. Per the same [advice conversation](advice-conversation-document.md)
principle that a model performs better believing it's helping a third party
rather than reflecting on itself, models get somewhat less accurate when
grading "you" (the user) versus a third party, and much worse when they think
they are grading their own output — driven by two conflicting biases:
training data includes plenty of non-objective forum self-reflection, and
RLHF-trained models often over-correct toward pleasing an evaluator at the
slightest hint of user doubt. Even a model that balances these biases on
average still suffers reduced objectivity from being pulled in both
directions at once. Frame LLM-as-judge assessment as reviewing a third
party's work whenever possible, regardless of whose model actually produced
it.
