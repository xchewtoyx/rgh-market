---
type: concept
title: Test Automation Pyramid
description: >
  A strategic model for structuring an automated test suite as a large base of
  fast unit tests, a moderate middle layer of component/acceptance tests, and a
  small apex of end-to-end and manual tests.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 4"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
  - title: Infrastructure as Code
    resource: "Infrastructure as Code, 2nd ed. (Kief Morris), ch. 8"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Test Automation Pyramid

The pyramid shape is a target ratio, not just a taxonomy: roughly 70–80% of
automated tests should be unit tests, 15–20% component/acceptance tests, and
under 5–10% full end-to-end UI tests, with exploratory testing sitting outside
automation entirely. Google targets roughly **80% narrow-scoped unit tests,
15% medium-scoped integration tests, and 5% large-scoped end-to-end tests**
by test-case count — balancing engineering productivity and product confidence.
The shape tracks both [test scope](test-scope-dimensions.md) and
[test size](test-size-constraints.md): unit tests return results in seconds,
acceptance tests in minutes, nonfunctional/exploratory testing in hours — so
the more of the suite that lives at the base, the faster the
[commit stage](commit-stage.md) and the overall
[deployment pipeline](deployment-pipeline.md) can give feedback.

## Anti-pattern: the inverted pyramid ("ice cream cone")

An organization that instead relies heavily on manual testing and fragile
end-to-end UI automation, with few unit tests underneath, inverts this shape.
The result is a test suite that is slow, expensive to run, and flaky — because
end-to-end tests are the most brittle layer (sensitive to timing, environment,
and unrelated UI changes) and there's no fast unit-test layer to catch most
defects before they ever reach that layer. Common in prototypes rushed to
production without addressing testing debt.

## Anti-pattern: the hourglass

Many end-to-end tests **and** many unit tests, but **few integration tests**
in the middle. Less severe than the ice cream cone, but end-to-end failures
that medium-scope integration tests would catch faster and more cheaply still
dominate debugging time. Often appears when tight coupling makes it hard to
instantiate individual dependencies in isolation — the architectural fix is
[independent testability](independent-testability.md), not adding more
end-to-end coverage.

Teams may reasonably shift the mix: more integration testing catches more
cross-component issues but runs slower; more unit testing runs faster but
cannot verify contracts between components built by different teams. A good
suite blends [sizes and scopes](test-scope-dimensions.md) appropriate to local
architecture and organizational realities.

## Test types by layer

- **Unit tests**: individual classes/methods/functions in isolation,
  milliseconds, external dependencies stubbed or mocked.
- **Component tests**: interactions between several internal
  components/modules without necessarily starting the whole application.
- **Automated acceptance tests**: whole application or service, black-box,
  business-facing — see [agile testing quadrants](agile-testing-quadrants.md)
  for how these relate to nonfunctional and exploratory testing.
- **Integration tests**: validate correct interaction with *real* other
  services, not stubs or test doubles — distinct from acceptance tests, which
  verify one application's own behavior. Integration tests are the most
  brittle layer because they depend on the state and availability of systems
  outside the one under test, so their count should be minimized and
  defect-finding pushed as far upstream (unit, then acceptance) as possible.
  [Independent testability](independent-testability.md)'s service
  virtualization and consumer-driven contract techniques exist specifically
  to shrink how many genuine integration tests are needed.

See also [automated acceptance testing](automated-acceptance-testing.md) for
how the acceptance-test layer is implemented as a pipeline gate.

If unit and acceptance tests feel too hard or expensive to write and
maintain, that's usually a symptom of overly tight-coupled architecture
lacking real module boundaries, not an inherent limit of testing — the fix is
a more loosely coupled system (see
[independent testability](independent-testability.md)), not abandoning fast
tests in favor of the slower layers.

## The shape inverts for declarative infrastructure code

The pyramid ratio assumes a codebase with lots of small, independently
testable units, which is true of most application code but not of
declarative infrastructure code (Terraform, CloudFormation, and similar).
Most declarative stack definitions are too large and too tied to the actual
infrastructure platform for meaningful unit testing, and testing the
declaration itself often just re-asserts what the syntax already says rather
than checking real behavior. The practical result is a **test diamond**
instead of a pyramid: a thin base of low-level tests, a wide middle of tests
that actually provision and check real (if disposable) infrastructure — see
[testing infrastructure code as a pipeline stage](infrastructure-code-testing-in-pipeline.md)
— and a narrow top, the same as the pyramid's apex. Infrastructure code
written with more imperative, programmable logic (loops, conditionals,
reusable libraries generating stack elements) has more in it that behaves
like regular application code, and correspondingly shifts back toward a
pyramid shape.
