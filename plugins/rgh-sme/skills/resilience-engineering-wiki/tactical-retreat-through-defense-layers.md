---
type: concept
title: Tactical Retreat Through Defence Layers
description: >
  As successive layers of defence-in-depth are breached, a system moves
  through normal, abnormal, and emergency operating envelopes in sequence —
  each breach a deliberate lowering of expectations, not a single jump from
  safe to unsafe.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

Defence-in-depth architectures (the same layered logic as [the Swiss cheese
model](swiss-cheese-model.md), viewed from the design side rather than the
failure side) define successive operational envelopes, each with its own
procedural character:

1. **Normal operation envelope** — disturbances stay within design limits
   and are absorbed by the system's intrinsic flexibility without any
   procedural departure at all.
2. **Abnormal operation envelope** — an anticipated departure (a single
   engine failure) exceeds normal design limits and calls for active,
   pre-defined procedural re-adaptation: a specific, rehearsed response
   exists and applies.
3. **Emergency operation envelope** — the departure is extreme, possibly
   unanticipated (simultaneous loss of both engines); critical components
   are gone, parameters exceed all standard bounds, and no predefined
   routine fits. The system cannot re-adapt through procedure; it has to
   stretch its available capability directly.

US Airways Flight 1549's bird-strike sequence shows five such layers built
specifically against bird hazard: reducing bird populations near airports,
certifying engines to survive bird impact, requiring aircraft to keep
climbing on one fewer engine than they have, providing emergency
flight-control power after total thrust loss, and engineering the airframe
and evacuation procedure for a survivable water landing as the last line.
Each layer is deliberately imperfect by design — hardening engines against
the largest possible bird flocks would make every aircraft too heavy and
fuel-inefficient to fly economically, so certification accepts an explicit,
priced trade-off between fuel efficiency and immunity to the rarest
extremes, the [efficiency–thoroughness trade-off](efficiency-thoroughness-trade-off.md)
made at design time rather than in the moment.

**Crossing from one envelope to the next is a tactical retreat, not a
neutral state change.** At each breach, operators explicitly lower their
sights: they accept more uncertainty, a higher probability of damage,
tighter time constraints, and outcomes that are progressively less
reversible. This is the operational meaning of moving from adapted, known
territory into de-adapted, unknown territory — the felt experience of
crossing [the boundary of potential
variability](boundary-of-potential-variability.md). The procedures
available at each layer change character to match: normal and abnormal
procedures are detailed and specific, while emergency-envelope guidance is
necessarily generic and goal-oriented, because no specific procedure could
have been written for an event this far outside the design envelope — the
real-time instance of [matching response abstraction to
uncertainty](matching-response-abstraction-to-uncertainty.md).
