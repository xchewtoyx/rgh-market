---
type: concept
title: Slowing Recovery Time as a Tipping-Point Signal
description: >
  How long a system takes to recover from routine disturbances is itself a
  leading indicator — recovery getting slower means adaptive capacity is
  being consumed, even while every individual disturbance still gets
  handled.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 9"
---

Complex systems research on tipping points gives resilience engineering a
usable early-warning signal that does not depend on anything actually
failing yet: **the time a system takes to recover from routine
disturbances**. As adaptive capacity is consumed, recovery from the same
class of disturbance takes measurably longer, well before the system
crosses into outright failure. This works as a signal precisely because it
is observable through a run of successes — every disturbance in the sequence
still gets handled, so an outcome-only view (did it recover, yes/no) reports
nothing unusual right up to the point capacity actually runs out.

This makes recovery time the practical, measurable counterpart to
[margin](buffering-margin-and-tolerance.md): margin is often not directly
observable, but the *trend* in recovery time is, and a lengthening trend is
exactly what margin erosion looks like from the outside. It gives an
organisation a way to detect that it is heading toward
[decompensation](decompensation.md) before decompensation's own signature
(sudden collapse of a previously stable parameter) actually appears —
recovery-time trend is available during compensatory masking, when nothing
else visible has changed yet.

The same logic that makes incident counts unreliable applies here too:
watching whether recovery *happened* is an outcome measure, and outcome
measures stay flat until they don't ([Wald's bomber
paradox](walds-bomber-paradox.md)). Watching how long recovery *took* is a
process measure that moves continuously, giving the same kind of leading
signal that [studying normal work](studying-normal-work.md) gets from
watching how work is actually done rather than only whether it succeeded.
