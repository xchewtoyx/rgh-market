---
type: concept
title: Escalation
description: >
  A formally defined dynamic process — an initial irregularity spreading
  across operational areas at accelerating tempo, generating consequences
  that are hard to overview and impossible to predict in advance.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 4"
---

Woods and Patterson's definition gives "escalating situation" a specific,
non-metaphorical meaning: a process in which an initial irregularity does
not stay contained but develops into a deteriorating situation, spreading to
other operational areas with accelerating tempo, and generating consequences
that become progressively harder to overview and eventually impossible to
predict from where the response started. Three properties distinguish
escalation from an ordinary, bounded problem: it cascades across areas of
responsibility rather than staying local, it accelerates rather than
proceeding at a constant rate, and its endpoint is not knowable in advance
from its starting conditions.

This is the umbrella term for the territory several other notes describe
from different angles: [decompensation](decompensation.md) is one specific
signature an escalation can take (compensation masking a growing disturbance
until capacity is exhausted); [working at
cross-purposes](working-at-cross-purposes.md) is what happens when the
cross-area spread outpaces coordination; and [tactical retreat through
defence layers](tactical-retreat-through-defense-layers.md) is what
successive breaches of the same escalation look like from the responding
system's side. Because prescriptive procedures are written for anticipated,
bounded problems, an escalating situation is close to the definitional case
of [the boundary of potential variability](boundary-of-potential-variability.md)
being crossed: what makes a situation an escalation rather than a handled
abnormality is precisely that it has moved past what pre-planned response
covers. The team-level competencies needed to respond, once procedure stops
being sufficient, are addressed in [generic competencies for escalating
situations](generic-competencies-for-escalation.md).
