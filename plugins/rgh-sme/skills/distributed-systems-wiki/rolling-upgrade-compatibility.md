---
type: concept
title: Rolling Upgrade Compatibility
description: >
  A rolling deploy puts old and new code on the wire and on disk at the same
  time, so every encoding a distributed system uses must stay both backward
  and forward compatible across that window.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 4"
---

# Rolling Upgrade Compatibility

Deploying new code one node at a time (rather than stopping the whole
system) is what lets a distributed system evolve without downtime — but for
the whole duration of the rollout, old and new code coexist and exchange
data through logs, network calls, and shared storage. Two independent
compatibility properties both have to hold across that window:

- **Backward compatibility**: newer code can read data written by older
  code. Usually easy — new code just knows how to handle the legacy shape.
- **Forward compatibility**: older code can read data written by newer
  code. Harder — old code has to gracefully ignore fields or record types it
  has never seen, rather than erroring or silently corrupting them.

Schema-driven binary formats (Protocol Buffers, Thrift, Avro) get this by
construction: fields are identified by a stable numeric tag or matched by
name against a separate reader/writer schema pair, not by position, so
adding a field is invisible to code that doesn't know about it yet, and
removing one only breaks readers that require it. This is exactly what
makes a [replicated log](replicated-log.md)'s [logical replication
log](replication-log-implementations.md) — the format built specifically to
survive leader and follower running different versions — practical: a
leader on newer code and a follower still on older code must still agree on
every entry's meaning during the rollout.

## Where this bites in a distributed system

- **Read-modify-write cycles on shared storage.** If an old-code instance
  reads a record a newer instance wrote, updates only the fields it knows
  about, and writes the record back, any unrecognized newer fields must
  survive that round trip untouched — losing them silently is a real bug
  class, not a hypothetical one.
- **Message-passing dataflow.** A [message broker](message-brokers.md) or
  [log-based](log-based-messaging.md) system decouples producer and consumer
  processes, which routinely run different code versions during a rollout;
  the wire format has to tolerate both directions of skew for as long as the
  rollout takes.
- **[State machine replication](state-machine-replication.md)'s determinism
  requirement.** Every replica must interpret a given log entry identically;
  a schema change that two versions of the apply function interpret
  differently is a determinism violation, not just a compatibility
  inconvenience — it produces silent replica divergence rather than a
  visible error.

The operational takeaway: any format choice for a log, a replication
stream, or an inter-service call needs an explicit answer to "what happens
when the reader and writer are on different code versions," because in a
system built for rolling upgrades, that situation isn't an edge case — it's
the normal state of the system for the whole rollout window.

The same discipline applies to a shared database schema, not just wire
formats: [expand-contract migration](expand-contract-migration.md) is the
technique for changing a schema in phases so that old and new application
code can both read and write it correctly throughout the rollout.
