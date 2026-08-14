---
type: concept
title: Bayesian Inversion Technique
description: When the probability you actually need is hard to estimate directly, estimate the easier reverse conditional probability instead and use Bayes' theorem to invert it into the answer you need.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 10"
---
# Bayesian Inversion Technique

Directly estimating "what's the probability this claim is true, given what I've observed?" is often hard. **Bayesian inversion** answers the easier reverse question instead — "if the claim were true, what's the probability I'd see this particular observation?" (and the same for it being false) — then uses Bayes' theorem to algebraically invert that into the probability actually needed. This is the deliberate, correct use of the same reverse-conditional relationship that produces [conditional probability inversion](conditional-probability-inversion.md) as an error when the two directions are confused rather than properly converted.

## Mechanics
Given a prior P(claim), and the two conditional probabilities P(observation | claim) and P(observation | ~claim) — both usually easier to estimate directly than the reverse — Bayes' theorem computes P(claim | observation). Worked structure: a product's prior chance of a strong first year (40%, from history) combined with how likely a positive test-market result is if the product does well (80%) versus if it doesn't (30%) inverts into a revised probability of a strong first year given an observed positive test result (64%, up from the 40% prior) or given a negative one (16%, down from 40%).

## Why This Matters for Verification
When a source or expert states a confidence level or probability, check whether they arrived at it by estimating the (hard) direct question or by estimating the (easier) reverse conditional and inverting correctly. A stated confidence that skips this inversion — for instance, treating "how likely is this test to catch a real effect" as if it directly answered "how likely is the effect real given a positive test" — has likely substituted the easy question for the hard one without doing the conversion, which is exactly the [conditional probability inversion](conditional-probability-inversion.md) error.

## Verification Action
When evaluating or eliciting a probability estimate for a claim, prefer decomposing it into the reverse conditional (how likely is this evidence if the claim is true/false) plus a prior, and perform the inversion explicitly, rather than accepting a direct gut-feel estimate of the forward probability. This also gives a reviewer a concrete way to challenge an unsupported confidence figure: ask what P(evidence | claim) and P(evidence | ~claim) the stated confidence implies, and check whether those implied values are themselves plausible.

## See Also
- [Conditional Probability Inversion](conditional-probability-inversion.md)
- [Calibrated Probability Assessment](calibrated-probability-assessment.md)
