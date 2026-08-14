---
type: concept
title: Batch Export Uses Both a Size and a Time Trigger
description: A telemetry exporter that batches spans/metrics/logs before sending must flush on whichever comes first — accumulated size crossing a threshold, or the oldest queued item waiting past a max delay — because either trigger alone either wastes throughput under light load or adds unbounded latency under heavy load.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 31, Request Batch"
---

Sending each telemetry record (span, log line, metric point) as its own network call pays a fixed per-request cost — connection/serialization/processing overhead — regardless of how small the payload is. Batching many records into one export call amortizes that fixed cost, which is why every serious telemetry SDK (OTel's `BatchSpanProcessor`, statsd clients, Kafka producers) batches by default rather than sending eagerly.

A batching exporter needs **two independent flush triggers**, not just one:

- **Size trigger** — flush once accumulated batch size crosses a configured threshold (e.g. Kafka's producer defaults to a 16KB batch).
- **Time trigger** — flush once the *oldest* still-queued record has waited longer than a configured max delay, regardless of whether the size threshold was reached.

The time trigger exists specifically for low-traffic periods: without it, a batch that never fills up would sit buffered indefinitely, and telemetry for anything that just happened would be invisible until enough further activity happened to fill the batch — directly undermining an observability system's job of surfacing what's happening *now*. The size trigger exists for high-traffic periods: without it, batches would only flush on a fixed timer, adding unnecessary latency and using more memory than needed for buffering during bursts.

Practical tuning notes carried over from this same trade-off in message-broker producers: batch size is empirically tuned, not maximized — batches in the megabytes range tend to show diminishing returns and can add processing overhead of their own. And a batch that fails to send as a whole (server error, connection drop) needs the same retry/backpressure handling as any other stage of a [telemetry pipeline](telemetry-pipeline-stages.md), including deciding how buffered records degrade under sustained export failure rather than being silently dropped or duplicated.
