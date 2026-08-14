---
type: concept
title: LLM Token and Cost Metrics
description: Track query count, input/output token volume, and tokens-per-second as first-class telemetry for LLM applications, since these double as both cost and latency proxies and as an early-warning signal for hitting provider rate limits.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Cost in an LLM application is driven almost entirely by token volume, which makes token/cost telemetry a distinct category worth tracking deliberately rather than deriving after the fact from a vendor invoice:

- **Query count** and **input/output token volume**, tracked per request so cost is attributable to the request that caused it (see [LLM request and configuration logging](llm-request-and-config-logging.md) for the accompanying request-level context).
- **Tokens per second (TPS)** as service-wide throughput — and, when useful, **tokens/s/user** to see how that rate scales as concurrency grows. Because prefill and decode are computationally distinct (and often decoupled onto separate machines), count **input and output throughput separately**; unqualified "throughput" in inference literature usually means output tokens. Direct TPS comparisons across models are only approximate — tokenizers differ — so **cost per request** (or per 1K requests) is often the fairer cross-model comparison.
- **Completed-request rate**: RPS works for short traditional requests, but foundation-model calls often take seconds, so **RPM (requests/minute)** is frequently the more readable concurrency signal. Track it against the provider's published rate limits as a leading indicator — crossing a limit causes service interruption, so the rate needs to be watched proactively rather than discovered via failed requests.

Throughput ties directly to compute cost. Rough conversion: if compute costs $2/h and the service sustains 100 output tokens/s, that is about $5.56 per 1M output tokens; prefill cost is computed the same way from request-prefill rate; total cost/request = prefill + decode. Smaller models and higher-end chips raise achievable TPS; consistent-length workloads are easier to optimize than variable-length ones. Pair these volume rates with [TTFT/TPOT latency histograms](llm-inference-latency-metrics.md) and judge them under a latency budget via [LLM inference goodput](llm-inference-goodput.md) — raw TPS can rise while UX fails. For whether the hardware itself is being used efficiently (as opposed to how many tokens you sold), see [MFU and MBU](model-flop-and-bandwidth-utilization.md).

Length-related metrics double as latency/cost proxies: a longer context or a longer generated response drives both higher latency and higher cost, so the same length measurement answers two different questions depending on which axis you're investigating. As with any other numeric measurement, choose the metric type (counter for volume, gauge for a live rate) per [metric anatomy and types](metric-anatomy.md).
