---
type: concept
title: The Test Pyramid
description: >
  Favor many fast unit tests, fewer integration tests, and the fewest
  end-to-end tests — each layer trades feedback speed against regression
  protection without sacrificing resistance to refactoring.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 4"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

The test pyramid advocates a ratio of three test types: **unit tests** (base,
widest), **integration tests** (middle), **end-to-end tests** (top, narrowest).
Layer width ≈ test count; layer height ≈ closeness to emulating end-user behavior.

Each layer trades [fast feedback against protection against
regressions](four-pillars-of-a-good-unit-test.md):

- **End-to-end** — best regression protection (exercises the most code) but
  worst fast feedback and maintainability; reserve for critical functionality
  where no bugs can be tolerated and lower layers cannot provide equivalent
  protection.
- **Unit** — best fast feedback; majority of the suite.
- **Integration** — middle ground.

**No layer sacrifices resistance to refactoring** — end-to-end and integration
tests score higher only as a side effect of being more detached from production
code, not because unit tests are exempt. All tests, including unit tests, must
minimize false positives by coupling to [observable behavior, not implementation
details](observable-behavior-vs-implementation-details.md).

**Integration-test guideline** (Khorikov): cover as many business-scenario edge
cases as possible with unit tests; use integration tests for one happy path per
scenario plus edge cases unit tests cannot reach. A *happy path* is successful
execution; an *edge case* yields an error.

**Shape varies by project**:

- Mostly CRUD with little algorithmic complexity — the pyramid **flattens toward
  a rectangle** of roughly equal unit and integration tests; trivial unit tests
  on simple code add little value while integration tests still verify subsystem
  wiring.
- API with a single out-of-process dependency (e.g. database, no UI) — more
  end-to-end tests become viable; without a UI they run fast and end-to-end
  tests become nearly indistinguishable from integration tests except that
  end-to-end requires external hosting.

Google's rough target mix (~80% narrow-scoped unit, ~15% medium-scoped
integration, ~5% large-scoped end-to-end) balances engineering productivity and
product confidence. Antipatterns:

- **Ice cream cone** — many end-to-end, few unit/integration tests; slow,
  unreliable; common when prototypes ship without addressing testing debt.
- **Hourglass** — many end-to-end and many unit tests but few integration tests;
  end-to-end failures that medium-scope tests would catch faster; occurs when
  tight coupling makes dependencies hard to instantiate in isolation.

See [integration versus end-to-end tests](integration-vs-end-to-end-tests.md)
and [test size versus test scope](test-size-vs-test-scope.md).
