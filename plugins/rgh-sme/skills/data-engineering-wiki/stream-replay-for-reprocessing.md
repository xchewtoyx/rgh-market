---
type: concept
title: Stream Replay for Reprocessing
description: >
  Using a streaming platform's retained history to re-derive a batch view or
  reprocess a range of past events, rather than treating streamed data as
  disposable once consumed.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 6"
---

Message queues traditionally treat stored data as transient — gone once
consumed or once a retention window passes. Distributed streaming platforms
(Kafka, Kinesis, Pulsar, Cloud Pub/Sub) — all
[log-based message brokers](log-based-message-broker.md) — instead support
effectively indefinite retention, often by tiering older, infrequently
accessed messages down into object storage behind the scenes.

**Replay** — reading back a historical range of stored stream data — is the
standard retrieval mechanism this retention enables, and it serves two
distinct pipeline needs: running a batch-style query over a past time range
against data that arrived as a stream, and reprocessing pipeline data after
discovering a bug or needing to backfill a downstream target. Replay is what
makes stream data usable as a genuine system of record for reprocessing
rather than just a transient transport mechanism — but it only produces a
correct result if the consuming job is
[idempotent](idempotent-and-replayable-jobs.md): replaying a range that was
already processed once must not double-count or duplicate whatever the
first pass already wrote.

Kafka's durable partitioned log was the breakthrough that moved stream
processing out of "approximation tools" into general-purpose data processing:
most modern engines (Flink, Spark, Storm, Apex, Kafka Streams) depend on
rewind-to-checkpoint replay on the input source for end-to-end
[exactly-once semantics](delivery-guarantees-exactly-once-vs-at-least-once.md)
— sources without replayability break end-to-end exactly-once even when
upstream delivery is reliable. See
[streaming platform lineage](streaming-platform-lineage-millwheel-to-beam.md)
for Kafka's historical role.
