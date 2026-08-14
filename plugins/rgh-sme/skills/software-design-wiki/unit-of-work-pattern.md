---
type: concept
title: Unit of Work Pattern
description: >
  A unit of work tracks objects affected by a business operation and applies
  all database updates together at the end, shortening transaction duration
  and often reducing round trips.
sources:
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 10"
---

A **unit of work** maintains a list of objects affected by a business operation;
when the operation completes, it determines the necessary database updates and
executes them as a single unit.

Compared with a plain [repository and transaction
separation](repository-and-transaction-separation.md) that commits each
repository call inside an overarching transaction, a unit of work **defers**
writes until the end. That minimizes how long the underlying database
transaction stays open (less congestion) and often cuts the number of database
calls.

In practice you rarely implement this yourself: most ORMs provide it (.NET
examples: NHibernate's `ISession`, Entity Framework's `DbContext`). After
adopting Entity Framework in the sample CRM, a custom `CrmContext` inheriting
`DbContext` replaces the hand-rolled `Transaction` class, and
`context.SaveChanges()` replaces `transaction.Commit()`. With the ORM acting as
mapper, separate user/company factory classes can disappear because the context
handles persistence mapping.

## Non-relational stores

Many non-relational databases lack classical multi-document transactions —
atomicity applies only within a single document (roughly one row). Business
operations that touch multiple documents remain prone to inconsistency.

Mitigating design guideline: **do not let one business operation modify more
than one document or aggregate at a time**. Documents are often more flexible
than relational rows and can embed complex side effects in one structure; when
each document corresponds to one aggregate, this parallels the
[aggregate consistency boundary](aggregate-consistency-boundary.md) rule of
one aggregate per operation.
