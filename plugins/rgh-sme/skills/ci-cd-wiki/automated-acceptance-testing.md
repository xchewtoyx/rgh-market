---
type: concept
title: Automated Acceptance Testing
description: >
  Automating business-facing acceptance criteria as executable, technology-run
  tests, so the deployment pipeline can gate every candidate on whether it
  actually meets its functional requirements, not just whether it compiles.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 8"
---

# Automated Acceptance Testing

The automated acceptance test gate is the [deployment pipeline](deployment-pipeline.md)
stage that answers "does this build actually do what the business needs,"
distinct from the [commit stage](commit-stage.md)'s "does this build compile
and pass unit tests." Manual regression testing at this scale is slow,
error-prone, and doesn't keep pace with a pipeline meant to run on every
commit — automation is what makes this gate viable as a routine, repeatable
part of delivery rather than an occasional, expensive activity.

## Executable specifications

Acceptance tests are written in clear domain language — a shared
**ubiquitous language** defined jointly by domain experts, developers, and
testers — so the same artifact serves two purposes: it's both an automated
regression test and living, always-current documentation of what the system
does. **Behavior-Driven Development (BDD)** structures these specifications as
`Given-When-Then` scenarios, synthesizing test-driven development with
acceptance criteria.

## Structuring the tests

See [acceptance test layering](acceptance-test-layering.md) for the
architecture that keeps these tests from becoming brittle as the UI or
protocol changes, and
[acceptance test data management](acceptance-test-data-management.md) for
keeping test scenarios isolated from each other.

## Performance targets

The full suite must run in under 1–2 hours, ideally under 30 minutes, to keep
the [deployment pipeline](deployment-pipeline.md)'s overall
[cycle time](cycle-time.md) reasonable. Two levers get it there:

- **Parallelization**: partition the suite and run scenarios concurrently
  across multiple runner nodes or a test grid.
- **Decouple UI from business logic**: run the large majority of scenarios
  directly against backend REST/gRPC APIs or service interfaces, reserving
  full browser/UI automation for a small number of key user journeys — this
  mirrors the [test automation pyramid](test-automation-pyramid.md)'s
  preference for cheaper, faster layers over the UI layer.
