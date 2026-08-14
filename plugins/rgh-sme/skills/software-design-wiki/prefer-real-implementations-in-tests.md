---
type: concept
title: Prefer Real Implementations in Tests
description: >
  Classical testing uses a dependency's real implementation when it is fast
  and deterministic, maximizing fidelity and catching cross-module contract
  violations that doubles would hide.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

Google's default preference: use the **real implementation** of a dependency in
tests when feasible — **classical testing** — contrasted with **mockist
testing**, which defaults to mocking frameworks. Classical style maximizes
fidelity to production behavior.

**Prefer realism over isolation**: doubles isolate the SUT from dependency
code, arbitrarily limiting what the test exercises to one class. A good test
targets the API under test, not internal structure. Real implementations mean
a bug in a dependency correctly fails dependent tests — a desirable signal of
production risk that good CI can trace to root cause.

**When real implementations shine**: fast, deterministic, simple dependencies
— value objects (money, dates, addresses, collections).

**When to switch to doubles**:

- **Execution time** — no fixed threshold; depends on team tolerance and test
  count. Use real until too slow, then switch. Parallelization and build
  caching mitigate cost.
- **Determinism** — real code may be nondeterministic (threads, live HTTP,
  system clock). Prefer a double with fixed time or a hermetic test instance.
- **Construction cost** — real implementations need full dependency trees;
  ideal fix is reusing production construction (factories, DI) with substitution
  points, not hand-wiring mocks per test.

**`@DoNotMock` pattern**: API owners can declare types that should never be
mocked because real implementations or [fakes](fake-objects.md) exist. Once
an API is mocked thousands of times, doubles drift from the real contract and
block safe API evolution.

See [classical versus London unit testing schools](classical-vs-london-unit-testing-schools.md)
and [fake objects](fake-objects.md).
