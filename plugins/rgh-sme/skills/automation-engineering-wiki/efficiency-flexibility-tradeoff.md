---
type: concept
title: Efficiency-Flexibility Trade-off
description: >
  A system tuned for high efficiency inside a narrow, predictable operating
  envelope becomes correspondingly brittle outside it, so standardizing for
  normal conditions trades away the adaptive range a system needs for
  abnormal ones.
sources:
  - title: Resilience Engineering in Practice
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 2"
---

# Efficiency-Flexibility Trade-off

Every system faces a trade-off between two properties that pull in opposite
directions:

- **Efficiency** — how well the system is adapted to a standard, expected
  environment.
- **Flexibility** — how wide a range of unexpected environmental variation
  the system can still adapt to.

Highly adapted systems reach high efficiency in a narrow, predictable niche,
but become extremely brittle once conditions shift beyond the thresholds
that niche assumed — the same way a desert lizard hyper-adapted to
extreme-arid conditions can be killed by a comparatively small climate
shift that a generalist species would shrug off. Increasing standardization
makes a system safer and cheaper *inside* its normal operating envelope
while making it progressively more brittle *at the edges* of that envelope,
because the specialization that buys the efficiency is the same thing that
narrows the range of conditions the system can still cope with.

This is the underlying mechanism behind the [irony of
resilience](irony-of-resilience.md): the more a blunt-end effort narrows a
system toward its anticipated envelope, the less capacity remains — in the
system and in the humans operating it — to handle whatever the anticipation
missed. It also explains why moving a procedure up the [automation maturity
spectrum](automation-maturity-spectrum.md) is never a pure win: each step
buys efficiency inside the cases the automation was built for, at the cost
of flexibility for the cases it wasn't.
