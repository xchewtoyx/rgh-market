---
type: concept
title: LLM Inference Latency Metrics (TTFT, TPOT, TBT/ITL)
description: >
  Autoregressive LLM latency must be instrumented as TTFT, TPOT (or
  TBT/ITL), and their combination — not a single end-to-end duration —
  because prefill and decode have different computational profiles and
  the same total latency can feel very different depending on the split.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

From a user's perspective the central axis of an inference service is
latency (response quality is a property of the model, not the service).
For autoregressive language models that latency is not one number: the
prefill step (processing input tokens in parallel, typically
compute-bound) and the decode step (emitting one token at a time,
typically memory-bandwidth-bound) have different profiles, so production
instrumentation records them separately.

- **TTFT (time to first token)** — time from query arrival to the first
  output token; corresponds to prefill duration and grows with input
  length. Chatbots want near-instant TTFT; long-document summarization
  tolerates more.
- **TPOT (time per output token)** — average speed of subsequent token
  generation. In streaming mode, TPOT should be faster than human reading
  (~120 ms/token for a fast reader) but need not be dramatically faster.
- **TBT (time between tokens)** / **ITL (inter-token latency)** —
  per-interval variants of the same idea (TBT used by LinkedIn, ITL by
  NVIDIA); useful when you need the distribution of gaps rather than a
  single average.

Total latency ≈ TTFT + TPOT × (number of output tokens). Two apps with
equal total latency can feel different depending on the TTFT/TPOT split —
instant first token with a slower stream versus a slightly delayed but
faster stream — so the preferred trade-off is an empirical UX question,
not something a single end-to-end histogram can answer. Shifting compute
between prefill and decode machines (or instances) trades TTFT for TPOT
and vice versa; instrumentation that only reports wall-clock completion
time cannot see that trade.

**Time to publish vs. model-internal first token.** User-observed TTFT
can diverge from what the model experiences. In chain-of-thought or
agentic flows, intermediate tokens (plans, tool-call scaffolding) are
generated but not shown; the model's "first token" happened in a hidden
earlier step. Some teams name the user-visible metric **time to publish**
explicitly so dashboards and SLOs do not silently mix the two. Capture
both when intermediate steps are hidden — and keep the intermediate
outputs in [LLM request and configuration logging](llm-request-and-config-logging.md)
so you can reconstruct which step owned the delay.

Record TTFT and TPOT/TBT as [histogram metrics](metric-anatomy.md) and
query [percentiles, not averages](latency-percentiles-not-averages.md): a
single multi-second outlier among otherwise fast requests pulls a mean
far above the typical experience, usually from network errors or unusually
long prompts, and is worth investigating as its own cohort. Plotting TTFT
against input length is a useful diagnostic for whether prefill cost is
behaving as expected. Pair these latency series with
[token/cost throughput](llm-token-and-cost-metrics.md) and judge
throughput against latency via [LLM inference goodput](llm-inference-goodput.md)
rather than raw tokens-per-second alone.
