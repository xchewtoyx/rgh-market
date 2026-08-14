---
type: concept
title: Allowed Lateness Horizon
description: >
  How long a streaming pipeline retains window state and still processes late
  records after the watermark passes a window's end, bounding state cost under
  heuristic watermarks.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 2"
---

Under **heuristic watermarks**, late data can arrive after the on-time pane
fires. An **allowed lateness horizon** bounds how late (relative to the
watermark) a record may still be processed; data beyond the horizon is
dropped. This simultaneously:

1. Determines how long window state must be kept (until the watermark exceeds
   the window's lateness horizon).
2. Lets the pipeline discard hopelessly late records without wasted processing.

**Low vs. high watermarks:** The Streaming Systems model uses **low
watermarks** — pessimistically tracking the oldest unprocessed record's event
time. Low watermarks remain correct regardless of how large event-time skew
grows. **High watermarks** (e.g., Spark Structured Streaming's usage) track
the newest known record optimistically; lateness is handled by garbage-
collecting windows older than (high watermark − user threshold). High-
watermark schemes work when skew stays within a roughly constant delta but
discard data more readily when skew spikes.

Specify the horizon in the **event-time domain**, not processing time. A
processing-time horizon (e.g., "10 minutes after watermark passes window
end") is vulnerable to pipeline stalls — worker crashes could cause windows
to miss their legitimate late-data window even though no actual lateness
occurred.

**Caveats:**

- With **perfect watermarks**, allowed lateness of zero is optimal — no late
  data is possible.
- **Global aggregates over a bounded keyspace** (e.g., total visits by browser
  family over all time) may not need a lateness horizon at all, since active
  windows are inherently bounded by the small keyspace.

Allowed lateness is the completeness knob paired with
[streaming accuracy](streaming-accuracy-vs-completeness.md): records dropped
beyond the horizon are a deliberate completeness trade-off, not an accuracy
failure for in-time records.
