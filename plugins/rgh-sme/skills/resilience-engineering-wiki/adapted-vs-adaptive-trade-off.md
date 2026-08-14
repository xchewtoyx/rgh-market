---
type: concept
title: Adapted versus Adaptive — The Optimality/Brittleness Trade-Off
description: >
  A complex adaptive system cannot be simultaneously fully optimised for its
  current environment and resilient to a changed one — tight tuning to
  "what is" is bought with brittleness against "what might become."
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 1"
---

Doyle's optimality/brittleness trade-off, from complex adaptive systems
theory: a system cannot be both fully **adapted** — hyper-optimised to its
current, static environment — and fully **adaptive** — flexible enough to
absorb a shift in that environment — at the same time. Every unit of
optimisation against the environment as currently known is a unit of
flexibility no longer available for the environment as it might become. This
is an architectural choice a system's designers make, often implicitly, not
a temporary state that more effort corrects.

Piaget's cognitive-development pair gives the same trade-off a mechanism at
the level of an individual or organisation's working model of its world:

- **Assimilation** — filtering new inputs to fit existing mental or
  procedural structures, via routine, homeostatic processing. Cheap, fast,
  and how most of normal work runs.
- **Accommodation** — revising the internal structures themselves to match
  what the environment now actually demands, triggered by the discomfort of
  inputs that no longer fit (cognitive dissonance).

A system's adaptive capacity depends on a standing, uncomfortable
**permanent under-adaptation** — some dissonance always present, providing
the pressure that drives accommodation rather than letting assimilation run
unchallenged indefinitely. A system tuned to eliminate that dissonance
entirely (every input smoothly assimilated, nothing ever provoking revision)
has traded away its own capacity to accommodate a future it did not
anticipate — the individual-cognition version of [the law of stretched
systems](law-of-stretched-systems.md) consuming reserve capacity, and the
mechanism behind why [second-order
adaptability](resilience-as-adaptive-capacity.md) cannot be designed in once
and left alone.

Practical corollary: an organisation that has driven out all its friction,
variance, and "inefficiency" against present conditions has very likely
optimised itself into exactly the brittleness this trade-off predicts — see
[buffering capacity, margin, and tolerance](buffering-margin-and-tolerance.md)
for the structural properties that quietly disappear when optimisation is
pursued without limit.

Restated at organisational-design granularity rather than individual
cognition, this is [the standardization-versus-flexibility organizational
tension](standardization-vs-flexibility-organizational-tension.md): five
concrete axes (formal procedure vs local autonomy, centralisation vs
decentralisation, and others) that an organisation manages continuously
rather than resolves once.
