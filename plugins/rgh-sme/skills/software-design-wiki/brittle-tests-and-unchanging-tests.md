---
type: concept
title: Brittle Tests and Unchanging Tests
description: >
  A brittle test fails on harmless production changes; the ideal test needs
  no updates except when requirements change — achieved primarily by testing
  through public APIs and asserting state, not interactions.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 14"
---

A **brittle test** fails in response to an unrelated, harmless change to
production code — distinct from a **flaky test**, which fails nondeterministically
with no code change. At scale, even a small fraction of spuriously breaking
tests wastes enormous engineering time.

**Strive for unchanging tests** — the ideal test never changes after being
written unless system *requirements* change. How production changes should
affect tests:

| Change type | Expected test impact |
| ----------- | -------------------- |
| Pure refactoring (internals change, interface doesn't) | No test changes |
| New features | Add new tests only |
| Bug fixes | Add missing test case; existing tests unchanged |
| Behavior changes | Update tests — the only expected case |

**Test via public APIs** ("use the front door first"): invoke the system the
way real users would. If a test works like a user, anything that breaks the
test would also break a user — the test encodes a genuine contract. Reaching
into internals (e.g. stripping `private` to test internal methods) makes tests
brittle: nearly any refactor can break them while users notice nothing.

"Public" here means exposed to third parties outside the owning team — not
necessarily a language `public` keyword. Rules of thumb:

- A helper class supporting one or two others is not its own unit — test it
  through those classes.
- A package/class anyone may depend on without consulting owners is a unit —
  test it directly via its own API.

**Test state, not interactions**: **State testing** observes outcomes after
exercise; **interaction testing** checks expected calls on collaborators.
Interaction tests are more brittle for the same reason testing private methods
is — they verify *how* a result was reached, not *what* the result is. A
`verify()` on a database write can miss a record deleted immediately after,
and can fail on an equivalent write via a different API. Prefer asserting
resulting state (e.g. record exists via a getter). Over-reliance on mocking
frameworks makes brittle interaction tests easy to write.

See [state testing over interaction testing](state-testing-over-interaction-testing.md),
[observable behavior versus implementation details](observable-behavior-vs-implementation-details.md),
and [four pillars of a good unit test](four-pillars-of-a-good-unit-test.md).
