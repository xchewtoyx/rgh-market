---
type: concept
title: Log-Based Message Brokers
description: >
  Brokers (Kafka, Kinesis) that store each topic partition as a durable
  append-only log with per-message offsets — ordered, replayable consumption
  instead of destructive reads.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 11"
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §3.3"
---

# Log-Based Message Brokers

Kafka, AWS Kinesis, and DistributedLog combine a database's append-only
durability with messaging's low-latency notification. A topic is
[partitioned](partitioning.md); each partition is an append-only log on disk,
and every message gets a monotonically increasing **offset** within its
partition.

Semantics that follow from the structure:

- **Total order per partition** (no order across partitions) — the broker is
  effectively [total order broadcast](total-order-broadcast.md) within a
  partition, so messages needing mutual ordering must share a partition key.
  A downstream consumer performing a stream-stream join or a windowed
  aggregation relies on exactly this: partitioning both input streams on the
  join/group key guarantees every record it needs to correlate lands on the
  same partition and therefore the same consumer process, with no
  cross-machine coordination needed to bring them together.
- **Non-destructive reads:** consumers just advance an offset; independent
  consumer groups read the same log without interfering — cheap fan-out. This
  works because consumption is [pull-based](push-vs-pull-consumption.md):
  the consumer, not the broker, drives which offset it asks for next.
- **Replay:** messages are retained on disk for days or weeks regardless of
  consumption, so reprocessing history is just resetting an offset — the
  property that makes logs a repeatable integration backbone
  ([CDC](change-data-capture.md), [event sourcing](event-sourcing.md),
  rebuilding [derived views](dual-writes-problem.md)) rather than fire-and-
  forget messaging. Consumption becomes more like reading a file than
  receiving ephemeral messages.
- **Throughput via sequential I/O:** appends and partition-parallelism scale
  to millions of messages/sec without tracking per-message acknowledgment.
- **Coarse parallelism:** within a consumer group, a partition is consumed by
  one consumer at a time — parallelism is capped by partition count, and a
  slow *message* blocks its partition (head-of-line). Transient
  [AMQP-style brokers](message-brokers.md) fit better when per-message load
  balancing matters more than order. Which consumer owns which partition is
  decided by [consumer group rebalancing](consumer-group-rebalancing.md),
  re-run only when group membership changes rather than per message.

A consumer's offset checkpoint is the recovery point: after a crash, it
resumes from the last recorded offset and re-reads anything processed but not
checkpointed — duplicates, hence [idempotent
processing](idempotency.md) or
[effectively-once machinery](effectively-once-delivery.md).

## Auditing to catch silent data loss

At-least-once delivery guards against under-counting message loss going
unnoticed only if something is actually watching for it — the guarantee
itself doesn't prove nothing was dropped along the way (a broker crash
before a message is durably written, a producer that fails to retry). A
count-reconciliation audit closes that gap without inspecting message
content: producers periodically emit their own "I published N messages for
this topic in this time window" counters as ordinary messages on a
dedicated audit topic, and consumers independently tally what they actually
received per topic per window and compare against the producer-reported
counts. Publishing the audit counters *through the same log* means the
audit trail inherits the log's own durability and ordering rather than
needing a separate reliable side-channel — a discrepancy between the two
tallies is the signal that something was lost somewhere in the pipeline,
even though which specific message and where require further digging.
