---
type: concept
title: Simple Models Beating Expert Judgment
description: >
  Equal-weight linear formulas and checklists often outperform expert judgment
  in low-validity environments because they are simpler and more consistent.
sources:
  - title: Thinking, Fast and Slow
    resource: "Thinking, Fast and Slow (Kahneman), ch. 21"
---

Experts underperform algorithms for two reasons:

1. **Complexity hurts.** Experts combine features in clever, complex ways that
   reduce validity more often than they help. Simple combinations of features
   are better. Human judges given a formula's score still overrule it, believing
   they have extra case-specific information — and are wrong more often than not.
   The **broken-leg rule** is the exception: override a formula (e.g. predicting
   whether someone goes to the movies tonight) only on decisive, rare information
   (a broken leg), not on routine impressions.

2. **Humans are inconsistent.** Given the same information twice, experienced
   radiologists contradict themselves on the same chest X-ray 20% of the time;
   similar inconsistency appears across auditors, pathologists, psychologists, and
   managers. Unreliable judgments cannot be valid predictors. Formulas return
   the same answer for the same input.

Robyn Dawes showed that selecting predictors with some validity, standardizing
them, and combining with **equal weights** predicts about as well as optimal
regression — often better, since regression weights are distorted by sampling
accidents. Useful algorithms can be built "on the back of an envelope." Example:
marital stability ≈ (frequency of lovemaking) − (frequency of quarrels).

The **Apgar score** (Virginia Apgar, 1953): five variables scored 0/1/2 one
minute after birth replaced inconsistent clinical judgment of newborn distress;
still used daily and credited with reduced infant mortality.

Orley Ashenfelter's Bordeaux wine formula (summer temperature, harvest
rainfall, winter rainfall) forecasts mature prices with correlation > .90,
beating both wine experts and efficient-market theory.

Practical rule: in [low-validity environments](wicked-and-low-validity-environments.md),
leave final decisions to formulas — especially when interviewers or tasters add
misleading subjective impressions. See [Meehl clinical vs statistical prediction](meehl-clinical-vs-statistical-prediction.md).
