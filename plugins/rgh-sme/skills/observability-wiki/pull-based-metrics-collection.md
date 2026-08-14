---
type: concept
title: Pull-Based Metrics Collection
description: A pull-based monitoring architecture has a central collector scrape known metrics endpoints on a schedule, rather than having each instrumented process push data outward, simplifying discovery and backpressure handling.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 10"
---

In a pull-based architecture (e.g. Google's Borgmon, or Prometheus), a monitoring daemon periodically scrapes an HTTP endpoint (conventionally `/varz` or `/metrics`) exposed by each target task, ingesting key-value metrics paired with timestamps. The collector controls its own scrape rate and load, and a target that's down simply produces a gap rather than an unbounded stream of retried pushes.

This contrasts with push-based collection, where each process sends its own metrics outward to a collector — simpler for the instrumented process, but it shifts backpressure and fan-in problems onto the receiving side and makes it harder for the collector to know whether "no data" means "healthy and quiet" or "target is down."

The scraped data typically lands in an in-memory, high-performance time-series buffer for near-real-time [alert rule evaluation](time-series-alert-rule-evaluation.md) before being persisted for longer-term querying.

The same collector-controls-the-pace idea appears for other telemetry types under a different name: [out-of-band telemetry collection](out-of-band-telemetry-collection.md) is trace data's version of this, buffering locally and letting a separate process pull from it rather than having the instrumented process push.
