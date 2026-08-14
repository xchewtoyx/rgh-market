---
type: concept
title: Integration Testing Fundamentals
description: >
  An integration test is any test that fails at least one unit-test criterion;
  use real managed dependencies and mock unmanaged ones, reserving integration
  tests for happy paths unit tests cannot cover.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 8"
---

Per the classical definition, a **unit test** verifies a single unit of
behavior quickly, in isolation from other tests. An **integration test** is
any test that fails at least one of those three criteria — typically by
touching a [shared or out-of-process dependency](classical-vs-london-unit-testing-schools.md),
running slowly, or verifying multiple units at once.

In practice integration tests verify how the system works with out-of-process
dependencies — covering the **controllers** quadrant in [four types of code for
testing priority](four-types-of-code-for-testing-priority.md). Unit tests cover
domain model and algorithms. If all out-of-process dependencies are mocked, a
controller test can still count as a unit test; most applications have at least
one dependency (typically the database) that cannot be mocked without losing
value.

Integration tests are slower and costlier to maintain (keeping external systems
operational, more collaborators inflating test size) but exercise more code for
better regression protection and sit further from production code for better
refactoring resistance. Follow the [test pyramid](test-pyramid.md): many unit
tests for edge cases, fewer integration tests for happy paths.

## Fail fast versus integration coverage

For integration tests, pick the **longest happy path** — the scenario touching
the most out-of-process dependencies. Skip edge cases whose incorrect execution
would **fail fast** — immediately crash the application with no data corruption
(e.g. a missing controller-level precondition check that `Precondition.Requires`
would catch on first run). Unit-test the domain precondition; integration-test
the happy path. "No tests are better than bad tests."

The **fail fast** principle — stop the current operation as soon as an
unexpected error occurs — is a viable alternative to integration testing for
some edge cases. Benefits: shorter feedback loop (bugs found in dev are cheaper
than in production) and protection of persistence state (fail fast before
corrupted state spreads). Implemented via exceptions, preconditions, and
startup validation of configuration.

## Managed versus unmanaged dependencies

Out-of-process dependencies split into:

- **Managed** — fully controlled by your application; interactions not visible
  externally (typical: application-only database).
- **Unmanaged** — not fully controlled; interactions observable externally
  (SMTP server, message bus).

Per [intra-system vs inter-system communication](intra-system-vs-inter-system-communication.md):
managed-dependency communications are implementation details; unmanaged ones
are observable behavior.

**Guideline: use real instances of managed dependencies in integration tests;
replace unmanaged dependencies with mocks.** Real managed dependencies verify
final system state from the external client's viewpoint and validate database
refactorings (column renames, vendor migrations). Mocks pin communication
patterns with unmanaged dependencies against refactoring.

**Dual-attribute dependencies**: a database another application also reads from
is both managed and unmanaged — a poor integration mechanism. Treat externally
visible tables as unmanaged (mock and assert interactions); treat the rest as
managed (assert final state). Never gratuitously change the communication
pattern with externally visible tables.

**When you cannot use a real database** (IT policy, prohibitive setup cost): do
not mock the database as a workaround — that compromises integration-test value.
If the database is the only out-of-process dependency, such a mocked test adds
nothing beyond unit tests except confirming which repository methods the
controller calls. Skip integration testing and focus on unit testing the domain
model instead.

See [integration versus end-to-end tests](integration-vs-end-to-end-tests.md),
[database integration test patterns](database-integration-test-patterns.md), and
[mocks for integration tests only](mocks-for-integration-tests-only.md).
