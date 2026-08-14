---
type: concept
title: Cost of Common Operations
description: A ballpark mental model of the relative cost of common operations (network calls, storage I/O, memory allocation, cache misses) that lets an engineer default toward the cheaper option without measuring every decision.
sources:
  - title: "A Philosophy of Software Design, 2nd Edition"
    resource: "A Philosophy of Software Design, 2nd Edition (John Ousterhout), ch. 20"
---

Not every design decision justifies a benchmark. A working knowledge of which operations are *fundamentally* expensive relative to each other lets an engineer default toward the cheap alternative whenever a clean, simple option exists on both sides — without stopping to measure. This is a middle path between two failure modes: micro-optimizing every statement (which slows development and often doesn't even pay off, since many "optimizations" don't matter) and ignoring cost entirely (which scatters many small inefficiencies through the code — a "death by a thousand cuts" that can leave a system 5-10x slower than necessary and is hard to fix retroactively, since no single change would move the needle).

## Ballpark Figures

These are order-of-magnitude figures for intuition-building, not benchmarks to cite verbatim — always confirm with real measurement, e.g. via a [micro-benchmark framework](micro-benchmark-framework-investment.md), before relying on a specific number for a specific system.

*   **Network round-trip, within a datacenter:** ~10-50 microseconds — tens of thousands of instruction times.
*   **Network round-trip, wide-area:** ~10-100 milliseconds.
*   **Secondary storage I/O:** spinning disk ~5-10 milliseconds (millions of instruction times); flash ~10-100 microseconds; emerging nonvolatile memory ~1 microsecond (still ~2000 instruction times). See [file system vs. disk latency](file-system-vs-disk-latency.md) for how the page cache decouples application-visible latency from these physical-device numbers.
*   **Dynamic memory allocation** (`malloc`/`new`): significant overhead from allocation, freeing, and garbage collection — enough that avoiding an unnecessary allocation is often cheaper than optimizing the code that follows it.
*   **Cache miss (DRAM fetch after an on-chip cache miss):** a few hundred instruction times — often as significant to overall performance as the raw computation itself. See [instructions per cycle](instructions-per-cycle.md) for how to detect a workload that is dominated by stalls of this kind rather than by compute.

## Applying the Cost Model

Two worked patterns illustrate "naturally efficient yet still simple" choices, where picking the cheaper option costs nothing in complexity:

*   **Hash table vs. ordered map** for key-based lookup when ordering isn't actually needed — both are equally simple to use via standard libraries, but a hash table can be 5-10x faster.
*   **Inline vs. pointer-indirected storage** — in languages with manual layout control, storing an array of structures inline (one contiguous allocation) rather than as an array of pointers to separately-allocated structures avoids a second layer of allocation overhead, for no extra complexity.

## When Efficiency Trades Off Against Complexity

Most of the time, the cheap option is also the simple option, and the cost model above is all that's needed. When the two genuinely diverge — the faster design would add real complexity — the decision rule shifts:

*   If the more efficient design adds only a small amount of complexity, and that complexity stays hidden (doesn't leak into interfaces), it may be worth adopting immediately.
*   If the faster design adds substantial implementation complexity or complicates interfaces, prefer starting simple and optimizing later — only if performance actually becomes a demonstrated problem, confirmed by [measuring before modifying](measure-before-optimizing.md).
*   If solid evidence already exists that a given path will matter for performance, it's reasonable to build the faster version immediately rather than deferring and re-paying the redesign cost later.

A justified upfront investment looks like deliberately taking on complexity — e.g., specialized networking hardware that bypasses the kernel — specifically because prior measurement already showed the simpler default path would be too slow for a hard latency target, letting the rest of the system stay simple around that one deliberately-complex piece.
