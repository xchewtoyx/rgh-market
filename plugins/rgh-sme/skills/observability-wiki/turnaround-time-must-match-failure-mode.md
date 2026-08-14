---
type: concept
title: Analysis Turnaround Time Must Match the Failure Mode Being Fought
description: An observability tool that's fast enough for one kind of live incident can still be useless for another, because different failure modes need fundamentally different kinds of analysis — a single slow example trace is available almost instantly, while diagnosing a sudden spike affecting a shared dependency needs bulk aggregation across many recent traces, which is a much slower operation to complete under time pressure.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §6.6"
---

Whether a telemetry tool is "fast enough" for live incident response depends on what question the failure mode actually requires answering, not just on how fresh the underlying data is:

- **Isolating one bottleneck in a single high-latency or timing-out service** typically only needs a handful of example [traces](trace-anatomy-and-spans.md) pulled live — for genuinely catastrophic failures, aggregate statistics usually aren't even necessary, a few concrete slow traces are enough to see where time is going.
- **A sudden spike hitting a shared dependency** (e.g. a shared storage service suddenly under load from many unrelated callers) needs the opposite: aggregated data across many recent requests, because the question ("who's driving this spike," "is this systemic or one bad tenant") can't be answered from any single request's trace — see [attributing shared-service load back to callers](attributing-shared-service-load-to-callers.md). That aggregation is a bulk computation, not a lookup, and it has its own turnaround time separate from how quickly individual traces reach storage.

The practical implication: when evaluating (or building) an observability tool for incident response, the meaningful freshness requirement is "how fast can this specific kind of question be answered," not a single global latency number. Google found that for shared-service incidents specifically, aggregated analysis needed to complete within roughly 10 minutes of an event's onset to be genuinely useful for firefighting — falling short of that turnaround left the tool much less valuable for that failure mode even though it was already fast enough for single-service bottleneck isolation. Design and capacity-plan the aggregation path for a pipeline's worst-case incident use, not just its steady-state analytical use.
