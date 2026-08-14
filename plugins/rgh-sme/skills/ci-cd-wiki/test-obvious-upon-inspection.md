---
type: concept
title: Tests Obvious Upon Inspection
description: >
  Automated tests should contain only the information needed to exercise and
  verify one behavior, with no control flow — because there are no tests for
  tests and reviewers must catch bugs manually.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 13"
---

# Tests Obvious Upon Inspection

A good automated test includes **only** what is required to set up, exercise,
and verify the behavior under question — nothing more. That aids code review
and failure diagnosis: when a test fails, the cause should be readable without
tracing loops or branches inside the test itself.

Corollary: **avoid control-flow statements in tests** — conditionals, loops,
and similar constructs risk bugs in the test code and obscure which assertion
failed. There are no tests for tests; they depend on careful manual review.

This pairs with [test size constraints](test-size-constraints.md)'s
**hermetic** requirement — a test should contain all information to set up,
execute, and tear down its environment without assuming execution order, shared
databases, or other ambient state (harder as tests grow larger, but still worth
pursuing). Together, obvious-upon-inspection and hermeticity support the
determinism goals in
[commit test suite design principles](commit-test-suite-design.md) and the
reliability checklist in
[automated test suite qualities](automated-test-suite-qualities.md).
