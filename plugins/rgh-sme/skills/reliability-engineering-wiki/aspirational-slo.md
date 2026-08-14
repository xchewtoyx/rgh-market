---
type: concept
title: Aspirational SLO
description: >
  A deliberately-set target the team can't yet hit, used to force visibility
  and motivation, ratcheted tighter as reliability genuinely improves rather
  than enforced with an error budget from day one.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 14"
---

An aspirational SLO is tracked but not [error-budget](error-budget.md)-
enforced: it exists to make a known reliability gap visible and to motivate
work toward closing it, without the false pretense that the current target
is actually being achieved today. It's the appropriate response when the
target itself is judged correct — it reflects what users genuinely need —
but the system isn't yet capable of meeting it.

This is distinct from simply picking an achievable target and calling it
done: aspirational SLOs are explicitly a temporary tool, meant to be
tightened into a real, budget-enforced SLO once the underlying reliability
work catches up. Compare against
[SLO evolution triggers](slo-evolution-triggers.md), which cover the more
general set of reasons a target might need to move in either direction.

Practical use: when an SLO's coverage of real incidents looks wrong (it
misses real incidents or false-alarms on non-events), the available fixes
are tightening/loosening the target, improving the SLI implementation, or —
if the target itself is right but not yet achievable — introducing it as an
aspirational SLO rather than forcing premature enforcement.
