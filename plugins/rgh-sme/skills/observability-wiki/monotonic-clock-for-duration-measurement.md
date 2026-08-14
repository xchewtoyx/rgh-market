---
type: concept
title: Measure Durations with a Monotonic Clock, Not Wall Time
description: A span or timer's duration should be computed from a monotonic clock (elapsed-time-only, never adjusted) rather than by subtracting two wall-clock readings, because NTP corrections or leap seconds can make wall time jump backward mid-measurement and produce a negative or nonsensical duration.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Unmesh Joshi), ch. 26, Lease"
---

Two different clock sources answer two different questions, and instrumentation code frequently reaches for the wrong one:

- **Wall clock** (e.g. `System.currentTimeMillis()`) reports calendar/real-world time, kept roughly correct by periodic NTP correction — which means it can jump backward between two successive reads on the same machine. It's the right source for a span's *start timestamp*, which needs to mean something in real-world time (and is the field affected by [cross-host clock skew](clock-skew-in-distributed-trace-timelines.md)).
- **Monotonic clock** (e.g. `System.nanoTime()`) reports elapsed time only, is unaffected by NTP or timezone changes, and is guaranteed non-decreasing on a single machine — but two monotonic readings taken on *different* machines are meaningless to compare.

A **duration** — how long a span, timer, or operation took — should always be computed as the difference between two monotonic-clock readings taken on the same machine, never as `end_wall_time - start_wall_time`. If the wall clock is corrected backward by even a few milliseconds during the measured operation, a wall-clock-based duration calculation can go negative or otherwise nonsensical, and that garbage value then propagates into every downstream percentile calculation, dashboard, and alert built on that instrumentation. This is purely a within-process concern — it does not require or benefit from cluster-wide clock synchronization, since the two readings never leave the one machine.

Practical check when reviewing or writing instrumentation: if a language runtime or SDK exposes distinct monotonic and wall-clock APIs (most do — Java's `nanoTime()` vs. `currentTimeMillis()`, Go's `time.Since()` vs. `time.Now()`, Python's `time.monotonic()` vs. `time.time()`), duration/latency measurement code should use the monotonic one; only the emitted start timestamp (for correlating with other telemetry) should use wall time.
