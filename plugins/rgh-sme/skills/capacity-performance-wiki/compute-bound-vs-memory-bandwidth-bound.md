---
type: concept
title: Compute-Bound vs. Memory-Bandwidth-Bound Workloads
description: Whether a workload's completion time is limited by how much arithmetic a processor can do or by how fast data can move to it determines which resource upgrade actually helps.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 9"
---

A workload running on a processor is limited by one of two distinct ceilings:

* **Compute-bound**: time-to-complete is set by the amount of computation needed — more or faster arithmetic units directly speed it up.
* **Memory-bandwidth-bound**: time-to-complete is set by the rate data can be moved between memory and the processing units, not by how fast the processor can compute once the data arrives.

Throwing more raw compute at a memory-bandwidth-bound workload does little — the processor sits idle waiting on data regardless of how many arithmetic units it has. Throwing higher-bandwidth memory at a compute-bound workload is similarly wasted. Correctly classifying a workload is a prerequisite for picking the right remediation, the same way the [USE method](use-method.md) requires knowing which resource to check before checking it.

## Terminology Ambiguity

"Memory-bound" is used two different ways in practice, and the ambiguity matters:

* **Memory-bandwidth-bound** (the sense used throughout this note): limited by data transfer *rate*.
* **Memory-capacity-bound**: limited by insufficient memory *size* (out-of-memory errors), typically worked around by splitting a task's data across multiple memory pools (e.g., across a GPU's and CPU's separate memory). That workaround itself introduces additional data-transfer time between the pools — so a capacity limitation, once worked around, becomes a bandwidth limitation underneath. People with a systems background tend to default "memory-bound" to the bandwidth sense; people with an application/ML background tend to default it to the capacity sense. State which one you mean when it isn't obvious from context.

## Diagnosing Which Bound Applies: Arithmetic Intensity

Whether a workload is compute-bound or memory-bandwidth-bound is a computable property, not a guess: **arithmetic intensity** is the ratio of arithmetic operations performed to bytes of memory accessed. A **roofline chart** plots achievable performance against arithmetic intensity to show, for a given piece of hardware, at what intensity a workload crosses from being memory-bandwidth-limited to compute-limited (the "roofline" paper: Williams et al., 2009). Profiling tools (e.g., NVIDIA Nsight) can generate this chart directly from a running workload.

The two bounds call for different remediation:

* Compute-bound workloads benefit from more processing units or higher-FLOP/s hardware.
* Memory-bandwidth-bound workloads benefit from higher-bandwidth memory, not more raw compute.

## Worked Example: LLM Inference's Two Phases

Autoregressive language model inference has two computationally distinct steps, and they land on opposite sides of this classification:

* **Prefill**: the model processes all input tokens in parallel in one pass. Throughput is limited by how many operations the hardware can do per unit time — **compute-bound**.
* **Decode**: the model generates one output token at a time, reloading large weight matrices into the processor on every single step. Throughput is limited by how fast that data can be loaded — **memory-bandwidth-bound**.

Because the two phases have opposite bottlenecks, running them on the same hardware makes them compete inefficiently: a processor near its compute ceiling on existing decode work can still absorb another memory-bandwidth-bound decode job, but adding a *new* request also means running its prefill (compute-bound) alongside the existing decode jobs, which drains the compute those decode jobs weren't contending for and slows all of them down.

Production inference systems commonly resolve this by **disaggregating** prefill and decode onto physically separate instances — a phase-level instance of the same functional-partitioning idea covered in [horizontal vs. vertical scaling](horizontal-vs-vertical-scaling.md) (splitting a workload by *what* it does onto independently-scaled pools, here applied to *which phase of a pipeline* rather than *which service*). Published results (DistServe, Zhong et al. 2024; "Inference Without Interference," Hu et al. 2024) report this significantly improves processed-request volume under a fixed latency constraint, and that the overhead of transferring intermediate state between the two pools is small on modern high-bandwidth interconnects. The right ratio of compute-phase to bandwidth-phase instances is workload-dependent: longer inputs need proportionally more of the compute-bound phase's capacity; which latency metric is prioritized also shifts the ratio (see [latency: first-unit cost vs. per-unit rate](latency-first-unit-vs-per-unit-rate.md) for how that latency trade-off is structured).

Long-context workloads in particular tend to push decode toward memory-bandwidth-bound more strongly (more cached state to reload per step); as accelerator hardware and inference software evolve, the balance across many real workloads may shift further toward compute-bound over time.

## Selecting Hardware for a Workload's Bottleneck

Once a workload is classified, hardware selection becomes a direct match: compute-bound workloads want processors with higher peak FLOP/s; memory-bandwidth-bound workloads want higher memory bandwidth (and enough capacity to avoid the capacity-bound trap above), not simply "more compute." Cost is comparatively straightforward once feasibility and speed are settled — usage-based cloud pricing is fairly comparable across providers, or computable from purchase price plus ongoing power draw for owned hardware (see [energy as a capacity resource](energy-as-a-capacity-resource.md) for how to account for that power draw).

## Relation to Other Bottleneck Signals

This is a workload-level, hardware-agnostic classification. It complements narrower, hardware-specific signals that reveal the same kind of split closer to the metal — see [instructions per cycle](instructions-per-cycle.md) for how a CPU's own stall-cycle profile reveals whether *it* is compute-bound or waiting on memory, and see the utilization pitfall in [the USE method](use-method.md) for why a resource reporting "100% busy" can still be far below its achievable throughput on either side of this classification.
