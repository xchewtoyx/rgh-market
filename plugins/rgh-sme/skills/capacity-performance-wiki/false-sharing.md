---
type: concept
title: False Sharing
description: A CPU cache performance pathology where independent threads writing to distinct variables that happen to share a cache line trigger repeated cache coherency invalidation, stalling both cores even though no logical data is actually shared.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 6"
---

**False sharing** occurs when two threads running on different CPU cores write to two *logically independent* variables that happen to be laid out within the same physical CPU cache line (typically 64 bytes). Even though the threads share no actual data, the hardware cache-coherency protocol treats the whole cache line as a single unit of coherence, and the two threads' unrelated writes contend for it as if they were sharing state.

## The Mechanism

Multi-core CPUs maintain cache coherency (commonly via the **MESI** protocol) at cache-line granularity, not per-variable. When one core writes to any byte in a cache line, the coherency protocol invalidates that line in every other core's cache, forcing them to re-fetch it from a shared cache level or memory before they can read or write it again. If two independent variables happen to sit in the same 64-byte line and are each written frequently by a different core, every write from either core invalidates the other core's copy — the line bounces back and forth between cores' caches even though neither core's logic has anything to do with the other's variable.

## Performance Impact

Each invalidation-and-refetch cycle costs tens to hundreds of CPU cycles — comparable to the memory-stall cost described in [Instructions Per Cycle](instructions-per-cycle.md). Under high write frequency from both cores, this "cache line bouncing" can dominate execution time, producing severe throughput degradation that is invisible to code review (the source code shows no shared state) and easy to misdiagnose as generic memory latency rather than a specific layout problem.

## Distinguishing From Lock Contention

False sharing produces symptoms superficially similar to [lock contention](lock-contention-overhead.md) — cores stalling on cache/memory activity under concurrent access — but the root cause and fix are different: lock contention is threads correctly synchronizing over data they intentionally share; false sharing is threads paying a synchronization-like cost for data they don't share at all, purely because of memory layout.

## Diagnosis and Mitigation

*   **Diagnosis:** Hardware performance counters for cache-line invalidation / cross-core cache traffic (via `perf c2c` on Linux) can directly identify cache lines with high cross-core contention, pinpointing the offending variables.
*   **Padding:** Insert padding bytes between frequently-written independent variables so each lands on its own cache line, eliminating the shared coherency unit.
*   **Struct layout review:** Group variables by which thread/core writes them, rather than by logical association, when the two don't match — a struct organized for readability can accidentally interleave hot variables from different threads into the same line.
