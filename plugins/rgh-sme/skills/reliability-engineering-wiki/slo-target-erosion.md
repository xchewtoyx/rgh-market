---
type: concept
title: SLO Target Erosion
description: >
  Quietly lowering an SLO target after repeated misses, rather than deliberately deciding to change it, sets up a reinforcing spiral toward ever-lower reliability instead of a stabilizing correction.
sources:
  - title: Thinking in Systems
    resource: "Thinking in Systems: A Primer (Meadows, ed. Wright), ch. 5"
---

An SLO is supposed to work as a *balancing* loop: measure actual
performance against the target, and when there's a gap, spend effort
closing it (see [error budget](error-budget.md) and [error-budget-driven
prioritization](error-budget-driven-prioritization.md)). **Target
erosion** is what happens when the target itself, instead of the
performance, is what moves to close the gap — each miss gets rationalized
("that's about all we can expect given the traffic growth," "not much
worse than last quarter") into a slightly loosened target, which shrinks
next quarter's discrepancy without anyone deciding to accept lower
reliability. This converts what should be a self-correcting loop into a
reinforcing one: lower perceived performance → lower target → smaller gap
→ less corrective pressure → lower actual performance → repeat. The
erosion is dangerous specifically because it's gradual — a single sharp
drop in reliability provokes an obvious, urgent response, but a slow drift
downward erodes the team's own memory of how good the service used to be,
normalizing an ever-lower bar along the way.

The antidote is structural, not just vigilance: **don't let a target's
next value be set by its own recent worst performance.** Two concrete
tactics:

- Keep the target anchored to something outside the loop — user needs,
  business requirements, or a competitor's bar — so a bad quarter doesn't
  mechanically produce a lower number next quarter. Revisiting a target is
  legitimate and expected (see [SLO evolution
  triggers](slo-evolution-triggers.md)), but the revisit should be an
  explicit, justified decision made against those external anchors, not an
  automatic response to the miss itself.
- Where practical, anchor goal-setting to the *best* recent performance
  rather than the worst — the same feedback structure that produces a
  downward spiral when biased toward bad news produces an upward one when
  biased toward good news, which is the same mechanism that makes
  [error budget surplus](error-budget-surplus-for-experimentation.md) worth
  deliberately spending down rather than letting it silently become
  the new implicit baseline (see [being too reliable is a real
  cost](too-reliable-is-a-cost.md) for that symmetric failure mode).

This is a special case of a more general pattern: a system whose own
recent performance quietly redefines its own goal has lost a degree of
[resilience](resilience-vs-stability.md) without anyone deciding to trade
it away.
