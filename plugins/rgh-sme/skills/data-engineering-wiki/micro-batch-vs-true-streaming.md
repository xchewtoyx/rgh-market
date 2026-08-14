---
type: concept
title: Micro-Batch vs. True Streaming
description: >
  Choosing between a batch-oriented framework run at high frequency and a
  genuine per-event streaming engine, based on actual latency needs rather
  than technology preference.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 8"
---

**Micro-batching** applies a batch-oriented processing framework to a
streaming situation at very high frequency — anywhere from every couple of
minutes down to every second. Some frameworks are purpose-built for this and
perform well when properly resourced at that frequency. **True streaming**
systems process one event at a time, at the cost of real per-event
processing overhead — though even true-streaming systems still batch some
internal work (a triggered window metric might only actually run every few
seconds even while individual event enrichment happens at low per-event
latency).

The right choice follows entirely from the use case's actual latency
tolerance and the team's existing expertise, not from technology fashion:
metrics that only need to update every few minutes (a sales dashboard during
a big promotional event, say) are almost certainly fine on a well-tuned
micro-batch, while sub-second anomaly or fraud detection likely genuinely
needs true streaming. A team already fluent in a batch framework can stand
up a micro-batch solution far faster than learning an unfamiliar
true-streaming framework from scratch — that operational reality is a
legitimate input into the decision, not a rationalization to ignore.

Be skeptical of vendor framing here specifically: "micro-batch" is often
used as a dismissive marketing label against a competing technology despite
being perfectly sufficient, and sometimes superior, for a given real
workload — the same caution [batch vs. streaming ingestion](batch-vs-streaming-ingestion.md)
already recommends against adopting streaming by default applies here too,
one layer further into the pipeline.

Classic **Spark Streaming** (1.x) embodied micro-batching: the strongly-
consistent batch engine ran repeatedly over successive one-second (default)
batches, gating progress on global batch barriers — correct without a
separate Lambda batch path for in-order work, but practically unable to
deliver both low per-key latency and high throughput simultaneously. See
[streaming platform lineage (MapReduce to Spark)](streaming-platform-lineage-mapreduce-to-spark.md).
