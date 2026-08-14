---
type: concept
title: Trace Anatomy and Spans
description: A trace is a tree of spans, each representing one step of a request's journey; a span needs five required fields — trace ID, span ID, parent ID, timestamp, and duration — to reconstruct the hierarchy and timing of the whole request.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
---

A **trace** represents the end-to-end journey of one transaction across services, composed of **spans** — individual steps — which nest as parent/child. Five fields are required on every span to reconstruct this structure:

- **Trace ID** — shared across every span belonging to the same request.
- **Span ID** — unique to this span.
- **Parent ID** — defines nesting; absent on the root span.
- **Timestamp** — when the span started.
- **Duration** — how long the span took.

Useful additions beyond the required fields: service name, span name, and span attributes (arbitrary key-values, structurally the same as a [structured log line](structured-logging.md)). A trace query over `WHERE trace.parent_id IS NULL` finds root spans; filtering by `trace.trace_id` assembles a full waterfall for one request.

Tracing is fundamentally logs (structured events) plus [context propagation](context-propagation.md) (passing the trace/span IDs across boundaries) plus this parent/child hierarchy — not a separate, unrelated telemetry primitive. See [deciding whether to create a span](deciding-whether-to-create-a-span.md) for when a piece of work deserves its own span versus being recorded as an attribute, and [timings as attributes, not child spans](timings-as-attributes-not-child-spans.md) for the most common instrumentation mistake with this structure. Because a span mixes structural fields (trace/span/parent id, timestamp, duration) with free-form application annotations, tracing infrastructure typically needs to [cap per-span annotation volume](annotation-volume-cap-protects-structural-span-data.md) so the former can never be crowded out by the latter.

Because each span's timestamp comes from its own host's wall clock, cross-host [clock skew can distort the reconstructed timeline](clock-skew-in-distributed-trace-timelines.md) even when causality and context propagation are both correct. Within a single span, [duration should come from a monotonic clock rather than wall-clock subtraction](monotonic-clock-for-duration-measurement.md), so an NTP correction mid-span can't produce a negative or corrupted duration.
