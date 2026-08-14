---
type: concept
title: Processing-Time Windowing Methods
description: >
  Two ways to emulate processing-time windows in an event-time-first streaming
  model, and why both are order-sensitive unlike event-time windowing.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 5"
---

**Processing-time windowing** is the right choice when analyzing the arrival
stream itself (QPS monitoring, outage detection) and the wrong choice whenever
when events actually happened matters (user behavior, billing, scoring).

In an event-time-first model (Beam), two methods emulate processing-time
windows:

1. **Triggers on a global window** — ignore event time (single global window
   spanning all event time), use aligned processing-time delay triggers with
   **discarding** [accumulation mode](streaming-accumulation-modes.md) so
   each pane acts as an independent processing-time slice.

2. **Ingress time** — overwrite each record's event time with arrival time at
   pipeline entry, then use normal event-time windowing with default watermark
   triggers. Ingress time affords a *perfect* watermark, so each window fires
   exactly once. This is essentially Spark Streaming 1.x semantics.

The methods diverge in **multistage pipelines**: with triggers, each stage
slices processing-time windows independently — a record in window N at one
stage may land in window N−1 or N+1 at the next. With ingress time, once a
record is placed in window N it stays there for the whole pipeline because
progress synchronizes across stages via watermarks (Dataflow), microbatch
boundaries (Spark Streaming), or an equivalent coordinating mechanism.

**Order sensitivity:** running the same events through different observation
orders produces identical *final* results under
[event-time windowing](streaming-window-types.md) but different results under
either processing-time method — even when underlying event data are identical.
Processing-time window contents change whenever input *observation order*
changes. If event times matter, event-time windowing is required; otherwise
results are meaningless relative to when events actually occurred.
