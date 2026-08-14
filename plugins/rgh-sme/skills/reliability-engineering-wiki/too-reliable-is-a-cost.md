---
type: concept
title: Being Too Reliable Is a Real Cost
description: >
  Consistently exceeding an SLO trains users to expect the higher bar as the
  new baseline, quietly erasing the slack the SLO was meant to protect.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
---

Over-delivering against an SLO isn't free. Sustained overperformance (e.g.
running near four-nines against a three-nines target) trains users to expect
the future to look like the recent past — see
[implicit SLOs from past performance](implicit-slo-from-past-performance.md)
— which erodes the slack the SLO was meant to protect: room for
experimentation, faster shipping, chaos engineering, or planned downtime all
quietly shrink because "the bar has moved" even though nothing was formally
promised.

This is a genuine trade-off decision, not just a nice-to-have: an SLO that's
consistently blown out of the water in the good direction should prompt the
same kind of review as one that's consistently missed — see
[identifying a miscalibrated SLO](identifying-a-miscalibrated-slo.md) and
[SLO evolution triggers](slo-evolution-triggers.md). Either lock in the
stricter target deliberately (at the cost of future velocity) or actively
spend the surplus down — see
[error budget surplus for experimentation](error-budget-surplus-for-experimentation.md).
