---
type: concept
title: The Four Abilities of Resilient Performance
description: >
  Anticipation, monitoring, response, and learning — the four abilities a
  system must exercise continuously to stay in control, each one's absence
  producing a distinct, named failure mode.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), epilogue"
---

Hollnagel's summary framework for what "staying in control" actually
requires, continuously and simultaneously, not as a one-time design property:

1. **Anticipation** — knowing what to expect: looking ahead to future
   demands and disruptions before they arrive.
2. **Attention / monitoring** — knowing what to look for right now: staying
   watchful for what is actually happening, as distinct from what was
   expected to happen.
3. **Response** — knowing what to do, and having the resources on hand to
   actually do it, once a demand is recognised.
4. **Learning** — continuously updating knowledge, competence, and resources
   from both successes and failures, so the other three abilities themselves
   improve over time rather than staying fixed.

**Each ability's absence is a specific, nameable failure**, not a generic
"the system wasn't careful enough." Jared Diamond's account of societal
collapse independently converged on the same three failure points — a
society fails to anticipate a problem, fails to perceive it once underway,
or fails to solve it once perceived — which map directly onto the negative
of the first three abilities here; Hollnagel's fourth, learning, is what
determines whether the same failure recurs.

The abilities are interdependent in ways that make partial success
misleading. Monitoring without anticipation catches only what is already
happening, with no lead time to respond. Response capability without
adequate anticipation or monitoring sits idle, unaware it is needed — a
[sacrifice judgement](sacrifice-judgements.md) can only be made by someone
who anticipated the need for one. And learning that only runs after failure,
never after success, misses most of the data: [Safety-II's whole
premise](safety-i-and-safety-ii.md) is that success and failure share the
same sources, so learning restricted to failure alone starves itself of most
of the available signal.

What actually blocks these four abilities in practice — the specific
constraints that turn "we should have anticipated/monitored/responded" into
"we couldn't have" — is addressed in [resilience as
control](resilience-as-control.md).

Learning is not merely the fourth item on this list — it directly enables
and reshapes the other three, and [three specific conditions determine
whether it actually happens](three-conditions-for-effective-learning.md).

A concrete organisational-level test of anticipation, monitoring, and
response together is whether the organisation can actually move between its
[functional states](state-space-model-of-organizational-functioning.md) when
conditions demand it — recognising that a transition is needed is
anticipation and monitoring; executing the transition is response.

Attempting to measure these four abilities directly with a survey runs into
a structural limit: an instrument administered to one operational function
tends to come back measuring [that function's micro-level operational
capabilities rather than the macro-level abilities
themselves](micro-survey-vs-macro-cornerstones-in-resilience-measurement.md).

A complementary framework sorts resilience not by which continuous ability
is exercised but by *when* relative to a threat: [Westrum's three temporal
horizons](westrum-three-temporal-horizons-of-resilience.md) — foreseeing and
avoiding, coping while a crisis unfolds, and repairing afterward — and a
system strong in one horizon is not thereby strong in the others.
