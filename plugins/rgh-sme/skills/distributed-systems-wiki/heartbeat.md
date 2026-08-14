---
type: concept
title: Heartbeat
description: >
  Periodically sending a liveness message to peers so absence of the message,
  not just a slow response, is what a timeout is measured against.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 7, HeartBeat"
---

# Heartbeat

Where [timeouts and failure detection](timeouts-and-failure-detection.md)
covers the receiver's dilemma (how long to wait before declaring a peer
dead), heartbeat is the sender-side half: periodically send a liveness
message to peers, purely so that its absence becomes the signal a timeout
measures. The three intervals involved must be ordered:

```
Timeout Interval > Request (heartbeat) Interval > Network round-trip time
```

Worked numbers: ~20 ms RTT → heartbeat every 100 ms → declare a timeout after
1 s, leaving room for several heartbeats to go missing before a failure
verdict is reached, which trades detection speed for fewer false positives.

## Small clusters: heartbeat flows leader to followers

In 3–5 node consensus clusters (Raft, ZooKeeper), heartbeats flow from leader
to followers; each arrival is timestamped, and a periodic check marks any
server whose last heartbeat is older than the timeout as down. A missed
heartbeat from the leader triggers a fresh
[election](leader-election.md) — but because the leader might merely be slow
rather than actually dead, a [generation clock](generation-clock.md) is
required so that a "deposed" leader which later reappears cannot have its
stale requests accepted.

### Practical failure modes for the heartbeat mechanism itself

- **Head-of-line blocking.** If heartbeats and data share a [single socket
  channel](single-socket-channel.md), a slow or large request queued ahead of
  a heartbeat can delay it enough to trigger a false failure detection. Fix:
  a [request pipeline](request-pipeline.md), so a server never has to wait
  for a prior response before sending the next message, heartbeats included.
- **Interaction with single-threaded processing.** If message handling runs
  through a [singular update queue](singular-update-queue.md), a slow disk
  write ahead of a scheduled heartbeat can delay the heartbeat's send (or a
  receiver's processing of an incoming one). Mitigation: send heartbeats from
  a separate thread, asynchronously from the main processing queue (Consul,
  Akka); a receiver that can't avoid the delay should widen its
  failure-detection window to compensate (Raft's LogCabin does this).
- **Local pause detection.** A runtime pause (e.g. GC) can delay heartbeat
  processing generally, independent of the network. Mitigation: if
  processing resumes after an unexpectedly long gap, treat that cycle as
  suspect and defer any failure marking to the next cycle rather than acting
  on stale timing data (Cassandra does this).

## Large clusters: heartbeats plus gossip

All-to-all heartbeating doesn't scale to hundreds or thousands of wide-area
nodes — it reproduces the O(N²) blowup described under [scaling
effects](scaling-effects.md). Large clusters instead combine a failure
detector with [gossip dissemination](gossip-dissemination.md) to propagate
liveness information, under two hard constraints: a fixed cap on messages
generated per server, and a bandwidth ceiling so failure-detection traffic
doesn't crowd out real data traffic. Because these clusters take disruptive
action on a failure verdict (moving data around), they favor *correct*
detection over *fast* detection — a bounded extra delay is an acceptable
trade for fewer false positives. The common mechanism is a per-process
suspicion number that increments whenever gossip fails to mention that
process within a calibrated window; the process is marked failed only once
the number crosses a threshold, rather than on a single missed message.

Two mainstream implementations: the **Phi Accrual failure detector** (Akka,
Cassandra), which outputs a continuous suspicion level rather than a binary
verdict by modeling the historical heartbeat-interval distribution, and
**SWIM with the Lifeguard enhancement** (HashiCorp Consul, memberlist). Both
scale to thousands of nodes.
