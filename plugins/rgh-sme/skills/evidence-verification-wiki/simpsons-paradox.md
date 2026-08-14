---
type: concept
title: Simpson's Paradox
description: >
  An aggregate association between two variables can reverse or disappear once a
  confounding stratification variable is controlled for.
sources:
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 5"
---
# Simpson's Paradox

**Simpson's paradox** occurs when a trend visible in aggregated data reverses (or vanishes) within every meaningful subgroup once a confounding variable is accounted for. The aggregate comparison said one thing; each subgroup said the opposite.

## Worked Example: Coast vs. Friend Count
Aggregated data showed West Coast data scientists with higher average friend counts than East Coast colleagues — tempting causal stories about climate, culture, or lifestyle. Splitting by PhD status reversed the pattern in *both* buckets: among PhDs, East Coast averages were slightly higher; among non-PhDs, East Coast averages were much higher. The aggregate "West beats East" comparison was driven by composition: the East Coast sample skewed much more heavily toward PhD holders, and PhD holders had fewer friends overall.

## Why "All Else Equal" Fails Without Stratification
Correlation is often described as measuring a relationship "all else being equal." That assumption holds when group assignment is random (as in a well-designed experiment) but can fail badly when class membership follows a deeper pattern — without degree data, a reviewer might wrongly conclude one coast is "inherently more sociable." The only real defense is knowing the data well enough to check plausible [confounding variables](confounding-variables.md), not always possible from the headline aggregate alone.

## Verification Action

When a draft compares two groups on an outcome, ask what stratification variables could change the composition of those groups and whether subgroup tables were checked. A reversal across all major subgroups is strong evidence the aggregate comparison is misleading. Treat unexplained aggregate differences as provisional until confound checks are shown — see [experimental vs. observational causal evidence](experimental-vs-observational-causal-evidence.md) for when random assignment makes stratification less necessary.
