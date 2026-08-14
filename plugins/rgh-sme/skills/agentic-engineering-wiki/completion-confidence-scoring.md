---
type: concept
title: Completion Confidence Scoring
description: >
  Average a completion's token logprobs into a confidence signal that can
  drive application behavior, without treating it as an absolute quality score.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

[Logprobs](logprobs-fundamentals.md) work as the model's "tone of voice": the
same way a confident expert answers instantly while an unsure guesser
hedges, a model's per-token probabilities signal how reliable a completion
likely is, even without knowing the right answer independently.

Summing logprobs across a whole completion gives an overall confidence
figure, but accuracy degrades with length — many equally-good phrasings of
the same idea ("for example" versus "for instance") can halve the summed
probability without indicating any real drop in quality, simply because
summing keeps adding negative numbers regardless of whether each token choice
was actually uncertain. **Averaging** is better: a simple average (sum of
logprobs divided by token count) is effective, especially when there's no
time or data to experiment further. A more refined approach found useful in
practice: average the *probabilities* (not the logprobs themselves) of the
completion's earliest tokens — `(exp(logprob_1) + … + exp(logprob_n)) / n` —
which tends to be more predictive of overall quality than averaging the raw
logprobs.

This average is not an absolute quality measure — it needs calibrating per
model and task before the numbers mean anything — but it's useful as a
logprob-based cutoff driving concrete application behavior:

1. Only surface a suggested correction when confidence is high.
2. Show a warning when the model is struggling more than usual.
3. Pull in more context or retry the request when confidence is low.
4. Escalate to a more capable (and more expensive) model for a better result,
   the same escalation [model tiering](model-router.md) makes on other
   grounds.
5. Only interrupt the user with proactive assistance when certainty that the
   interruption is actually needed is high — an unwanted assistant popping up
   uninvited is worse than staying silent.

For higher quality at higher compute cost, another lever is generating
multiple completions at a raised temperature and picking the best one by
logprobs — as a rough rule of thumb, only raise `n` above 1 if temperature is
also raised above 0 (otherwise every completion comes out identical), with
temperature roughly scaling as `sqrt(n) / 10`.
