---
type: concept
title: Mocks for Integration Tests Only
description: >
  Domain code should be complex without out-of-process collaborators; controllers
  orchestrate unmanaged dependencies — so mocks belong in integration tests,
  not unit tests of domain logic.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 9"
---

Per [four types of code for testing priority](four-types-of-code-for-testing-priority.md):
code should either talk to out-of-process dependencies **or** be complex — never
both. Two layers result:

- **Domain model** — complexity; covered by unit tests without mocks.
- **Controllers** — orchestration and unmanaged communication; covered by
  integration tests where mocks apply.

Since mocks apply only to unmanaged dependencies, and only controllers touch
those in a well-factored design, **mocks are for integration tests only** —
not unit tests of domain classes.

**Mock count per test is not a smell** — one behavior may legitimately involve
multiple unmanaged dependencies (logger + message bus); count follows dependency
participation, not "units of code."

When interaction testing at the edge, verify both existence **and** absence of
calls (`Times.Once`, `VerifyNoOtherCalls()`) for backward compatibility.

See [mock at system edges](mock-at-system-edges.md) and [classical versus London
unit testing schools](classical-vs-london-unit-testing-schools.md).
