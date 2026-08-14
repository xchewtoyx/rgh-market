---
type: concept
title: Data Censoring
description: When a study's observation window ends before an outcome has occurred for some subjects, dropping or misclassifying those still-ongoing cases and skewing the result.
sources:
  - title: "Calling Bullshit: The Art of Skepticism in a Data-Driven World"
    resource: "Calling Bullshit (Carl T. Bergstrom, Jevin D. West), ch. 6"
---
# Data Censoring

**Right-censoring** occurs when a data collection window ends before an outcome (death, failure, resolution) has happened for some subjects in the sample — a naive analysis that only counts subjects for whom the outcome has already occurred, while dropping or excluding the still-ongoing cases, produces a systematically skewed result.

## Worked Example
Tracking the age at which members of different cohorts die will understate lifespan for any cohort whose still-living members haven't died yet by the time the study window closes — those survivors get dropped from a naive "age at death" calculation, making a recently-started cohort look artificially short-lived compared to an older cohort whose members have mostly already died and so are fully represented. The same mechanism explains why "average age at death" statistics broken out by category can make a newer category look artificially young-dying: most of that category's members are still alive and thus structurally excluded from an age-at-death calculation, while an older category's statistic is built from a much more complete (less censored) set of outcomes.

## Verification Action
When a draft reports an outcome statistic (average time-to-event, failure age, resolution time) computed from a dataset with an observation cutoff, check whether ongoing/unresolved cases were excluded from the calculation rather than properly accounted for. A category, cohort, or population that is newer, younger, or more recently started will be disproportionately distorted by this exclusion — flag any age-at-outcome or time-to-outcome statistic that doesn't explicitly address how still-ongoing cases were handled.

## See Also
- [Selection Bias](selection-bias.md)
- [Claim Scope Calibration](claim-scope-calibration.md)
