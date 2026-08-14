---
type: concept
title: Logprobs Fundamentals
description: >
  A model computes a full probability distribution over the next token, not
  just the one it picks, and can return those log-probabilities at no extra cost.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

LLMs are usually treated as "text in, text out," but the model also exposes
the numerical values behind its text choices. At each generation step, the
model computes a full probability distribution over the next token, not just
the one it ends up emitting; these can be returned as **logprobs** (log of
the probability). A logprob is always negative or zero — more negative means
less probable, and 0 means certain — and converts back to a plain probability
with `exp`. For example, logprobs of −0.405 for "Yes" and −1.099 for "No"
correspond to roughly 66% Yes versus 33% No.

Many APIs can return logprobs for tokens the model considered but didn't
choose, alongside the ones it did — retrieving them costs no extra compute,
since the model calculates the full distribution anyway as part of generating
the chosen token. One practical caveat: some commercial providers disable
logprob access, largely out of concern about reverse-engineering their model
via the exposed probabilities, so factor this into
[model selection](model-selection-tradeoffs.md) if these techniques matter to
an application.

Three applications build on this foundation:
[completion confidence scoring](completion-confidence-scoring.md),
[logprob classification calibration](logprob-classification-calibration.md),
and [critical point detection](critical-point-detection-via-logprobs.md).
