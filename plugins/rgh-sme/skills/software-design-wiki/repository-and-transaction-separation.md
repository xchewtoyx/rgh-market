---
type: concept
title: Repository and Transaction Separation
description: >
  Split data access from commit/rollback decisions by giving repositories
  short-lived enlistment in a long-lived transaction whose Commit and Dispose
  guarantee atomic business operations.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 10"
---

A class that opens a new database connection on every method call creates an
**implicit independent transaction per call**. A controller that invokes four
such methods for one business operation runs four separate transactions — fine
for read-only work, but dangerous when the operation mutates data: one step can
commit while a later step fails, leaving related rows inconsistent (e.g. company
employee count updated while the corresponding user row never saved).

**Atomic updates** mean all-or-nothing: every update in the set completes fully
or has no effect at all.

## Splitting what to update from whether to keep it

The controller cannot decide both *what* to persist and *whether* to roll back
at the same moment — it only knows the operation succeeded once every step has
run. Separate two concerns a monolithic database wrapper conflates:

- **Repositories** — access and modify specific entity types
  (`UserRepository`, `CompanyRepository`). Short-lived: dispose after each
  database call completes.
- **Transaction** — wraps the database's native transaction mechanism (e.g.
  .NET `TransactionScope`). Long-lived: spans the whole business operation and
  is disposed at the very end.

Repositories are constructed against the **current transaction** (injected),
enlisting their modifications so the transaction can roll them back later.
The transaction exposes:

- `Commit()` — mark success; call only when the entire business operation
  succeeded, at the very end of the controller method. Any early return
  (validation failure or unhandled exception) skips it.
- `Dispose()` — end unconditionally. If `Commit()` ran, persist; otherwise roll
  back.

`Commit()` requires orchestration judgment and stays in the controller (or
[application service](application-service-orchestration-only.md)).
`Dispose()` needs no business decision and can live in infrastructure code
that also constructs the controller.

This `Commit()` + `Dispose()` pairing alters the database only on the happy
path. See [unit of work](unit-of-work-pattern.md) for the common upgrade that
defers writes until the end of the operation.

See [ports and adapters architecture](ports-and-adapters-architecture.md) for
where repository interfaces sit in a layered module, and [aggregate consistency
boundary](aggregate-consistency-boundary.md) for why a single business
operation often maps to one aggregate's invariants.
