---
type: concept
title: Rule of Five
description: A random sample of just five observations from any population is already 93.75% likely to bracket that population's true median between its smallest and largest values.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 3"
---
# Rule of Five

> There is a 93.75% chance that the median of a population lies between the smallest and largest values in any random sample of five drawn from that population.

Derivation: the chance any single random draw falls above the true population median is 50% (by definition of median). The chance all 5 draws land above the median is 0.5^5 = 1/32 ≈ 3.125% (same for all landing below). So the chance the sample *fails* to bracket the median is about 2 × 3.125% = 6.25%, leaving 93.75% that it succeeds. This holds regardless of the population's size — it works identically for a population of 30 or 30 million, and for an infinite population — because the derivation never uses population size, only the definition of "median."

## Why This Matters for Verification
A common objection to a small sample ("five people is nowhere near a large enough fraction of ten thousand") is a misconception: fractional sample coverage is irrelevant to what a random sample can tell you about a median. If this objection were valid, no measurement in biology, physics, or polling would be possible given how astronomically large most real populations are relative to any feasible sample.

## Caveats
- The rule bounds only the **median**, not the mean, variance, or tails of the distribution.
- It assumes the sample is genuinely random — it does not correct for non-random selection effects (e.g., a commute-time survey that under-samples people with unusually long commutes) or for known systematic biases in what's being measured. See [sampling and measurement bias](sampling-and-measurement-bias.md).

## Verification Action
When a draft dismisses a small sample (n≈5) as uninformative purely because it is a tiny fraction of a large population, check whether that's actually true for the specific quantity being estimated — for a population median specifically, a random sample of five already carries meaningful evidentiary weight, and the "fraction of the population" framing is not the right lens to argue otherwise.

## See Also
- [Single Sample Majority Rule](single-sample-majority-rule.md)
- [Sampling and Measurement Bias](sampling-and-measurement-bias.md)
- [Mean vs. Median Selection](mean-vs-median-selection.md)
