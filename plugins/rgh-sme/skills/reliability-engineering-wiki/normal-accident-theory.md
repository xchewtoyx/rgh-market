---
type: concept
title: Normal Accident Theory
description: >
  In systems with high interactive complexity and tight coupling, failure is not an anomaly to be engineered away but a statistically inevitable property of the system itself.
sources:
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 3"
---

**Normal accident theory**, from Dr. Charles Perrow's study of the Three Mile
Island partial nuclear meltdown, holds that in a sufficiently complex system
no single person can see the whole system or fully predict how its parts
interact. Once a failure begins, it cascades unpredictably along paths of
least resistance — the exact propagation path can't be foreseen even by
experts who understand every individual component. Perrow's conclusion:
accidents in such systems aren't due to isolated negligence or a component
that should have been engineered better — they are a "normal," statistically
expected property of running a system with high interactive complexity and
tight coupling at all. Related: Dr. Sidney Dekker's observation that in
complex systems, doing the same thing twice will not predictably yield the
same result, meaning static checklists and best practices, while valuable,
cannot alone prevent or fully contain catastrophe.

This reframes the goal of reliability work: not to search for a design that
eliminates failure, but to build a [system stability](system-stability.md)
posture that assumes failure is inevitable and optimizes for detecting it
early and containing its blast radius — the same conclusion that motivates
[embracing risk via error budgets](hundred-percent-reliability-is-the-wrong-target.md)
rather than chasing zero-failure targets, and that motivates structural
containment patterns such as the [circuit breaker
pattern](circuit-breaker-pattern.md), [load shedding](load-shedding.md), and
the [bulkhead pattern](bulkhead-pattern.md) described under [cascading
failure](cascading-failure.md). It also underlines why [system
understandability](system-understandability.md) is a reliability property in
its own right: interactive complexity is exactly what erodes an engineer's
ability to reason about a system's behavior under stress.

Tight coupling — the degree to which a failure in one part of a system
propagates directly and quickly into another, with little slack to absorb or
delay the effect — is the second necessary ingredient alongside interactive
complexity; see [loose architectural coupling](loose-architectural-coupling.md)
for the structural countermeasure of deliberately reducing coupling between
services.
