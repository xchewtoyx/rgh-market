---
type: concept
title: Single Socket Channel
description: >
  Routing all communication between a pair of nodes through one long-lived
  TCP connection, relying on TCP's own ordering instead of building message
  ordering at the application layer.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 30, Single Socket Channel"
---

# Single Socket Channel

[Leader-follower](leader-election.md) communication needs messages kept in
order, with retry on loss, without paying repeated connection-setup latency.
Since TCP already provides ordered, reliable delivery, the simplest way to
get this is to route *all* traffic between a given pair of nodes through one
long-lived socket, opened once and never closed under normal operation. The
receiving side hands each incoming message off to a [singular update
queue](singular-update-queue.md) rather than answering inline, keeping
message ordering and state mutation aligned.

A read timeout is essential — the connection must not block forever on a
silent failure — and is set as a multiple (roughly 10x is typical) of the
[heartbeat](heartbeat.md) interval already flowing over the same channel:
since heartbeats are continuous background traffic, an absence of *any*
message for that long safely signals a dead connection, accounting for
normal round-trip variance without needing a separate liveness mechanism.

## The cost: head-of-line blocking

Funneling everything through one channel means a large or slow request
queued at the front can delay everything behind it — including a
time-sensitive heartbeat, which is exactly the false-failure-detection risk
[heartbeat](heartbeat.md) describes. The fix is not multiple channels (which
would reintroduce the ordering problem this pattern exists to avoid) but
[request pipelining](request-pipeline.md): stop waiting for each response
before sending the next request, so nothing has to queue behind a single
slow one in the first place.

ZooKeeper, Kafka's follower-to-leader replication, and Raft's LogCabin
reference implementation all use one dedicated socket per peer pair for
exactly this reason.
