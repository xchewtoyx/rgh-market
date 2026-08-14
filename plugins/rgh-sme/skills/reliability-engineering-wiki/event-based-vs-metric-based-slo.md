---
type: concept
title: Event-Based vs. Metric-Based SLOs
description: Event-based SLOs evaluate individual request events for success, whereas metric-based SLOs aggregate events into time buckets, which can cause disproportionate budget burn and limit backfilling.
sources:
  - title: Observability Engineering
    resource: "Observability Engineering (Majors, Fong-Jones, Miranda), ch. 12"
---

When implementing a [service-level objective](service-level-objective.md), engineers must decide whether to evaluate reliability at the individual request level (event-based) or over pre-aggregated time windows (metric-based or time-series-based).

## Definitions

*   **Event-Based SLOs**: Evaluate every qualifying transaction (e.g., an HTTP request or database query) as either a success or a failure. The [service-level indicator](service-level-indicator.md) is calculated as:
    $$\text{SLI} = \frac{\text{Good Events}}{\text{Total Valid Events}}$$
*   **Metric-Based SLOs**: Aggregate events into fixed time buckets (e.g., 1-minute or 5-minute windows) and evaluate the aggregate performance of each bucket against a threshold. The SLI is calculated as:
    $$\text{SLI} = \frac{\text{Good Time Windows}}{\text{Total Time Windows}}$$

## The Aggregation Pitfall of Metric-Based SLOs

For highly stringent SLOs (99.99% or higher), metric-based evaluation introduces significant distortion:
1.  **Disproportionate Error Budget Burn**: If a 5-minute window has a temporary blip where success rate drops to 94%, a metric-based SLO might mark the entire 5-minute window as "bad" (0% successful). This burns a disproportionately large fraction of the monthly [error budget](error-budget.md). An event-based SLO, by contrast, only counts the specific 6% of failed requests during that window as budget burn.
2.  **Loss of Grain**: Metric-based systems discard the rich context (like user ID, request path, or dependency attributes) of individual failures during pre-aggregation, making root cause analysis difficult.
3.  **Inability to Backfill**: If an SLI definition is changed (e.g., adjusting a latency threshold), metric-based SLOs cannot re-evaluate historical data because the raw events are gone. Event-based SLOs, storing structured event data, allow engineers to backtest and backfill SLI definitions over historical logs. See [SLO measurement infrastructure design goals](slo-measurement-infrastructure-design-goals.md).

## Summary Comparison

| Property | Event-Based (Recommended) | Metric-Based (Time-Series) |
| :--- | :--- | :--- |
| **Granularity** | Per-request | Per time bucket (e.g., 1m, 5m) |
| **Budget Burn Accuracy** | High (burns exact failed request count) | Low (a single bad event can spoil a whole window) |
| **Cardinality & Context** | High (retains trace/request attributes) | Low (attributes are pre-aggregated out) |
| **Historical Backfilling** | Supported (runs queries over raw log data) | Unsupported (pre-aggregated data is immutable) |
