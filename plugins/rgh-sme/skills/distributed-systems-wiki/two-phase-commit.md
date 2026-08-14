---
type: concept
title: Two-Phase Commit (2PC)
description: >
  The atomic commit protocol making multiple nodes commit or abort a
  transaction together — safe, but blocking: a crashed coordinator leaves
  participants in doubt, holding locks.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 9"
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 21, Two Phase Commit"
---

# Two-Phase Commit (2PC)

Atomic commit across nodes: a transaction touching several nodes (or several
systems) must commit everywhere or abort everywhere — partial commits violate
atomicity irreversibly, since committed data may already be visible to other
transactions. 2PC achieves this with a **coordinator** and two phases:

1. **Prepare:** the coordinator asks every participant "can you commit?".
   Each participant writes the transaction's data durably (WAL), checks
   constraints, and answers yes or no. Voting **yes is an irrevocable
   promise**: the participant must be able to commit later no matter what —
   crash, restart, disk-full excuses are not allowed.
2. **Commit/abort:** if *all* voted yes, the coordinator writes the commit
   decision to its own log on disk — **that log write is the commit point** —
   then tells everyone to commit. Any no vote or timeout means abort
   everywhere. Once decided, the coordinator must retry until every
   participant complies.

## The blocking flaw: in-doubt participants

If a participant votes yes and the coordinator then crashes, the participant
is **in doubt**: it cannot abort (the decision may have been commit) and
cannot commit (it may have been abort). It must hold its locks — typically
exclusive row locks — until the coordinator recovers and replays its decision
log. A lost coordinator log means those locks are held *indefinitely*, taking
out unrelated traffic that touches the same rows.

The **X/Open XA** standard implements 2PC across heterogeneous systems
(databases plus message brokers) via a C API; its coordinator commonly lives
in the application process, making coordinator loss routine. Recovery then
requires manual admin intervention or destructive "heuristic decisions"
(participants unilaterally commit/abort, breaking atomicity). Other XA
drawbacks: the coordinator becomes a non-replicated stateful single point of
failure, and the protocol is a lowest common denominator that amplifies
failures — any participant timeout aborts everything, the opposite of
fault tolerance.

2PC ensures agreement but not availability. Making the *decision itself*
fault-tolerant — so a crashed coordinator cannot block the system — is the
job of [consensus](consensus.md); log-based
[derived-data pipelines](change-data-capture.md) avoid needing atomic commit
across systems in the first place.

## Distinguishing it from Paxos-style agreement

2PC solves a different problem from [Paxos](paxos.md) or a [replicated
log](replicated-log.md): those coordinate nodes that are all replicating the
*same* value or log entry. 2PC instead coordinates nodes holding
*different* data — separate [partitions](partitioning.md) — where each
participant can itself internally be a replicated-log group (a "Multi-Raft"
shape: genuinely separate replicated logs, one per partition, as opposed to
"Multi-Paxos," one logical log built from many per-entry Paxos rounds). The
coordinator is chosen dynamically, conventionally whichever node holds the
first key the client touches, and persists its own transaction bookkeeping
to a [write-ahead log](write-ahead-log.md) so it can resume correctly after
a crash — on restart it replays that log and simply re-sends `commit` to any
transaction it finds already marked prepared, since "prepared" durably means
every participant already promised to commit. A client's actual reads and
writes go directly to whichever node holds each key rather than being routed
through the coordinator, avoiding a double network hop; because a key's
leader can change mid-transaction on failover, participants are tracked by
key, not by fixed server address.

Concurrent transactions competing for the same locks at prepare time produce
genuine cross-node deadlocks that a distributed system can't cheaply detect
with a waiting-for graph — see [wound-wait and wait-die
deadlock avoidance](wound-wait-and-wait-die.md) for how real systems resolve
this by aborting one side deterministically instead.

## Lock-free reads via Versioned Value

Holding read locks for a long-running, read-only report needlessly blocks
concurrent writers. The fix combines 2PC with [versioned
value](versioned-value.md): at prepare time, each participant reports the
timestamp it can safely write at; the coordinator picks the *maximum* across
all participants as the single commit timestamp, and every participant
stores its part of the transaction under that shared timestamp. Because a
value at a given timestamp is thereafter immutable, a read-only query pinned
to a fixed timestamp can proceed without taking any lock at all, with a
guaranteed-consistent snapshot — real systems use a [hybrid
clock](hybrid-clock.md) (MongoDB, CockroachDB) to generate these timestamps.
This only helps read-only transactions; a read that is part of a
read-write transaction still needs ordinary locking.

That scheme in turn needs a **monotonic write-after-read guarantee**: once a
value has been read at timestamp T, no later write may land at a timestamp
≤ T, or a value a client already saw could be silently superseded in the
past. Google Percolator and TiKV enforce this with a dedicated Timestamp
Oracle service handing out monotonically increasing timestamps cluster-wide;
MongoDB and CockroachDB instead rely on a hybrid clock, where every message
exchange advances a server's clock to at least the maximum it has seen. A
read at a timestamp for which a write is still prepared-but-uncommitted is
genuinely ambiguous — CockroachDB errors in that case, while Spanner has the
read wait until the in-flight write resolves.
