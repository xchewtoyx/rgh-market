---
type: concept
title: LSM-Tree Write Amplification and Compaction Tail Latency
description: LSM-tree storage engines rewrite the same data multiple times as background compaction merges segments, trading total disk write volume for higher sustained write throughput — but that same background work competes with foreground I/O for disk bandwidth and can spike tail latency or exhaust disk space if it falls behind.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 3"
---

An **LSM-tree** (log-structured merge-tree) storage engine writes incoming data sequentially to disk as immutable sorted segment files, then merges those segments together in the background (**compaction**) to bound how many segments a read has to check and to reclaim space from overwritten or deleted keys. Each compaction pass rewrites every key it touches, so over a key's lifetime it can be physically written to disk many times as it moves through successive rounds of merging — this is the storage-engine-level analog of [SSD write amplification](ssd-write-amplification.md), though the mechanism is different: SSD WAF comes from the flash controller's erase-block granularity, LSM-tree amplification comes from the storage engine's own compaction strategy.

## Throughput Trade-off vs. B-Trees

Despite writing more total bytes than the logical write volume, LSM-trees typically sustain **higher write throughput** than B-tree storage engines, because every LSM write is a sequential append rather than a random in-place page overwrite. B-trees have a smaller, more predictable write amplification (roughly 2x: once to the write-ahead log, once to overwrite the modified page) but pay for every one of those writes with a random disk seek; LSM-trees pay a larger, workload-dependent amplification factor but in sequential I/O, which is dramatically cheaper on both spinning disks and — despite the SSD-specific write amplification concerns above — still generally faster than random writes on flash. Which storage engine wins on throughput for a given workload depends on which cost (seek-bound randomness vs. compaction rewrite volume) dominates.

## Compaction as a Background Load Competing With Foreground I/O

Compaction runs continuously in the background while the engine keeps serving foreground reads and writes, and it consumes the same disk bandwidth those foreground operations need. Two capacity failure modes follow directly from this:

*   **Tail latency spikes:** when compaction and foreground I/O contend for disk bandwidth, foreground write (and sometimes read) latency spikes at the high percentiles (p99, p99.9) even though median latency looks fine — the same shape of problem as [SSD garbage collection stalls](ssd-write-amplification.md), but triggered by the storage engine's own merge process rather than the flash controller's.
*   **Disk space exhaustion:** if the incoming write rate sustains higher than compaction can keep up with, uncompacted segments accumulate faster than they're merged away, and disk usage grows without bound until the volume fills — a capacity failure that a throughput benchmark measured over a short window won't reveal, since it only manifests once sustained write rate has outpaced compaction for long enough. This is a reason [soak testing](capacity-test-types.md) matters specifically for LSM-backed systems: a load test that runs too briefly to let compaction fall meaningfully behind will not surface it.

## Capacity Planning Implications

*   Provision [headroom](capacity-headroom-safety-margin.md) in both disk I/O bandwidth and disk space, not just for the logical write rate but for the compaction rewrite volume that rate implies — a workload's *effective* disk I/O demand is its logical write rate multiplied by the storage engine's write amplification factor, not the logical rate alone.
*   Compaction strategy choice (size-tiered vs. leveled) changes this trade-off: leveled compaction bounds the space overhead of compaction more tightly at the cost of more total rewriting, while size-tiered compaction rewrites less overall but requires more transient disk space during merges. Neither eliminates the underlying trade-off between total rewrite volume and space overhead — it only shifts where on that curve the system sits.
