---
type: concept
title: Non-Conclusive Evidence Still Shifts Probability
description: Several popular epistemic maxims claim a non-conclusive observation tells you nothing, but Bayes' theorem shows any observation that would be conclusive if it went the other way must shift belief even when it doesn't.
sources:
  - title: "How to Measure Anything: Finding the Value of Intangibles in Business"
    resource: "How to Measure Anything, 3rd ed. (Douglas W. Hubbard), ch. 10"
  - title: "Data Modeling with Snowflake"
    resource: "Data Modeling with Snowflake (Serge Gershkovich), ch. 7"
---
# Non-Conclusive Evidence Still Shifts Probability

Several widely repeated maxims assert that an inconclusive, negative, or partial observation carries zero evidentiary weight. Bayes' theorem shows these are false as literally stated, though a weaker, correct version of each survives. The shared underlying mathematical fact: if a *positive* result would fully confirm a hypothesis (probability 1), the law of total probability mathematically forces a *negative* or absent result to still shift the prior probability in the opposite direction — just not all the way to certainty. Only proof, not evidence, is actually being denied by a non-conclusive result.

## The Maxims and Their Correct Versions
- **"Absence of evidence is not evidence of absence."** False as stated: if failing to find something (e.g., a weapons program) would be impossible were the thing present, and you look and don't find it, that failure to find it does mathematically raise the probability of absence — not to certainty, but genuinely. The defensible version is "absence of evidence is not *proof* of absence."
- **"Ambiguous or negative results tell us nothing."** Traced to old diagnostic literature ("a positive result is evidence of disease, but a negative result is not evidence either way"). Structurally the same error: a negative result still shifts the prior via the same total-probability logic, unless the positive and negative outcomes happen to be exactly equally likely a priori regardless of the truth — a genuinely symmetric edge case that is rare in real problems.
- **"This alone tells me nothing; I need to know many other things first."** If a single variable (e.g., a product's category, before price or marketing plan is known) changes your assessment under *any* combination of the other still-unknown variables, it carries information in isolation too — you don't need the full picture before a partial fact can move your estimate. (Knowing only that someone smokes, with zero other health information, still legitimately changes a life-expectancy estimate.)

## Why This Matters for Verification
A reviewer or source dismissing an inconclusive test, a negative result, or a single partial fact as "telling us nothing" is making a specific, checkable logical claim — and that claim is usually wrong. The correct move is not to treat the non-conclusive evidence as proof either, but to size how much it should shift the estimate, rather than rounding it down to zero information value.

The same asymmetry shows up in checking whether a database column is a valid unique key by querying for duplicates in existing data: finding none does not *prove* the column is unique (a future or unobserved row could still violate it), but it is real, informative evidence in favor of uniqueness — worth recording as a supporting finding rather than dismissed as inconclusive, while still being honest that only an authoritative source (here, a declared constraint, or confirmation from whoever owns the business rule) can settle the question conclusively.

## Verification Action
When a draft or a source declares that an inconclusive, negative, or single partial observation "doesn't tell us anything," check whether a positive/conclusive version of the same observation would have been treated as informative. If so, the actual negative/partial result must also carry some evidentiary weight in the opposite direction by the same logic, and the "tells us nothing" framing should be corrected to something calibrated, like [hedge words for uncertain claims](hedge-words-for-uncertain-claims.md), rather than accepted as a full dismissal.

## See Also
- [Correlation vs. Causation](correlation-vs-causation.md)
- [Bayesian Inversion Technique](bayesian-inversion-technique.md)
- [Publication Bias](publication-bias.md)
