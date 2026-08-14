---
type: concept
title: SLO Count and Scope
description: >
  A small number of representative SLOs per service, roughly three to five,
  is easier to make decisions from and statistically less prone to false
  alarms than a large sprawling set.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
---

More SLOs makes it harder to make decisions from conflicting signals, harder
to report status to outsiders, and statistically more likely to trip the
"multiple comparison problem" — the more measurements exist, the higher the
chance something looks anomalous by pure chance, wasting investigative
effort chasing noise. Recommendations across sources converge on roughly
3–5 representative SLOs per service; use additional fine-grained metrics for
internal debugging without promoting all of them to SLO status.

For services with components owned by multiple teams, each component's team
should generally have its own SLIs/SLOs in addition to any overarching
service-level SLO, so each team has data to justify its own prioritization.
For a service entirely owned by one team, it's often sufficient to define
SLIs at the [critical user journey](critical-user-journey.md) level without
necessarily SLO-ing every internal component individually.

This count discipline is closely related to
[measuring many things by measuring only a few](measuring-many-things-by-measuring-a-few.md):
the goal is finding the small set of signals whose health implies the rest,
not exhaustively covering every internal metric.

Model-backed systems push the "SLOs for adjacent systems too" case further
than most: see
[ML system SLO entanglement](ml-system-slo-entanglement.md) for why an ML
system's SLO usually can't be scoped in isolation from the systems it's
entangled with.
