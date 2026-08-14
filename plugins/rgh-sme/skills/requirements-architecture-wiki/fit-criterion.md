---
type: concept
title: Fit Criterion
description: >
  A fit criterion is a quantifiable, solution-independent measure attached
  to a requirement that converts an ambiguous statement into a testable
  pass/fail acceptance test.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 12"
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 12"
---

A fit criterion is an objective, quantifiable measure that tests whether a
proposed solution satisfies a specific requirement. Its purpose is to
convert a natural-language statement — which is inherently open to
interpretation — into something a tester can run a pass/fail check
against. It has to be unambiguous (words like "fast," "user-friendly,"
"secure," and "reliable" are not fit criteria until they've been converted
into numbers), testable, and solution-independent (expressed in terms of
the business result, not in terms of how the code happens to achieve it).

For example: "the product shall report weather alerts rapidly" is not
testable; "weather alerts shall appear on screen within 2.0 seconds of
reception, 99.9% of the time, under a peak load of 500 concurrent users"
is. Every [requirement](requirement-vs-design-decision.md) in the Volere
process must have exactly one fit criterion — a requirement without one
has not actually finished being specified, and the [quality
gateway](quality-gateway.md) checks for exactly this.

When a quality seems to resist quantification altogether, see
[decomposition for measurability](decomposition-for-measurability.md) for
a technique that breaks it into estimable sub-variables instead of
accepting "untestable" as the final word.

The same idea applies directly to architecture-level quality attributes:
treating a performance, security, or scalability claim as a testable
scenario — including runtime/production evidence where relevant — rather
than an unverified assertion in a design document is fit criteria applied
to [non-functional requirements](non-functional-requirement.md) at the
system level. See [quality-attribute scenario
testing](quality-attribute-scenario-testing.md) for that specific
technique, and [SLO as documented requirement](slo-as-documented-requirement.md)
for a worked case of a fit criterion for a reliability target.
