---
type: concept
title: Statistical Type Errors and Power
description: >
  How significance thresholds trade off false-positive (type 1) and false-negative
  (type 2) errors, and why power depends on specifying what "false" concretely means.
sources:
  - title: "Data Science from Scratch, 2nd Edition"
    resource: "Data Science from Scratch, 2nd ed. (Joel Grus), ch. 7"
---
# Statistical Type Errors and Power

Classical hypothesis testing accepts a controlled rate of **type 1 errors** (false positives): rejecting a null hypothesis even though it is true. Conventionally this **significance** level is set at 5% or 1%. A two-sided test at 5% significance rejects when the observed statistic falls outside the central 95% of the distribution assumed under the null — so if the null is true, roughly one run in twenty will incorrectly reject it anyway.

**Type 2 errors** (false negatives) are the mirror failure: failing to reject the null when it is actually false. **Power** is one minus the type 2 error rate — the probability of correctly detecting an effect when one exists. Power is not a property of the test alone; it requires specifying what "the null is false" means in concrete terms (e.g., not merely "p ≠ 0.5" but "p = 0.55").

## One-Sided vs Two-Sided Tests Change the Tradeoff

A one-sided test concentrates rejection in one tail of the null distribution, so it can be more powerful against a directional alternative at the same significance level — it stops rejecting outcomes that are implausible under the stated alternative anyway. Reviewers should check whether a one-sided test matches the claim being made; a claim of "different in either direction" needs a two-sided test, not a one-sided test chosen because it clears significance more easily.

## Verification Action

When a draft cites a significance threshold or "95% confidence" in a hypothesis test, check whether the document acknowledges the built-in false-positive rate at that threshold — a procedure set to reject at 5% will produce roughly 5% false positives even when nothing real is going on, which is why lone significant results after many tries are weak evidence (see [cherry-picking](cherry-picking.md)). When a draft claims a study was "underpowered" or "powerful," check that power was computed against a specific alternative effect size, not a vague "not null" statement.
