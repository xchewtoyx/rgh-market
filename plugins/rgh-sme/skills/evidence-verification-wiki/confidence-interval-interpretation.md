---
type: concept
title: Confidence Interval Interpretation
description: >
  A frequentist confidence interval is a statement about the interval-construction
  procedure, not the probability that a fixed parameter lies inside one observed interval.
sources:
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 7"
---
# Confidence Interval Interpretation

A **95% confidence interval** is often misread as "there is a 95% probability the true parameter lies in this interval." In the frequentist framing, that reading is wrong: the parameter is treated as fixed, and the interval is what varies across repeated experiments. The correct statement is procedural — if the same experiment were repeated many times and a 95% interval computed each time, about 95% of those intervals would contain the true (fixed) parameter.

## Common Misuses to Flag

- Treating an interval as a posterior probability statement about the parameter without a Bayesian model or independent prior reasoning — the same class of error as [p-value misinterpretation](p-value-misinterpretation.md).
- Using "fair value falls inside the interval, so we can't reject fairness" without noting that a true null will fail to be rejected at the nominal rate when intervals are misapplied (e.g., substituting a point estimate for an unknown standard deviation in the variance formula is a common shortcut that is "not entirely justified" but widespread).
- Presenting a bare point estimate with no interval at all when the underlying measurement is genuinely uncertain — see [measurement as uncertainty reduction](measurement-as-uncertainty-reduction.md).

## Verification Action

When a draft states a confidence interval and then asserts a probability about the parameter ("we are 95% sure p is between …"), rewrite mentally to the procedural claim or flag the leap. When a decision hinges on whether a reference value (0, a baseline rate, a fairness threshold) lies inside the interval, check that the interval method matches the claim (sample size, substitution of estimated variance, one- vs two-sided logic) rather than treating "inside the interval" as automatically equivalent to "verified unchanged."
