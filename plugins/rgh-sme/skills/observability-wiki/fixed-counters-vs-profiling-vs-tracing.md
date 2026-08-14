---
type: concept
title: Fixed Counters vs. Profiling vs. Tracing
description: Fixed counters, statistical profiling, and event tracing are the three fundamental ways to collect low-level system data, and they trade off overhead against completeness in three different ways.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 4"
---

Three fundamentally different ways to observe what a system is doing, each with a different overhead/completeness trade-off:

- **Fixed counters** — kernel-maintained integers incremented on events (packets transmitted, bytes written, page faults, CPU ticks). Reading accumulated state from kernel memory interfaces (`/proc`, `/sys`) has virtually zero overhead, but it only gives aggregated, time-averaged summaries — no event distributions, latencies, or per-event context.
- **Profiling (statistical sampling)** — periodically sample execution state (e.g. the CPU instruction pointer and stack trace at 99 Hz, or on a hardware-counter threshold overflow). Overhead is predictable and bounded by the sampling frequency regardless of overall transaction volume. Good for finding CPU hot spots, call hierarchies, and building [flame graphs](cpu-flame-graphs.md). This is the "profiles" telemetry type; see [continuous profiling](continuous-profiling.md) for running it always-on rather than just during incidents.
- **Tracing (event instrumentation)** — record data on every occurrence of a targeted event (syscall entry/exit, block I/O dispatch, function call). Overhead is proportional to event rate — instrumenting a very high-frequency event (e.g. every memory allocation, >500,000/sec) can introduce severe overhead unless aggregated in-kernel (see [in-kernel aggregation over event streaming](in-kernel-aggregation-over-event-streaming.md)). Best for latency outlier detection, parameter inspection, and rare-event debugging.

The general rule: the more fine-grained and complete the data (tracing), the higher the potential overhead; the cheaper the collection (fixed counters), the less it tells you about any individual event. [Profiling and tracing are complementary](profiling-vs-tracing-complementary.md) rather than substitutes for each other — tracing finds *which* call is anomalous at the request level, profiling finds *why* at the function level.
