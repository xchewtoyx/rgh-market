---
type: concept
title: Leader Election Mechanics
description: >
  How a cluster actually picks a leader — in-process voting for small
  consensus clusters versus delegating to an external linearizable store for
  large ones — and why quorum reads/writes alone can't substitute for it.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 6, Leader and Followers"
---

# Leader Election Mechanics

[Leader failover](leader-failover.md) names electing a new leader as one of
its three steps and treats it as "a consensus problem"; this note is the
mechanics of that step. Two structurally different approaches, chosen by
cluster size:

## Small clusters: voting inside the cluster (Raft, Zab)

For 3–5 node consensus-style clusters, election runs inside the cluster with
no external dependency. On startup every server looks for an existing
leader; if none is found, it starts an election, and no client requests are
served cluster-wide until one completes. Every election bumps the
[generation clock](generation-clock.md). A [heartbeat](heartbeat.md) absence
from the current leader triggers a fresh election.

Only the **most up-to-date** servers may legitimately win, judged by (a) the
highest generation clock, then (b) the highest write-ahead log index. Ties
break by implementation-specific rules (server rank in Zab; whichever
candidate's vote request other servers happen to see first in Raft, aided by
randomized election timeouts to make simultaneous elections unlikely). Once a
server casts a vote for a given generation, it must keep returning that same
vote for that generation forever — this is what stops a second concurrent
election in the same generation from also succeeding. Whoever collects votes
from a [quorum](truth-defined-by-majority.md) (majority) becomes leader and
starts sending heartbeats.

Raft and Zab differ in exactly *when* the generation increments and what
state a server defaults to, but the shape — bump generation, request votes,
require majority, break ties on log recency — is the same one described
generically for [consensus](consensus.md) protocols.

## Large clusters: delegating to an external store (ZooKeeper, etcd)

For clusters of up to thousands of nodes, running an in-cluster vote doesn't
scale, so election is delegated to a [coordination
service](coordination-services.md). This needs three primitives from the
store: an atomic "create this key only if absent" (etcd exposes
compare-and-swap directly; ZooKeeper emulates it via a node-creation
exception), a heartbeat/TTL mechanism that expires the leader's key if it
stops renewing (ZooKeeper uses [lease](distributed-locks.md)-like ephemeral
nodes tied to session liveness instead of an explicit TTL), and a
notification mechanism — every server subscribes to the leader key and is
told when it disappears, re-triggering an election attempt. Whichever server
wins the create-if-absent race becomes leader and must keep refreshing the
key before it expires.

## Why quorum reads/writes alone cannot replace this

A worked counter-example shows why [quorum reads and
writes](quorum-reads-and-writes.md) on their own don't give the guarantee a
leader gives. Three-node cluster, replication factor 3, key `x` starts at 1:
a write sets `x = 2` on node1 only (node2/node3 are unreachable); a first
client reads `x` from node1 + node2 and sees the new value 2 (node1 answers);
node1 then briefly goes down, and a *second*, later client reads `x` from
node2 + node3 and sees the stale value 1. Two consecutive reads showed a
value that then "disappeared" — a value already visible to one client became
invisible to a later one, even though nothing was lost forever (the cluster
still converges once node1 recovers and [read repair](read-repair-and-anti-entropy.md)
runs). Quorum overlap alone guarantees at least one *fresh* replica is in any
read set; it says nothing about whether a value already observed stays
observable through a subsequent failure. Routing every write and every
strongly-consistent read through a single leader is what closes that gap:
the leader's own view of "current" is the one true state, not an
after-the-fact reconciliation of scattered replicas.
