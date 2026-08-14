---
type: concept
title: Database Integration Test Patterns
description: >
  Run integration tests sequentially against the same DBMS as production, clean
  data at the start of each test, and reuse arrange helpers without coupling tests.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 10"
---

Shared database instances require **sequential execution** and **cleanup between
runs**. Tests must establish required state themselves — never depend on
pre-existing database state.

## Execution and cleanup

**Parallel integration tests** need unique data per test and tricky cleanup —
significant effort. Recommendation: run integration tests **sequentially** (separate
test collection with parallelization disabled). Container-per-test parallelization
turns integration tests into unit tests but adds image maintenance, batching, and
disposal burden — not recommended unless execution time is an absolute constraint.
A single shared instance *in* Docker is fine.

**Cleanup options** (best to worst for typical use):

1. Restore backup before each test — slow.
2. Clean up at end — fast but skipped cleanup on crash/debug leaves corrupt state.
3. Uncommitted transaction rollback — avoids skipped cleanup but introduces
   production/test mismatch (overarching transaction artifact).
4. **Clean up at beginning** — recommended: fast, consistent, not prone to skipped
   cleanup. Implement cleanup in the **arrange** section; no separate teardown.

Write deletion SQL by hand (respect foreign-key order) rather than disabling
constraints — simpler, more control. Put `ClearDatabase()` in a base class
constructor. Remove regular data only; **reference data** stays under migration
control.

**Avoid in-memory databases** (e.g. SQLite substituting for production DBMS) —
not functionality-consistent with production; false positives/negatives waste
effort. Use the **same DBMS vendor** in tests as production (version/edition may
differ).

## Shortening tests without coupling

Extract technical, non-business bits into private helpers:

- **Arrange — Object Mother**: private factory methods with default arguments
  (`CreateUser(email, type, isEmailConfirmed)`) so call sites specify only
  scenario-relevant parameters. Prefer over Test Data Builder fluent interfaces
  unless readability gain justifies boilerplate. Start factories in the test class;
  move to helper class on duplication; keep base class for universal setup only
  (e.g. `ClearDatabase()`).
- **Act — decorator methods**: wrap controller calls with database context
  creation/disposal.
- **Assert — query helpers + fluent extensions**: `QueryUser`/`QueryCompany` with
  fluent assertions.

Trade-off: extracted helpers may open more database transactions (five vs three)
— slower but substantially more maintainable; acceptable on a developer-machine
database.

## Transaction and unit-of-work boundaries in tests

**Do not reuse a database transaction or [unit of
work](unit-of-work-pattern.md) across arrange, act, and assert.** In
production, each business operation gets its own exclusive context — created
immediately before the controller call and disposed immediately after. An
integration test that shares one `DbContext` (or equivalent) across all three
sections creates an environment production never sees.

The assert section needs its **own** instance even when it only reads user and
company rows independently of arrange, because many ORMs **cache previously
requested entities** inside a context. Assertions against a shared context can
pass against cached in-memory state instead of freshly persisted database rows,
hiding real persistence bugs.

**Guideline: use at least three transactions or units of work per integration
test** — one for arrange, one for act, one for assert. Decorator helpers that
wrap controller calls with context creation/disposal naturally satisfy the act
boundary; assert helpers should open a fresh context for re-queries.

The same production/test mismatch applies to wrapping an entire test in one
uncommitted transaction rolled back at the end (listed above as a cleanup
anti-pattern): production code never runs inside that overarching transaction
artifact.

See [integration test state verification](integration-test-state-verification.md)
for how assert sections should re-read state through production paths.

## What to test

**Writes** deserve thorough testing — data corruption risk, possibly affecting
external systems.

**Reads** have a higher threshold — bugs usually less damaging. Test only complex
or important reads. Reads need no domain model (no invariants to protect across
changes); plain SQL often outperforms ORM for reads. Few abstraction layers mean
unit tests aren't useful for reads — use integration tests against a real database
if you test them at all.

**Do not test repositories independently** — they sit in the controllers quadrant
(low complexity, high maintenance via out-of-process dependency). Dedicated
repository tests overlap integration coverage with inferior regression protection.
Extract small mapping complexity into pure factories/algorithms and unit-test
those; ORM mappings require database hits. Same for `EventDispatcher` — cover in
overarching integration tests only.

Well-crafted database integration tests against [managed
dependencies](integration-testing-fundamentals.md) give strong confidence for
database refactorings, ORM switches, and vendor changes.

See [integration test state verification](integration-test-state-verification.md),
[fresh fixtures over shared fixtures](fresh-fixtures-over-shared-fixtures.md), and
[integration testing fundamentals](integration-testing-fundamentals.md).
