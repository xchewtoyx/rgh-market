---
type: concept
title: Cache Replacement Algorithms
description: Which entry a full cache evicts to make room for a new one should match the workload's actual access pattern — recency-based, frequency-based, and hybrid policies each protect a hit ratio against a different kind of traffic.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 5"
  - title: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale"
    resource: "MillWheel: Fault-Tolerant Stream Processing at Internet Scale (Akidau et al.), §8.3 (framework-level caching)"
---

When a cache is full and a miss needs to make room for a new entry, which existing entry gets evicted determines how well the cache's [hit ratio](cache-hit-ratio-economics.md) holds up under real traffic — and the right policy depends on what kind of access pattern the cache actually sees.

*   **LRU (Least Recently Used):** evicts whichever entry was accessed longest ago. Effective when access has strong short-term repetition — an entry hit recently is likely to be hit again soon (e.g. DNS caching, where a rarely-hit typo domain naturally ages out on its own).
*   **LFU (Least Frequently Used):** evicts whichever entry has the lowest access *count*, tracked over all time or over a rolling window. Effective when raw popularity, not recency, predicts future access — a video that gets sustained heavy repeat viewing should survive even a temporary lull, which pure recency-based eviction wouldn't protect.
*   **ARC (Adaptive Replacement Cache):** solves a specific failure mode both LRU and LFU are vulnerable to — a sudden flood of one-off, low-value reads (the canonical case: a full-table backup scan reading every record exactly once) flushing a cache's genuinely useful working set with junk that will never be accessed again. ARC places newly cached entries in a **probationary** pool and only promotes an entry to the protected main cache on a *second* access — so a single sequential scan only ever churns through the probationary pool, leaving the real working set in the main cache untouched.

*   **Custom, trigger-aware eviction:** LRU, LFU, and ARC all assume that recency or frequency of *past* access predicts future access. Some workloads invert that assumption — data is written once, buffered, and its one read is triggered by an external condition rather than by request traffic (e.g., a stream-processing framework that buffers records in storage until a windowing timer or watermark passes, then fetches them for aggregation). Under this pattern the most recently written row is the one *least* likely to be read soon, which is the opposite of what LRU predicts — a generic recency- or frequency-based policy actively evicts the wrong entries. The fix is a cache that is told (not inferring) how the data will be used, evicting based on the same trigger condition (e.g., watermark position) that determines when a read will actually happen, rather than on access history.

## Choosing a Policy

The failure mode ARC targets — one bulk, sequential, non-repeating scan wiping out a cache's hit ratio for everything else — is worth checking for specifically whenever a cache sits in front of a data store that also serves batch or backup-style full scans, since that's exactly the traffic pattern plain LRU handles worst (a scan looks "recently used" to LRU right up until it evicts the entries that actually mattered). Where the access pattern is known to be either purely recency-driven or purely popularity-driven, LRU or LFU are simpler to implement and reason about than ARC's two-pool bookkeeping, and simplicity is a legitimate tie-breaker when either policy would achieve a similar hit ratio in practice.
