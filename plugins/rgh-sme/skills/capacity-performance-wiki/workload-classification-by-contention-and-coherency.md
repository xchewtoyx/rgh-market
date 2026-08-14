---
type: concept
title: Workload Classification by Contention and Coherency
description: A four-way taxonomy of workload types by whether they exhibit contention, coherency delay, both, or neither, used to build intuition for what a fitted Universal Scalability Law result should look like.
sources:
  - title: "Guerrilla Capacity Planning"
    resource: "Guerrilla Capacity Planning (Neil J. Gunther), ch. 6"
---

The two parameters of [the Universal Scalability Law](universal-scalability-law.md) — contention ($\sigma$/$\alpha$) and coherency ($\kappa$/$\beta$) — sort familiar workload types into four classes, useful as a sanity check on a fitted result or as a prior when no measurement exists yet:

*   **Class A — Ideal concurrency** ($\sigma = 0$, $\kappa = 0$): shared-nothing platforms with no coordination between workers, e.g. read-only text search over a sharded, replicated index. Scales linearly with essentially no ceiling from the model's perspective; a workload in this class achieving massive horizontal scale (tens of thousands of nodes) is unsurprising precisely because it avoids both contention and coherency entirely.
*   **Class B — Contention-only** ($\sigma > 0$, $\kappa = 0$): message-based queueing systems, MPI applications, transaction monitors, polling services, peer-to-peer systems. Throughput asymptotes toward a ceiling (behaves exactly like [Amdahl's Law](amdahls-law.md)) but never declines.
*   **Class C — Incoherency-only** ($\sigma = 0$, $\kappa > 0$): scientific/HPC computation, OLAP, data mining, decision-support workloads. No serialization bottleneck, but shared-state consistency costs still eventually produce a throughput peak and decline.
*   **Class D — Worst case** ($\sigma > 0$, $\kappa > 0$): anything with shared writes under concurrent access — hotel reservation systems, banking OLTP. Both a lock-wait phase (contention) and a stale-cache-refetch phase (coherency) are present in the same request path, producing the steepest retrograde throughput curve of the four classes.

## Using the Classification

Before measuring, classifying a workload by its expected class sets expectations for what a fitted curve should look like: a Class B workload with an unexpectedly large fitted $\kappa$ is a signal something outside the expected model (e.g. an unplanned shared-write hot path) is present. Conversely, a workload assumed to be Class D that fits with $\kappa \approx 0$ suggests the coherency cost was successfully engineered away (e.g., via partitioning or a cache design that avoids cross-node invalidation) even though the workload's superficial description (shared writes) would suggest otherwise.
