---
type: concept
title: High Water Mark
description: >
  The log index confirmed replicated to a quorum of followers, below which
  entries are safe to apply and serve — nothing beyond it may ever be exposed
  to a client.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 12, High-Water Mark"
---

# High Water Mark

A [write-ahead log](write-ahead-log.md) recovers one crashed server's own
state, but a [replicated log](replicated-log.md) can still leave followers
holding divergent contents — some missing entries, some further ahead than
others — after a leader dies partway through replicating. Each server needs
to know exactly which prefix of *its own* log is actually durable across the
cluster before it can safely expose that data to clients.

The **high water mark** (Raft calls it `commitIndex`) is the index of the
last log entry confirmed replicated to a [quorum](truth-defined-by-majority.md)
of servers. The leader tracks every follower's acknowledged index and
computes the mark as the *median* of all tracked indexes — equivalently, the
highest index acknowledged by a majority — then propagates it to followers
piggybacked on ordinary replication traffic or [heartbeats](heartbeat.md).
The governing rule is absolute: **no server may serve a client anything
beyond its own high water mark**, because an entry past it has no
cross-cluster durability guarantee — if the leader fails right now, that
entry might not exist anywhere else, and a differently-elected leader could
overwrite it.

## The startup hazard this creates

If the old leader died before ever propagating the high water mark to any
follower, the cluster must bring every server's log fully up to date before
anyone can answer clients again — otherwise a client could be served from a
server holding entries that get silently discarded once real replication
resumes. Two documented resolutions: Raft appends a **no-op entry**
immediately after a successful election and withholds client service until a
quorum confirms it (this doubles as the "a new leader must commit at least
one entry from its own [generation](generation-clock.md) before it can treat
anything from a prior generation as committed" safety rule — see [replicated
log](replicated-log.md)); ZAB instead has the new leader explicitly push all
of its own entries to every follower before it starts serving clients at
all.

## Log truncation on rejoin

A server rejoining after a crash or a network partition may hold entries
that never reached a quorum, or entries that conflict with what the cluster
actually settled on. On rejoin it contacts the current leader, finds the
point where its log diverges (comparing index and
[generation](generation-clock.md), not just index), truncates its own log
back to that matching point, then pulls everything after it from the leader.
This is the same conflict-repair mechanism [replicated log](replicated-log.md)
uses during ordinary catch-up, just triggered by a full rejoin instead of a
single lagging follower.

Every consensus algorithm relies on some form of this concept to know when a
proposed mutation is safe to apply; Kafka's replication protocol maintains
its own high water mark so consumers can only see entries confirmed across
replicas, and Apache BookKeeper's analogous "last add confirmed" marks the
entry replicated to a quorum of bookies.
