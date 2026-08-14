---
type: concept
title: Textual Optimizer Momentum
description: >
  Keep a window of past variable values in the optimizer context so updates see
  trajectory history, not only the latest textual gradients.
sources:
  - title: "TextGrad: Automatic Differentiation via Text"
    resource: "TextGrad (Yuksekgonul et al.), Appendix B"
---

Scalar SGD momentum mixes past gradients numerically. TextGrad’s **momentum**
instead injects **past iterations of the variable** into the optimizer prompt
(e.g. `momentum_window=3` → `<PAST_ITERATIONS>…</PAST_ITERATIONS>`). The
rewriter sees how the prompt or solution evolved, which can reduce oscillation
when [textual gradients](textual-gradients.md) conflict across batches.

Treat the window size as a harness knob under
[textual gradient descent](textual-gradient-descent.md): too small forgets
useful history; too large burns context and may anchor on early bad variants.
Combine with [natural-language optimizer constraints](natural-language-optimizer-constraints.md)
when format must stay fixed across iterations.
