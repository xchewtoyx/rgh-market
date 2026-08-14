---
type: concept
title: The Simultaneous Triple-State Theorem
description: >
  Every complex adaptive system is well-adapted, under-adapted, and
  maladapted all at once, in different respects — which is why a linear
  causal model cannot predict how it will behave under a new disruption.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 10"
---

Woods's simultaneous triple-state theorem: a complex adaptive system is, at
any given moment, all three of the following at once, each with respect to a
different slice of its environment — not moving between the three states
over time, but occupying all of them simultaneously:

1. **Well-adapted** to the specific aspects of its environment it has
   already tuned itself against. The **fluency law** names the observable
   signature: skilled work in these areas proceeds with a facility that
   conceals how much difficulty and trade-off-balancing is actually being
   resolved underneath — competence looks effortless exactly where the
   system is well-adapted.
2. **Under-adapted**, in the sense of carrying a standing, intrinsic drive
   to keep improving its fit as the environment keeps varying — this is the
   same [permanent under-adaptation](adapted-vs-adaptive-trade-off.md) that
   provides the pressure for genuine accommodation rather than settling into
   pure assimilation.
3. **Maladapted or brittle** with respect to whichever unexpected events or
   shifts fall outside the boundaries its current adaptation was built for
   — the same territory [the boundary of potential
   variability](boundary-of-potential-variability.md) describes.

Because all three states hold at once, a single number or label like "how
adaptive is this system" is not meaningful — the honest answer is always
"adaptive with respect to what." This is also why a linear causal model
cannot predict how the system will respond to a new disruption: the same
system that handles one class of surprise with fluent, well-adapted ease can
turn out brittle on the very next disruption if it falls in the maladapted
slice instead, and nothing about the first response predicts which slice the
next disruption will land in. Modelling this honestly needs non-linear tools
that can represent tipping points, and it needs a metric that tracks
direction, not a snapshot: whether the system's [margins of
manoeuvre](preserving-margin-for-future-response.md) are currently expanding
or contracting, since that trend is what actually indicates which way the
brittle slice is moving.
