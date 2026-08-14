---
type: concept
title: Interactive Latency Thresholds
description: Human-perceived responsiveness to latency is nonlinear — specific millisecond bands mark where an interactive operation feels instant, where attention starts to drift, and where users fully context-switch — and those bands should drive latency budget targets.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Titus Winters, Tom Manshreck, Hyrum Wright, eds.), ch. 19"
---

Interactive systems — developer tools, search UIs, navigation flows — don't degrade linearly as latency increases. Empirical UX bands give concrete targets when setting a [latency budget](throughput-vs-latency-tradeoff.md) or deciding whether a change is worth the [efficiency investment](efficiency-investment-vs-resource-cost.md):

*   **Below ~200 ms:** the operation feels responsive; users stay in flow. This is a common design target for frequent, high-volume interactive operations (e.g., code search, file navigation).
*   **Around ~1 second:** attention starts to drift; the user notices the wait even if they don't abandon the task.
*   **Around ~10 seconds:** users are likely to fully context-switch — open another tab, start unrelated work — which carries a much higher productivity cost than the wait itself.

These thresholds explain why optimizing from 500 ms to 200 ms on a high-frequency path can matter more than shaving the same absolute amount off an already-slow background job: the marginal user impact is concentrated in the sub-200 ms band, not spread evenly across the latency scale. When measuring whether a system meets its budget, [goodput vs. throughput](goodput-vs-throughput.md) applies the same idea at the SLO level — a service can report high completion throughput while most requests miss the interactive band that actually determines user experience.
