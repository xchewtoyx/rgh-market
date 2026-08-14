---
type: concept
title: Read Path and Write Path
description: >
  Indexes, caches, and materialized views shift work between eager
  write-time computation and lazy read-time computation — a boundary that
  can extend all the way to end-user devices.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 12"
---

# Read Path and Write Path

Every piece of derived state sits on a boundary between two kinds of work:

- **Write path (eager):** computation done when data arrives, regardless of
  whether anyone ever reads it — updating indexes, maintaining materialized
  views, pre-aggregating metrics.
- **Read path (lazy):** computation done on demand at query time.

Indexes, [caches](caching-tiers.md), and materialized views are all devices
for *moving the boundary*: precompute more on the write path to make reads
cheap, or keep writes cheap and pay at read time. Write
[fan-out](fan-out.md) (e.g. materializing a timeline per follower on every
post) is the extreme write-path position; running the full query on read is
the extreme read-path position. There is no universally right point — the
read/write ratio and skew of the workload decide.

The boundary need not stop at the server. Stateful offline-first clients
hold a local replica of relevant server state (the screen is a materialized
view of the local model, itself a [lagging
replica](replication-lag.md)); push transports (WebSockets, server-sent
events) extend the *write path* to the device, replacing poll-based
request/response with subscribe-and-update dataflow. That reframes client
sync as ordinary replication — with offline devices as extreme-lag replicas
and [conflict handling](write-conflict-resolution.md) on reconnect, per
[multi-leader replication](multi-leader-replication.md).
