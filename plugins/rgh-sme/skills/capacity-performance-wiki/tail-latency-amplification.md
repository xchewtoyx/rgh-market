---
type: concept
title: Tail Latency Amplification
description: In fan-out call chains, a single end-user request's latency is dictated by the slowest of its parallel backend calls, so tail latency compounds with the number of calls fanned out.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §8 (evaluation)"
---

**Tail latency amplification** occurs when serving a single end-user request requires making multiple backend calls in parallel (a fan-out), and the request cannot complete until *all* of those calls return. The overall request latency is therefore dictated by the **slowest** of the parallel calls, not their average.

## Why It Compounds

Even if each individual backend call has a well-behaved latency distribution (say, p99 = 1% chance of being slow), the probability that *at least one* of $N$ parallel calls hits its tail grows with $N$:

$$P(\text{at least one slow call}) = 1 - (1 - p)^N$$

For a call with a 1% chance of being slow ($p = 0.01$) fanned out to 100 backends, the probability that the overall request is slow is $1 - 0.99^{100} \approx 63\%$ — a rare individual-call event becomes the *typical* outcome for the aggregate request. The more backends a request fans out to, the more its latency profile is pulled toward the tail of the slowest individual dependency, not the median.

## Consequences for Latency Budgets

This is why a [latency budget](throughput-vs-latency-tradeoff.md) allocated across a call chain must account for fan-out width, not just chain depth: a request that fans out wide needs each dependency's tail (not its median or mean) to be tight, because any one dependency's tail event becomes the whole request's latency. Widening fan-out to parallelize work can reduce average latency while simultaneously making p99+ latency worse, if the added parallel calls each carry their own tail-event risk.

## Mitigations

*   **Hedged requests:** issue a duplicate request to a backup replica if the primary hasn't responded within some threshold (e.g., p95), taking whichever response returns first — trades some extra load for a bounded worst case.
*   **Bounding fan-out width:** reduce the number of parallel calls a single request depends on, e.g., via the kind of hybrid strategy described in [fan-out-on-write vs. fan-out-on-read](fan-out-on-write-vs-fan-out-on-read.md), so fewer dependencies can each contribute a tail event.
*   **Per-dependency latency SLOs:** hold each fanned-out dependency to a tight tail latency target, since the aggregate request's tail is bounded below by the worst dependency's tail.

## A Second Cause: Fleet Size Alone, Without Fan-Out

Fan-out width is not the only thing that degrades the tail — the sheer size of the serving fleet does too, even for a workload with no per-request fan-out at all. MillWheel's own scaling benchmark ran an identical single-stage pipeline at sizes from 20 to 2,000 CPUs, scaling input proportionally: median per-record latency stayed roughly constant across that entire range, but p99 latency got significantly worse as the fleet grew, on the reasoning that more machines means more independent opportunities for something (a GC pause, a scheduling hiccup, a slow disk) to go wrong somewhere in the fleet at any given moment. This is the same "more independent chances to hit an outlier" mechanism as fan-out amplification, but the population being sampled from is the fleet over time rather than the parallel calls of one request — so it degrades the tail even for workloads with fan-out width of one. It means p99+ SLOs should be expected to get harder to hold, not easier, purely as a side effect of scaling a fleet out to handle more load, independent of any application-level fan-out.

## Code-Level Analogue

The same compounding-from-many-small-additions pattern occurs one level down, inside a single hot code path rather than across a fan-out call chain: see [critical path redesign](critical-path-redesign.md) for how accumulated special-case checks on a critical path tax the common case in the same way that accumulated fanned-out dependencies tax the aggregate request.

## Related Measurement Pitfalls

Correctly reasoning about tail latency amplification depends on measuring the tail accurately in the first place — see [latency percentiles vs. mean](latency-percentiles-vs-mean.md) for why averages hide this effect entirely, and [coordinated omission](coordinated-omission.md) for a common load-testing mistake that undercounts exactly this kind of tail event.
