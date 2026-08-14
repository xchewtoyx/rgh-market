---
type: concept
title: Streaming Platform Lineage (MillWheel to Beam)
description: >
  How MillWheel, Kafka, Cloud Dataflow, Flink, and Beam each advanced
  out-of-order correctness, durable replay, unified batch/stream semantics,
  checkpointing, and portable APIs — the post-Storm lineage of large-scale
  stream processing.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 11"
---

The second wave of large-scale stream processing (after MapReduce/Hadoop/
Storm/Spark — see
[streaming platform lineage (MapReduce to Spark)](streaming-platform-lineage-mapreduce-to-spark.md))
converged on
out-of-order event-time correctness, durable replay, and unified batch/stream
programming. Five systems mark the arc:

## MillWheel — out-of-order processing

Google's first general-purpose stream architecture (Seattle, ~2011). Started
as a low-latency/weak-consistency niche like Storm, but two early customers
— sessionization over search data and the Zeitgeist anomaly-detection pipeline
— demanded reliable outputs. Out-of-order support was similarly customer-
driven: Zeitgeist needed a genuine output **stream** of anomaly signals, not
a materialized view consumers poll.

**True streaming vs. materialized-view semantics:** systems like Spark
Structured Streaming and Kafka Streams often limit themselves to repeated
updates to an eventually consistent output table — simpler, but unsuitable
when consumers need a stream of discrete events (anomaly firings, not
table diffs). That omission is a real trade-off, not a strictly more general
approach.

Zeitgeist's dip-detection need drove
[watermarks](watermark-computation-and-propagation.md): you cannot infer an
anomalous absence from zero counts alone — you need a signal of input
*completeness*. Processing-time delays failed under out-of-order data
(floods of false dip anomalies). MillWheel combined
[exactly-once](delivery-guarantees-exactly-once-vs-at-least-once.md),
[persistent state](streaming-persistent-state.md),
[watermarks](watermark-computation-and-propagation.md), and
[timers](watermark-and-wall-time-timers.md) for robust low-latency
out-of-order processing on commodity hardware. Later integrated as
"Streaming Flume"; successor Windmill powers Cloud Dataflow.

Prefer **low watermarks** (pessimistic completeness tracking) over **high
watermarks** (newest known event time, as Spark Structured Streaming uses for
GC) — high watermarks discard data more aggressively as event-time skew
varies across the pipeline.

## Kafka — durable streams and streams-and-tables

LinkedIn's transport layer (not a processor) became one of stream processing's
most influential pieces via two contributions:

1. **Durability and replayability on streams** — prior systems used ephemeral
   queues (RabbitMQ, TCP) with at-best upstream backup. Kafka brought the
   database world's durable partitioned log to streaming. Replay is now the
   foundation most engines (Flink, Spark, Storm, Apex, Kafka Streams) rely on
   for end-to-end exactly-once — each needs rewind-to-checkpoint on the
   input; sources without replay break end-to-end exactly-once regardless of
   upstream delivery guarantees. See
   [log-based message broker](log-based-message-broker.md) and
   [stream replay for reprocessing](stream-replay-for-reprocessing.md).

2. **Popularizing [streams-and-tables theory](streams-and-tables-duality.md)**
   — the framing that unifies MapReduce-family systems, SQL databases, and
   stream processors under three operation types (nongrouping, grouping,
   ungrouping).

## Cloud Dataflow — unified batch plus streaming

Google's managed service (2015) packaged MapReduce/Flume/MillWheel experience.
Primary contribution: the **unified batch-plus-streaming programming model**
— transformations, windowing, watermarks, triggers, accumulation, and the
[what/where/when/how](dataflow-model-four-questions.md) framing. Key insight:
batch and streaming differ mainly in the ability to incrementally
[trigger tables into streams](streaming-triggers-and-panes.md); conceptually
both are [streams and tables all the way down](streams-and-tables-duality.md).
(Caveat: batch engines still apply bounded-data optimizations streaming
hasn't fully replicated.)

Targets: unaligned event-time windows (sessions), custom windowing, flexible
trigger/accumulation trade-offs, watermark-based completeness for absence
detection, and logical abstraction over execution mode so microbatch size
doesn't leak into the API.

## Flink — open-source innovator

Rose rapidly from 2015 by (1) early adoption of the Dataflow/Beam model and
(2) efficient **Chandy–Lamport distributed snapshots** for strong consistency
— periodic barriers propagate along worker paths; when a consumer receives a
barrier on all inputs, it checkpoints all active keys (see
[stream processing fault tolerance](stream-processing-fault-tolerance.md)).
Tuning barrier frequency trades latency (side effects materialize at
checkpoints) against throughput.

**Savepoints** extend snapshots: restart an entire pipeline from any past
point — extending Kafka's durable-replay concept from transport to full
pipeline state. As of publication, among the first big steps toward graceful
evolution of long-running pipelines. Also brought the first practical
streaming SQL API at distributed scale.

## Beam — portability

Apache Beam is a programming model and portability layer, not an execution
engine — the programmatic analogue of SQL:

- **Unified model** (from Dataflow) — language/runtime independent.
- **SDKs** (Java, Python, Go) — idiomatic per language.
- **DSLs** atop SDKs (Scio, SQL DSL).
- **Runners** translate logical pipelines to physical ones on Apex, Flink,
  Spark, Cloud Dataflow, etc.

Deliberately neither the intersection (lowest common denominator) nor union
(kitchen sink) of runner features — includes the best cross-community ideas
and allows innovation in both directions (Beam API ahead of runners, e.g.
SplittableDoFn; runner features ahead of Beam, e.g. savepoints). Identical
Beam semantics can still differ greatly in runtime characteristics — runner
choice requires due diligence per use case.
