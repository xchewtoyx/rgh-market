---
type: concept
title: Output-Based Testing
description: >
  Exercise a pure or isolated decision function by asserting on its return
  value or instruction objects — no mocks, no shared mutable state, fast and
  maintainable when the core is truly side-effect free.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 6"
---

**Output-based testing** asserts on return values or decision objects from
[referentially transparent](referential-transparency-and-pure-functions.md)
core logic — contrast with state-based testing (assert mutated object state)
and communication-based testing (verify calls to collaborators).

Audit-system refactor trajectory:

1. **Direct filesystem** — integration-style; slow, hard to parallelize; poor
   fast feedback and maintainability despite good regression/refactoring scores.
2. **Mock filesystem** — legitimate mock use when filesystem I/O is observable
   to external consumers; faster but convoluted setup hurts readability.
3. **Functional core** — `AddRecord(files, visitor, time)` returns `FileUpdate`;
   `Persister` applies it. Test: plain input array → assert `FileUpdate`. No
   mocks; maintainability reaches "good."

Making output types **value objects** (struct/custom equality) collapses
multi-field assertions to one comparison.

Output-based tests run as fast as mocked versions when the core has no
out-of-process collaborators. Prefer when [functional architecture for
testability](functional-architecture-for-testability.md) separates core from shell.

## Style comparison

Three verification styles (a single test may combine them):

| Style | What it checks | Refactoring resistance | Maintainability |
| --- | --- | --- | --- |
| Output-based | Return value | Best — couples only to the method under test | Best — short, no out-of-process deps |
| State-based | Resulting state after operation | Medium — also depends on class state API | Medium — state assertions often verbose |
| Communication-based | Calls to collaborators | Worst when misapplied — see [intra-system vs inter-system](intra-system-vs-inter-system-communication.md) | Worst — mock setup and chains add bulk |

Protection against regressions and fast feedback do not depend on style — they
depend on how much significant code is exercised. Communication-based tests can
be marginally slower because mocks add runtime latency, but the difference is
negligible unless the suite is huge. Overusing communication-based testing can
produce shallow tests that mock everything else — a common failure mode, not an
intrinsic property of the style.

**Maintainability mitigations for state-based tests**: helper methods hiding
assertion boilerplate (worthwhile only when reused across many tests); converting
asserted types to **value objects** with library equality (e.g. `BeEquivalentTo`)
— works only when the class is inherently a value; otherwise causes [code
pollution for testing](code-pollution-for-testing.md).

**Conclusion**: prefer output-based when the code permits; in most OOP codebases
that means restructuring toward [functional architecture for
testability](functional-architecture-for-testability.md).

Errors can be explicit in signatures (e.g. tuple with `Error`) for shell handling.

See [four pillars of a good unit test](four-pillars-of-a-good-unit-test.md).
