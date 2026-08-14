---
type: concept
title: Rebuild Fixtures Fresh Per Test, Not Shared
description: >
  A fixture hoisted to suite scope only stays safe if it's genuinely never
  mutated by any test — rebuilding it fresh before every test avoids
  intermittent, order-dependent failures for a rebuild cost that's rarely
  noticeable.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 4"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 3"
---

Anti-pattern: hoisting a shared fixture object to suite (`describe`-block)
scope. The danger is that `const` (or equivalent) only freezes the
*reference*, not the object's contents — if any one test mutates the shared
object, other tests become order-dependent, producing intermittent,
hard-to-debug nondeterministic failures depending on run order.

Preferred pattern: rebuild the fixture fresh in a `beforeEach` hook before
every test. The performance concern this raises — rebuilding a fixture on
every single test — is usually not noticeable in practice; a shared fixture
is only safe once it is genuinely, verifiably immutable. A `beforeEach`
setup also documents intent to the reader: it signals "every test in this
block starts from this same base state," making the standard starting point
easy to learn once instead of re-derived per test.

Standard test phases this fits into: setup, exercise, verify (also known as
arrange-act-assert or given-when-then), plus an often-unstated fourth phase,
teardown — usually handled implicitly by the framework tearing down
`beforeEach` fixtures between tests, though an explicit teardown can matter
when a fixture is intentionally shared because it's genuinely expensive to
rebuild.

## Constructor-based reuse anti-pattern

Initializing shared fixtures in the test class constructor (or framework setup
hooks) shortens tests but has two drawbacks:

1. **Coupling between tests** — modifying one test's arrangement (e.g. inventory
   quantity) can invalidate assumptions in others, causing unrelated failures.
   Distinct from execution isolation (ch. 2): here the concern is independent
   *modifiability*. Avoid shared mutable private fields in test classes.
2. **Diminished readability** — the reader cannot see the full picture from the
   test method alone and must inspect the constructor.

**Better: private factory methods** — e.g. `CreateStoreWithInventory(product,
quantity)`, `CreateCustomer()` called explicitly from each test. Keeps context
in the test body; as long as factories accept parameters (desired inventory,
etc.), tests stay decoupled.

**Exception**: instantiate in a shared base class constructor when nearly every
test in a suite needs the same expensive fixture (commonly a database connection
in integration tests) — e.g. `CustomerTests : IntegrationTests` inherits setup
from `IntegrationTests : IDisposable`, keeping concrete test classes
constructor-less.

xUnit uses constructor/`IDisposable` per test (no `[SetUp]`/`[TearDown]`);
`[Fact]` emphasizes each test as an atomic domain fact — a passing test proves
the fact holds; a failing test means rewrite the story or fix the system.
