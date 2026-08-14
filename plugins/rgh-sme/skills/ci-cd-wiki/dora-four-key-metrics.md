---
type: concept
title: DORA Four Key Metrics
description: >
  Four outcome-based, global metrics — deployment frequency, lead time for
  changes, mean time to restore, and change failure rate — that together
  measure a delivery pipeline's tempo and stability without being locally gameable.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 1, 2"
---

# DORA Four Key Metrics

Two tempo metrics and two stability metrics, chosen because each is global
(measures the whole delivery system's output, not a team's internal process)
and outcome-based (not gameable the way
[output metrics](output-vs-outcome-metrics.md) are):

- **Deployment frequency** (tempo): how often code is deployed to production.
  Acts as an operational proxy for batch size — deployment frequency is
  roughly inversely proportional to batch size, so higher frequency directly
  implies smaller batches, which reduces
  [cycle time](cycle-time.md) and flow variability.
- **Lead time for changes** (tempo): time from code commit to that code
  running in production — the same measure as
  [cycle time](cycle-time.md), scoped specifically to the delivery phase
  (commit onward) rather than the more variable "fuzzy front end" of product
  design.
- **Mean time to restore (MTTR)** (stability): how quickly full service is
  restored after a production incident. Assumes failure is inevitable in
  complex systems and measures recovery speed rather than trying to prevent
  all failure.
- **Change failure rate** (stability): the percentage of production changes
  that cause degradation, an outage, or require immediate remediation
  (hotfix, rollback, patch).

## Performance clusters (2017 benchmark)

- **High performers**: on-demand deploys (multiple/day), lead time under an
  hour, MTTR under an hour, change failure rate 0–15%.
- **Medium performers**: deploys weekly-to-monthly, lead time 1 week–1 month,
  MTTR under a day, change failure rate 31–45%.
- **Low performers**: deploys every 1–6 months, lead time 1–6 months, MTTR
  1 day–1 week, change failure rate 46–60%.

Medium performers sometimes show a *higher* failure rate than low performers —
this shows up during active transformation, when a team pushes tempo up before
the testing/deployment automation (the
[test automation pyramid](test-automation-pyramid.md),
[deployment pipeline](deployment-pipeline.md) gates) is in place to support
it, accumulating technical debt and instability faster than it ships
capability.

See [the speed/stability trade-off myth](speed-stability-tradeoff-myth.md) for
why high performers don't sacrifice one pair of metrics for the other.
