---
type: concept
title: Synchronous vs. Asynchronous Ingestion Coupling
description: >
  Whether pipeline stages must finish in strict sequence before the next can
  start, versus each event flowing through independently with a buffer
  absorbing rate spikes.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

**Synchronous ingestion** chains source, ingestion, and destination with
strict sequential dependencies — step A must finish before step B, B before
C. This is common in older ETL systems, and its failure mode is severe: if
any step fails, the whole run typically has to restart from the beginning.
A real-world case: a transformation pipeline built as dozens of tightly
coupled synchronous steps took over 24 hours end to end, and a single
failure meant a full restart with poor error messages, turning diagnosis
into a multi-day ordeal that left the business without updated reports the
entire time — the same [blast-radius](pipeline-granularity-and-blast-radius.md)
problem that oversized batch jobs create in general, here caused by
coupling rather than sheer job size.

**Asynchronous ingestion** operates at the individual-event level, similar
to a microservice backend: each event becomes available downstream as soon
as it individually finishes its own step, and later stages process items as
they arrive rather than waiting for a whole batch to complete. A typical
architecture chains an upstream buffer (e.g., a Kinesis or Kafka stream)
between stages, which acts as a **shock absorber** — it moderates load so a
rate spike doesn't overwhelm the next stage, and any backlog that does build
up clears itself once the event rate falls, rather than requiring a full
pipeline restart.

The practical choice is a trade-off between simplicity (synchronous chains
are easier to reason about linearly) and resilience (asynchronous stages
with buffering isolate failures and absorb bursts) — see also
[idempotent and replayable jobs](idempotent-and-replayable-jobs.md), which is
what makes it safe for an asynchronous stage to reprocess events after a
partial failure without restarting everything upstream of it.
