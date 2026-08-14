---
type: concept
title: Buffering Capacity, Margin, and Tolerance
description: >
  Four structural properties — buffering capacity, flexibility, margin, and
  tolerance — that distinguish a resilient system from a brittle one under
  the same disruption.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 2"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 17"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 7"
---

Woods gives resilience four structural correlates, each independently
observable in a system's design or current state, that together separate a
resilient system from a brittle one facing the same disruption:

1. **Buffering capacity** — the size or class of disruption the system can
   absorb without structural collapse or fundamental performance breakdown.
2. **Flexibility versus stiffness** — the system's capacity to restructure
   itself, reallocating resources and reorganising operations in response to
   a shift in external pressure, rather than holding a fixed configuration
   until it breaks.
3. **Margin** — how close the system is *currently* operating to its
   performance boundaries, as distinct from how close it was designed to
   operate. [Rasmussen's boundary model](rasmussen-boundary-model.md)
   describes the space these margins are measured against; [the law of
   stretched systems](law-of-stretched-systems.md) describes why margin
   erodes by default rather than by decision.
4. **Tolerance** — the system's behaviour *near* a boundary: whether
   performance degrades gracefully as the boundary is approached, giving
   warning and time to recover, or collapses precipitously once crossed.

These four are properties of the system's structure and current state, not
of any single actor's skill or vigilance — which is what separates this
framework from the process capabilities in [resilience as adaptive
capacity](resilience-as-adaptive-capacity.md) (recognise, steer back,
recover, detect). The two are complementary: buffering capacity, flexibility,
margin, and tolerance describe *what the system has available* to draw on;
the four capabilities describe *whether anyone is actually using it* in
time. A system can have ample buffering capacity and still fail if nobody
recognises the boundary is being approached, and a vigilant operator cannot
compensate for a system with no flexibility left to restructure.

**"Going solid"** is the operational term for margin fully depleted: the
system is operating at total capacity with no buffer left at all, so any
further demand has nowhere to go. It rarely arrives as one decision — small,
individually reasonable trade-offs erode the buffer incrementally, the same
mechanism documented before the Columbia accident. One institutional
resource that resists this erosion under acute economic pressure is
professionalism: a practitioner's professional standards can hold a line an
organisation's short-term incentives would otherwise erase, functioning as a
buffer guard independent of any formal margin-tracking system. A
lengthening [trend in how long the system takes to recover from routine
disturbances](slowing-recovery-time-as-tipping-point-signal.md) is a
leading indicator that a buffer is heading toward "solid" well before it
gets there.

Buffering capacity takes concrete organisational form as **resource
buffers** ("harm absorbers"): reserve capacity held in advance against a
sudden stress increase or emerging hazard, of two distinct kinds. *Material*
buffers are dedicated emergency-response teams or auxiliary staff held in
reserve; *design/temporal* buffers are built-in reaction margins — "white
time" — that give operators and managers room to reflect, diagnose, and
formulate a deliberate response rather than reacting under immediate time
pressure. Whether an organisation actually draws on this margin, and how far
down short-term productivity it is willing to sacrifice to protect it during
an escalating operational-pressure period, is itself a recurring management
trade-off decision rather than something the buffer's mere existence settles.
A documented instance of temporal buffer plus flexibility working together:
during a high-risk liver transplant with massive intraoperative bleeding, an
anaesthesiology team transformed seamlessly from routine monitoring into a
coordinated crisis-response team — adding staff and administering rapid
transfusions without formal orders or disrupted safety checks — then quietly
returned to baseline once the patient stabilised. Positive adaptations like
this are exactly what [Safety-I-style analysis omits](safety-i-and-safety-ii.md):
traditional safety assessment counts failures, not the successful absorption
that resource buffers make possible.

Once a system is approaching [its yield point](organizational-stress-strain-model.md),
restoring margin decomposes into exactly three levers, independent of
domain: **add capacity** (bring in more people or specialised roles),
**remove stressors** (address whatever is consuming capacity without adding
value — fatigue, cold, poor tooling — without reducing the work itself), and
**remove load** (defer or relocate non-critical scope so less capacity is
required in the first place). The three are not interchangeable
substitutes for the same underlying problem: adding capacity does nothing
for a stressor that degrades the capacity already present, and removing a
stressor does nothing if the load itself is simply too large for any
plausible capacity.

Margin and tolerance are the two properties least visible from inside normal
operation: because [Safety-II](safety-i-and-safety-ii.md) observes that
success and failure share the same variability, a system can be logging
routine successes right up to the point its margin runs out, with tolerance
— not warning — determining whether the transition past the boundary is
graceful or sudden.
