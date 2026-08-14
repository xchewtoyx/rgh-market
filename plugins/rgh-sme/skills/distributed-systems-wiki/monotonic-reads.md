---
type: concept
title: Monotonic Reads
description: >
  The guarantee that a user's successive reads never move backward in time —
  once a value is seen, an older state is never returned.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 5"
---

# Monotonic Reads

Under [replication lag](replication-lag.md), successive reads may hit different
followers with different lag: a user sees a new comment on one refresh, then
refreshes again against a more-lagged replica and the comment is gone — time
appears to run backward. Monotonic reads guarantees this never happens: after
seeing state at some point in time, later reads never return earlier state.

It is a weaker guarantee than [read-your-writes](read-your-writes-consistency.md)
(it says nothing about seeing your own writes promptly) and stronger than plain
[eventual consistency](eventual-consistency.md).

Standard implementation: **pin each user's reads to one replica**, e.g. by
hashing the user ID to a replica rather than picking randomly. If that replica
fails, the user is rerouted and the guarantee needs re-establishing (the new
replica must be at least as current as the last read).
