---
type: concept
title: State Testing Over Interaction Testing
description: >
  Assert on returned values or resulting state after exercising the system;
  interaction testing that verifies collaborator calls is a brittle fallback
  when state cannot be observed.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 6"
---

Two verification styles (also called **state-based** and **communication-based**
in Khorikov's three-style taxonomy — the third style, [output-based
testing](output-based-testing.md), is state testing on return values only):

- **State testing** — call the system under test and assert on a return value
  or resulting state change.
- **Interaction testing** — assert that particular functions were called with
  specific arguments and counts, without executing real implementations.

**Prefer state testing.** Interaction tests leak [implementation
details](observable-behavior-vs-implementation-details.md): they check *how* a
result was produced, not *what* happened. They can miss real bugs (e.g. a
save followed immediately by delete) and fail on harmless refactors (equivalent
write via a different API). Google engineers call overused interaction tests
**change-detector tests**.

**When interaction testing is appropriate**:

- No usable real implementation or [fake](fake-objects.md) exists — fallback
  confidence, ideally supplemented by larger-scope state tests.
- The **number or order of calls itself** is the behavior under test (e.g.
  verifying a cache limits database reads: `atMostOnce()` on `selectRecords()`).

**Best practices when interaction testing**:

- Prefer interaction verification for **state-changing** functions (send
  email, save record), not queries whose return values can be asserted directly.
- Avoid overspecification — one behavior, minimum necessary assertions; use
  flexible matchers (`any()`, `eq(...)`) where exact args aren't the point.

**Don't assert interactions with stubs**: a stub supplies input data; verifying
its calls is [overspecification](mocks-vs-stubs-taxonomy.md). Command-query
separation maps cleanly: doubles for commands are mocks; doubles for queries
are stubs.

See [brittle tests and unchanging tests](brittle-tests-and-unchanging-tests.md)
and [overabstracted tests](tests-should-assert-behavior-not-call-mechanics.md).
