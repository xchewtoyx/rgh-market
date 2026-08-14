---
type: concept
title: SLO-Based Reporting vs Incident Counting
description: >
  Counting incidents, bucketing severity levels, and averaging Mean Time to
  X metrics all systematically misrank reliability compared to what SLO and
  error-budget data show directly.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 17"
---

Common reliability-reporting methods fall short in specific, avoidable ways:

- **Counting incidents** — "incident" itself is hard to define consistently
  (paged on a threshold? a public status-page update? a customer complaint
  volume?) — every definition is either too fragile (needs accurate
  alerting to even count correctly) or too subjective (thresholds vary
  across people and orgs). A related pitfall: naively tracking "reduce the
  number of CVEs found" creates a perverse incentive to stop *finding*
  vulnerabilities rather than stop *having* them.
- **Severity levels** (S0–S5-style buckets) add structure but still can't
  cleanly classify real incidents — they flap between levels, or progress
  through several levels over one incident's lifetime, and ignore
  time-of-day/business-criticality context (a 3am blip vs. a Black Friday
  outage of the same technical size).
- **Mean Time to X (MTTX)** metrics have two compounding flaws: incidents
  are unique enough that averaging across them is often not statistically
  meaningful (even "the same" incident type resists clean bucketing), and
  means aren't always representative — a worked counterexample shows 20
  short incidents (400 total minutes) can produce a *better*-looking MTTR
  (20-minute average) than a single 3-hour outage (180 minutes, but far less
  total downtime), even though the frequent-incident quarter caused users
  objectively more cumulative harm. This critique is specifically about
  human-experienced incident reporting; MTTX-style math remains legitimately
  useful for things like pure hardware time-to-failure modeling.

**SLOs and error budgets resolve all of this at once**: they correctly rank
the 20-short-incidents quarter as worse than the 3-hour-outage quarter,
matching real user-perceived impact, and sidestep incident-counting and
severity-bucketing ambiguity entirely — the question of whether two waves of
an attack are "one incident or two" simply doesn't need answering; you just
read how much budget was burned. Similarly, tracking [user-impact minutes](user-impact-minutes.md)
provides a duration-based metric that adjusts for the scope of the outage.

This is the core reason [reliability burndown reporting](reliability-burndown-reporting.md)
and error-budget status are recommended as the primary reporting artifacts
to leadership, rather than incident counts or severity tallies: they are
entirely user-focused, so once the underlying
[SLI](service-level-indicator.md) is validated as tracking real user
experience, there's no separate need to worry whether raw log or metric
counts correlate with what users actually felt.
