---
type: concept
title: Executable Specification
description: >
  Writing acceptance criteria as automated tests in shared domain language
  makes a requirement specification that cannot silently go stale — it
  fails the moment the system's actual behavior diverges from it.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Jez Humble, David Farley), ch. 4, ch. 8"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 17"
---

An executable specification is an acceptance test written in clear,
domain-level language that serves two purposes at once: automated
regression verification, and living documentation of what the system
actually does. Because it runs against the real system, it cannot go
silently stale the way a prose requirements document can — if the
behavior changes, the specification fails until someone updates it,
rather than quietly describing a system that no longer exists.

This depends on a shared **ubiquitous language** — a vocabulary defined
jointly by domain experts, developers, and testers and used directly in
the specification text, so a business stakeholder can read and validate
the requirement without a technical translation step. Behavior-Driven
Development operationalizes this with structured Given-When-Then
scenarios that read as both a requirement and a test simultaneously — the
same content Volere would capture as a [scenario for a business use
case](scenario-for-business-use-case.md), written precisely enough to run.

Getting to an executable acceptance criterion this concrete works best
when it's written collaboratively and early: QA, business analysts, and
developers agreeing on acceptance criteria as executable specifications
*before* development starts, rather than testers writing verification
after the fact against whatever got built. A related device for the same
purpose at the feature-hypothesis level is a fixed template — "we believe
[change] will result in [outcome]; we will have confidence to proceed when
[measurable threshold]" — which forces a proposed change to state its
expected outcome and an explicit, falsifiable acceptance threshold before
work begins, functioning as a [fit criterion](fit-criterion.md) for a
hypothesis rather than a fully specified feature.
