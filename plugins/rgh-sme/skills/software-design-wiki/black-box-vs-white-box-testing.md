---
type: concept
title: Black-Box Versus White-Box Testing
description: >
  Write tests from requirements without peeking at internals (black-box) for
  refactoring resistance; use white-box analysis only to find coverage gaps,
  then write black-box tests for those gaps.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 4"
---

- **Black-box testing** — verifies functionality without knowledge of internal
  structure; built around specifications and requirements — tests *what* the
  system should do, not *how*.
- **White-box testing** — verifies inner workings; tests derived from source
  code, not requirements.

| | Protection against regressions | Resistance to refactoring |
| --- | --- | --- |
| White-box | Good | Bad |
| Black-box | Bad (alone) | Good |

White-box testing is more thorough — source analysis surfaces errors
specification-only testing may miss — but resulting tests tend to be brittle,
coupled to specific implementation, producing false positives and often
untraceable to business-meaningful behavior (a signal of fragility and low
value).

Since [resistance to refactoring](four-pillars-of-a-good-unit-test.md) is
non-negotiable (binary — a test either has it or not), **choose black-box
testing by default** at every level — unit, integration, end-to-end. If a test
cannot be traced back to a business requirement, treat that as brittleness:
restructure or delete rather than keeping it. Exception: utility code with high
algorithmic complexity (see [four types of code for testing
priority](four-types-of-code-for-testing-priority.md)).

**Best combination**: use white-box techniques to *analyze* the suite — coverage
tools to find unexercised branches — then write tests for those branches using
the black-box method (treating the code as unknown). White-box for gap analysis,
black-box for test construction.

See [observable behavior versus implementation details](observable-behavior-vs-implementation-details.md)
and [test pyramid](test-pyramid.md).
