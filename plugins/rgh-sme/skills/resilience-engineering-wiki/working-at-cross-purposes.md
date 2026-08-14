---
type: concept
title: Working at Cross-Purposes — Locally Adaptive, Globally Maladaptive
description: >
  Units or echelons each making locally rational adjustments can collectively
  undermine the whole system, the same dynamic as a tragedy of the commons
  with safety margin as the depleted shared resource.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 10"
---

The second of three basic patterns by which adaptive systems fail (alongside
[decompensation](decompensation.md) and [getting stuck in outdated
behaviours](getting-stuck-in-outdated-behaviors.md)): uncoordinated units or
echelons each pursue sub-goals that are individually sound but collectively
corrosive, because no one actor's adaptation is scoped to see the whole
system it is operating inside.

**Safety as a common-pool resource.** Ostrom's tragedy-of-the-commons
archetype — short-term rational behaviour by individual users depleting a
shared resource everyone depends on — applies directly once safety margin is
treated as the shared pool. Each line manager's incremental,
[locally rational](local-rationality-principle.md) trade-off of margin for
production looks costless from where they sit, exactly like each herder
adding one more animal to a shared pasture; the margin only becomes visibly
scarce once many uncoordinated actors have each drawn on it a little,
by which point no single actor's drawdown looks like the cause. NASA's Space
Shuttle Columbia accident shows the pattern at organisational scale: no
single group's local trade-off was unreasonable in isolation, and the
depletion was only legible in aggregate, after the fact.

Sub-patterns of the same underlying dynamic:

- **Vertical miscoordination** — conflicting adaptations across levels of
  the control hierarchy (a policy at one echelon undermines an adaptation
  another echelon is relying on).
- **Horizontal miscoordination** — conflicting adaptations among peer units
  operating in the same space or time.
- **Missing side effects of change** — a local adaptation shifts demand or
  timing elsewhere in the system in ways no one tracked, because tracking
  side effects was no single unit's job.
- **Role fragmentation / silos** — organisational boundaries that prevent
  any one party from seeing the cross-cutting pattern at all.
- **Failure to resynchronise after disruption** — units that adapted
  independently during a disturbance do not reconcile their individually
  adjusted states once conditions stabilise.
- **Double binds** — an actor faces two demands from different parts of the
  system that cannot both be satisfied, and satisfying either one
  undermines the other (see [the authority–responsibility
  mismatch](authority-responsibility-mismatch.md) for the accountability
  version of this).

**Perspective determines whether an action reads as adaptive or maladaptive
at all.** The same local decision looks like sound [local
rationality](local-rationality-principle.md) from inside the actor's own
scope of attention and goals, and like a maladaptive drain on the shared
system from a global vantage point — both readings are correct
simultaneously, for different observers. Local adaptation constrains or
releases what other units can do next: an upward workaround that resolves a
sharp-end impasse can violate a regional constraint nobody at the sharp end
could see, and a downward policy meant to simplify things regionally can
generate exactly the operational complexity that forces the next sharp-end
workaround. This co-adaptive web is why fixing "the" cross-purposes conflict
by correcting one unit's behaviour rarely works: the same coordination gap
regenerates the next locally-rational adaptation elsewhere in the web.
