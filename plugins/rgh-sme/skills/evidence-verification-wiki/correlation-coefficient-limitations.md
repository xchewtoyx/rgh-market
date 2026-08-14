---
type: concept
title: Correlation Coefficient Limitations
description: >
  What a correlation coefficient does and does not establish — including sensitivity
  to outliers, blindness to nonlinear relationships, and silence on practical magnitude.
sources:
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 5"
---
# Correlation Coefficient Limitations

A Pearson-style **correlation coefficient** summarizes *linear* co-movement on a -1 to +1 scale. It is useful for screening relationships but easy to over-read during verification.

## Outlier Sensitivity
A single extreme point can materially change the coefficient. In one worked dataset, one verified bad record (an internal test account, not a real user) weakened an otherwise stronger positive correlation; removing that documented outlier roughly doubled the coefficient. Reviewers should ask whether outliers were identified, why they were kept or excluded, and whether exclusion was decided before or after seeing the correlation — see [cherry-picking](cherry-picking.md).

## Zero Correlation ≠ No Relationship
Correlation near zero only rules out a *linear* relationship, not every deterministic link. Example pattern: `y = |x|` can have zero correlation even though y is a perfect function of x — because correlation asks whether above/below-mean positions on x align with above/below-mean positions on y, not whether any functional form exists.

## Magnitude vs. Practical Significance
Perfect or near-perfect correlation can still describe a relationship too small to matter for the decision at hand — two variables moving together in tiny absolute steps may be statistically aligned but operationally irrelevant. Conversely, a "weak" correlation can still be decision-relevant when the stakes or base rates make small shifts important. Do not treat the coefficient alone as a verdict on importance — see [evidence strength vs. effect magnitude](evidence-strength-vs-effect-magnitude.md).

## Verification Action

When a draft cites a correlation coefficient as evidence, check (1) outlier handling, (2) whether a nonlinear relationship was plausibly possible but untested, and (3) whether practical significance was argued separately from statistical association. Pair coefficient claims with [correlation vs. causation](correlation-vs-causation.md) review whenever a causal story is implied.
