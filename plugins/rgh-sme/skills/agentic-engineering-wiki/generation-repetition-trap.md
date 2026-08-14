---
type: concept
title: Generation Repetition Trap
description: >
  Once a repetitive pattern starts by chance, continuing it is statistically
  more likely at every subsequent step than breaking it, since the model has
  no mechanism for getting bored.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
---

[Autoregressive generation](autoregressive-generation.md) makes each token a
local decision with no memory of "I've said this kind of thing enough
already." Once a repetitive pattern has, by chance, started — a numbered list,
a recurring sentence structure, a recurring specific word — continuing it is
statistically more likely at each subsequent step than breaking it, because
the growing context now contains that pattern as evidence of what a plausible
continuation looks like. A list that should naturally stop at 3-5 items can
instead run on indefinitely once the model settles into "continue the list"
as the higher-probability choice at every step; a set of stated reasons can
drift into repeating the same few words ("legacy, following, future,
foundation, fanbase...") ad nauseam once that vocabulary becomes
self-reinforcing. A documented failure case: an early chat model whose
end-of-turn stop signal was misconfigured never learned to stop at all —
completions that had already produced a complete, intelligible answer would
spiral into repeated sign-offs ("Hope you have a nice day!" ... "...a
wonderful day!" ... "...a festive day!" ...) until hitting the hard token
limit, because nothing in the generation process itself provides a "this is
enough" signal.

At temperature 0 the model always takes whatever option it judges more
likely, so once a repetitive pattern is established the trap is essentially
inescapable at that setting — continuing scores higher, every single step.

Two mitigations, addressing the trap from different ends:

- **Detect and filter repetitive output after the fact**, catching runaway
  patterns in post-processing rather than trying to prevent them during
  generation.
- **Introduce randomness via [temperature](temperature-and-sampling.md)**, so
  the model has a genuine, non-zero chance of choosing the natural stopping
  token even while continuation still scores higher on average — over many
  steps this pulls the expected pattern length back toward what the training
  distribution would actually produce, rather than getting stuck at the
  temperature-0 extreme.

This is a narrower, generation-time complement to [completion stop-condition
design](completion-stop-condition-design.md), which attacks the same
"where does this end" problem from the harness side — stop sequences and
streaming cancellation cut generation off at a known boundary regardless of
whether the model itself would have kept going.
