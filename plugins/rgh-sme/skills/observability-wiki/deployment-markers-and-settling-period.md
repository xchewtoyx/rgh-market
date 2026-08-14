---
type: concept
title: Deployment Markers and Settling Period
description: Overlaying deployment, maintenance, and backup events as vertical markers on metric graphs makes their side effects visually obvious, and tracking how quickly performance returns to normal after a change (the settling period) distinguishes expected transient degradation from a real regression.
sources:
  - title: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 14"
  - title: "The Site Reliability Workbook"
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 16"
---

Because most production issues are caused by production changes, overlaying deployment events (and maintenance/backup events) as vertical markers on every metric graph lets anyone spot an unintended side effect at a glance, without having to separately cross-reference a deploy log against a timestamp. Etsy's engineering culture called this practice, only half-jokingly, its "unparalleled and unmatched vertical line technology."

A related concept is the **settling period**: after a change, performance may degrade substantially for a while as caches miss and warm back up, connection pools re-establish, or JIT-compiled code re-optimizes. This is expected transient behavior, not a regression — but it's only distinguishable from a real regression if you're tracking *how quickly* performance returns to its prior baseline. A settling period that's unexpectedly long, or that never fully recovers, is itself a symptom worth investigating.

Both practices depend on being able to see [change correlation](change-correlation-in-debugging.md) directly in the same view as the metric it might have affected.

## Telemetry and Metric Requirements for Canary Releases

When validating releases using canary deployments (comparing a canary group to a control group), the monitoring system and metric design must satisfy specific operational constraints:

* **Symptom-Focused Metric Selection**: Select a small, stack-ranked set of metrics (capped at roughly a dozen) that directly indicate user-facing problems (e.g., latency, error ratios) rather than internal resource utilization (e.g., CPU, memory), which are often too noisy. See [symptom-based vs. cause-based alerting](symptom-based-vs-cause-based-alerting.md).
* **Population-Level Breakdown**: The telemetry store must support querying metrics sliced by deployment group (canary vs. control). Evaluating metrics only at the aggregate service level makes defects in the canary statistically invisible (for example, a 20% error rate on 5% of traffic displays as only a 1% overall error rate).
* **Granular Aggregation Windows**: The metric aggregation window (e.g., 1 minute) must be smaller than the canary evaluation duration. Large aggregation windows (e.g., 1 hour) muddy the signal by blending pre-canary and post-canary data.
* **Pipeline and Asynchronous Canaries**: For batch or data processing pipelines, canaries must run long enough to span at least one complete work unit. Additionally, to avoid signal contamination, work units must be isolated so that all processing stages of a single unit are executed by the same canary or control worker pool.
