---
type: concept
title: Matching Response Abstraction to Uncertainty
description: >
  As a situation departs further from what was anticipated, the useful
  response shifts from concrete, action-level protocols toward abstract,
  goal-level guidance — a fixed procedure is only well-matched to low
  uncertainty.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 1"
---

Pre-planned responses are written at a fixed level of specificity, but the
uncertainty they are deployed into is not fixed — it rises as a situation's
defence layers breach one after another. A response that stays useful across
that rise has to change its own level of abstraction as it goes: concrete,
step-by-step, action-oriented protocols are well-matched only to the low end
of the uncertainty range, where the situation resembles what the protocol's
authors anticipated closely enough for its steps to still apply. As
uncertainty rises past that range, the same fixed steps stop being useful —
not because people execute them badly, but because a specific action-level
answer is the wrong *kind* of guidance for a question whose situation no
longer matches its premises. What remains useful is abstract, goal-oriented
guidance: the intent behind the response, not its concrete steps, because
intent still applies to situations the original authors never enumerated.

This gives [the three specification levels of organisational
rules](goal-process-action-rules.md) — goal, process, action — a real-time
reading, not just an organisational-design one: as a live situation
escalates, effective guidance migrates from the action-rule level toward the
goal-rule level, and an operator or team who can only execute at the action
level runs out of applicable guidance exactly at the point they need it
most. This is also why [communicated intent](upward-and-downward-resilience.md)
from the blunt end matters more, not less, as uncertainty rises — a goal
rule is only usable in the moment if its reasoning was actually explained in
advance, not just its steps.

The same shift shows up inside the practitioner's own cognition, not just in
which guidance applies: see [traversing the goal-means
hierarchy](traversing-the-goal-means-hierarchy.md) for how a resilient
response requires moving upward from concrete, low-level goals to the
abstract, high-level goal they actually serve.
