---
type: concept
title: Version Vectors
description: >
  Per-replica version counters attached to values, letting a system decide
  whether two versions are ordered (overwrite) or concurrent (keep siblings).
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 18, Version Vector"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.4"
---

# Version Vectors

When multiple replicas accept writes for the same key
([multi-leader](multi-leader-replication.md) or
[leaderless](leaderless-replication.md)), a single version counter cannot
capture [happens-before](happens-before-and-concurrency.md) — writes on
different replicas increment independently. A **version vector** keeps one
version number *per replica* per key, e.g. `[replica_1: 5, replica_2: 3]`.

Comparison rule: version X happened before Y if every counter in X is ≤ the
corresponding counter in Y (Y knew everything X knew) — then Y may overwrite
X. If each has some counter greater than the other's, the versions are
**concurrent** and both must be kept as siblings for
[conflict resolution](write-conflict-resolution.md).

Operationally, the vector travels with the data: the database returns it to
clients on read as a *causal context*, and clients send it back on write, so
the database can tell an informed overwrite from a concurrent write. (Riak
encodes this as an opaque "causal context" string; the closely related term
*vector clock* is often used interchangeably.)

Version vectors are also what [multi-leader
topologies](multi-leader-replication.md) need to order writes correctly when
replication messages overtake each other on different network paths.

Contrast with [versioned value](versioned-value.md): that pattern uses a
single monotonically increasing counter per key in a leader-based system,
where one leader totally orders every write, so there's no concurrency to
detect — the counter is for addressing history and gating staleness, not for
resolving conflicts.

(Terminology note: a *vector clock* tracks every event a server has seen; a
*version vector* tracks concurrent updates to one specific key across
replicas and is therefore stored per key, not per server — related
mechanics, different scope.)

## Who increments, and how siblings accumulate

In a [leaderless](leaderless-replication.md) key-value store, the
client/coordinator picks one replica as the effective "primary" for a given
write; only that node increments its own slot in the vector, and the
resulting value is copied verbatim (same vector) to the other replicas —
they never bump it themselves. This is exactly how genuinely concurrent
values arise even from a single logical write path: if client A can't reach
the usual primary and falls through to a different replica, while client B's
write lands on the original one, the two replicas now hold values whose
vectors compare as concurrent, with no malicious or buggy behavior involved
anywhere.

On write, a store rejects an incoming value outright if some value it
already holds *dominates* it (an old, already-superseded write arriving
late), and otherwise merges: any existing value the new one dominates is
dropped, but anything concurrent with the new value is kept alongside it —
this is precisely how "sibling" values for a key accumulate. Reading a key
therefore returns a set, not a single value; a client-supplied
`ConflictResolver` (Riak's approach) picks a winner, or the store falls back
to [last-write-wins](last-write-wins.md) on a plain timestamp instead of
keeping siblings at all — simpler for clients, but only as safe as the
cluster's clock synchronization, since a genuinely later write can be
silently discarded by an earlier one that happened to get a higher
timestamp. [Read repair](read-repair-and-anti-entropy.md) piggybacks on this
same read path: while resolving a read across replicas, whichever replicas
are found missing the resolved-latest version get a `put` of it as a side
effect of serving the read, rather than needing a separate background
process.

## Keying by client instead of by node

Keying the vector by node id means a *second* concurrent write to the
*same* node can be rejected outright if it's based on a now-stale version —
a real limitation. The alternative is keying by client id instead: each
client increments its own slot, so two different clients' writes never
reject each other, only ever produce siblings to reconcile later. The cost
is **sibling explosion** — the vector (and the accumulated sibling count)
grows with the number of distinct clients that have ever written the key,
not with the number of nodes, which can balloon without bound over a key's
lifetime. Riak's evolution traces exactly this trade-off: client-id-based
vectors, then node-based vectors to fix sibling growth, then a further
refinement called the *dotted version vector* to address remaining edge
cases in the node-based scheme.

## Bounding growth by truncation

Even a node-keyed vector can grow unboundedly in one specific circumstance:
Dynamo normally has one of a key's top-N preference-list nodes coordinate
every write to it, so the vector's entry count stays bounded by N — but
under partitions or multiple simultaneous failures, coordination can fall
through to nodes outside the top N, and each such node adds its own new
entry. Dynamo bounds this with **clock truncation**: it stores a timestamp
alongside each (node, counter) pair recording when that node last updated
the item, and once the pair count crosses a threshold (the original paper
cites 10), it drops the **oldest** pair. The trade-off is explicit: dropping
history can degrade the accuracy of later ancestor/concurrent
determinations, occasionally causing an already-superseded value to be
treated as concurrent (an unnecessary sibling) rather than correctly
discarded — a cost paid only when clock growth is already pathological. In
production, Dynamo's authors report divergent (sibling) versions of a value
are themselves rare — over a 24-hour sample of a shopping-cart-style
service, 99.94% of reads saw exactly one version — and the versions that do
appear are driven mainly by many concurrent writers (often automated
clients), not by node or datacenter failures.
