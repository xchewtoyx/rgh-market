---
type: concept
title: Temperature and Sampling
description: >
  A model computes a full probability distribution over the next token, and
  sampling — controlled by temperature — decides how faithfully generation
  follows versus deviates from the single most likely choice.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 2"
---

At each [autoregressive](autoregressive-generation.md) step, a model doesn't
just compute the single most likely next token — it computes a probability
for every token in its vocabulary. **Sampling** is the process that picks one
token from that distribution; these probabilities are also what [logprobs
fundamentals](logprobs-fundamentals.md) exposes at no extra compute cost.

Mechanically, the network outputs a **logit** vector — one raw score per
vocabulary token, not yet a probability (logits don't sum to one and can be
negative). A **softmax** layer converts logits to a proper probability
distribution: `p_i = e^(x_i) / Σ_j e^(x_j)`. **Greedy sampling** always picks
the single highest-probability token; it's fine for closed-ended
classification, but for open-ended language generation it produces boring,
generic text, since it always reaches for the most common word. Sampling
proportionally to the full distribution instead — "red" 30% of the time,
"green" 50%, if that's the learned distribution for "my favorite color is
___" — is what makes generation varied rather than deterministic-by-default.

**Temperature** is a number ≥ 0 that controls how faithfully sampling follows
the raw distribution versus flattening it toward more uniform, "creative"
selection. The sampling formula:

```
p(token_i) = exp(logprob_i / t) / Σ_j exp(logprob_j / t)
```

Recommended regimes:

- **0** — always the single most likely token, no alternatives considered.
  Use when correctness matters most, or when repeatability matters — though
  it isn't perfectly deterministic in practice, since floating-point rounding
  differences can occasionally shift which token is "most likely" between
  runs. Division by the temperature formula is technically undefined at T=0,
  so in practice this setting is implemented as greedy sampling (argmax)
  directly, skipping softmax altogether rather than evaluating the formula at
  the limit.
- **0.1-0.4** — a small chance for a near-tied alternative to be picked
  instead. Useful for generating a handful of different candidate solutions
  to filter afterward, or for one slightly more varied completion than
  temperature 0 would give.
- **0.5-0.7** — chance plays a bigger role; the model will sometimes skip a
  clearly-more-likely option. Useful for generating a larger set (roughly 10+)
  of independent candidate solutions.
- **1** — the token distribution exactly mirrors the training-set statistical
  distribution the model learned. If a phrase is followed by option A 51% of
  the time and option B 31% of the time in training, sampling many times at
  temperature 1 reproduces those frequencies.
- **>1** — output becomes more random than even the training distribution:
  standard continuations get relatively less likely, "weird" ones relatively
  more likely, than training data would itself suggest — pushed far enough,
  this makes completions "sound drunk." Because temperature only reshapes the
  final probability-to-token step (not the computation that produced those
  probabilities), errors compound over a long generation at high temperature:
  the model treats its own earlier error as part of the pattern in the
  now-longer context and mimics that error-pattern going forward, and each
  further high-temperature draw adds more noise on top — producing visible
  degradation that gets worse toward the end of a long completion.

A worked illustration of the tradeoff: a typical training-set list naturally
stops after a small number of items. At each new line the model predicts
either "continue" or "stop." At temperature 0 it always takes whichever it
judges more likely — often meaning it keeps continuing well past where a
list would naturally end (see the [generation repetition
trap](generation-repetition-trap.md)). At temperature 1, if the model
estimates continuation probability as *x* at a given point, it continues with
probability *x* at that step — so, aggregated over many draws, the expected
list length converges toward what the training distribution would actually
produce, rather than sitting at whichever extreme temperature-0 happens to
select. The general trade: higher temperature yields more varied output and
generation-length statistics that better match the training distribution;
lower temperature yields more replicable, deterministic output. Which side of
that trade to take is a per-application choice — a factual lookup wants
temperature 0; a brainstorming task wants a higher one.

Most providers cap the temperature parameter between 0 and 2 (self-hosted
models can typically be run at any non-negative value); 0.7 is a commonly
recommended default balance between predictability and variety, but it should
be tuned per application rather than assumed.

**Restricting the candidate pool before sampling** is a separate, composable
lever from temperature — instead of (or alongside) reshaping the whole
distribution, restrict which tokens are even eligible to be sampled:

- **Top-k** — only the *k* highest-logit tokens are considered (softmax
  itself requires two passes over the full vocabulary, which is expensive at
  scale, so this also cuts compute). Typical *k*: 50-500, far smaller than a
  full vocabulary. A smaller *k* gives more predictable, less varied output.
- **Top-p (nucleus sampling)** — instead of a fixed count, sum probabilities
  of the most-likely tokens in descending order until the cumulative sum
  reaches *p*, and sample only within that set. The candidate-set size then
  varies by context automatically: few real options for a prompt with an
  obvious yes/no answer, many for an open-ended one. Typical *p*: 0.9-0.95.
  Unlike top-k, top-p doesn't necessarily reduce softmax compute, but tends
  to improve contextual appropriateness and has become the more popular
  choice.
- **Min-p** — sets a minimum probability threshold a token must individually
  clear to be eligible at all, rather than constraining by rank or cumulative
  mass.

**Beam search** is an alternative to per-token sampling: instead of committing
to one token at each step, it looks ahead several tokens to check a likely
follow-on sequence exists before committing, avoiding "painted into a corner"
situations that per-token sampling can't see coming. It can produce more
accurate solutions but costs much more time and compute, so it sees less use
in production applications than plain sampling.
