---
type: concept
title: Request Waiting List
description: >
  Correlating asynchronously arriving peer responses back to the client
  request that triggered them, and firing a callback once a completion
  criterion such as quorum is met.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 14, Request Waiting List"
---

# Request Waiting List

A cluster node often must talk to peer nodes — for replication, for a
[quorum](truth-defined-by-majority.md)-gated write — before it can answer a
client, and that inter-node communication is asynchronous. The node must
therefore correlate each peer response, as it arrives, back to the original
pending client request, and decide when its completion criterion has been
satisfied.

The mechanism is a map from a **key** to a **callback**: the key is whatever
identifies "this response belongs to that pending thing" — a correlation id
for one outbound message, or a [replicated log](replicated-log.md)'s [high
water mark](high-water-mark.md) for a value being awaited. The callback
inspects each incoming response and decides whether the original request can
now complete. For a quorum-gated write, the callback counts responses and
fires the *first* time either successes or errors reach quorum, ignoring
whatever arrives after — a slower remaining reply is irrelevant once the
decision is already made.

This pairs directly with a [singular update queue](singular-update-queue.md):
the queue keeps state mutation single-threaded, while the waiting list is
what lets the single worker thread hand off "wait for more input" without
blocking on it — register a callback and move on to the next item, rather
than parking the thread until the peer responses arrive.

## Expiry

Peer responses can simply never arrive — a dead peer, a dropped message. The
waiting list needs its own periodic sweep that scans for entries older than
a configured expiration window and invokes their callback's error path,
otherwise a silently-abandoned entry leaks forever and the caller never
learns its request failed. This is the same
[timeout](timeouts-and-failure-detection.md) trade-off applied to individual
in-flight requests rather than to whole-peer liveness.

Cassandra correlates asynchronous inter-node messages with quorum decisions
this same way; Kafka calls its version of this structure the **purgatory**;
etcd maintains an analogous wait list to answer client requests once enough
peers respond.
