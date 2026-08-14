---
type: concept
title: Catch-Up-Time Deadline Alerting
description: >
  For a long-running job with a hard deadline, alert on projected lateness
  (current elapsed time plus estimated catch-up time versus the deadline)
  rather than on every fluctuation in progress, to surface a likely miss far
  enough ahead to act on it.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

Some pipeline work — a model training run, a large batch job — spans many
hours or days against a hard deadline, which is itself a
[freshness SLI](pipeline-sli-types.md) ("job completes within Y"). Naively
alerting on every dip in progress rate is too noisy to be useful across a
run that long. The more useful signal is projected lateness: track how much
**catch-up time** would be needed to finish on schedule at the current rate,
and alert when `current time + catch-up time` exceeds the deadline — this
surfaces a likely miss while there's still time to react, rather than only
once the deadline has already passed.

Worked example: a 20-hour build against a 24-hour deadline progresses
normally for 8 hours, then stalls for 4 hours. At that point 12 wall-clock
hours have been consumed with 12 hours of deadline remaining; resuming at the
previous rate would need roughly 12 more hours of work, which is likely to
blow the deadline. Catching this 12 hours in — rather than waiting to see if
the deadline is actually missed — is the value of the technique.

This is the same underlying idea as [burn rate](burn-rate.md) — projecting
forward from a current consumption rate to catch a slow-developing problem
before it fully manifests — applied to a deadline-style freshness SLI instead
of an error-ratio SLI measured over a rolling window.
