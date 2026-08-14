---
type: concept
title: The Heinrich Triangle Myth
description: >
  The claim that minor incidents and fatalities occur in a fixed ratio is
  refuted — in safe complex systems minor incidents and catastrophes have
  different causal mechanisms, so low injury counts do not predict disaster.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 5"
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 7"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 12"
---

Heinrich's safety triangle asserts a fixed proportional ratio between minor
incidents, major injuries, and fatalities (canonically 300 : 30 : 1), implying
that suppressing minor incidents automatically prevents major disasters. The
numbers came from insurance actuary data, not safety science.

Modern research shows that in safe, complex industries the base and the apex of
the triangle have **radically different causal mechanisms**. Minor incidents
are driven by routine slips and workarounds; catastrophes are driven by
[systemic drift](drift-into-failure.md) and [goal
trade-offs](goal-conflicts-and-production-pressure.md). Minor-incident metrics
are therefore lousy predictors of catastrophic risk.

The canonical counterexample: Transocean/BP executives were aboard Deepwater
Horizon celebrating six years without a lost-time injury the day before the
Macondo blowout killed 11 workers (2010) and caused the largest marine oil
spill in history.

The empirical evidence goes beyond decoupling — the correlation actually
runs *negative*:

- **Saloniemi & Oksanen (1998)**: across 14 years of Finnish construction
  and manufacturing (1977–1991), non-fatal incident rates and fatality rates
  correlated at r = −0.82 (p < 0.001). The sites reporting the *fewest*
  incidents suffered the *highest* fatality rates.
- **Barnett & Wang (2000)**: among major US jet carriers (1990–1996),
  higher nonfatal incident and accident reporting rates went with *lower*
  passenger mortality risk (r = −0.10 incidents; r = −0.34 serious nonfatal
  accidents).

The interpretation flips the triangle's logic: a healthy stream of reported
minor events is a marker of a system that is still learning — [Wald's bomber
paradox](walds-bomber-paradox.md) — while a suspiciously quiet record marks
suppressed reporting and isolation from learning, not safety.

Practical consequences:

- A low personal-injury or minor-incident rate is not evidence of low
  process/system risk; treating it as such feeds the overconfidence that
  drives drift. Guarding against that overconfidence is the point of
  [chronic unease](chronic-unease.md).
- Programmes that pressure workers to keep minor-incident counts down (zero
  harm targets, injury-rate bonuses) suppress reporting rather than risk, and
  poison the [reporting and learning loop](blame-suppresses-reporting.md).
- To anticipate catastrophe you must study how normal work is actually done
  and where margins are eroding — the [Safety-II](safety-i-and-safety-ii.md)
  stance — not count recordables.
- A related but separate discipline is [normalising for risk
  exposure](risk-exposure-normalization.md): even a well-chosen metric is
  uninterpretable without knowing how many opportunities the hazard actually
  had to materialise.

Commercial aviation runs the same fallacy under a different name: the
**"iceberg" theory**, the unexamined assumption that suppressing minor
incidents automatically prevents accidents because the two are just
different depths of the same submerged mass. In practice, a stable or
declining trend in reported minor events routinely gets no further scrutiny
at all, while weak signals of *systemic* risk that don't show up as
counted events — training cuts, an organisational restructuring, eroding
technical expertise — go unexamined because handling them competes with
already-heavy workload. The iceberg model and Heinrich's triangle share the
same falsified premise: that catastrophe is the deep continuation of the
same causal process that produces minor events, rather than a distinct
process ([systemic drift](drift-into-failure.md)) that a minor-event count
cannot see at all.
