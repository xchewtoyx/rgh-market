---
type: concept
title: Logprob Completion Quality Signal
description: >
  Use average token logprobs (or early-token probabilities) as a relative
  confidence signal to gate show/warn/retry/escalate decisions in the harness.
sources:
  - title: Prompt Engineering for LLMs
    resource: "Prompt Engineering for LLMs (Berryman), ch. 7"
---

Models expose next-token **logprobs** (log probability; more negative = less
likely) at little or no extra compute when the API supports them. Treat them as
the model’s “tone of voice” for harness control — not as absolute truth.

**Scoring a completion:** summing logprobs degrades with length (paraphrase
choice halves probability without lower quality). Prefer **mean logprob**
(sum / token count), or — stronger when available — the mean of **early-token
probabilities** \(\mathrm{mean}(\exp(\mathrm{logprob}_i))\) over the first few
tokens. Use relative cutoffs to:

1. Show corrections only when confident.
2. Warn when the model struggles more than usual.
3. Fetch more context or retry on low confidence.
4. Escalate to a stronger model under
   [LLM model selection criteria](llm-model-selection-criteria.md) /
   [model router](model-router.md).
5. Interrupt the user with proactive help only at high certainty.

For higher quality at higher cost: raise temperature, sample \(n\) completions,
pick the best by these scores. Rule of thumb: if \(n > 1\), use temperature
\(> 0\); roughly \(T \approx \sqrt{n}/10\). Factor logprob availability into
model choice — some commercial APIs disable them. Pair with
[consistency-as-uncertainty](consistency-as-uncertainty-signal.md) when voting
across samples, and with
[logprob classification calibration](logprob-classification-calibration.md) for
fixed-label decisions.
