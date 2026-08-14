---
type: concept
title: Snapshot Isolation and MVCC
description: >
  Each transaction reads from a consistent snapshot of the database at its
  start time, implemented by keeping multiple versions of every object
  (MVCC); readers and writers never block each other.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# Snapshot Isolation and MVCC

[Read committed](read-committed.md) still allows **read skew**
(nonrepeatable reads): a multi-query transaction sees different parts of the
database as of different moments — a balance transfer observed halfway makes
money vanish. Tolerable for a page reload; fatal for backups (parts of the
dump at different times, permanently inconsistent when restored) and
long-running analytic or integrity-check queries.

**Snapshot isolation** fixes this: every transaction reads from a
*consistent snapshot* — the database as it was when the transaction began.
Marketed as "repeatable read" (PostgreSQL, MySQL) or even "serializable"
(Oracle); the naming is chaotic, check semantics not names.

## MVCC implementation

The principle: *readers never block writers, writers never block readers.*

- Every transaction gets a monotonically increasing transaction id (txid).
- Rows carry `created_by` and `deleted_by` txid metadata; an update soft
  deletes the old version and inserts a new one — multiple committed
  versions coexist (multi-version concurrency control).
- Visibility rule: a transaction sees a version if its creator committed
  before the transaction started, and it wasn't deleted (or its deleter
  hadn't committed) by then. In-progress, aborted, and later transactions'
  writes are invisible.

(Append-only B-trees — CouchDB, LMDB — get the same effect with a new tree
root per transaction, old pages immutable.)

## Position in the landscape

The snapshot is a [causally consistent](causal-ordering.md) view — it never
shows an effect without its cause. But reading from a (slightly old)
snapshot is precisely why snapshot isolation is not
[linearizable](linearizability.md), and it still admits
[lost updates](lost-updates.md) (in some engines) and
[write skew](write-skew-and-phantoms.md) — decisions made on the snapshot
can be invalidated by concurrent commits. Closing that gap is
[serializability](serializability.md)'s job, and
[SSI](serializability.md) builds it directly on top of snapshot isolation.
