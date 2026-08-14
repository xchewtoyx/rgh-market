---
type: concept
title: Burn Rate
description: >
  The speed at which a service is consuming its error budget relative to
  what's sustainable, expressed as a multiple of the rate that exactly
  exhausts the budget at the end of the SLO window.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
---

```
burn rate = (observed errors per period) / (allowable errors per period)
```

A burn rate of 1.0 means the service is consuming exactly 100% of its
[error budget](error-budget.md) over the SLO's own window — the budget will
hit zero exactly at the end of the window if nothing changes. A burn rate of
14.4 means the same budget would be consumed in roughly 1/14.4th of the
window (e.g. about 2 days of a 30-day budget). A result above 1 means the
budget is being spent faster than sustainable; below 1 means the service is
within budget.

Burn rate requires maintaining a historical window to compute — and the
window used for *alerting* on burn rate need not equal the window the SLO
itself is defined over. This distinction is what makes burn-rate alerting
tunable independently of the SLO's own measurement period; see
[multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md)
for how that independence is exploited.

Burn rate is the mechanism that makes SLO-based alerting able to catch a
[slow burn](fast-burn-vs-slow-burn.md) — a steady trickle of errors with no
single dramatic transition — which simple threshold alerting structurally
cannot see, since no individual sample looks abnormal.

[Catch-up-time deadline alerting](catch-up-time-deadline-alerting.md) applies
the same forward-projection idea to a deadline-style freshness SLI instead of
a rolling error-ratio SLI.
