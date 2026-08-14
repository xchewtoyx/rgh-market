---
type: concept
title: Anchoring Bias in Examples
description: >
  Few-shot examples set an expectation that skews completions toward the
  examples' implied distribution, whether or not that was intended.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 5"
---

Few-shot examples don't just teach a pattern — they anchor the model's
expectations. This mirrors the cognitive-science bias of the same name: an
initial, incomplete piece of information sets an expectation that unduly
influences later judgment. Demonstrated with wildly different "how old does
this name sound" completions depending on whether the prompt's examples
anchored to early-20th-century versus early-21st-century names.

Anchoring can't be fully avoided — even a fully representative set of
examples still communicates an expectation, and any probability distribution
the examples imply over outputs shapes the completion. A rating-prediction
prompt showing each star rating (1 through 5) exactly once could wrongly imply
they're equally likely, when in reality 5-star ratings are the most common in
the real distribution — so an uninformed guess should lean toward 5, not
toward the middle. The mitigation is to draw examples from a representative
sample of real past cases when one is available, rather than constructing a
tidy, artificially balanced set. Matching the real distribution gets harder as
outputs get more complex, since length, vocabulary, and other output
properties each have their own distribution to match.

A moderate amount of anchoring bias is actually desirable, not just a risk to
minimize: including edge cases as [few-shot examples](few-shot-example-formatting.md)
is an effective way to teach the model how to handle exceptions it would
otherwise mishandle unpredictably. Aim to cover all the major classes of case
the task will encounter, without over-representing exotic ones relative to
how often they actually occur.
