---
type: concept
title: Sharp-End Myopia
description: >
  Distributed practitioners each handling an unfolding situation as a fresh,
  local event — without projecting beyond the immediate window to integrate
  history or anticipate trajectory — can trap the whole system in a local
  minimum even though every individual response looks reasonable.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 16"
---

When [centralised coordination tools](coordination-dimensions-of-resilience.md)
fail or don't apply to the situation at hand, practitioners fall back on
"emergence-through-use" coordination: direct, local, ad hoc interaction with
whoever else is at hand. This works — up to a structural limit borrowed from
swarm intelligence and distributed robotics: simple local agent rules do
generate coherent macro-behaviour without any central controller, but purely
distributed control with no global representation can trap the whole
collective in a **local minimum** — a "myopic" state where every agent's next
move looks sensible from where they stand, yet the collective never finds
the actual solution.

The sociotechnical version: each practitioner treats their own encounter
with an unfolding situation as a routine, self-contained emergency, giving
precedence to what they can perceive right now and restarting reasoning from
scratch rather than integrating the pattern that earlier practitioners
already saw. A patient who visits three different care providers across
twenty-four hours does not get three data points combined into one
deteriorating trajectory — each provider reruns the diagnostic process from
the beginning, "stammering" through the same reasoning steps, because the
medical record functioned as a static reference to consult rather than a
live input to a shared trajectory. Redundant expertise (multiple independent
opinions) is not the same thing as integrated expertise (one picture built
across time), and the former can create an *illusion* of the latter — extra
visits look like extra safety margin while actually breaking the temporal
task integration that iterative diagnosis depends on.

**Local flexibility is not automatically virtuous.** High-Reliability
Organization theory prizes front-line flexibility and localised
decision-making (see [HRO theory](high-reliability-organizations.md)), but
sharp-end adaptation that stays purely local is exactly the myopic pattern
described here — flexibility without projection. Operational crisis cultures
that valorise pure action ("you act — you do not have time to think") make
this worse, not better: they actively discourage the pause that would let
someone step back and ask whether this local window is part of a larger,
non-linear trajectory.

**Resilience therefore requires two distinct capabilities, not one:**

1. **Immediate coping** — local, spontaneous adaptation to what is in front
   of you right now. This is the capability myopic coordination already
   supplies.
2. **Spatio-temporal projection** — the capacity to reach beyond the local
   immediate: integrating past history, symbolising how the situation could
   plausibly evolve, and reading the current moment as one point on a
   trajectory rather than an isolated event.

The second capability is not a stronger version of the first; it requires
structural reorganisation of how the system coordinates — moving decisively
back toward synchronic, dialogic interaction (people actually discussing the
trajectory together) rather than leaving asynchronic, static records to
carry the integration work they cannot do — the same weak point [coordination
dimensions of resilience](coordination-dimensions-of-resilience.md) names in
its account of interaction type. It is also the organisational-scale version
of [anticipation](four-abilities-of-resilient-performance.md): a system that
can only monitor and respond to its own local window, moment to moment, has
monitoring and response without the anticipation that would let it recognise
its own local window as part of something larger.
