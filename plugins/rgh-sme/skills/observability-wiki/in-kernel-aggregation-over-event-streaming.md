---
type: concept
title: Aggregate at the Source Instead of Streaming Raw Events
description: When an event fires too frequently to log individually, aggregate it into counts/histograms at the point of collection and only transmit the summary, rather than streaming every raw occurrence downstream.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 14"
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 15"
---

High-frequency events (memory allocations, spinlock acquisitions, block I/O completions) can exceed hundreds of thousands of occurrences per second. [Tracing](fixed-counters-vs-profiling-vs-tracing.md) every one of them individually — writing a log record per event and streaming it to a collector — introduces overhead proportional to the event rate and can dominate the cost of the very thing being measured.

The alternative is to aggregate *at the point of collection*, before anything leaves the source, and ship only the resulting summary:

- Linux's Ftrace supports **histogram triggers** that aggregate event frequencies or latencies directly into an in-kernel memory histogram, without ever writing a per-event log line.
- eBPF programs use **BPF maps** (hashtables, arrays, LRU maps) to compute running statistics — counts, latency histograms — inside the kernel; user space reads only the final aggregated map when the tool exits or on a periodic flush interval, never the underlying stream of raw events.

This is a general instrumentation pattern, not specific to kernel tracing: whenever a signal is high-[cardinality](cardinality.md) *and* high-frequency, decide at collection time whether you need every raw event (worth the cost for rare/anomalous cases) or just the aggregate shape (cheap, sufficient for routine monitoring). It's the same trade-off that motivates [sampling strategies](sampling-rate-selection-strategies.md) and pre-aggregated [metrics](metric-anatomy.md) more generally — the difference here is that the aggregation happens at the collection point itself rather than at a downstream pipeline stage.
