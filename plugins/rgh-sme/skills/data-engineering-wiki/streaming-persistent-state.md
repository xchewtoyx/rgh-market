---
type: concept
title: Streaming Persistent State
description: >
  Why unbounded-data pipelines need durable state beyond the input log, and
  how checkpointing partial progress enables correctness and efficiency after
  failure.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 8"
---

**Persistent state** is the durable tables introduced under grouping in a
streaming pipeline — stored in media relatively immune to loss (replicated
disk across locations; in-memory-only does not count).

Unbounded-data pipelines are intended to run indefinitely, but machine
failures, maintenance, code changes, and misconfigurations will interrupt
them. Resuming requires a durable recollection of prior progress. This isn't
strictly streaming-specific — bounded batch systems often assume full input
reprocessing on failure — but unbounded inputs cannot be fully replayed, so
data no longer available from the source must be accounted for in durable
checkpoints. At-most-once needs no checkpointing; at-least-once and
[exactly-once](delivery-guarantees-exactly-once-vs-at-least-once.md) require
it.

Persistent state provides:

- **Correctness basis** — continue processing after the input source has
  forgotten records it already delivered.
- **Efficiency** — checkpoint partial progress (intermediate results plus
  input position) so operations before the checkpoint need not replay from
  durable inputs.

Minimize persisted volume by storing compact intermediate forms (running
sum + count for a mean, not all raw values) and garbage-collecting state for
records known fully processed. Combined with intelligent GC,
[allowed lateness](allowed-lateness-horizon.md), and incremental combining,
state volume over unbounded input can stay manageable indefinitely.

The practical spectrum balances always-persist-everything (good consistency,
bad efficiency) against never-persist (nonoption when consistency matters).
See [incremental combining vs. raw grouping](incremental-combining-vs-raw-grouping.md)
for the two implicit forms at opposite ends, and
[generalized streaming state API](generalized-streaming-state-api.md) when
neither implicit form offers enough flexibility in data structures, I/O
granularity, or processing-time scheduling.

Log-based brokers like Kafka serve a similar function for replayable input,
but operator state for aggregations and joins still needs its own durable
store — see [stream processing fault tolerance](stream-processing-fault-tolerance.md).
