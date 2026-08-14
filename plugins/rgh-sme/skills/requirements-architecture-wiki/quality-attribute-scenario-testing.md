---
type: concept
title: Quality-Attribute Scenario Testing
description: >
  Treating a quality attribute claim — performance, security, scalability
  — as a testable scenario with production evidence behind it, rather
  than an unverified assertion in a design document.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 12"
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 3"
---

A design document can assert that a system is "scalable" or "secure"
without that claim ever being checked against anything. Quality-attribute
scenario testing closes that gap: it exercises a
[non-functional requirement](non-functional-requirement.md) as a concrete,
testable scenario — including, where appropriate, actual production or
runtime evidence — so the claim is reconciled against reality rather than
resting on a slide in a design review. See [quality attribute
scenario](quality-attribute-scenario.md) for the six-part format
(stimulus, source, environment, artifact, response, response measure)
that makes a scenario precise enough to test in the first place.

This is the same discipline a [fit criterion](fit-criterion.md) applies to
a functional or non-functional requirement, applied specifically to
architecture-level quality attributes: instead of "the system must be
secure," state and test a specific scenario ("an unauthenticated request
to this endpoint is rejected within Xms under Y concurrent load") that can
actually pass or fail. See [SLO as documented
requirement](slo-as-documented-requirement.md) for the most fully worked
example of this pattern applied to reliability specifically — a target
that is not just stated but continuously, automatically checked against
production behavior.
