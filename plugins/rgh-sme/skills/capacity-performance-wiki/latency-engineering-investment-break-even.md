---
type: concept
title: Latency Engineering Investment Break-Even
description: A back-of-the-envelope decomposition of aggregate user wait time against the cost of a dedicated latency-optimization team determines whether investing in latency engineering pays off at a given query volume.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 19"
---

When a high-volume interactive service adds latency per request, the productivity loss across all users can exceed the headcount cost of a team dedicated to reducing that latency — but only above a certain usage threshold. The decision is a specific instance of the broader [efficiency investment vs. resource cost](efficiency-investment-vs-resource-cost.md) trade-off, applied to latency rather than raw compute.

## Worked Example: Developer Search

Google Code Search processes well over one million developer queries per day. A [Fermi-style decomposition](fermi-decomposition-for-capacity-estimation.md) of the productivity cost of one extra second of latency per query:

*   One second × one million queries/day ≈ **35 full-time-engineer-days of idle wait** per day across the user population.
*   The dedicated search-backend team is roughly a tenth of that headcount.

At that scale, latency engineering clearly pays for itself. The rough break-even point — where aggregate wait time equals the cost of maintaining a latency-focused team — lands around **~100,000 queries/day** (corresponding to on the order of a few thousand active developers, depending on queries per developer).

## How to Use the Estimate

*   **Decompose before deciding.** Split total wait into (daily query volume) × (latency delta in seconds) × (value of developer time per second). Each factor is easier to bound than the combined productivity loss.
*   **Nonlinearity matters.** Because [interactive latency thresholds](interactive-latency-thresholds.md) are nonlinear, the productivity damage of moving from 1 s to 2 s is not the same as moving from 200 ms to 1.2 s — the latter may cross the attention-drift band while the former only deepens an already-bad wait. Frame the "latency delta" in terms of which UX band the change crosses, not just absolute milliseconds.
*   **Below break-even, buy capacity or accept latency.** Under the threshold, a dedicated latency team is hard to justify; simpler levers (more hardware, coarser features, higher [utilization targets](utilization-vs-efficiency.md) with accepted tail risk) may be the rational choice until volume grows.
