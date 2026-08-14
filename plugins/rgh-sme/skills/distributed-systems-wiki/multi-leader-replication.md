---
type: concept
title: Multi-Leader Replication
description: >
  Replication design where several nodes accept writes independently and
  replicate asynchronously to each other, trading write conflicts for local
  write latency and partition tolerance.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Multi-Leader Replication

An extension of [single-leader replication](single-leader-replication.md) where
more than one node accepts writes; each leader applies writes locally and
forwards them asynchronously to the other leaders (each leader is
simultaneously a follower of the others).

## Where it makes sense

- **Multi-datacenter deployment:** one leader per datacenter. Writes are
  handled in the local datacenter (low latency, hidden inter-DC link), and each
  datacenter keeps operating through the outage of another or of the inter-DC
  link. Contrast single-leader, where every write crosses the WAN to the
  leader's datacenter.
- **Clients with offline operation:** every device is a "datacenter" with a
  local leader (calendar apps, CouchDB) syncing when connectivity returns —
  multi-leader replication with extreme lag.
- **Collaborative editing:** concurrent editors each apply changes to their
  local replica without locking (Etherpad, Google Docs).

## The cost: write conflicts

The same data can be concurrently modified through two different leaders, and
the conflict is only detected **asynchronously, after both writes have already
succeeded** — too late to ask either user to resolve it. This forces a
[conflict-handling strategy](write-conflict-resolution.md): avoid conflicts by
routing each record's writes to one home leader, or resolve them convergently
after the fact.

## Topologies

Replication flows form a topology: circular, star/tree, or all-to-all. In
circular and star topologies, each write is tagged with the node IDs it has
passed through to prevent infinite loops, and a single node failure can sever
the replication path. All-to-all is more fault-tolerant but network paths can
overtake each other — an update arriving at a replica before the insert it
depends on. Ordering writes correctly requires
[version vectors](version-vectors.md); simple timestamps are not sufficient
(see [unreliable clocks](unreliable-clocks.md)).
