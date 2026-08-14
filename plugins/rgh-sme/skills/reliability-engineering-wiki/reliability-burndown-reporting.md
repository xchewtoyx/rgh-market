---
type: concept
title: Reliability Burndown Reporting
description: >
  A time-series view of remaining error budget, more flexible than a raw
  budget-status snapshot, that lets humans spot emerging trends visually
  ahead of automated detection.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 17"
---

A reliability burndown is closely related to but more flexible than a
point-in-time [error budget](error-budget.md) status check — it can be
viewed over any arbitrary time window, not just the SLO's official
measurement window, and it pairs naturally with
[burn-rate](burn-rate.md) alerting.

Dashboards built around burndown remain valuable even with excellent
automated detection, because humans are exceptionally good at visually
spotting emerging trends ahead of automated alerting — use burndown
dashboards as a periodic reporting tool (daily/weekly syncs), not something
engineers are expected to watch continuously.

**Framing preference**: time-based framing tends to read better for
reporting than raw event counts — "we have 17 minutes of error budget
remaining" is immediately understandable and actionable to almost anyone,
though a stricter phrasing ("we project ~17 more minutes of unreliability
before we start losing users") is worth considering, since word choice here
is not incidental. See
[time-based vs request-based availability](time-based-vs-request-based-availability.md)
for why this preference holds even when the underlying SLI is computed as an
event ratio. Plotting remaining budget as a time series, not just a
point-in-time number, conveys trajectory rather than only current state.

A simple boolean current-status indicator (good/bad) is especially useful to
dependent teams debugging whether your service is the root cause of their
own problems — it answers the first, most urgent question before any detail
is needed.
