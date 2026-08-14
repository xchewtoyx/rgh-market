---
type: concept
title: "Latency Decomposition: First-Unit Cost vs. Per-Unit Rate"
description: For workloads that produce output incrementally, total latency splits into a fixed cost to produce the first unit plus a per-unit rate multiplied by how many units follow, and the two halves trade against each other.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

Any workload that produces its output incrementally — streamed tokens, paginated results, chunked file transfer, progressively rendered results — has a total latency that decomposes into two components with different causes:

$$\text{Total latency} = \text{first-unit cost} + \text{per-unit rate} \times \text{(number of units} - 1)$$

* **First-unit cost**: the fixed delay before *any* output is visible — everything the system must do up front (parsing the request, initial lookups or computation) before it can emit the first unit.
* **Per-unit rate**: the steady-state marginal cost of producing each subsequent unit once output has started flowing.

## Why the Split Matters More Than the Total

Two systems with identical total latency can feel completely different to a user depending on how that total splits between the two components — one with a long first-unit delay followed by fast steady output, versus one that starts responding almost instantly but delivers each subsequent unit more slowly. Which trade-off users actually prefer is an empirical UX question, not something derivable from the total alone, so it needs to be measured rather than assumed.

## Worked Example: LLM Token Streaming

Streaming LLM responses name these two components explicitly:

* **TTFT (time to first token)** — the first-unit cost; corresponds to the prefill computation and scales with input length.
* **TPOT (time per output token)** — the per-unit rate for every token after the first. In streaming mode, TPOT only needs to outrun human reading speed, not be minimized outright — roughly 120ms/token (6–8 tokens/second) matches a fast reader's pace, so pushing TPOT much lower than that buys little perceived benefit.

Total latency = TTFT + TPOT × (output length − 1). Because TTFT corresponds to a [compute-bound phase and TPOT to a memory-bandwidth-bound phase](compute-bound-vs-memory-bandwidth-bound.md) in this particular workload, the trade-off between the two isn't just a UX choice — it maps directly onto how compute is physically partitioned between the two phases' resource pools. Shifting instances from one pool to the other is a concrete lever for trading TTFT against TPOT.

## Practical Implication for Latency Budgets

A single blended [latency budget](throughput-vs-latency-tradeoff.md) or SLO for an incrementally-produced response hides which component is actually the target. Deciding explicitly whether the SLO binds on first-unit latency, on total completion latency, or on both separately determines where engineering effort should go — optimizing the wrong half of the split (e.g., chasing a faster per-unit rate when users are actually latency-sensitive to the first unit) wastes effort. See [goodput vs. throughput](goodput-vs-throughput.md) for how an SLO defined this way then gets applied to a capacity target.

## A Measurement Caveat

What a *user* perceives as the first unit can differ from what the *system* internally produces first — in agentic or multi-step flows, the system may generate hidden intermediate output (a plan, a tool call) before anything is shown, so the model's true first output and the user-visible first output are different events. When this distinction matters, measure and name them separately (e.g., "time to publish" for the user-visible one) rather than conflating them under one first-unit metric.
