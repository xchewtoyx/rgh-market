---
type: concept
title: Memory-to-Flash Read-Path Tiering
description: When a read-heavy working set outgrows RAM, moving it to flash cuts cost by an order of magnitude but raises access latency by two — and data structures designed for in-memory random access often perform poorly on the slower tier without redesign.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 19"
---

Large read-heavy indexes — search inverted indices, reference graphs, lookup tables — often start entirely in memory for minimum latency. As the index grows, keeping it all in RAM becomes the dominant cost. **Flash storage** offers a middle tier: typically **>10× cheaper per byte than memory**, but with **>100× higher access latency** than RAM (see [cost of common operations](cost-of-common-operations.md) for ballpark I/O figures).

Moving an index from all-in-memory to flash is not a transparent capacity expansion. Structures optimized for memory — many small random fetches, large per-query working sets — degrade disproportionately on flash because each fetch pays the full latency penalty. A trigram-based substring index that issues many large inverted-list reads per query may be fast in RAM and unusable on flash; a denser n-gram scheme that reduces both the **number** and **size** of fetches per query can trade a larger total index size for fewer random I/Os, making flash viable.

## The Design Trade-Off

| Tier | Cost per byte | Access latency | Index design bias |
| :--- | :--- | :--- | :--- |
| Memory | High | Low (~ns–µs) | Maximize query speed; tolerate larger fetch counts |
| Flash | ~10× lower | ~100× higher (~10–100 µs) | Minimize fetch count and bytes per fetch; accept larger index footprint |

This is a specific instance of the [throughput vs. latency trade-off](throughput-vs-latency-tradeoff.md) applied to storage media: flash buys more capacity per dollar but pushes the system toward latency-sensitive, fetch-minimizing index layouts rather than throughput-maximizing in-memory structures.

## Capacity Planning Implications

*   **Model the tier transition explicitly.** Forecasting "we'll need 2× the RAM" may actually mean "we'll need to redesign the index for flash" — a different cost, latency profile, and engineering timeline.
*   **Watch query latency percentiles after tiering.** Median latency may survive the move; tail latency often does not, because the queries that touch the most inverted lists pay the flash penalty repeatedly. See [latency percentiles vs. mean](latency-percentiles-vs-mean.md).
*   **Local workspace overlays.** A hybrid pattern serves the bulk corpus from the tiered history index while routing per-developer uncommitted changes through dedicated in-memory brute-force search on small, frequently synced diffs — keeping interactive freshness for active edits without re-indexing the entire corpus on every keystroke.
