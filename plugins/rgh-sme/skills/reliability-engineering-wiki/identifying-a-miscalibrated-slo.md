---
type: concept
title: Identifying a Miscalibrated SLO
description: >
  Diagnostic signs that an SLO is measuring the wrong thing — the budget
  never lines up with real user happiness, or a known incident doesn't move
  the data at all.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 14"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
---

Two diagnostic patterns both indicate a mis-defined
[SLO](service-level-objective.md):

- **Always out of budget, but users are happy.** The target is stricter than
  anyone actually needs.
- **Always plenty of budget, but users are unhappy.** The
  [SLI](service-level-indicator.md) isn't capturing what actually matters to
  users, or the target is too loose to catch real problems.

**Paying attention to failures**: if a known real incident doesn't move the
SLI or error-budget data at all, the wrong thing is being measured, or the
calculation has a defect — a genuine failure should always be visible in the
numbers.

**Correlating against independent signals**: compare SLI/error-budget dips
against independently observed incidents (support tickets, manual outage
logs, social media, user surveys) — a technique like Spearman's rank
correlation can quantify how well the SLO tracks real-world incidents. If the
correlation is weak, either the SLO's coverage needs tightening/loosening or
the underlying [SLI implementation](sli-specification-vs-implementation.md)
needs to move closer to the user — see
[SLI measurement point selection](sli-measurement-point-selection.md).

**How to fix it**: start from the SLI (is it measuring the right thing?),
then the SLO (is the target right for user happiness?), then the error-budget
window (is the span of data right?) — the process for correcting an existing
SLO is essentially identical to the process for choosing the first one.

Some kind of scheduled revisit should exist regardless — even a two-minute
"no change needed" check-in — both to catch drift early and to give standing
to defer ad hoc pressure to revisit outside that cadence, as long as the team
isn't actively losing users or breaking a contract. See
[SLO evolution triggers](slo-evolution-triggers.md) for the situations that
should prompt an out-of-cycle look.
