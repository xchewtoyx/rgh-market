---
type: concept
title: Streaming Accuracy vs. Completeness
description: >
  Why exactly-once delivery guarantees correctness of what was processed but
  not whether all expected data arrived, and how pipelines configure the
  completeness knob separately.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 6"
---

**Accuracy** in a streaming pipeline means no record is silently dropped or
duplicated — every in-time record is processed exactly once. **Completeness**
means the pipeline waited long enough to see all records it should before
closing a window or emitting a final result. These are independent axes:
a pipeline can be perfectly accurate while deliberately incomplete.

Exactly-once processing (see
[delivery guarantees](delivery-guarantees-exactly-once-vs-at-least-once.md))
addresses accuracy only. How long to wait for
[late-arriving data](late-arriving-data.md) — via watermarks, triggers, and
an [allowed-lateness horizon](allowed-lateness-horizon.md) — is the
completeness decision. Records arriving after that horizon are dropped by
policy; that is not an accuracy failure because every record processed
in-time still counted exactly once.

Batch pipelines exhibit the same split under a different name: a job that
runs at 2 AM over "yesterday's data" is accurate for the slice it processed
but not complete relative to records that landed after 2 AM. Treating
completeness as a configurable optimization rather than a semantic
requirement — new data arrive, old results get retracted or updated — is the
reframe that makes event-time streaming workable on unbounded, disordered
inputs.
