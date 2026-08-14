---
type: concept
title: The Data Engineering Lifecycle
description: >
  The five stages a pipeline's data passes through — generation, storage,
  ingestion, transformation, serving — plus the cross-cutting undercurrents
  that make every stage work in practice.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Data moves through five stages on its way from a source system to a consumer:
**generation** (in a source system) → **storage** → **ingestion** →
**transformation** → **serving**. Storage isn't really a single discrete step —
it recurs throughout, since many systems (cloud warehouses, Kafka/Pulsar) blend
storage with ingestion, transformation, and serving at once. The middle stages
commonly get jumbled, repeat, or occur out of order in a real pipeline; that's
normal, not a design smell.

This lifecycle is a subset of data's full lifespan — it covers only the stages
an engineer actually controls, not everything that ever happens to the data.

Six **undercurrents** cut across every stage and determine whether it actually
works in production, not just in a diagram: security, data management,
[DataOps](dataops-pillars.md), data architecture, [orchestration](orchestration-vs-scheduling.md),
and software engineering. A stage that looks complete on a whiteboard but
ignores these will fail operationally.

Across all five stages, an engineer is optimizing for three things
simultaneously: maximize ROI / reduce cost, reduce risk (security, data
quality), and maximize the data's value and utility to downstream consumers.

Related stage-level concepts: [source system evaluation](source-system-evaluation.md)
and [schema evolution in source systems](schema-evolution-in-source-systems.md)
(generation), [data temperature tiering](data-temperature-tiering.md) (storage),
[batch vs streaming ingestion](batch-vs-streaming-ingestion.md) and
[change data capture](change-data-capture.md) (ingestion), and
[reverse ETL](reverse-etl.md) (serving).
