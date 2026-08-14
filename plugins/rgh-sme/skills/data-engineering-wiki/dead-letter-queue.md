---
type: concept
title: Dead-Letter Queue
description: >
  Rerouting events that fail ingestion to a separate quarantine queue instead
  of blocking or discarding the rest of the flow, so they can be diagnosed
  and reprocessed later.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 7"
---

When an event fails ingestion — a message on an unrecognized topic, an
oversized payload, a schema violation, an expired TTL — the pipeline reroutes
it to a dead-letter queue rather than blocking the main flow of otherwise-good
events or silently dropping the failure. This is the streaming-ingestion
instance of a general
[data quality](data-quality-dimensions.md) quarantine pattern: isolate the
bad record so it can't corrupt or stall processing of everything else, while
keeping it around for diagnosis.

A dead-letter queue only earns its keep if something actually consumes it:
the point is to let engineers investigate root cause and, once the
underlying issue is fixed (a [schema registry](schema-registry.md)
incompatibility resolved, a size limit raised, a bug patched), reprocess the
quarantined messages back through the pipeline rather than losing them. A
dead-letter queue nobody monitors is functionally the same as silently
dropping failed events — it just delays discovering that the failures were
ever happening.
