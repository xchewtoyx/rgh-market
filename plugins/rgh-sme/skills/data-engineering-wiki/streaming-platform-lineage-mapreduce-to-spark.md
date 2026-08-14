---
type: concept
title: Streaming Platform Lineage (MapReduce to Spark)
description: >
  How MapReduce, Hadoop, Flume, Storm, and Spark each shaped large-scale data
  processing — from scalable batch primitives through composable pipelines,
  weak-consistency streaming, and batch-grade correctness without Lambda
  duplication.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 11"
---

A decade-and-a-half arc from Google's MapReduce (2003) to modern unified
engines. Each system's headline contribution to streaming as it exists today:

## MapReduce — simplicity and scalability

Google engineers noticed data processing, scalability, and fault tolerance on
commodity hardware were each hard alone. MapReduce handled the last two so
engineers focused on logic — a simple map/reduce API over two functional
primitives. Under the hood (see
[streams-and-tables duality](streams-and-tables-duality.md)): table → stream
→ stream → table for both Map and Reduce halves. Published OSDI 2004; no
source release, so outsiders built bespoke systems. Nothing since has matched
its internal scale at Google.

## Hadoop — the open-source ecosystem

Doug Cutting and Mike Cafarella open-sourced HDFS and Hadoop (from Nutch)
under Apache; Yahoo's adoption gave engineering weight. Hadoop's openness
incubated Pig, Hive, HBase, Crunch, and the broader ecosystem — the single
most important contribution to later streaming systems, even though Hadoop
itself is batch-oriented.

## Flume — high-level pipelines and optimization

Google Seattle's Flume (not Apache Flume) addressed MapReduce's rigid Map →
Shuffle → Reduce chaining: multi-job pipelines needed proliferating
orchestration; map-only stages (filter, enrich) still paid full shuffle cost;
hand-optimization obscured logic.

Flume introduced composable **PCollection/PTransform** APIs (later in Beam)
with an optimizer generating efficient physical MapReduce sequences. Two
automatic optimizations:

- **Fusion** — run logically independent stages as one physical job
  (sequential consumer-producer fusion or parallel sibling fusion), eliminating
  intermediate serialization/network.
- **Combiner lifting** — partially lift a post-group-by combine (e.g., sum)
  into the preceding stage for partial aggregation before shuffle — especially
  valuable for hot keys. See
  [incremental combining](incremental-combining-vs-raw-grouping.md).

FlumeJava (2009) was an instant hit; later decoupled from MapReduce to a
custom engine (Dax) enabling **dynamic work rebalancing** ("liquid sharding")
from straggler shards to idle workers. Extended to MillWheel for streaming —
most high-level streaming concepts entered Flume before Cloud Dataflow/Beam.
See [streaming platform lineage (MillWheel to Beam)](streaming-platform-lineage-millwheel-to-beam.md).

## Storm — low latency, weak consistency, Lambda Architecture

Nathan Marz's Storm (from BackType/Twitter firehose processing) loosened
strong consistency — at-most-once or at-least-once, per-record processing,
no consistent persistent state — for lower latency than batch-style systems.
Users wanted both low latency and eventual correctness, which Storm alone
couldn't provide.

This drove the **[Lambda architecture](batch-streaming-unification-architectures.md)**
(Marz): weakly consistent Storm streaming for low-latency approximate results
plus strongly consistent Hadoop batch for exact results, merged in a serving
layer — popular despite dual-pipeline cost because nothing else met the need.
Twitter later replaced Storm internally with Heron (2015, API-compatible).

## Spark — strong consistency for streaming

UC Berkeley AMPLab (~2009): in-memory computation via Resilient Distributed
Datasets (RDDs) capturing lineage for failure recomputation (requires
replayable, deterministic inputs). Spark Streaming ran the batch engine
repeatedly over successive batches — correct results without a separate batch
job for suitable use cases (no Lambda needed).

Caveats for Spark Streaming 1.x: processing-time windowing only — event-time
and late data needed substantial user code; best for in-order or event-time-
agnostic work. Anchors the
[micro-batch vs. true streaming](micro-batch-vs-true-streaming.md) debate:
global batch barriers make simultaneous low per-key latency and high
throughput difficult, though seconds/minutes latency suffices for most cases.
Spark 2.x greatly expanded semantic capabilities and added a true-streaming
architecture.
