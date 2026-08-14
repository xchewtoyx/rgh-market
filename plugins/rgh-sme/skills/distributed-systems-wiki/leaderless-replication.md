---
type: concept
title: Leaderless Replication
description: >
  Dynamo-style replication with no leader: clients send reads and writes to
  several replicas in parallel and rely on quorum overlap, read repair, and
  anti-entropy for consistency.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.3, §4.5, §5"
---

# Leaderless Replication

Pioneered by Amazon's Dynamo; implemented in Riak, Cassandra, and Voldemort.
There is no leader and no failover: any replica accepts writes directly, and
the client (or a stateless coordinator node) sends each read and write to
several replicas in parallel.

- Writes are sent to all n replicas holding the key and considered successful
  after w acknowledgements; reads query the replicas in parallel and take r
  responses — see [quorum reads and writes](quorum-reads-and-writes.md) for
  why w + r > n gives overlap.
- Stale replicas are healed by [read repair and
  anti-entropy](read-repair-and-anti-entropy.md), since there is no
  replication log pushing them forward.
- Version numbers attached to values let the reader tell which responses are
  stale, and [version vectors](version-vectors.md) distinguish newer values
  from [concurrent](happens-before-and-concurrency.md) ones that need
  [conflict resolution](write-conflict-resolution.md).

The appeal is availability and tolerance of node failures without
[failover](leader-failover.md) machinery: a node being down just means fewer
acknowledgements, and [sloppy quorums with hinted
handoff](sloppy-quorum-and-hinted-handoff.md) can keep accepting writes even
when the "home" replicas for a key are unreachable. The price is weaker
consistency: even strict quorums do not give
[linearizability](linearizability.md), and applications must cope with stale
reads and concurrent-write siblings.

## Preference lists and coordinators

The n replicas "holding the key" are determined by walking the
[partitioning](hash-partitioning.md) scheme forward from the key's hash
position — Dynamo's **coordinator node** for a key is joined by its n-1
clockwise successors on the ring. Because that list only has to skip past
*unhealthy* nodes to stay reachable, it is built with a few extra positions
beyond n from the start (the **preference list**) — and where the ring uses
[virtual nodes](fixed-partitions.md), building it also has to skip
positions that map back to a physical node already in the list, so the
preference list ends up with n *distinct physical* nodes rather than
n positions.

Any node can act as read coordinator; a write coordinator must be one of
the preference list's own top-n nodes, because it is the one responsible
for minting the new version's [version vector](version-vectors.md) entry.
A request that lands on some other node (e.g. via a load balancer) is
simply forwarded to the right one. Choosing *which* of the top-n nodes
coordinates a given write is itself a tuning knob — see [request
routing](request-routing.md) for the client-driven vs. server-driven
routing trade-off this creates.

Always having the *same* node (e.g. the first in the preference list)
coordinate every write to a key looks simplest, but concentrates load
unevenly once request rates vary key by key — so any of the top-n nodes is
allowed to coordinate. Since a write is usually preceded by a read, Dynamo
picks the write's coordinator to be whichever node answered that preceding
read *fastest* (carried in the read's returned context) — this both evens
out load across the preference list and raises the odds (not a guarantee)
of [read-your-writes](read-your-writes-consistency.md): the node likely to
coordinate a client's next write is the one that just proved it has the
freshest data for that client.
