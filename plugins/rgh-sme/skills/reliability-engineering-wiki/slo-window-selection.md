---
type: concept
title: SLO Window Selection
description: >
  Rolling windows track user experience more faithfully than calendar-bound
  windows, but calendar windows are easier to communicate and align with
  planning cycles — the choice is a real trade-off, not a default.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 5"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

**Rolling windows** (e.g. a moving 30-day lookback) update continuously and
avoid a "cliff" reset at a period boundary — they track user experience more
faithfully, since users don't psychologically forget an outage just because
a calendar month ended. Prefer an integral number of weeks to avoid
weekday/weekend skew.

**Calendar-bound windows** (aligned to week/month start) are easier to
communicate and report, and align with billing or planning cycles, but can
let failures "age out" faster than users actually forget them, and can
create a pathological pattern where feature work backs up during a
budget-exhausted period and all lands at once when the calendar flips —
immediately re-exhausting the new period's budget.

**Choosing the window length**: prefer human-familiar windows (7-day,
28/30-day) over "precisely accurate" fractional windows — clarity beats
pedantic precision. Broader, product-level SLOs may warrant longer windows
(90-day, yearly) so a single bad day doesn't dominate reporting;
component-level SLOs can use shorter windows, with 30-day being a common
default. Google's own default is a 4-week rolling window, complemented by
weekly summaries for task prioritization and quarterly reports for project
planning — shorter windows enable faster course-correction, longer windows
give better data for larger strategic bets.

Note that the window an [SLO](service-level-objective.md) is defined over
need not equal the window used for burn-rate *alerting* on that same SLO —
see [multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md).
