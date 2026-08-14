---
type: concept
title: Free vs. Available Memory
description: Free memory is RAM that is completely unused, while available memory adds back reclaimable page cache and slab memory — using the wrong one as a utilization metric misjudges real memory headroom.
sources:
  - title: "Systems Performance, 2nd Edition"
    resource: "Systems Performance, 2nd Edition (Brendan Gregg), ch. 7"
---

Linux memory reporting distinguishes two numbers that are easy to conflate but mean very different things for capacity assessment:

*   **Free memory:** RAM that is completely unallocated and unused by anything — no process data, no kernel structures, no cache.
*   **Available memory:** an estimate of how much memory could be given to a newly starting application without forcing the system into swapping. It is computed as free RAM plus the portion of page cache and slab (kernel object cache) memory that the kernel could reclaim on demand if an application needed it.

## Why This Matters for Capacity Assessment

On a healthy, well-utilized Linux system, "free" memory is often deliberately small — the kernel uses otherwise-idle RAM to cache file data and metadata, since caching costs nothing until the memory is actually needed elsewhere. A system reporting only a few hundred megabytes of *free* memory can still be nowhere near real memory pressure, because most of the "used" memory is reclaimable page cache the kernel will happily evict under demand.

Reading raw "free" memory as a [USE Method](use-method.md) utilization signal produces a false-positive memory-pressure alarm: a system can look almost fully "used" while actually having abundant headroom in the form of reclaimable cache. **Available** memory is the correct number to use as a memory-utilization or headroom signal — it already accounts for what the kernel can give back.

## The Real Warning Sign

Genuine memory pressure shows up not as low free memory (which is normal and expected) but as declining *available* memory alongside active reclaim activity — see [direct reclaim stalls](direct-reclaim-stalls.md) for what happens once available memory can no longer keep pace with allocation demand.
