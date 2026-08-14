---
type: concept
title: Consumer Group Rebalancing
description: >
  How a log-based broker divides a topic's partitions among a consumer
  group's members without a lock service — deterministic assignment computed
  independently by each consumer, re-run whenever membership changes.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3.2"
---

# Consumer Group Rebalancing

A [log-based broker's](log-based-messaging.md) partition is consumed by only
one consumer within a group at a time — the design deliberately avoids
letting multiple consumers share a partition, because that would need locking
and shared state-tracking on every message instead of only when membership
changes. The trade-off this buys: coordination happens rarely (only on
**rebalance**, when a consumer or broker joins or leaves), not on every
message. For load to actually balance, a topic needs many more partitions
than any group has consumers — deliberately over-partitioning so a rebalance
has room to redistribute work in more than a few chunks.

## Decentralized assignment via a coordination service

Rather than run a master node to hand out assignments, each consumer computes
its own assignment independently, in a way guaranteed to agree with every
other consumer's computation. This works by pushing the shared state each
consumer needs into a [coordination service](coordination-services.md)
(historically ZooKeeper) as several registries:

- **Broker registry** and **consumer registry** — [ephemeral](state-watch.md)
  entries written on startup, removed automatically on crash or disconnect,
  so membership tracking rides on the coordination service's own failure
  detection rather than a separate heartbeat protocol.
- **Ownership registry** — one entry per partition, holding the id of the
  consumer currently assigned to it.
- **Offset registry** — one *persistent* entry per partition holding the last
  offset that group has consumed, surviving across rebalances and restarts.

Each consumer [watches](state-watch.md) the broker and consumer registries.
On startup, or whenever a watch fires because the broker or consumer set
changed, every consumer in the group independently re-derives the same
assignment: read the current broker and consumer registries, release any
partitions it currently owns, sort the group's live partitions and its live
consumers into two canonical lists, locate its own position in the sorted
consumer list, and claim the corresponding contiguous slice of the sorted
partition list. Because every consumer sorts the same two sets the same way,
they all compute an identical, non-overlapping assignment without exchanging
a single message with each other — the coordination service is the only
shared state, and the algorithm, not a lock, is what prevents conflicting
assignments in the steady state.

## Handling the transition race

Watch notifications don't arrive at every consumer at the same instant, so
during a rebalance one consumer can briefly try to claim a partition the
ownership registry still shows as belonging to another consumer that hasn't
released it yet. Rather than resolve this with a lock, the losing consumer
just backs off: release every partition it currently holds, wait briefly, and
retry the whole rebalance computation from scratch. In practice this
converges after only a few retries — a self-healing race rather than
something that needs explicit arbitration, because a rebalance is a rare
event relative to normal message consumption.

A group with no prior offset history (a brand-new consumer group) starts each
partition at either the earliest or latest available offset, per a
broker-side configuration choice, rather than at any recorded position.
