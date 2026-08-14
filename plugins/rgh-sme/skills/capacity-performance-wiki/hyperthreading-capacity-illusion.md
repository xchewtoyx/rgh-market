---
type: concept
title: Hyperthreading Capacity Illusion
description: A hyperthreaded core presenting as two logical processors does not deliver two physical cores' worth of throughput, and treating it as such in a capacity model overstates available capacity and produces an early, unexplained saturation point.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 7"
---

Simultaneous multithreading / hyperthreading exposes each physical core as two (or more) logical processors to the OS and to performance tools, by duplicating a small amount of register state so a second instruction stream can use execution cycles the first stream leaves idle. Capacity models that count these logical processors as if they were independent physical cores systematically overstate available capacity — a phenomenon nicknamed the **"Missing MIPS"** problem: measured throughput saturates well before the logical processor count would predict, and elapsed time rises faster than linear (super-linear) once concurrency exceeds the number of *physical* execution units, not the number of logical ones.

## Two Ways to Frame It

*   **Hardware view (1+ε model):** one execution unit is under-utilized; a second thread lets it capture the idle cycles. Typical realistic gains are modest — often ε ≈ 0.1 to 0.5, well short of a full second core's worth of throughput (ε = 1 would mean a full doubling).
*   **Software/tooling view (2−δ model):** the OS and most performance tools see two full logical processors and assume 2x capacity is available. Since δ = 1 − ε and realistic ε is well under 1, δ is typically large — meaning a large fraction of the "second processor" that tools report is not real, additional capacity.

Both framings describe the same underlying reality; the practical trap is that dashboards and capacity tools default to the software view (counting logical processors), quietly assuming capacity that the hardware view says isn't really there.

## Why It Shows Up as an Abrupt Knee, Not a Smooth Discount

The effect isn't just "logical processors are worth less than physical ones" as a flat discount — it produces a distinct behavior change once concurrent work exceeds the number of hardware thread buffers a core can hold. Below that point, each request gets a free buffer and runs at normal service time; once concurrent requests exceed available buffers, the *service time itself* increases (extra internal register/cache management overhead per instruction stream), not just the queueing wait — so elapsed time rises faster than a simple queueing-theory model assuming constant service time would predict. This shows up as a "hockey-stick" jump in a throughput-vs-concurrency chart at a load level lower than the (wrong) logical-processor-count would suggest, which — without accounting for this — looks like an unexplained anomaly rather than a predictable consequence of hyperthreading internals.

## Practical Implication

Do not size thread pools, worker counts, or capacity headroom against the OS-reported logical processor count on hyperthreaded hardware without first measuring the real effective capacity per core for the actual workload — the discount varies by processor generation, vendor, and workload type (CPU-bound workloads show the effect much more clearly than I/O-bound ones). Qualifying this ratio empirically (a small controlled benchmark sweeping concurrency from below to above the physical core count) as part of hardware acceptance testing catches the gap before it becomes a production capacity surprise. See [container CPU throttling](container-cpu-throttling.md) and [CPU steal time](cpu-steal-time.md) for related cases where the OS-visible CPU accounting diverges from the CPU capacity a workload actually receives.
