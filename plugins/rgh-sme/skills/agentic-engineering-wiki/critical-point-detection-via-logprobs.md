---
type: concept
title: Critical Point Detection via Logprobs
description: >
  Requesting logprobs on the prompt itself, not just the completion, surfaces
  surprising, anomalous, or high-information-density passages in the input.
sources:
  - title: "Prompt Engineering for LLMs"
    resource: "Prompt Engineering for LLMs (John Berryman), ch. 7"
---

Some APIs support an `echo`-style parameter that returns
[logprobs](logprobs-fundamentals.md) for the *prompt* tokens too, not just
the completion — useful even without requesting any completion token at all.
This surfaces surprising or anomalous parts of input text, including typos: a
typo that produces an unusual token split (getting only a fragment of the
intended word as one token, followed by an unexpected continuation) shows up
as an abnormally low logprob at that point, flagging exactly where something
odd happened without needing any separate spell-checking pass. More
generally, logprobs on the prompt reveal higher-information-density passages
— useful for directing an application's or a user's attention toward the
parts of a document that are actually saying something unexpected, as
opposed to boilerplate or highly predictable filler.

Practical thresholds are fuzzy: negative single-digit logprobs are fairly
common in ordinary text, while negative double-digit logprobs usually
indicate the model finding something genuinely odd — but there's no fixed
universal threshold, and the right cutoff varies by model, by genre, and even
within a single text (logprobs tend to run lower near the start of a
document than toward the end, since topic and style only become predictable
once the model has read enough of the document to establish them).

One operational warning: logprobs are not perfectly deterministic due to
floating-point behavior in the underlying computation — they can vary by as
much as roughly ±1 depending on model deployment details, even for the exact
same input. Any [evaluation](eval-test-granularity.md) or automated check
built on logprob thresholds should tolerate this variation, or mock the
model's logprob output entirely rather than asserting on exact values.
