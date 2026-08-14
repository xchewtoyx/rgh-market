---
type: concept
title: Autoregressive Generation
description: >
  A model produces one committed token at a time with no ability to pause,
  backtrack, or edit — any correction has to be engineered on top, not
  expected from the raw generation process.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 2"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 1"
---

A single model pass produces the statistically most likely *next* token, not
a whole response. That token is appended to the prompt, the model runs
another pass over the now-longer input to get the token after that, and so on
— one token at a time, each prediction conditioned on every prediction before
it. This is **autoregressive** generation, and it's a fundamental structural
difference from human writing: a human can pause, fact-check, think, or
revise before committing words to a page; the model produces exactly one
token per step, gets no extra "thinking time," and cannot stall.

**Once a token is emitted, the model is committed.** It cannot backtrack or
erase it, and it does not naturally issue in-line corrections, because
finished training documents rarely contain explicit takebacks — humans revise
*before* publishing, so the correction itself gets edited out of what the
model actually trains on. This can make a model look "stubborn" when pursuing
an obviously bad path partway through a generation. The fix — mistake
recognition and backtracking — has to be supplied by the application
designer, not expected from the raw model: [chain-of-thought
prompting](chain-of-thought-prompting.md) and [pause
tokens](pause-tokens.md) both work by giving the model extra tokens or
timesteps to think *before* committing to an answer, and [reflection and
error correction](reflection-and-error-correction.md) and [self-critique
prompting](self-critique-prompting.md) work by evaluating and, if needed,
discarding and regenerating a whole completion *after* the fact — neither
approach lets the model edit a token in place, because that ability doesn't
exist.

**Reading is much faster than generating.** Autoregression only constrains
the generation side: while processing a *given* prompt, computation for
different token positions can happen in parallel (nothing later in the prompt
is being predicted yet), but each generated token requires a full model pass
that depends on every token generated before it, so generation is inherently
sequential. In practice this makes LLMs read prompts roughly an order of
magnitude faster than they generate completions — one commonly cited figure
is around 10 ms per generated token, meaning even a short 100-token
completion costs on the order of a second, which is already at odds with the
~100 ms latency budget typical of interactive web applications. This
asymmetry is a first-order input to [model selection
tradeoffs](model-selection-tradeoffs.md) and to [context gathering latency
tiers](context-gathering-latency-tiers.md): a design that reads a large
amount of context but generates only a short completion pays a very different
latency cost than one that reads little but generates at length.

One consequence of never being able to reconsider a committed token is the
[generation repetition trap](generation-repetition-trap.md): once a pattern
starts, the model has no mechanism for getting bored of it.
