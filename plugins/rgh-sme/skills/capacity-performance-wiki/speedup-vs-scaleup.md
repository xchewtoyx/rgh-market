---
type: concept
title: Speedup vs. Scaleup
description: Two distinct motivations for adding parallel processing capacity — finishing fixed work faster (speedup) versus handling proportionally more work at a fixed response time (scaleup) — that arrive at the same underlying scaling equation.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 4"
---

Adding parallel processing resources (more CPUs, more workers, more nodes) can be justified by two different goals, common to scientific and commercial computing respectively:

*   **Speedup**: the total amount of work is fixed; the goal is to reduce elapsed time by spreading that fixed work across more processors. This is the classic motivation in parallel numerical computing (e.g., finishing the same simulation faster).
*   **Scaleup**: per-user response time is held fixed; the goal is to handle proportionally more total work (more users, more transactions) as processors are added, without individual users seeing worse response times. This is the typical commercial/OLTP motivation — a business adds capacity to support more users, not to make any single user's request finish faster.

## Why They Converge on the Same Formula

Despite starting from opposite assumptions (fixed work vs. fixed response time), both scenarios derive to the identical scaling equation — [Amdahl's Law](amdahls-law.md):

$$S(p) = C(p) = \frac{p}{1 + \sigma(p-1)}$$

The underlying reason (the serial-parallel duality) is that for any integer number of processors $p$, the ratio between the serial fraction $\sigma$ and the parallelizable fraction $\pi = 1-\sigma$ is invariant under the scaling transformation each scenario applies — speedup shrinks the parallel portion by $1/p$ while holding $\sigma$ fixed, scaleup grows the serial portion by $p$ while holding $\pi$ fixed, and both transformations preserve $\sigma/\pi$.

## Scaled Speedup: Beating the Amdahl Ceiling

A third variant, **scaled speedup** (Gustafson, 1992), assumes the *parallelizable portion itself* scales with $p$ — instead of a fixed-size problem being split across more processors, the problem size grows to use the added processors (data-parallel / SPMD workloads). Under this assumption, capacity scales linearly with processor count:

$$C_{ss}(p) = \sigma + (1-\sigma)p$$

This looks like it "beats" [Amdahl's Law](amdahls-law.md)'s asymptotic ceiling, and Sandia National Laboratories reported linear scaling on scientific workloads under this model. In practice it's hard to sustain because this formula ignores interprocessor communication overhead — as $p$ grows, that overhead reintroduces exactly the kind of coherency cost that [the Universal Scalability Law](universal-scalability-law.md) accounts for and Amdahl's Law does not.

## Practical Implication

Whether a capacity question is really a speedup question or a scaleup question changes what "success" looks like: a speedup analysis asks "how much faster does a fixed job finish," while a scaleup analysis asks "how much more load can this system take before individual response times degrade." Conflating the two can lead to over-optimistic scaling projections — a workload that scales up well (handles more users at a flat response time) is not automatically one that speeds up well (finishes a fixed job faster with more processors), and vice versa.
