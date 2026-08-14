---
type: concept
title: Bayesian Updating with Base Rates
description: >
  Combining prior base-rate beliefs with diagnostic evidence via Bayes's rule
  to reach calibrated posterior probabilities.
sources:
  - title: Thinking, Fast and Slow
    resource: "Thinking, Fast and Slow (Kahneman), ch. 14"
---

Bayes's rule formalizes how beliefs should change in light of evidence: prior
beliefs ([base rates](base-rate-neglect.md)) combine with the evidence's
*diagnosticity* — the degree to which it favors one hypothesis over
alternatives.

Worked example (Tom W): if 3% of graduate students are in computer science and
Tom W's description is judged 4× more likely for a computer-science student
than for others, the posterior probability is ~11%. If the base rate were 80%
instead, the posterior would be 94.1%. Base rates matter even given
case-specific evidence — a fact that is not intuitively obvious.

Intuitive impressions of diagnosticity are themselves often flawed; formal
updating corrects [representativeness-based](representativeness-heuristic.md)
overreaction to stereotype-matching evidence.

Probability logic constraints follow from the same framework: if P(rain
tomorrow) = 40%, then P(no rain) = 60%, and P(rain tomorrow morning) cannot
exceed 40%; if P(elected first time) = 30% and P(reelected | elected once) =
80%, then P(elected twice in a row) = 24%.
