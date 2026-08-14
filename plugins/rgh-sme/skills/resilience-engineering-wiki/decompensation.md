---
type: concept
title: Decompensation — Exhausting the Capacity to Adapt
description: >
  A two-phase failure signature in which visible stability conceals a
  control mechanism working harder and harder to mask a growing disturbance,
  until its capacity is exhausted and the masked parameter collapses
  suddenly.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 10"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 3"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 6"
---

Decompensation is one specific signature an [escalating
situation](escalation.md) can take, and one of three basic patterns by
which adaptive systems fail
(alongside [working at cross-purposes](working-at-cross-purposes.md) and
[getting stuck in outdated
behaviours](getting-stuck-in-outdated-behaviors.md)). It occurs when
external disturbances grow faster than the responses available to meet
them, and it has a distinctive two-phase signature:

1. **Compensatory masking** — a lower-order control mechanism (automation,
   or a sharp-end team) actively resists the growing disturbance and
   succeeds at holding the target parameter stable. From outside, everything
   looks fine, because the parameter being watched *is* fine — that is
   exactly what compensation means. What is not visible is that the
   mechanism is working progressively harder to hold that same stable
   output.
2. **Decompensation collapse** — the compensating mechanism's capacity is
   exhausted. There is no gradual warning at this transition: the controlled
   parameter, which had been perfectly stable, collapses abruptly, because
   it was never a measure of the underlying disturbance in the first place.

**The diagnostic implication is which parameter to watch.** Monitoring the
output parameter alone cannot catch this pattern — by construction, it stays
flat right up to the moment of collapse. What must be monitored instead is
the *control effort* the compensating mechanism is exerting relative to its
own capacity limit: how hard the lower-order loop is working, not merely
whether it is succeeding. A supervisory level that only watches outputs
experiences decompensation as a late, sudden, "bumpy" transfer of control,
because it had no visibility into the exhaustion building underneath a
reading that looked healthy the entire time.

Two recurring sub-patterns:

- **Falling behind the tempo of operations** — demand keeps rising (an
  emergency room during a surge, an ICU running out of beds) faster than
  capacity can be added, so the gap between demand and capacity itself
  becomes the disturbance nothing is compensating for.
- **Inability to transition to emergency operating modes** — a severe
  anomaly requires a qualitatively different mode of operation (mass-
  casualty protocols, an emergency descent) rather than more effort in the
  current mode, and the system stays in the current mode past the point
  where more effort could still work.

A stress-strain framing of the same two phases gives it engineering
vocabulary: normal operation sits in an **elastic region**, where responses
stay proportional to stress because procedures, training, and pre-allocated
resources absorb it as designed. Stress that exceeds this proportional
coping capacity pushes the system into a **non-uniform, "extra" region**,
where performance starts to deteriorate and only local improvisation and
extra resource mobilisation — not the standard response — can still hold
things together. Compensatory masking is what the extra region looks like
from outside while it is still working: a **compensation area** where
opportunistic adjustments are outweighing the disruption and keeping
measured risk acceptable, even as the adjustments themselves mask the
dysfunction building underneath. Collapse is what happens when the same
region's compensatory mechanisms exhaust themselves — the **decompensation
area** proper.

**When people, not automation, are the compensating control loop, they can
supply the missing diagnostic signal themselves.** Effective team members
explicitly communicate unusual control effort to teammates — saying out loud
that holding the line is getting harder — precisely to surface the
otherwise-invisible Phase 1 signal before it becomes a Phase 2 collapse.
Experienced clinicians use a related technique to judge how much reserve a
patient's physiology has left: rather than relying only on a static baseline
or history, they read the *dynamics* of the response (a "sluggish" reaction
to a stimulus) or deliberately inject a small test perturbation to see how
much give is actually left — probing for margin directly instead of waiting
for it to be exhausted.

At the point disturbances actually do combine to trigger collapse, the
dynamics resemble **Highly Optimized Tolerance (HOT)**: systems tuned by
repeated optimisation against common, expected disturbances become
correspondingly fragile against the rare, large, or novel ones optimisation
never selected for — the systems-theory generalisation of [the
adapted-versus-adaptive trade-off](adapted-vs-adaptive-trade-off.md).

Decompensation is the mechanism-level account of what [the law of stretched
systems](law-of-stretched-systems.md) describes at the organisational
level: capacity consumed by rising demand looks fine, by design, until it
doesn't. Protecting against it means deliberately holding [tactical reserve
capacity](preserving-margin-for-future-response.md) uncommitted, precisely
so a compensating mechanism has somewhere left to go when its normal
capacity runs out.
