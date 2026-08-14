---
type: concept
title: Stubbing in Tests
description: >
  Stubbing hardcodes a dependency's return value inline in a test — quick but
  prone to obscuring intent, brittleness, and duplicating contracts without
  fidelity guarantees.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

**Stubbing** gives a function hardcoded behavior or return values in a test,
typically via a mocking framework's `when(...).thenReturn(...)`.

**Risks when overused**:

- **Unclear tests** — stubbing code obscures intent; a red flag is needing to
  trace the SUT to understand why a stub exists.
- **Brittle tests** — stubs leak [implementation details](observable-behavior-vs-implementation-details.md);
  tests break when internals change though user-facing behavior is unchanged.
- **Less effective tests** — nothing guarantees stubbed behavior matches the
  real contract (e.g. stubbing `add(1,2)` to return 3 duplicates logic with
  no fidelity check). Stubs cannot model internal state (save-then-retrieve
  flows).

**When stubbing is appropriate**: force the SUT into a hard-to-reach state
or error condition via a return value that real code or a [fake](fake-objects.md)
can't easily produce. Each stub should relate directly to assertions; many
stubs signal overuse or an overly complex SUT needing refactor.

Even then, [real implementations or fakes](prefer-real-implementations-in-tests.md)
remain preferred when feasible.

In Khorikov's taxonomy, a stub configured with `.Setup().Returns()` but never
`.Verify()` is still a stub even if created from a mocking-library `Mock<T>`.
Never `.Verify()` stub interactions — that is [overspecification](mocks-vs-stubs-taxonomy.md).

See [mocks versus stubs taxonomy](mocks-vs-stubs-taxonomy.md).
