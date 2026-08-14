---
type: concept
title: Canary Population and Duration Selection
description: >
  Sizing a canary is a trade-off between statistical confidence and how
  much error-budget risk the canary itself consumes, tuned against the
  system's real historical failure patterns rather than worst-case theory.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Canary Population and Duration Selection

Sizing and timing a [canary release](canary-release.md) is a balance of
several, often conflicting, dimensions:

- **Duration must fit release cadence** — weekly releases can afford long
  canaries; releases shipping tens of times a day need short ones.
- **Run only one canary at a time** — simultaneous canaries add cognitive
  load and risk one canary's signal contaminating another's.
- **Size/duration must be statistically representative** — long/large
  enough to be more than a handful of queries.
- **Traffic volume** — more homogeneous traffic needs a smaller sample to
  be representative; heterogeneous traffic needs more.
- **Time of day** — performance defects often only manifest under peak
  load; canarying off-peak can hide a real regression.
- **Metrics being evaluated** — some metrics (e.g. queue depth) need larger
  populations or longer windows for a clear signal than others (e.g. a
  simple success ratio); see [canary metric selection](canary-metric-selection.md).

A useful sizing heuristic: canary risk to the error budget is
approximately

    canary population fraction × defect failure rate × canary duration

i.e. risk scales with canary size, not full-fleet size — canarying a
100%-failure-rate bug to 5% of traffic costs roughly 5% of the blast
radius a full rollout would have cost. The model deliberately assumes
worst case (100% failure) and uniform load; use the simplest model that
meets business needs rather than over-engineering the risk estimate, since
more sophisticated models have diminishing returns.

Tune canary parameters against the system's own real historical failure
patterns, not just worst-case theory — a system whose regressions
historically show up only under peak load needs a duration/timing rule
theory alone wouldn't suggest.
