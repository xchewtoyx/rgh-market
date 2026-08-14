---
type: concept
title: Batch vs. Streaming Ingestion
description: >
  Why streaming is the underlying nature of data and batch is just a
  convenient chunking of it, and how to decide which fits a given pipeline.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 2"
---

Virtually all data is inherently a continuous stream at its source. **Batch
ingestion** is simply a convenient way of chunking that stream — e.g.,
collecting a full day of events and moving them at once. It happens on a time
interval or size threshold and is a "one-way door": once data is chunked,
downstream latency is inherently bounded by the batch cadence. Batch has long
been the default (legacy system limits) and remains extremely popular,
especially for analytics and ML training.

**Streaming ingestion** delivers data to downstream systems continuously.
"Real-time" or "near real-time" means available a short time after
production — commonly under a second, though the acceptable bar varies by
domain. [Separation of storage and compute](compute-storage-separation.md),
plus the spread of managed streaming platforms, has made continuous
processing far more accessible than it used to be.

Deciding whether to go streaming-first should be driven by a checklist, not by
technology fashion:

- Can downstream storage actually handle the ingestion rate?
- Do you truly need millisecond latency, or would a micro-batch (say, every
  minute) satisfy the use case?
- What specific business benefit does real-time delivery provide over batch
  for *this* use case?
- Will streaming cost more — in engineering time, money, maintenance, and
  operational risk — than batch would?
- Is the streaming pipeline reliable and redundant against infrastructure
  failure?
- Which tooling fits: a managed service (Kinesis, Cloud Pub/Sub, Cloud
  Dataflow) or a self-managed platform (Kafka, Flink, Spark, Pulsar) — and who
  owns operating it?
- What's the read impact on a live production source system?

The practical recommendation: batch is excellent for most common cases
(model training, weekly reporting). Adopt true real-time streaming only after
identifying a business use case that actually justifies the added cost and
complexity — not by default.

**Ingestion frequency sets a hard ceiling on serving frequency**: no
downstream stage can serve data fresher than the frequency at which it was
ingested, no matter how fast transformation and serving run. This means the
ingestion decision has to be made with an eye on every downstream use case a
dataset might ever need, not just the one in front of you today — if *any*
legitimate use case for a dataset needs streaming freshness, that dataset
should be ingested as a stream even while most consumers of it stay on a
batch cadence, because batch ingestion forecloses the streaming option
entirely while streaming ingestion never forecloses batch consumption.
