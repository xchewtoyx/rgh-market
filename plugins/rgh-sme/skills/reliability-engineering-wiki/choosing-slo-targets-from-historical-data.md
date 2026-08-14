---
type: concept
title: Choosing SLO Targets from Historical Data
description: >
  Basic descriptive statistics and percentiles over historical performance
  give a grounded starting point for an SLO target; without any history, an
  educated guess is fine as long as it's explicitly revisable.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
---

A basic statistics toolkit ("the five Ms") over a time-series sample informs
target-setting: min, max, mean, median, mode, plus range (max − min) as a
quick measure of dispersion.

**Percentiles** identify the value below which X% of observations fall (P50
= median, P90, P95, P99, P99.9…). Two uses: isolating outliers/long tails
without discarding them entirely, and directly informing a target — "our
historical P99 was X ms, so target maintaining ≤X ms at P99 going forward."
See [layered percentile SLO thresholds](layered-percentile-slo-thresholds.md)
for how these percentiles turn into an actual multi-tier SLO definition.

**Without history** (a new service, no users yet): make an educated guess,
informed by any dependencies' published SLOs, and remember an SLO is an
objective you can revise, not a permanent contract — set an initial target
from as little as two weeks of observed baseline once real traffic exists,
and treat the first target as provisional. See
[calibrated estimation for SLO targets](calibrated-estimation-for-slo-targets.md)
for how to turn that educated guess into an explicitly-uncertain range
rather than a single number presented as settled; where a genuinely
comparable existing system's real data is available, see
[comparability analysis for reliability prediction](comparability-analysis-for-reliability-prediction.md)
for adjusting that system's data instead of guessing from nothing. See
[SLO evolution triggers](slo-evolution-triggers.md) for how and when to
revisit it once real data accumulates.

Before committing to a candidate target, backtest it against historical data
to estimate resulting alert frequency — never set a target or alert
threshold without first estimating how often it would have fired against the
recent past. See
[SLO measurement infrastructure design goals](slo-measurement-infrastructure-design-goals.md).
