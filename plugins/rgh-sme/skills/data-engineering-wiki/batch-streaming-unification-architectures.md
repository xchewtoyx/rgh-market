---
type: concept
title: Batch/Streaming Unification Architectures (Lambda, Kappa, Dataflow Model)
description: >
  Three successive architectural attempts to serve both batch and real-time
  views from one pipeline, and why treating batch as bounded streaming won
  out over running two separate systems.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
---

**Lambda architecture** (early 2010s, Kafka + Storm/Samza era, originating
from Nathan Marz's Storm work): an immutable
append-only source feeds two independent systems — a low-latency "speed"
layer (typically NoSQL) and a batch layer producing precomputed aggregated
views (e.g., in a warehouse) — with a serving layer merging results from
both. In practice, keeping two separate codebases and systems reconciled
turned out to be as hard as it sounds and error-prone; it's no longer a
first recommendation, though it still shows up often in search results.

**Kappa architecture** (Jay Kreps, 2014): responds to Lambda's duplication by
using a single stream-processing platform as the backbone for ingestion,
storage, and serving — both batch and real-time reads go against the same
live event stream, with large replays standing in for what a batch layer
would have computed. It hasn't seen wide adoption, for two reasons: streaming
itself remains operationally hard for many teams despite being simple to
describe, and Kappa turns out complex and expensive in practice — batch
storage and processing remain more cost-effective for large historical
datasets even where streaming is technically capable of the same job.

**The Dataflow model** (Google Cloud Dataflow, implemented in **Apache Beam**)
reframes the problem instead of choosing a side: treat all data as events
aggregated over windows. An ongoing stream is unbounded data; a batch is just
a *bounded* event stream where the boundary supplies a natural window. Real-
time and batch processing run through nearly identical code in the same
system — "batch as a special case of streaming" — with incremental
[triggering](streaming-triggers-and-panes.md) as the main practical
difference. This philosophy has since spread to Flink and Spark. See
[streaming platform lineage](streaming-platform-lineage-millwheel-to-beam.md)
for how Cloud Dataflow, Flink, and Beam developed the unified model. This is
the pattern worth reaching for today when a pipeline genuinely needs to unify
batch and streaming logic, rather than duct-taping Lambda- or Kappa-style
separate systems together; see also
[batch vs. streaming ingestion](batch-vs-streaming-ingestion.md) for when
unification is even worth the complexity.

**Why Lambda Architecture failed in practice** (beyond the abstract "two
codebases" complaint): users underestimated failure impact and were shocked
when 10%+ of records were lost or duplicated on bad days — without a full
[accuracy guarantee](streaming-accuracy-vs-completeness.md), "anything is
possible." The batch and streaming pipelines often used different data
semantics, making comparable results harder than expected. Streaming results
diverged from daily batch results by an uncertain, randomly changing amount,
so users stopped trusting the streaming view and waited for batch — defeating
low latency. Lambda by design cannot deliver low-latency *correct* results;
[exactly-once streaming](delivery-guarantees-exactly-once-vs-at-least-once.md)
with event-time tooling removes the need for the parallel batch correction
path for many workloads.

A well-designed streaming system is a strict superset of batch functionality
(modulo efficiency): batch is
[bounded data](bounded-vs-unbounded-data.md) as a special case of streaming.
Beating batch on efficiency alone requires incorporating batch-style shuffle
and bundling optimizations into an unbounded-data engine — a design choice,
not an inherent streaming limitation.
