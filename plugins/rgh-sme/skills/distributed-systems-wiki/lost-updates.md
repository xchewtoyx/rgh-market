---
type: concept
title: Lost Updates
description: >
  The read-modify-write race where a later write overwrites a concurrent
  update without incorporating it — and the spectrum of fixes from atomic
  operations to compare-and-set.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 7"
---

# Lost Updates

Two clients run a **read–modify–write** cycle on the same object
concurrently — incrementing a counter, editing a JSON document, saving a wiki
page. Each reads the same starting value; the second write overwrites the
first, which is silently lost (a "clobber"). One of the most common
concurrency bugs.

Fixes, in rough order of preference:

1. **Atomic write operations** in the database:
   `UPDATE counters SET value = value + 1 WHERE key = 'foo'` — the
   read-modify-write happens under an internal exclusive lock. Use these
   whenever the modification is expressible; beware ORMs that silently turn
   them back into read-modify-write in application code.
2. **Explicit locking:** `SELECT ... FOR UPDATE` locks the rows the decision
   depends on. Correct but easy to forget a needed lock.
3. **Automatic detection:** [snapshot isolation](snapshot-isolation.md)
   engines can detect a concurrent update to the same row and abort the
   loser for [retry](transaction-aborts-and-retries.md) (PostgreSQL
   repeatable read does; MySQL InnoDB's does **not** — engine-specific).
4. **Compare-and-set:** `UPDATE ... WHERE id = 123 AND content = <old>` —
   only safe if the comparison reads current state, not an old snapshot.

In replicated multi-writer systems
([multi-leader](multi-leader-replication.md)/
[leaderless](leaderless-replication.md)), locks and compare-and-set don't
apply — there is no single current copy. There the answer is commutative
atomic operations (CRDT counters/sets in Riak) or keeping concurrent
versions as siblings for [merge](write-conflict-resolution.md);
[last-write-wins](last-write-wins.md) institutionalizes the lost update
instead of preventing it.

A subtler cousin where the two writes touch *different* objects is
[write skew](write-skew-and-phantoms.md).
