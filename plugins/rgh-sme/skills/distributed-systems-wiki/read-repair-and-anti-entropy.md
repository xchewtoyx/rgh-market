---
type: concept
title: Read Repair and Anti-Entropy
description: >
  The two mechanisms leaderless systems use to bring stale replicas up to
  date: fixing staleness observed during reads, and background comparison of
  replica contents.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
  - title: "Dynamo: Amazon's Highly Available Key-value Store"
    resource: "Dynamo: Amazon's Highly Available Key-value Store (DeCandia et al.), §4.7, §5"
---

# Read Repair and Anti-Entropy

[Leaderless replication](leaderless-replication.md) has no log stream pushing
missed writes to a recovering or lagging replica, so catching up needs
explicit healing:

- **Read repair.** Several replicas are queried [in
  parallel](quorum-reads-and-writes.md) and version numbers reveal that some
  responses are stale. In Dynamo this is done by the coordinating node, not
  the client: after returning a response, the coordinator's state machine
  waits a short additional period for any outstanding replies and pushes the
  latest version to whichever replicas responded stale — an optimization that
  relieves the anti-entropy protocol of catching up frequently-read data.
  Effective for frequently read data, free-riding on read traffic — but values
  that are rarely read stay stale indefinitely.
- **Anti-entropy.** A background process continuously compares replica
  contents (typically via Merkle-tree hashing to avoid scanning everything)
  and copies missing data across. No ordering guarantee and potentially
  significant delay, but it covers cold data that read repair never touches.

Systems without anti-entropy (e.g. Voldemort by default) trade durability:
data on a replica that dies before ever being read again may never propagate.

## Merkle-tree anti-entropy mechanics

A **Merkle tree** is a hash tree: leaves are hashes of individual keys'
values, and each parent is the hash of its children, up to a single root
hash. Dynamo keeps one such tree **per key range** (the span a virtual node
owns) on each node that hosts it. Two replicas compare a shared key range by
exchanging just the **root hash**: equal roots mean the entire range is in
sync with no data transferred at all; unequal roots trigger exchanging the
next level of child hashes, recursing down only the branches that disagree
until the specific out-of-sync keys are pinpointed. This bounds both the
network transfer and the number of disk reads needed to find a
discrepancy — a node never has to scan or download a whole range just to
check it.

The scheme's cost center is **rebuild after rebalancing**: because trees are
scoped to key ranges, every node join or leave that reassigns ranges forces
the affected trees to be recomputed from scratch, which is expensive at
production scale (see [rebalancing partitions](rebalancing-partitions.md) —
this is exactly the cost that motivated fixing partition boundaries
independently of node membership).

## Background repair traffic competes with foreground traffic

Anti-entropy scans and hinted-handoff transfers are I/O- and
network-intensive background work sharing the same nodes, disks, and links
as ordinary foreground reads and writes — left unregulated, they degrade
live request latency exactly when the cluster can least afford it (right
after a failure or rebalance, precisely when there's the most repair work
queued). Dynamo's answer is admission control specific to this
competition: background tasks consume a shared pool of resource "slices,"
and a feedback loop continuously watching foreground latency and error
percentiles (e.g. 99th-percentile disk read latency over a trailing window)
grows or shrinks that pool to keep background repair from ever pushing
foreground performance past its target. The general shape of this
trade-off — protecting latency-critical traffic from background or bulk
work sharing its infrastructure — is a load-shedding and backpressure
concern in its own right, distinct from the replication mechanics here.
