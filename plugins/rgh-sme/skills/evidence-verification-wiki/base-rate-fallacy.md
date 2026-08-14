---
type: concept
title: Base Rate Fallacy
description: Misjudging a positive test result's reliability by ignoring how rare the condition being tested for actually is in the population.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 9"
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 10"
---
# Base Rate Fallacy

A test's accuracy alone does not determine how reliable a positive result is — the underlying prevalence (**base rate**) of the condition in the tested population matters just as much, and is often ignored. This is the same structural error as the [conditional probability inversion](conditional-probability-inversion.md) that produces the prosecutor's fallacy.

## Worked Example
A diagnostic test with a 5% false-positive rate, applied to a condition with a true prevalence of only 1 in 1,000, yields a **positive predictive value under 2%** even after a positive result — because out of 10,000 people tested, roughly 10 true positives are swamped by roughly 500 false positives. The same test with the same 5% false-positive rate, applied to a much more common condition (roughly 20% prevalence), instead yields a positive predictive value around 5-in-6. Identical test accuracy produces wildly different real-world reliability depending on the base rate alone.

## Verification Action
When a draft cites a test's sensitivity/specificity or false-positive rate to support a claim about how likely a positive result is to be a true positive, check whether the underlying base rate/prevalence of the condition is also accounted for. A test can be individually accurate and still produce a result that is more likely wrong than right, purely because the thing being tested for is rare.

## Worked Example: Descriptive Traits vs. Group Size
The same fallacy appears without any explicit "test" at all: told that a randomly picked person from a room of 95 lawyers and 5 pediatricians "loves children and science," most people guess pediatrician — ignoring that even a modest 10% of lawyers sharing that trait would still outnumber the pediatricians in absolute terms (9.5 vs. 5). The group-size base rate has to be weighed against the trait's descriptive fit, not overridden by it; a vivid, matching description feels like stronger evidence than a dry population ratio, but the ratio often dominates the correct answer. Simple awareness that the base rate needs to be weighed at all measurably reduces this error, and explicitly stating each conditional probability involved (and checking them for mutual consistency) reduces it further.

## Application to the Scientific Literature
The same logic applies to published research as a whole: if most hypotheses that get tested are, a priori, unlikely to be true (a "rare condition"), then even a low false-positive rate in individual studies means a large share of *published, statistically significant* findings will still be false positives. See [publication bias](publication-bias.md) for how this combines with selective publication to further inflate the apparent reliability of a body of literature.

## See Also
- [Conditional Probability Inversion](conditional-probability-inversion.md)
- [P-Value Misinterpretation](p-value-misinterpretation.md)
