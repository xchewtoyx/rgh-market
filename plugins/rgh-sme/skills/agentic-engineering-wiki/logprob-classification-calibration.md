---
type: concept
title: Logprob Classification Calibration
description: >
  Shift a classifier's per-token logprobs by a constant to match the
  confidence threshold the application actually needs, not the model's default.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

A model's predicted certainty via [logprobs](logprobs-fundamentals.md) often
isn't calibrated to the threshold an application actually wants. Example: an
app that blocks unfriendly emails, asking "Is this a professionally written
email? 1. Yes/No 2. Explanation" — if too many unprofessional emails are
getting through, you want the model to answer "No" only when it's very
confident, not at whatever confidence threshold the model happens to default
to internally.

The general method: shift each candidate token's logprob by a constant before
comparing them, e.g. add a constant to "No"'s logprob to make the classifier
stricter, or to "Yes"'s logprob to make it more lenient toward "No." Find
these per-token constants either by experimentation or with classical ML —
minimizing cross-entropy loss against a set of ground-truth labels, the same
objective logistic regression uses. Once good constants are found, you often
don't need to touch raw logprobs directly again: many providers expose a
`logit_bias` (or similarly named) API parameter that applies exactly this
kind of per-token shift for you at generation time, without needing to
post-process returned logprobs by hand.

This is a narrower, single-classification-decision instance of the same
threshold-tuning idea [completion confidence scoring](completion-confidence-scoring.md)
applies to whole-completion confidence more generally, and it depends on
avoiding the [shared token prefix trap](shared-token-prefix-trap.md) first —
calibration is meaningless if the compared probabilities were already
distorted by prefix compounding. Use alongside
[logprob completion quality signals](logprob-completion-quality-signal.md) for
whole-completion confidence and
[intent classification for routing](intent-classification-for-routing.md) as a
typical consumer of a calibrated accept/reject decision.
