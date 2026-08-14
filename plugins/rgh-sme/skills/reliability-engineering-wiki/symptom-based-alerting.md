---
type: concept
title: Symptom-Based Alerting
description: Paging on user-visible defects rather than their underlying system roots to minimize false alarms and focus on actual reliability.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
---

Symptom-based alerting is the practice of triggering high-priority pages only when there is actual or imminent user-visible degradation. It stands in contrast to cause-based alerting, which alerts on the underlying system conditions that might lead to user impact.

## Symptom vs. Cause

*   **Symptoms** represent *what* is broken from the perspective of the service consumer. Examples include elevated error rates (e.g., HTTP 500s) or slow response times (e.g., p99 latency above a threshold).
*   **Causes** represent *why* the symptom is occurring. Examples include high database CPU utilization, high memory usage, network interface packet drops, or single-node failures.

## Why Cause-Based Alerting Fails for Pages

Paging on causes (such as CPU > 90% or disk space > 80%) degrades operational sustainability in several ways:
1.  **False Positives**: Modern resilient architectures are designed to tolerate internal failures (e.g., through auto-scaling, active-active redundancy, or graceful degradation). A cause-based alert may fire even when the user experience remains completely unaffected.
2.  **Alert Fatigue**: Constant false alarms erode the responder's responsiveness, leading to a degraded ability to notice actual outages. See [actionable alert philosophy](actionable-alert-philosophy.md).
3.  **Maintenance Overhead**: Internal resource thresholds are heavily dependent on system capacity and traffic patterns. They require constant adjustment, whereas symptom thresholds are tied directly to stable [service-level objectives](service-level-objective.md).

## Implementation in Service-Level Management

An effective symptom-based alerting system is anchored in [user-centric SLI selection](user-centric-sli-selection.md). Rather than guessing at individual resource limits:
*   Identify the user's primary expectations (availability, latency, durability).
*   Define the [service-level indicator](service-level-indicator.md) that measures these symptoms.
*   Paging strategies, such as [multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md), consume the [error budget](error-budget.md) based on active symptoms, ensuring pages are only triggered by significant, ongoing user impact.
