---
type: concept
title: P-Value Misinterpretation
description: The common error of reading a p-value as the probability a hypothesis is true, rather than as the probability of the observed data under the null hypothesis.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 9"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 9"
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 7"
---
# P-Value Misinterpretation

A p-value states the probability of observing data at least as extreme as what was measured, *assuming the null hypothesis is true* — it does not state the probability that the null hypothesis is false, and it does not state the probability that any specific alternative hypothesis is true. This is a specific instance of [conditional probability inversion](conditional-probability-inversion.md).

## Why the Confusion Matters
A p-value cannot, by itself, tell a reviewer how much to believe a claimed effect is real, because that depends on the *prior* plausibility of the alternative explanation — which the p-value doesn't measure. The same p-value can support very different conclusions depending on how plausible the alternative hypothesis was to begin with. A vanishingly unlikely alternative (e.g., a claim of genuine ESP) needs much stronger evidence to become credible than a mundane, independently plausible alternative (e.g., a claim that a small measurement drifted or a participant made an error) — even when both produce an identical p-value.

## Named Case: Media Reporting of a Physics Discovery
News coverage reported physicists as "more than 99 percent certain" of a discovery based on a p-value of 0.01 — directly conflating the p-value with the posterior probability the finding was real. In that specific case the conclusion happened to be correct, because physicists already had strong independent prior grounds to expect the result — but the stated reasoning (p-value = certainty) is invalid as a general inference, and the same fallacy in the opposite direction has been used to lend false credibility to claims with an intrinsically implausible alternative hypothesis.

## "Statistically Significant" Answers a Different Question Than the One That Matters
"Statistically significant" means, precisely and only, that the p-value fell below a chosen threshold (commonly .05) — it is not a synonym for "big," "important," or "probably true." The question a decision or claim actually needs answered — "what's the probability this effect is real?" — is different from the question classical significance testing answers — "assuming the effect isn't real, what's the probability of seeing data this extreme?" A result can be statistically significant and have essentially zero practical importance (a tiny, decision-irrelevant effect detected via a huge sample), and conversely a "non-significant" result from a small study can still meaningfully move an estimate's plausible range. Treat "statistically significant" and "important/decision-relevant" as two separate claims that both need independent support, not as synonyms — checking the size and real-world relevance of an effect is a distinct verification step from checking its p-value.

## No Universal Minimum Sample Size
There is no fixed sample size (30, 100, 600, and 1,000 have all been asserted at different times) that is "required" for a result to be meaningful. The often-cited "30" is simply the point where the t-distribution and normal distribution converge closely enough to use simplified tables — not a threshold for validity or significance. Whether a given sample size is adequate depends on the population's actual variability and on how the resulting uncertainty compares to a decision threshold, not on matching a remembered round number. Reject a claim that a sample is "too small to mean anything" (or, conversely, that a sample is "big enough" to trust) when it isn't backed by an actual calculation of the resulting confidence interval or margin of error.

## Distribution Assumptions Must Match the Inference
Many p-value calculations silently assume the test statistic is approximately normal (or otherwise drawn from a named distribution). Claims like "the chance of this happening at random is one in a million" are meaningless if the data are not roughly normal — or if the wrong distribution was used. Before accepting a p-value, check whether the document shows the data meet the assumed distribution (formal normality test, plot, or other justification), not just that the formula was applied.

## Verification Action
When a draft states a p-value and then asserts a probability of truth, certainty, or "proof" from it, treat that inferential leap itself as an unverified claim. Check whether the document's confidence is actually informed by independent prior evidence for the hypothesis, not just the p-value in isolation, and confirm the document isn't presenting a single significance test as more conclusive than it is — see [claim scope calibration](claim-scope-calibration.md). Separately, when a draft calls a result "significant" and treats that as settling whether the result matters, or dismisses a small-sample result as inherently unreliable with no calculation behind the dismissal, flag both as unsupported inferential leaps. When a p-value rests on a normal approximation, verify the approximation is justified for that sample and data shape — an unjustified distribution assumption makes the stated probability as unreliable as a misread [confidence interval interpretation](confidence-interval-interpretation.md).

## See Also
- [Conditional Probability Inversion](conditional-probability-inversion.md)
- [Cherry-Picking](cherry-picking.md)
