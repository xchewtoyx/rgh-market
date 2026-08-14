---
type: concept
title: Multiwindow, Multi-Burn-Rate Alerting
description: >
  The recommended SLO alerting design — layering several burn-rate/window
  pairs, each paired with a short confirmation window, to catch both fast
  and slow budget burns with good precision, recall, and reset time.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
---

SLO alerting sophistication evolves through recognizable stages:

1. Alert when error rate crosses the SLO threshold over a short window —
   good detection time, very poor precision (most alerts don't actually
   threaten the SLO).
2. Widen the window — better precision, terrible reset time (an alert can
   linger up to the whole window after recovery).
3. Require the condition to persist for a fixed duration before firing — not
   recommended: detection time doesn't scale with severity (a 100% outage
   takes as long to alert as a 0.2% one), and a metric that briefly dips
   back in range resets the duration timer, so a flapping SLI may never
   alert.
4. Alert on [burn rate](burn-rate.md) directly — good precision and
   detection, but a single threshold tuned for one severity has poor recall
   for slower burns.
5. Layer multiple burn-rate/window pairs (e.g. 2% budget in 1h → page at
   14.4x; 5% in 6h → page at 6x; 10% in 3d → ticket at 1x) — catches both
   fast and slow-burning incidents, with faster/higher thresholds paging and
   slower/lower ones filed as tickets.
6. **Multiwindow, multi-burn-rate (recommended)**: add a short window
   (roughly 1/12 the long window) that must *also* exceed the threshold
   before the alert fires — this lets the alert clear quickly once the
   error rate actually drops, solving the reset-time problem of approach 5
   while keeping its precision and recall.

A commonly cited starting table: page at 14.4x burn over 1h (with a 5-minute
short window) for 2% of budget; page at 6x over 6h (30-minute short window)
for 5% of budget; file a ticket at 1x over 3d (6-hour short window) for 10%
of budget.

An alert threshold can't, by itself, "defend" a 30-day budget if its own
evaluation window is shorter than 30 days — always pair a hard-constraint
alert on outright SLO violation with the shorter, more sensitive layered
alerts for early warning. See
[fast burn vs slow burn](fast-burn-vs-slow-burn.md) for the underlying
distinction this design is built to catch both sides of, and
[alerting response-time floor](alerting-response-time-floor.md) for the
lower bound on how tight any of these windows can usefully get.
