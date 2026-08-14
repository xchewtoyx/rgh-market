---
type: concept
title: Feedback Delay Masks Accumulating Risk
description: >
  A time gap between a risk-increasing cause and its visible effect does more
  than slow the response — it generates false confidence while risk
  accumulates unseen, and can push a correction, once it finally arrives, to
  overshoot.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 8"
---

System-dynamics models of organisational drift (reinforcing loops that
amplify a trend, balancing loops that seek equilibrium) treat delay between
cause and effect as a structural element in its own right, not just
friction that slows an otherwise-accurate signal. A long delay does three
specific things a short one does not: it masks dynamic complexity by
separating a decision from its consequence far enough that the two are never
mentally connected; it generates false confidence, because the absence of a
visible effect gets read as the absence of an effect at all rather than as
"not yet arrived"; and it can induce instability or overcorrection, because
by the time the delayed effect is finally visible, so much has accumulated
behind it that the response has to be larger and more disruptive than it
would have been if the causal link had been visible in real time.

NASA's Space Shuttle programme is the modelled case. A **reinforcing loop**
("Pushing the Limit") connected accumulated accident-free launches to rising
management optimism, a shift toward labelling the vehicle "operational"
rather than experimental, reduced safety priority, and higher launch-rate
expectations — each element reinforcing the next. A **balancing loop**
("Safety Program") nominally opposed it. Simulation of the integrated model
against the actual programme history showed the pattern [decrementalism](decrementalism.md)
and [the law of stretched systems](law-of-stretched-systems.md) predict
qualitatively, now with a mechanism for exactly why it is durable:
post-accident, systemic safety fixes spike briefly during the return-to-flight
period, then taper off quickly once flight operations resume and performance
pressure re-establishes dominance — while underlying technical risk drops
only slightly post-mishap and then climbs continuously over the long
horizon, driven by vehicle aging, deferred maintenance, and a bias toward
symptom-level rather than systemic repair. Fixing the specific symptom that
caused the last accident (foam shedding, an O-ring) without addressing the
organisational pressures that produced it reproduced rapid risk escalation
in simulation; fixing the systemic factors did not. Even the strongest
single-lever intervention modelled — giving the safety function genuinely
independent technical authority — lowered the *baseline* risk level but did
not flatten the long-term upward slope, because the background mechanisms
driving it (complacency, vehicle aging) keep operating regardless of who
holds authority over safety decisions.

The practical corollary for monitoring: because delay is what allows [Rasmussen's
boundary migration](rasmussen-boundary-model.md) to proceed invisibly, the
model-derived intermediate signals — flight backlog pressure, safety
staffing and attrition, the ratio of symptom-fixes to systemic fixes closed
— function as [leading indicators](leading-vs-lagging-indicators-are-level-relative.md)
specifically *because* they sit upstream of the delay, giving [proactive
monitoring](proactive-monitoring-control-model.md) something to read before
the delayed technical-risk consequence would otherwise become visible on its
own.
