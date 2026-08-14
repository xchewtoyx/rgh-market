---
type: concept
title: Mocks Versus Stubs Taxonomy
description: >
  Mocks examine outgoing side-effect interactions; stubs supply incoming query
  data without verification — never verify stub calls, and reserve mocks for
  commands at unmanaged boundaries.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
---

Gerard Meszaros names five test-double types (dummy, stub, spy, mock, fake).
Khorikov groups by function into two roles:

- **Mocks** — emulate and *examine* **outgoing** interactions (calls that change
  dependency state — side effects).
- **Stubs** — emulate but do **not** examine **incoming** interactions (calls
  to fetch input data).

Spies are handwritten mocks. Dummies and fakes serve the stub role; dummies are
hard-coded placeholders; fakes are full stand-ins when the real dependency
doesn't exist yet. See [fake objects](fake-objects.md) and [test doubles
overview](test-doubles-overview.md).

**"Mock" is overloaded**: (1) any test double generically, (2) mocking-library
class (`Mock<T>`), (3) the interaction-examining double. A `Mock<T>` configured
with `.Setup().Returns()` but never `.Verify()` is a **stub**; with `.Verify()`
it's a **mock** — same library type, different role.

**Never assert interactions with stubs** — verifying a stub call is
**overspecification** (checking means, not end results). Easy to spot; always
wrong.

One double can be both: stub `HasEnoughInventory()`, verify `RemoveInventory()`
— convention: call it a mock when both roles apply (mock is the stronger fact).

**Command-query separation (CQS)**: commands (side effects, often void) → mocks;
queries (return values, no side effects) → stubs. `stack.Pop()` is a known
exception (mutates and returns).

See [state testing over interaction testing](state-testing-over-interaction-testing.md),
[stubbing in tests](stubbing-in-tests.md), and [mock objects](mock-objects.md).
