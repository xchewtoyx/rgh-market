---
type: concept
title: Classical Versus London Unit Testing Schools
description: >
  The schools disagree on what "isolation" means — isolating tests from each
  other versus isolating the system under test from collaborators — and that
  single disagreement drives mock usage, unit granularity, and TDD style.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 2"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 5"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 13"
---

A unit test verifies a small piece of code quickly in an isolated manner.
Speed is largely uncontroversial; **isolation** is disputed and splits the
**classical** (Detroit) and **London** (mockist) schools.

| | Isolation of… | A unit is… | Test doubles for… |
| --- | --- | --- | --- |
| London school | The SUT from collaborators | A class | All but immutable dependencies |
| Classical school | Unit tests from each other | A class or set of classes | Shared dependencies only |

**London school**: replace all collaborators with [test doubles](test-doubles-overview.md).
Claimed benefits: failure localizes to the SUT; breaks up dense object graphs;
enables one test class per production class. Risk: over-specification —
coupling tests to [implementation details](observable-behavior-vs-implementation-details.md).
Drives **outside-in TDD**: higher-level tests set expectations; mocks specify
collaborator interactions while implementations are deferred.

**Classical school**: isolate tests from each other, not code from
collaborators — tests may exercise several classes together if none touches
shared state. A unit need not be a single class. Drives **inside-out TDD**:
start from the domain model, add layers until usable. Google's default aligns
here: [prefer real implementations in tests](prefer-real-implementations-in-tests.md)
when fast and deterministic.

**Dependency taxonomy** (classical):

- **Shared dependency** — reused across tests; enables interference (DB,
  static mutable state).
- **Private dependency** — fresh instance per test.
- **Out-of-process dependency** — proxy to data not yet in memory; usually
  shared but not always (read-only DB, per-run Docker DB).
- **Volatile dependency** — needs special runtime setup or is nondeterministic
  (RNG, clock).
- **Collaborator** — shared *or* mutable; values/immutable objects are
  dependencies but not collaborators.

**Rebuttals to London-school claims**:

1. Tests should verify **units of behavior**, not units of code — class count
   is irrelevant.
2. A large interconnected graph is a design problem; mocking hides it rather
   than fixing it — difficulty unit-testing is a [good negative indicator](goal-of-unit-testing.md).
3. Cascade failures on a broken class are informative and usually traceable
   when tests run after every change.

**London school and intra-system mocking**: the London school does not
differentiate [intra-system from inter-system
communication](intra-system-vs-inter-system-communication.md), so it mocks
class-to-class collaborations as readily as application-to-external-system
ones — indiscriminate mocking that routinely couples tests to implementation
details. The classical school is better (it substitutes only shared
dependencies, which in practice means out-of-process ones) but still
over-mocks somewhat when it treats every out-of-process dependency as
mock-worthy — an application-owned database is an implementation detail, not
observable behavior.

See [mocks versus stubs taxonomy](mocks-vs-stubs-taxonomy.md) and
[state testing over interaction testing](state-testing-over-interaction-testing.md).
