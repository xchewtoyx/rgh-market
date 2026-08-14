---
type: concept
title: Test Doubles Overview
description: >
  A test double stands in for a real dependency in a test, trading fidelity
  for speed and control — but doubles require upfront testability design and
  can produce brittle tests when overused.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
---

A **test double** is an object or function that stands in for a real
implementation in a test (stunt-double analogy). Doubles enable small, fast,
non-flaky tests for code that would otherwise need slow or unreliable
dependencies.

**Trade-offs**:

- **Testability** — code must be designed so real implementations can be
  swapped ([seams](seam.md), [dependency injection](dependency-injection-pattern.md)).
  Retrofitting is costly.
- **Applicability** — improper use, especially at scale, produces brittle,
  complex, low-value tests.
- **Fidelity** — how closely the double matches production. Low fidelity
  yields low-value tests; perfect fidelity is often infeasible. Unit tests
  with doubles usually need larger-scope tests against real implementations.

**Three usage techniques** (Google):

1. **Faking** — lightweight, behaviorally similar alternative (in-memory DB).
   See [fake objects](fake-objects.md) and [contract tests for fakes](contract-tests-for-fakes.md).
2. **Stubbing** — hardcoded return values inline (often via mocking frameworks).
   Quick but can leak implementation details. See [stubbing in tests](stubbing-in-tests.md).
3. **Interaction testing** — verify calls (args, count) without running real
   code. Narrow use cases; generally avoid. See [state testing over interaction
   testing](state-testing-over-interaction-testing.md).

Khorikov collapses Meszaros's five types (dummy, stub, spy, mock, fake) into
two functional roles: **mocks** examine *outgoing* interactions (commands,
side effects); **stubs** emulate *incoming* data (queries) without examination.
See [mocks versus stubs taxonomy](mocks-vs-stubs-taxonomy.md).

Google's culture shifted from overusing mocking frameworks toward
[classical testing with real implementations](prefer-real-implementations-in-tests.md)
when possible — mocks were cheap to write but expensive to maintain.

**Mocking frameworks** (Mockito, `unittest.mock`, googlemock) create doubles
inline, reducing boilerplate but encouraging overuse if unchecked.

See also [mock objects](mock-objects.md) and [mock only types you own](mock-only-types-you-own.md).
