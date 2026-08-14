---
type: concept
title: Cost-Benefit Inequality for Building a Change Mechanism
description: >
  A quantified test for whether building a reusable flexibility mechanism
  is worthwhile — compare N times the cost of handling each anticipated
  change without it against the mechanism's build cost plus N times the
  cost of handling each change with it.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 8"
---

A sharper, quantified version of [every piece of design infrastructure must
pay for itself](design-cost-benefit-of-infrastructure.md), applied
specifically to the decision of whether to build a reusable mechanism for
handling a class of anticipated future change (a configuration system, a
plug-in interface, a code generator) versus just hand-editing the code each
time a change of that kind is needed.

Given **N** anticipated future modifications of the same kind:

> N × (cost of one change *without* the mechanism) ≤ (cost of *building*
> the mechanism) + N × (cost of one change *with* the mechanism in place)

Build the mechanism only if the left side is at least as large as the
right — i.e., only if the mechanism's savings per change, multiplied
across all N anticipated changes, actually exceed what it cost to build in
the first place. This spans the whole spectrum from "no mechanism at all"
(cost per change without it is the full price of a source edit plus
revalidation) to a full self-adapting system (near-zero per-change cost,
but a very high mechanism-build cost).

Three caveats keep this from being a mechanical formula to plug numbers
into:

- **N is itself a prediction.** Fewer future changes than expected can
  turn an expensive mechanism into a net loss even though the inequality
  looked favorable at design time — see
  [YAGNI](yagni.md) for the discipline this argues toward: build the
  mechanism once the anticipated need is actually confirmed, not on a
  speculative guess about N.
- **Building the mechanism has opportunity cost.** Money and time spent on
  it isn't spent on features, performance, or other work — the inequality
  compares mechanism cost against the changes it saves, but doesn't
  account for what else that budget could have bought.
- **The inequality ignores time-to-availability.** A mechanism that's
  cheaper in the long run doesn't help if it isn't ready by the time the
  first anticipated change actually needs to land.

Never building any such mechanism while a class of change keeps recurring
anyway is itself a decision — and, left unexamined, is one of the concrete
ways a codebase accumulates [technical debt](technical-debt-as-a-design-decision.md).
See [binding time](binding-time.md) for how the mechanism, once built,
determines how late in the life cycle each individual change can actually
be applied.
