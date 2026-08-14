---
type: concept
title: Pager Load Management
description: Treating the volume of paging incidents per on-call shift as a measurable quantity to be actively reduced, not an inevitable cost of running a service.
sources:
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 8"
---

**Pager load** is the number of paging incidents an engineer receives per
shift. It is governed by three factors, each with its own reduction
techniques:

- **Preexisting bugs**: reduce by keeping systems no more complex than
  necessary, keeping dependencies current, running destructive
  testing/fuzzing, and regular load testing.
- **New bugs**: catch them before production by asking "how could we have
  caught this preproduction?" after every incident, testing with synthetic
  traffic in staging, and using canary releases. Prefer "detect, roll back,
  fix, roll forward" over repeatedly rolling forward, which requires small,
  frequent, cheap-to-roll-back releases. Test beyond typical-day traffic
  patterns — bugs are often seasonality-dependent (peak shopping days, DST
  shifts, unusual regional usage).
- **Alerting configuration and human processes**: see below.

### Reducing delay, not just volume

Two delays compound pager load's cost, each with distinct countermeasures:

- **Identification delay**: good alert-to-console linking that correlates
  black-box and white-box signals, [preparedness drills](preparedness-drills.md)
  that build pattern recognition, small/frequent canaried releases that make
  it easy to correlate a bug with a specific change, and a searchable timeline
  of change events.
- **Mitigation delay**: prefer rollback over a slow forward fix — for a
  service with a tight error budget (e.g., ~15 minutes per quarter at 99.99%
  availability), a forward fix that takes longer than that exhausts the
  budget before it lands. Rollback is not always sufficient (it cannot undo
  data corruption). Isolate broken functionality behind feature flags so one
  broken feature doesn't force disabling unrelated ones, and drain traffic
  away from a buggy component rather than rolling back an entire release
  where possible.

### Alerting discipline

Alerts must be immediately actionable with a high signal-to-noise ratio.
Prefer SLO-based, symptom-based paging (e.g., API responsiveness) over
low-level infrastructure noise (e.g., database lock waits) — the latter
causes alert fatigue and chases transient issues that don't affect users.
Relaxing alert thresholds is rarely the right fix for a symptom-based alert
that is firing correctly but too often; the underlying rate of real problems
needs to come down instead. New alerts should get a
[runbook](runbooks-and-checklists.md) entry and a team review/test-mode
vetting period (roughly a week) before going live as pages, and their
predicted trigger rate should be measured against the team's pager budget
before approval.

### Rigor of follow-up

Every page should drive toward a true systemic cause, not a "cause unknown"
closure — use paging events as leverage for systemic fixes, not just point
fixes. Weigh the fix against a break-even calculation: if a systemic
automation fix costs 120 engineering hours and each recurrence costs 4 hours
of manual handling, the fix pays for itself after roughly 30 prevented
pages. File a placeholder bug per alert type and link every page to it, so
which components generate the most pages — and how that correlates with
other signals — becomes a data-driven question rather than a guess. Distinct
response tiers exist for a single occurrence: a **point fix** resolves the
immediate instance, a **systemic fix** removes the underlying cause (e.g.,
automating a manual rebalancing step), and a **prevention/monitoring fix**
catches the precursor condition before it becomes service-impacting.

### Vigilance against creeping overload

Track a trailing average (e.g., over 21 days) of pager load in regular
production-review meetings, and set a warning threshold that triggers a
ticket when crossed. Left unwatched, operational overload creeps in
unnoticed — the "boiling the frog" failure mode — until a team is
permanently firefighting instead of doing project work. Once that
threshold is crossed, see [operational overload
recovery](operational-overload-recovery.md) for how to diagnose and pull a
team back out.
