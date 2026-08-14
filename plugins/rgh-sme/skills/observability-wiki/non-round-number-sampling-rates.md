---
type: concept
title: Use Non-Round Sampling Rates
description: Statistical profiling should sample at a prime or otherwise non-round frequency (49 Hz, 99 Hz, 997 Hz) rather than a round one (100 Hz, 1000 Hz), to avoid lockstep phase alignment with periodic timer ticks or batch routines that would systematically bias the samples.
sources:
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 4"
  - title: Systems Performance, 2nd Edition
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 13"
---

Statistical sampling (see [profiling](fixed-counters-vs-profiling-vs-tracing.md)) periodically observes execution state at a target frequency. If that frequency shares a common factor with some periodic activity in the system — a timer tick, a batch job's cycle, a garbage-collection interval — the sampler can fall into lockstep with it, repeatedly sampling at the same phase of the periodic activity and producing a systematically biased picture rather than a representative one.

The fix is cheap: pick a prime or otherwise non-round sampling frequency (e.g. 49 Hz or 99 Hz instead of 50 Hz or 100 Hz; 997 Hz instead of 1000 Hz). In production profiling with tools like `perf`, keeping the rate at 49–99 Hz also keeps overhead below roughly 1% CPU; frequencies above 1000 Hz are best avoided in production for cost reasons alone, independent of the lockstep concern.
