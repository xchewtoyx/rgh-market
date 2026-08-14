---
type: concept
title: State Machine Replication
description: >
  Keeping replicas identical by feeding the same deterministic operations, in
  the same order, to every replica — the log is the system's ground truth.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: "Time, Clocks, and the Ordering of Events in a Distributed System"
    resource: "Time, Clocks, and the Ordering of Events in a Distributed System (Lamport), \"Ordering the Events Totally\""
---

# State Machine Replication

If a process is deterministic — its next state depends only on its current
state and the operation applied — then several replicas that start identical
and apply **the same operations in the same order** remain identical forever.
Replication then reduces to agreeing on the order of operations, which is
exactly what [total order broadcast](total-order-broadcast.md) provides and
what [consensus](consensus.md) algorithms implement.

This is the conceptual core beneath several familiar mechanisms:

- A database [replication log](replication-log-implementations.md): followers
  applying the leader's log in order are replicated state machines. See
  [replicated log](replicated-log.md) for the concrete append/repair/commit
  mechanics Raft-family protocols use to keep that log agreed-upon.
- Coordination services: ZooKeeper and etcd replicate a small key-value state
  machine over Zab/Raft (see
  [coordination services](coordination-services.md)).
- [Event logs](log-based-messaging.md) feeding multiple consumers that each
  derive identical state.

The determinism requirement is strict: wall-clock reads, random numbers, and
external side effects must be excluded or captured in the log itself,
otherwise replicas diverge silently.

## Origin, and why the original version doesn't survive contact with failure

Lamport's original formulation (the paper that also introduced [Lamport
timestamps](lamport-timestamps.md)) has each process independently
**simulate** the state machine: every process collects commands from every
other process, orders them by [timestamp](lamport-timestamps.md), and may
execute a command once it has learned of *every* command, from *every*
process, timestamped no later than it — the distributed mutual-exclusion
protocol built directly on top of this is a worked instance, where
"commands" are resource-request and resource-release events and the
"state" is the queue of pending requests.

The catch, which Lamport flags explicitly: this requires the **active
participation of every process**. A single process failing to send its
commands stalls every other process indefinitely, since no one can ever be
sure they've seen everything timestamped up to a given point. This is why
practical [consensus](consensus.md) algorithms replaced "wait for all
processes" with "wait for a **majority quorum**" — the [majority
overlap argument](truth-defined-by-majority.md) tolerates minority failures
where the original all-participants scheme tolerates none. The reduction
from "replicate a state machine" to "agree on operation order" survives
unchanged; what changed over the following decades is how that ordering
agreement itself is made fault-tolerant.
