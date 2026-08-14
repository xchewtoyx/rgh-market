---
type: concept
title: N+M Redundancy
description: >
  Provisioning N units of baseline capacity plus M spare units so the loss of any M units still leaves enough capacity to meet demand, turning "is it up" into a continuous capacity-headroom question.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 4"
---

**N+M redundancy** provisions N units of capacity to meet actual demand
plus M extra units held in reserve, so that up to M simultaneous unit
failures can be absorbed without falling below the capacity a service
actually needs. N+1 survives one simultaneous failure; N+2 survives two.
The arithmetic compounds under sustained failure: a 3+1 pool that loses one
unit becomes 3+0 — still meeting demand, but with zero redundancy left, so
a *second* failure immediately drops it below the required capacity
("oversubscribed").

This reframes reliability from a binary up/down question into a continuous
one: instead of asking "is the service up," the operational question
becomes "how much spare-capacity headroom is left," monitored as a gauge
with an alert threshold rather than paged the instant any single unit dies.
It is the capacity-side counterpart to [dependency reliability
composition](dependency-reliability-composition.md) — where that concept
governs how reliability composes *across* dependencies on a critical path,
N+M redundancy governs how much spare capacity a single pool of
interchangeable units needs to absorb failures without a capacity-driven
outage. It also underpins [load shedding](load-shedding.md) and [graceful
degradation](graceful-degradation.md) as the *next* line of defense: those
patterns are what a service falls back to once its redundancy margin is
actually exhausted.

**Sizing the spare margin** trades off two costs: bigger pools are more
capital-efficient (1+1 wastes 50% of capacity as spare; 20+1 wastes under
5%), but the real sizing question is how likely a *second* failure is to
land during the repair window of the first. That likelihood is
approximately `MTTR / MTBF` (mean time to repair divided by mean time
between failures) — a fast repair (seconds, for an auto-restarted process)
keeps that risk negligible even at N+1, while a slow repair (weeks, for
hardware requiring shipped replacement parts) can make a second failure
during the repair window a coin flip, which is when N+2 becomes justified
rather than optional. A useful minimum default is N+1 for any service,
moving to N+2 specifically when a second failure during the first repair
is plausible given the dependency's real MTTR.

**Load sharing vs. spares** are the two ways to structure the M spare
capacity: in **load sharing** (active-active), every unit carries traffic
and its share of the spare margin simultaneously; in a **standby spare**
(active-passive), one or more units sit idle or semi-idle, ready to take
over if the active unit fails. The same N+M accounting applies to both,
but load sharing gets more use out of the spare capacity in the common
case (no failure).

Standby spares themselves come in three grades, trading recovery time
against the runtime cost of keeping the spare current:

- **Hot spare** — the spare runs in parallel with the active unit(s),
  processing the same inputs and staying synchronously state-matched, so
  failover takes milliseconds. Most expensive to run, fastest to recover.
- **Warm spare** — the spare doesn't process live traffic but receives
  periodic state updates from the active unit, so its state is only as
  fresh as the last update — a middle ground between cost and recovery
  time.
- **Cold spare** — the spare stays powered off or fully out of service
  until failover, then goes through a full power-on/initialization
  sequence before it can take over. Cheapest to run, but its slow recovery
  time makes it a poor fit wherever a demanding [MTTR](optimize-for-mttr-over-mtbf.md)
  target applies.

None of these grades protect against a unit that stays up but produces a
*wrong* answer rather than failing outright — that failure mode needs
[voting, not spares](voting-and-triple-modular-redundancy.md).
