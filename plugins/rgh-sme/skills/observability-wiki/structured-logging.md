---
type: concept
title: Structured Logging
description: A structured log is a discrete, timestamped event parseable into key-value pairs, rather than free text — turning a set of logs into something table-like and queryable instead of something that requires regex extraction to analyze.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 4"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 5"
---

A **log** is a discrete, timestamped event. Modern practice favors **structured** logs — key-value pairs (effectively flat JSON) — over free text, because a structured log line can be filtered, grouped, and aggregated directly, while a free-text line requires regex extraction before it can be queried at all.

Turning free-text logs into structured key-value records is what makes queries tractable, and is the same underlying substrate a trace is built from: a **request ID (or trace ID) attached to every log line is the seed of distributed tracing** — tracing is, at its core, "fancy logs" (structured events) plus [context propagation](context-propagation.md) (passing IDs across process/service boundaries) plus a parent/child hierarchy between spans. Treating tracing libraries as unknowable "magic" rather than recognizing this underlying relationship fosters cargo-cult instrumentation, where spans get added without understanding what they actually encode. See [trace anatomy and spans](trace-anatomy-and-spans.md) for the specific fields that formalize this hierarchy, and [structured events as the observability substrate](structured-events-as-observability-substrate.md) for how logs, metrics, and traces are all views over the same underlying record shape.
