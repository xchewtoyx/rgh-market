---
type: concept
title: Read Committed Isolation
description: >
  The baseline isolation level: no dirty reads (only committed data is seen)
  and no dirty writes (only committed data is overwritten).
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# Read Committed Isolation

The most basic transaction isolation level, and the default in PostgreSQL,
Oracle, and SQL Server. Two guarantees:

- **No dirty reads:** you only see data that has been committed — never a
  half-applied state of a running transaction, and never data that later gets
  rolled back.
- **No dirty writes:** you only overwrite committed data — two concurrent
  transactions can't interleave writes to the same objects (which would mix
  their updates, e.g. a car sale where the listing goes to one buyer and the
  invoice to another).

Implementation: dirty writes via **row-level exclusive locks** held until
commit/abort; dirty reads *without* read locks (readers would otherwise stall
behind long writers) — the database keeps both the old committed value and
the in-flight new value, serving the old one to readers until commit.

What it does **not** prevent: [read skew](snapshot-isolation.md) (seeing
different points in time within one transaction),
[lost updates](lost-updates.md), and
[write skew and phantoms](write-skew-and-phantoms.md). Applications on read
committed carry the burden of avoiding all three.
