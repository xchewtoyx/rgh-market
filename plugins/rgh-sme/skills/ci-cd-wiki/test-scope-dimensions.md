---
type: concept
title: Test Scope Dimensions
description: >
  Test scope measures how much code a test validates — from a single method
  to full-system behavior — independently of the resources the test consumes.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Test Scope Dimensions

**Test scope** is how much of the codebase a test validates. It is a separate
dimension from [test size constraints](test-size-constraints.md) (resources
and runtime permissions). Executing a line of code is not the same as
asserting it behaved correctly — size and scope correlate but do not determine
each other.

Three scope levels:

- **Narrow** ("unit tests") — logic in a small, focused part of the codebase
  (a class or method).
- **Medium** ("integration tests") — interactions between a small number of
  components (e.g. a server and its database).
- **Large** (functional/end-to-end/system tests) — several distinct parts of
  the system, or emergent behaviors not expressible in a single class.

Important nuance: **narrow scope refers to code being validated, not code being
executed.** A unit test naturally invokes dependencies; Google prefers keeping
real dependencies in place when feasible rather than doubling everything away
— see [independent testability](independent-testability.md) for when doubles
and service virtualization still pay off.

Scope/size independence examples:

- A broad-scoped server-endpoint test (parsing, validation, business logic)
  can remain **small** if all out-of-process dependencies are doubled.
- A narrow-scoped UI date-picker test may require a full browser and therefore
  be **medium-sized**.

Narrow scope tends to pair with small size and broad scope with medium/large
size, but pipeline designers should classify both dimensions explicitly when
placing tests in [presubmit vs. postsubmit](presubmit-vs-postsubmit-testing.md)
stages and when balancing the
[test automation pyramid](test-automation-pyramid.md).
