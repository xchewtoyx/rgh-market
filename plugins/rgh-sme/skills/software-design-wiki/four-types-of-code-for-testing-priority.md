---
type: concept
title: Four Types of Code for Testing Priority
description: >
  Plot production code by complexity or domain significance versus number of
  collaborators to find where unit tests pay off, where they don't, and
  where overcomplicated design needs refactoring before testing.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 7"
---

All production code can be categorized along two dimensions:

- **Complexity or domain significance** — complexity measured by cyclomatic
  complexity (1 + branching points; compound predicates count as multiple
  branches). Domain significance is how directly code connects to end-user
  goals. The two are independent: zero branches can still be business-critical.
- **Number of collaborators** — dependencies that are mutable, out-of-process,
  or both (implicit and explicit). Immutable value objects don't count.
  Out-of-process collaborators are worst for the domain model: they force mock
  machinery and threaten [resistance to refactoring](four-pillars-of-a-good-unit-test.md).

Crossing the axes yields four quadrants:

| Quadrant | Profile | Testing guidance |
| -------- | ------- | ---------------- |
| Domain model and algorithms | High complexity/significance, few collaborators | Best ROI — unit test thoroughly |
| Trivial code | Low complexity/significance, few collaborators | Don't test (constructors, one-line properties) |
| Controllers | Low complexity/significance, many collaborators | Brief integration tests, not unit tests |
| Overcomplicated code | High complexity/significance, many collaborators | Refactor first — split into algorithms + controllers |

**Tip**: the more important or complex code is, the fewer collaborators it
should have. Eliminating the overcomplicated quadrant and unit-testing only
domain model/algorithms yields a valuable, maintainable suite. One hundred
percent coverage is not the goal — "better to not write a test at all than
to write a bad test."

**Hidden branching**: reconstruction/utility code may have few visible
branches yet still warrant tests because framework operations (array indexing,
casts) contain hidden decision points that can throw.

**Preconditions**: test preconditions with domain significance (invariants);
skip preconditions that are pure data-shape guards without domain meaning.

See [humble object pattern](humble-object-pattern.md) for extracting
testable domain logic from orchestration, and [functional architecture for
testability](functional-architecture-for-testability.md) for pushing
collaborators out of the core entirely.
