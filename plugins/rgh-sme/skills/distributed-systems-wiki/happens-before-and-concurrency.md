---
type: concept
title: Happens-Before and Concurrency
description: >
  Two operations are concurrent when neither knew about the other; causality
  (happened-before), not wall-clock time, is what defines conflicts and
  ordering in distributed systems.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    resource: "Time, Clocks, and the Ordering of Events in a Distributed System (Lamport), \"Introduction\"; \"The Partial Ordering\""
---

# Happens-Before and Concurrency

Operation A **happened before** operation B if B knew about A — B read the
value A wrote, depends on it, or otherwise builds on it. If neither A nor B
happened before the other, they are **concurrent**: each was executed unaware
of the other.

This relation originates in Lamport's formal treatment of distributed
systems: → is defined as the *smallest* relation satisfying (1) same-process
events are ordered by their local sequence, (2) a message's send always
happens before its receipt, and (3) transitivity across chained
dependencies — which makes it an irreflexive **partial order**, not a total
one. The core motivating claim of that treatment carries over directly to
the operation-centric framing above: in a system where processes only
observe each other through messages, "it is sometimes impossible to say
that one of two events occurred first" — not a measurement limitation to be
engineered around, but the actual shape of the problem.

Two points matter for acting on this definition:

- **Wall-clock time is irrelevant.** Physically, A may complete long before B,
  but if the network delayed A's propagation, B was still executed in
  ignorance of A — they conflict just the same. This is why [physical
  timestamps](unreliable-clocks.md) cannot define "later", and why
  [last-write-wins](last-write-wins.md) loses data.
- **Concurrency is what makes a conflict.** If A happened before B, B is a
  legitimate successor and may overwrite A. Only concurrent operations need
  [conflict resolution](write-conflict-resolution.md).

## Capturing happens-before on a single replica

A server keeps an incrementing version number per key. Every read returns the
current value(s) with the version number; every write must carry the version
number from the client's preceding read. The server overwrites values at or
below that version (the client provably knew them) but keeps higher-versioned
values as **siblings** — they are concurrent with the incoming write. Deletes
must leave **tombstones** (versioned deletion markers) so a sibling merge
doesn't resurrect removed items.

With multiple replicas accepting writes, a single counter is not enough — the
generalization is the [version vector](version-vectors.md). The
happened-before relation is also the foundation of
[causal ordering](causal-ordering.md) as a system-wide consistency model.
