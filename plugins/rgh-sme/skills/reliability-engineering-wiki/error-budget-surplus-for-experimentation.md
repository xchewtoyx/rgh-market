---
type: concept
title: Using Error Budget Surplus for Experimentation
description: >
  A surplus error budget is a deliberate signal for when it's safe to run
  controlled experiments, load tests, or even purposely burn reliability to
  learn something the team couldn't otherwise find out.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 5"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

A surplus in the [error budget](error-budget.md) isn't just headroom to ship
faster — it's an explicit, quantified license to take on risk that would
otherwise be unjustifiable, since there's room to fail and roll back without
missing the SLO:

- **Experimentation / chaos engineering** — controlled experiments (config
  changes, cache TTL changes, GC algorithm swaps, error injection,
  automating manual review steps).
- **Load and stress tests** — surplus is a signal for when it's safe to run
  production load/stress tests.
- **Blackhole exercises** — deliberately cutting off a data center, region,
  or service to validate failure-mode assumptions and discover unknown
  dependencies, best done with budget surplus and rollback confidence. A
  team's lack of confidence to do this at all is itself a sign of
  insufficient resilience/testing investment.
- **Purposely burning budget** — the most advanced technique: deliberately
  degrading or shutting down a service periodically to prevent downstream
  teams from silently forming unacknowledged
  [hard dependencies](hard-vs-soft-dependency.md) on it. A well-known case
  study: a distributed lock service was deliberately shut down globally
  whenever it had budget surplus each quarter, repeatedly exposing teams
  that had built unadvertised hard dependencies on it. Only recommended once
  a team's error-budget culture and policies are mature.
- **Deliberately relaxing reliability to learn business impact** — e.g.
  adding latency to quantify its effect on conversions. Quantifies the
  reliability/business trade-off directly, but is risky (users may lack
  alternatives *today* and leave once a competitor appears) and should only
  be attempted with budget to spare.
- **Error budgets for humans** — the same math can apply to non-software
  processes: ticket queue mis-filing rates, PR review turnaround time,
  retrospective cadence, or whether people are taking their allotted time
  off.

See [error-budget-driven prioritization](error-budget-driven-prioritization.md)
for the complementary set of uses on the *deficit* side of the budget.
