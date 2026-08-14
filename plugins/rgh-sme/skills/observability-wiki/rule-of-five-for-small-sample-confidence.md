---
type: concept
title: The Rule of Five for Small-Sample Confidence
description: A random sample of just five values from any population has a 93.75% chance that the population's true median falls between the sample's smallest and largest value — a cheap way to bound plausible values when investigating a low-traffic service or a short time window with very few data points.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything (Douglas W. Hubbard), ch. 3"
---

The **Rule of Five**: for any population, a random sample of just five values has a 93.75% chance that the population's true median lies between the smallest and largest value in that sample. The derivation is simple — any single random draw has a 50% chance of landing above the true median (like a coin flip), so the chance all five draws land above it is 0.5⁵ ≈ 3.125%, and the same for all landing below; 100% minus those two tail cases leaves 93.75% coverage in between. This holds regardless of how large the underlying population is — the common intuition that five samples is "too small a fraction" of a large population to say anything is a misconception; the rule's accuracy depends on the sample being random and the population size, not on the sample being some minimum *percentage* of it.

This matters directly for debugging low-traffic services or short observation windows, where [percentile metrics need a sample-size floor to mean anything](latency-percentiles-not-averages.md) — a p95 or p99 is unreliable with only a handful of data points, but the plain min/max range of even five requests still bounds the plausible median with reasonable confidence. When investigating an issue on a service that only received five requests in the window you can inspect, the Rule of Five is the honest thing to say about what that data does and doesn't tell you: it brackets the typical case reasonably well, but says nothing about tail behavior, and any single one of those five requests could itself be the outlier rather than representative. For a success-ratio metric like an SLI, where a defensible prior belief about typical reliability is available, [Bayesian estimation](bayesian-estimation-of-sli-values.md) can fold that prior in to sharpen the estimate rather than relying only on this prior-free bound.

The rule is a statement about the **median**, not the mean, and it doesn't correct for sampling bias (e.g., a time window that systematically overrepresents a particular kind of request) — it only tells you how much confidence a genuinely random small sample earns you, not whether your five observations were actually drawn at random from the population you care about.
