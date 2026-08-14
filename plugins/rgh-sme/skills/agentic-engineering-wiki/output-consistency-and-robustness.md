---
type: concept
title: Output Consistency and Robustness
description: >
  Because generation is probabilistic, the same or a near-identical prompt
  can yield meaningfully different completions across calls — a property to
  manage, not a bug to eliminate.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 2"
---

[Sampling](temperature-and-sampling.md) makes generation probabilistic rather
than deterministic: asking a model the same question twice can yield
different answers, the same way two people might genuinely disagree, except
here it's one system disagreeing with itself. This surfaces in two related
but distinct ways:

- **Same input, different output across calls** — a documented case had the
  same model score the identical essay 3/5 on one run and 5/5 on a re-run of
  the exact same prompt.
- **Slightly different input, disproportionately different output** — even a
  cosmetic change like a capitalization difference can swing the completion
  far more than the size of the input change would suggest. This case is
  harder to fix than the first: careful prompting and a well-designed context
  and memory system are the main available levers, since fixing generation
  settings alone helps less here than for same-input variance.

A model is **robust** to the extent that small input variations don't
dramatically change its output. Robustness is a property to design around,
not eliminate — the less robust a model is, the more it benefits from
[test-time compute sampling](test-time-compute-sampling.md) (generating
several candidates and selecting among them) as a workaround, though the more
durable fix for a persistently brittle model is to reconsider [model
selection](model-selection-tradeoffs.md) rather than layer workarounds on
top indefinitely.

Mitigations for same-input inconsistency, in rough order of how much control
they give:

- **Cache answers** — see [response caching](response-caching.md) for the
  exact-match and semantic-match variants; a cached response is trivially
  consistent because it's the same response.
- **Fix the sampling variables** — temperature, top-p, top-k held constant
  across calls removes one source of run-to-run variance, though it doesn't
  eliminate it, since sampling at any temperature above 0 remains genuinely
  stochastic by design.
- **Fix the random seed**, where the API exposes one. Even with temperature,
  top-p/top-k, and seed all pinned, 100% reproducibility still isn't
  guaranteed: the specific hardware executing the generation can affect
  floating-point rounding and therefore the output, and different machines
  round differently. This is controllable if self-hosting on fixed hardware,
  but generally not controllable against a third-party API where the serving
  hardware isn't chosen or disclosed by the caller.

None of these guarantee perfect consistency — they reduce one source of
variance at a time. Treat the residual inconsistency as an expected property
of the system to design against (via evaluation, caching, and [reflection and
error correction](reflection-and-error-correction.md)), not as a defect to
chase to zero.
