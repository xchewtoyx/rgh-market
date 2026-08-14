---
type: concept
title: Fast Burn vs Slow Burn
description: >
  Near-total outages and steady trickles of intermittent errors both consume
  error budget but need fundamentally different alerting approaches to catch.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
---

- **Fast burn** — a near-total outage. Well-served by simple
  threshold-style alerting, since the signal is large and unambiguous.
- **Slow burn** — budget being eaten by a steady trickle of intermittent
  errors, not a hard outage. No single "transition" event stands out, so
  this requires *stateful* alerting that aggregates failures over a window —
  this is the core innovation SLO-based alerting adds over threshold
  alerting.

Both consume the same underlying [error budget](error-budget.md) and both
need to be caught, but a single alert threshold tuned for one poorly detects
the other — a threshold sensitive enough to catch a slow burn quickly will
false-positive constantly on ordinary noise, and one loose enough to avoid
noise will miss a slow burn until it's nearly exhausted the budget.

This is the underlying reason
[multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md)
layers multiple burn-rate/window pairs rather than picking one: each pair is
tuned to catch one class of burn with good precision, and together they
cover both.

Troubleshooting differs by class too: fast-burn alerts are usually
diagnosable with familiar coarse indicators, while slow-burn alerts usually
require a breadth-first "chase high cardinality" approach across dimensions
rather than an unguided, slow depth-first search.
