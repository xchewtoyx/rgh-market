---
type: concept
title: LLM Inference Goodput
description: >
  Goodput for an LLM inference service is the rate of requests that
  satisfy a latency SLO (typically TTFT and TPOT bounds), not raw
  tokens-per-second — so optimizing throughput or cost without this
  filter can report success while UX is failing.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Inference services face a latency/throughput trade-off: batching and
related optimizations raise tokens-per-second (and lower cost per token)
but can inflate [TTFT and TPOT](llm-inference-latency-metrics.md). Teams
that optimize purely for throughput or cost therefore risk a dashboard
that looks healthy while users experience a sluggish product. LinkedIn's
AI team (2024) reported it is not uncommon to double or triple throughput
by sacrificing TTFT and TPOT.

**Goodput**, adapted from networking, is the measurement that closes that
gap: the number of requests per unit time that satisfy a stated
service-level objective on the latency axes you actually care about. If
the SLO is TTFT ≤ 200 ms and TPOT ≤ 100 ms, and the service completes
100 req/min but only 30 meet both bounds, goodput is 30 req/min — not
100. Computing it is event-level SLI math over per-request latency
fields: count requests whose recorded TTFT and TPOT (or TBT/ITL)
fall inside the bounds, then divide by the window. Setting the bound
values themselves is a reliability-policy decision; the telemetry job is
preserving the per-request latency attributes so the goodput query stays
honest under load.

Instrument goodput alongside raw
[token throughput and cost](llm-token-and-cost-metrics.md). Raw TPS
answers "how hard is the hardware working / how cheap is a token?";
goodput answers "how many of those tokens arrived under the latency
budget the product promised?" Prefer
[percentiles of the underlying latency distributions](latency-percentiles-not-averages.md)
when diagnosing *why* goodput dropped — a p99 TTFT excursion and a
uniform TPOT shift need different remedies.
