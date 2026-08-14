---
type: concept
title: AAA Test Structure
description: >
  Split every unit test into arrange, act, and assert so readers can scan any
  test quickly — act is usually one line, and multiple act sections signal a
  test covering more than one behavior.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 3"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 14"
---

Every unit test splits into three parts:

- **Arrange** — bring the system under test (SUT) and dependencies to desired state.
- **Act** — invoke the SUT; capture outputs if any.
- **Assert** — verify return value, final state, or (when appropriate) outgoing
  interactions.

Uniform structure reduces suite-wide maintenance cost once readers internalize it.

**Given-When-Then** is the same composition with names better suited to
non-programmers (Given = arrange, When = act, Then = assert).

Under TDD, starting from assert (expected outcome) then working backward is
viable; when production code already exists, start from arrange.

**Avoid multiple act sections** in unit tests — signals multiple behaviors;
split into separate tests. Exception: slow integration tests against
hard-to-reset out-of-process state may combine acts to reduce external
interactions; [unit tests should never multi-act](mocks-for-integration-tests-only.md).

**Avoid if statements in tests** — always split; no integration-test exception.

**Sizing**:

- Arrange often largest; extract to helpers or Object Mother / Test Data Builder
  when it dominates.
- **Act should normally be one line** — multi-line act may mean the public API
  forces clients to remember follow-up calls ([invariant violation](information-hiding.md)
  risk); fix encapsulation in business logic, less strictly for utilities.
- **Multiple assertions per test is fine** when they verify one unit of
  behavior's outcomes — "one assertion per test" wrongly equates unit with class.
  Oversized assert sections may signal missing equality/abstraction in production.

Name the SUT instance `sut` when several objects appear — clarifies the entry
point under test.

Use `// Arrange` comments when blank lines alone aren't enough (complex integration
setup); drop comments when structure is obvious.

See [test behaviors not methods](test-behaviors-not-methods.md) and [DAMP over
DRY in test code](damp-over-dry-in-tests.md).
