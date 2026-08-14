---
type: concept
title: Amdahl's Law
description: The serial (non-parallelizable) fraction of a workload caps the maximum speedup or scaleup achievable by adding processors or workers, no matter how many are added.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 4"
---

**Amdahl's Law** quantifies how much a workload's throughput can improve by adding parallel processing resources, given that some fraction of the work is inherently serial and can't be parallelized (e.g. a database lock wait, a single-threaded coordination step). It is usually credited to Gene Amdahl (1967), though the equation itself is credited to Ware (1972) — Amdahl's own paper was empirical and equation-free.

## The Equation

Let $\sigma$ ("seriality") be the fraction of a unit of work that must execute serially, $0 < \sigma < 1$. For $p$ parallel processing units:

$$S(p) = \frac{p}{1 + \sigma(p-1)}$$

This same equation describes two different scenarios, arrived at independently:

*   **Speedup** — fixed total work, more processors reduce elapsed time (the classic parallel-computing case).
*   **Scaleup** — fixed per-user response time, more processors handle proportionally more total work (the common commercial/OLTP case). See [speedup vs. scaleup](speedup-vs-scaleup.md) for the derivations and why they converge on the same formula.

## The Asymptote

As $p \to \infty$:

$$S(p) \to \sigma^{-1}$$

No matter how many processing units are added, throughput can never exceed $1/\sigma$ times the single-unit baseline. A workload with just 1% inherent seriality ($\sigma = 0.01$) has a hard ceiling of 100x, regardless of how many processors are thrown at it — the serial portion comes to dominate elapsed time as parallelism grows, which was Amdahl's actual point: a fast single processor can beat many slower ones once the serial fraction is accounted for.

## Efficiency and Recovering Seriality From Measurements

**Efficiency** is the average speedup contributed per processing unit: $E(p) = S(p)/p$. In the ideal (no-overhead) case, $1/E(p)$ grows linearly with $p$; any measured deviation from that linear growth signals lost parallelism (Karp and Flatt, 1990).

Seriality can be recovered directly from a measured speedup curve without needing to know its physical source:

$$\sigma = \frac{p/S(p) - 1}{p - 1}$$

This makes Amdahl's Law usable as a diagnostic: measure throughput at a couple of concurrency levels, solve for $\sigma$, and use it to project (or bound) throughput at other concurrency levels — without first knowing which specific lock, code path, or shared resource is causing the serialization.

## Amdahl's Law Is a Worst-Case Bound, Not an Immovable Ceiling

Amdahl's Law can be derived from a queueing-theoretic repairman model in two equivalent ways: by shrinking a fixed workload's execution time as it's split across more processors, or by adding whole, identical units of work under **synchronous** processing — where all $N$ requests must be serviced in strict, fully-serialized sequence before any can complete. That second derivation reveals something important: Amdahl's Law is exactly the queueing model's *worst-case* (synchronous) throughput bound, not some fundamental physical limit. It represents the specific case of maximal queueing at the shared serialization point. Mean/typical throughput under less synchronized conditions is provably better than this bound.

The practical corollary: since the ceiling comes specifically from synchronous, fully-serialized request handling, making request handling asynchronous is a direct way to beat it — not by eliminating contention, but by avoiding the worst-case queueing pattern that produces Amdahl's asymptote in the first place. See [asynchronous offload for capacity](asynchronous-offload-for-capacity.md) for the practical pattern this motivates.

## What Amdahl's Law Can't Explain

Amdahl's Law only accounts for contention (serialization on shared resources) — it asymptotes but never predicts throughput *decreasing* as concurrency increases. Real systems commonly show throughput rising, peaking, and then declining as load increases past a point (**retrograde throughput**), which requires a second term for coherency delay (the cost of keeping shared state consistent across processors) — see [the Universal Scalability Law](universal-scalability-law.md), which extends Amdahl's Law with exactly this term.
