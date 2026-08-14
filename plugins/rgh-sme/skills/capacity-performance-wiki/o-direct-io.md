---
type: concept
title: O_DIRECT I/O
description: A file access mode that bypasses the OS page cache entirely, giving an application direct control over disk I/O at the cost of requiring its buffers, offsets, and lengths to be aligned to storage block boundaries.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 8"
---

**`O_DIRECT`** is a file-open flag (Linux and other Unix-like systems) that bypasses the kernel's page cache for reads and writes, sending I/O requests straight to the storage device instead of buffering through RAM first.

## Why Bypass the Page Cache

Applications that implement their own caching layer — databases being the canonical example — have no use for the kernel also caching the same data in the page cache: doing so means the same bytes are held twice in RAM (once in the application's own cache, once in the kernel's), wasting memory on **double buffering**, and the kernel's cache eviction policy has no visibility into which pages the application's own cache logic considers hot. `O_DIRECT` lets the application manage exactly one copy of hot data, under its own eviction policy, and issue I/O that reflects the true cost of a real storage access rather than a cache hit.

## The Alignment Requirement

Bypassing the page cache also bypasses the kernel code that would otherwise handle misaligned or partial-block I/O by reading a full block into the cache and copying out the requested slice. Without that layer, the application's I/O request goes to the storage device largely as-is, so the device's block-level constraints become the application's problem directly: the memory buffer's address, the file offset, and the transfer length must all be aligned to the underlying storage's block size (typically 512 bytes or 4 KB). An unaligned `O_DIRECT` request fails outright rather than being silently handled, which is why application code using `O_DIRECT` must explicitly manage aligned buffer allocation (e.g., via `posix_memalign`) rather than using ordinary heap allocation.

## Relevance to Benchmarking

Because `O_DIRECT` removes the page cache from the I/O path entirely, it is also the standard technique for [avoiding the "benchmarking cache instead of storage" pitfall](benchmarking-pitfalls.md): a storage benchmark using `O_DIRECT` is guaranteed to measure actual device performance rather than accidentally measuring RAM speed through an unintentional cache hit.
