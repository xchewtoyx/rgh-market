---
type: concept
title: Schema Registry
description: >
  A metadata service that tracks schema versions for streaming messages so
  producers and consumers can evolve independently without breaking
  deserialization.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §4"
---

A schema registry is a metadata repository that maintains schema and type
integrity for streaming messages as producer and consumer schemas evolve
over time. It tracks schema versions and history, and it's what enables
consistent serialization and deserialization across many independently
deployed producers and consumers reading and writing the same topic — used
across most major streaming platforms and clouds.

This is the concrete mechanism behind
[schema evolution in source systems](schema-evolution-in-source-systems.md)'s
abstract requirement to have *some* answer for "how are schema changes
communicated downstream?" — a registry makes that answer machine-enforced
rather than relying on prose documentation or word of mouth, by resolving
[backward and forward compatibility](schema-compatibility-modes.md) between
whatever schema a message was written with and whatever schema the consumer
reading it expects. It doesn't
eliminate the need for proactive communication about planned changes (a
registry can reject an incompatible schema, but it can't tell a downstream
team *why* a field disappeared), so it's best paired with, not substituted
for, direct communication with the owning team — and with a
[dead-letter queue](dead-letter-queue.md) to catch whatever still slips
through despite the registry.

**A consumer only needs to resolve a given schema ID once, not once per
message**: since a registered schema is immutable once assigned an ID, the
lookup result is safe to cache for the lifetime of the consumer process —
every subsequent message tagged with the same ID reuses the cached schema
instead of hitting the registry again, which is what keeps the registry off
the hot path of per-message deserialization at high message volume.
