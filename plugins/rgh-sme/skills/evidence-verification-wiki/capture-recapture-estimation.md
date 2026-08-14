---
type: concept
title: Capture-Recapture Estimation
description: Estimating the size of a hidden or uncountable population by taking two independent samples and measuring how much they overlap — the smaller the overlap, the larger the true population.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 9"
---
# Capture-Recapture Estimation

Originating in wildlife biology (tag a sample of fish, release them, later catch a second sample and see what fraction is tagged), **capture-recapture estimation** infers the size of a population that cannot be directly counted from the overlap between two independent samples of it. If 1,000 fish are tagged and a later catch of 1,000 fish contains 50 tagged individuals (5%), the total population is estimated at 1,000 / 0.05 = 20,000 — the smaller the recapture rate, the larger the inferred total. Standard binomial-proportion error math applies to bound the estimate's confidence interval.

## Generalization Beyond Wildlife
The same logic applies to any situation where two independent detection processes can be compared for overlap: estimating a census undercount, the number of undiscovered species in a region, the number of undetected intrusions into a system, or the size of an unadvertised prospective-customer base. The general pattern for a verifier: **run (or find) two independent detection processes over the same hidden population and measure their overlap** — for example, comparing how many defects two independent QA reviewers each caught individually versus how many both caught mirrors the tagged/untagged fish math exactly, and can be used to estimate the total number of defects still undetected by either reviewer.

## Why This Matters for Verification
A claim that some hidden or hard-to-count quantity (undetected fraud cases, unreported incidents, total defects in a system) is "unknowable" or "impossible to estimate without a full audit" is often false — if two even partially independent detection efforts already exist or can be cheaply run, their overlap alone yields a defensible estimate of the undetected remainder, without needing an exhaustive census.

## Verification Action
When a document claims a quantity is unmeasurable because the full population can't be directly counted, check whether two independent, even partial, detection or sampling efforts exist (or could be run cheaply) over that population. If so, their overlap rate can produce a genuine estimate and confidence interval for the true total, including the undetected remainder — treat a claim of "no way to know how many we're missing" as often false when this method is available.

## See Also
- [Rule of Five](rule-of-five.md)
- [Sampling and Measurement Bias](sampling-and-measurement-bias.md)
