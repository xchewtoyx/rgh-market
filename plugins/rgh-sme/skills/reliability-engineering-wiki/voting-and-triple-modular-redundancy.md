---
type: concept
title: Voting and Triple Modular Redundancy
description: >
  Running several independent implementations of the same function in parallel and comparing their outputs so a single faulty result gets outvoted rather than propagating.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 4"
---

**Voting** detects a fault by comparing results from multiple sources
expected to agree and picking the trustworthy one (majority rule, or a
computed average) rather than trusting any single result outright. The
voting logic itself must be a simple, rigorously tested singleton, since it
becomes a new single point of failure if it isn't. Three variants differ in
where the diversity lives:

- **Replication** — identical clones running the same implementation on the
  same inputs. Protects only against random hardware failure; a bug in the
  shared implementation or specification produces identical wrong answers
  from every clone, so replication alone gives no protection against
  design or implementation defects.
- **Functional redundancy** — independently-built implementations of the
  same specification, guarding against common-mode implementation bugs.
  Still vulnerable to a shared *specification* error, and costs more to
  build and verify than plain replication.
- **Analytic redundancy** — diversity extends to the inputs and outputs
  too, not just the implementation, so even a specification error in one
  approach doesn't produce the same wrong answer everywhere (e.g. avionics
  computing altitude three separate ways: barometric pressure, radar
  altimeter, and geometric look-down angle). This is the strongest
  guarantee but needs a more sophisticated voter — one that can judge
  relative sensor reliability and blend/smooth values rather than apply a
  simple majority or average.

**Triple Modular Redundancy (TMR)** is the standard concrete instantiation
of voting: three identical components fed identical inputs, with a voter
that flags disagreement and selects an output. It generalizes to 5-way,
19-way, or higher odd-numbered redundancy, but three is usually treated as
the practical sweet spot — with three independent components, the
probability of two or more failing simultaneously is vanishingly small, so
additional replicas buy little extra protection for their added cost.
Voting-based fault detection traces back to von Neumann's work on building
reliable systems out of unreliable components.

Voting/TMR is a stronger, more expensive alternative to a bare [N+M
redundancy](n-plus-m-redundancy.md) pool: N+M assumes a failed unit is
detectable by its own crash or health-check failure, whereas voting also
catches a unit that stays "up" but silently produces a *wrong* answer —
the failure mode N+M redundancy cannot see. This makes voting the right
tool specifically when incorrect output, not just downtime, is the risk
being defended against.
