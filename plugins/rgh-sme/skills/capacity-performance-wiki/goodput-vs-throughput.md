---
type: concept
title: Goodput vs. Throughput
description: Raw throughput counts every completed request regardless of how slow it was, while goodput counts only the requests that met the latency SLO — a service can raise throughput while goodput falls.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

**Throughput** counts completed work per unit time — requests/second, or however the resource's output is measured — with no regard for how long any individual unit of work took to complete. **Goodput** (a term adapted from networking) counts only the subset of that throughput that meets a defined [SLO](throughput-vs-latency-tradeoff.md): requests per second that finished *and* stayed within the latency target.

## Worked Example

A service is required to keep TTFT (time to first response) under 200ms and per-unit latency under 100ms. It completes 100 requests/minute overall, but only 30 of those actually satisfy both latency bounds. Throughput is 100 req/min; **goodput is 30 req/min**. The other 70 completed, but too slowly to count as a good outcome by the service's own definition of "working."

## Why Throughput Alone Is a Misleading Optimization Target

The [throughput vs. latency trade-off](throughput-vs-latency-tradeoff.md) means that techniques which raise throughput — larger batches, higher concurrency, more aggressive queueing — routinely do so by adding latency to individual requests. Pushed far enough, that added latency pushes requests past the SLO threshold. A team optimizing purely for throughput or for reported cost-per-request can end up in a state where throughput is *rising* while goodput — the number of requests actually meeting the bar the business cares about — is *falling*. One real-world report found it not uncommon to double or triple raw throughput by sacrificing per-request latency this way, which is a win only if nothing downstream actually required that latency to stay low.

## Consequences for Capacity Planning

* **Capacity targets should be stated in goodput, not throughput**, whenever the workload has a real latency requirement — sizing to a throughput number alone silently permits an SLO-violating tuning that a throughput-only dashboard won't flag.
* **Goodput needs the same latency-distribution discipline as any other latency metric** — see [latency percentiles vs. mean](latency-percentiles-vs-mean.md) for why the SLO threshold itself must be checked against the actual response-time distribution, not an average.
* The [RED method](red-method.md)'s Duration metric is what goodput is computed *from*: goodput is the fraction of the Duration distribution that falls inside the SLO, applied to the Requests rate.
