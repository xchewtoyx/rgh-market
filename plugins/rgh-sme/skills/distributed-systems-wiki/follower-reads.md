---
type: concept
title: Follower Reads
description: >
  Routing read-only traffic to the nearest or least-loaded follower to
  offload the leader, and the mechanisms that bound how stale an answer a
  client is willing to accept.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 16, Follower Reads"
---

# Follower Reads

Sending every read to the [leader](leader-election.md) wastes the whole
point of having followers: writes must go through the leader for
consistency, but reads can go anywhere that has the data, and an overloaded
leader or a remote client in a multi-datacenter setup both benefit from
spreading read load off it. The caveat that has to be accepted up front:
followers can return **stale** values. Even under Raft-style consensus there
is always some lag, because a leader still needs an extra message to inform
a follower an entry is committed even after the leader itself knows it — see
[replication lag](replication-lag.md). Follower reads are only appropriate
where a bounded amount of staleness is acceptable.

## Picking a replica

A client (or coordinator) tracks live latency per follower — commonly a
moving average updated opportunistically from the periodic
[heartbeats](heartbeat.md) nodes already exchange, so no extra measurement
traffic is needed — and prefers same-region followers, falling back to any
follower if none exist in-region. A follower that hasn't heard from the
leader in a while, or that has fallen behind due to a slow disk, should stop
serving reads entirely rather than return arbitrarily stale data: some
systems let operators cap the allowed staleness and exclude replicas beyond
it, while others (e.g. a consumer requesting a log offset a follower doesn't
have yet) simply reject the request and force a fallback to the leader.

## Read-your-own-writes via a causality token

The sharp failure mode: a client corrects a bad value through the leader,
then immediately reads it back, but the read lands on a follower that hasn't
caught up — the client's own correction appears to vanish. (This was a real,
long-standing gap in Amazon S3's consistency model.) The fix reuses
[versioned value](versioned-value.md): every write response includes the
version it was applied at; the client attaches that version to its
subsequent read; a follower compares its own current version against the
requested one and, if it's behind, **waits** (bounded by a timeout) until it
catches up rather than answering with stale data — or times out and lets the
client retry elsewhere. This is the same "register a callback, fire it when
the condition becomes true" shape as a [request waiting
list](request-waiting-list.md), just keyed on a log version instead of a
peer-response correlation id, and it is the concrete implementation behind
the "causality tokens" technique in [read-your-writes
consistency](read-your-writes-consistency.md).

Real systems converge on the same idea under different names: Neo4j's
"bookmark," MongoDB's `operationTime`, and CockroachDB's leader-published
"closed timestamps" (the latest point up to which all writes are known
complete, so a follower may answer any read at or before it) are all a
version or timestamp a client carries forward to bound staleness on its next
read.

When staleness genuinely cannot be tolerated, the read has to go to the
leader instead — the same trade-off [coordination
services](coordination-services.md) and [stale-leader
reads](stale-leader-reads.md) address from the leader's own side.
