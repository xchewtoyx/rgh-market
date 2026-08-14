---
type: concept
title: Feature Freeze as a First Error Budget Policy
description: >
  A recommended starting error budget policy for teams new to SLOs — a
  simple no-new-features freeze once budget is exhausted, softened by a
  "thaw tax" for genuinely urgent exceptions.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 6"
---

For the first year of adopting [error budget policy](error-budget-policy.md),
having exactly *one* policy — a feature freeze once budget is exhausted — is
a recommended starting point, rather than designing a sophisticated
graduated response from scratch.

Worked example: a 99.9% availability SLO gives a 43.2-minute/30-day error
budget; a 60-minute outage overspends the budget by 1.39x, triggering a
roughly 12-day feature freeze (computed from the excess-time-to-budget
ratio). During the freeze, changes are still allowed — but only changes that
make recurrence less likely (monitoring, rollback speed, staged rollout),
and the operations side should drive the freeze-period backlog as part of
the new social contract between engineering and operations.

**Silver bullets**: giving a head of product a small number of one-time
"breakout" passes to ship during a freeze for truly critical reasons is a
recognized but lukewarm option — it has no feedback loop and an arbitrary
cap.

**Thaw tax** (preferred alternative): unfreezing costs extra frozen days at
a penalty rate (e.g. 50% — 2 days unfrozen adds 3 days back to the freeze
period). This forces leaders to weigh urgency deliberately rather than
treating "just this once" as free.

The exact mechanism matters less than actually creating a policy and
sticking to it — the moment that actually proves an organization is serious
about error budgets isn't the day everyone signs off, it's the first time
the budget is genuinely exhausted and the policy has to be enforced. Making
an exception "just this once" the first time tends to unravel the whole
effort; following through the first time makes every subsequent enforcement
progressively easier.
