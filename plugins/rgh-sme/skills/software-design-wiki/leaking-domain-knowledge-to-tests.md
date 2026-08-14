---
type: concept
title: Leaking Domain Knowledge to Tests
description: >
  Re-deriving expected results in a test using the same algorithm as production
  duplicates implementation in the test and destroys resistance to refactoring.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 11"
---

Common in tests for complex algorithms: the test computes the expected value
with the same logic as production (e.g. `expected = value1 + value2` before
calling `Add(value1, value2)`). This duplicates the implementation — coupling
to [implementation details](observable-behavior-vs-implementation-details.md)
— and scores near zero on [resistance to refactoring](four-pillars-of-a-good-unit-test.md):
it cannot distinguish legitimate failures from false positives. Teams may
copy-paste updated production logic into tests without investigating.

**Fix**: hard-code expected results (`[InlineData(1, 3, 4)]`). Values should
be pre-calculated independently of the system under test — ideally with a
domain expert. Warranted when the algorithm is complex enough to double-check.
When refactoring legacy systems, legacy outputs can serve as independently
derived expected values ([characterization tests](characterization-tests.md)).

Contrast with [DAMP over DRY](damp-over-dry-in-tests.md): duplicating literal
expected values in tests is good; duplicating production *algorithms* in
tests is not.

See also [observable behavior versus implementation details](observable-behavior-vs-implementation-details.md).
