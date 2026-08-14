---
type: concept
title: Failure Demand
description: >
  Failure demand is the operational workload created by failing to deliver a stable service or change correctly the first time, consuming capacity that would otherwise go to value-adding work.
sources:
  - title: "Accelerate: The Science of Lean Software and DevOps: Building and Scaling High Performing Technology Organizations"
    resource: "Accelerate (Forsgren, Humble, Kim), ch. 4"
---

Originally conceptualized by John Seddon in service design, **failure demand** is the demand for work created by a failure to do something correctly for the customer or system the first time. It contrasts with **value demand**, which represents the demand for new features, enhancements, or capabilities that directly deliver value.

In reliability engineering and service-level management, failure demand is a key driver of operational overhead and velocity degradation.

## Manifestations in System Operations

Failure demand in software delivery systems and reliability practices typically manifests as:

*   **Incident Response**: The unplanned, highly urgent work of responding to alerts, troubleshooting production outages, and restoring service.
*   **Rework and Remediation**: The overhead of writing hotfixes, executing manual rollbacks, patching systems under pressure, and performing post-incident cleanup.
*   **Customer Support Influx**: Spikes in support tickets or customer complaints resulting from degraded service availability or latency.
*   **Operational Toil**: Repetitive, manual operations required to keep a fragile system running (e.g., manually restarting leaked processes or cleaning full disks).

## The Capacity Vicious Cycle

Because failure demand is urgent, it naturally preempts planned engineering work. This creates a feedback loop that degrades system performance over time:

```
┌───────────────────────────┐
│ System Reliability Dips  │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│   Failure Demand Rises    │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Engineers Reassigned to   │
│ Firefighting & Remediation│
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Slack Capacity Erased;    │
│ Reliability Debt Defers   │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ System Reliability Drops  │ (Feedback Loop)
└───────────────────────────┘
```

This cycle erases the team's capacity to do proactive engineering work. The team pays a heavy "incident tax" that slows feature delivery and threatens the [sustained velocity](initial-vs-sustained-velocity.md) of the project.

## Mitigating Failure Demand

Reducing failure demand requires shifting from downstream inspection (reactive firefighting) to building quality and safety into the delivery lifecycle:

1.  **Continuous Delivery Capabilities**: Implementing automated testing (developer-maintained), trunk-based development, and version-controlling both code and configuration ensures that defects are caught in the pipeline rather than in production.
2.  **Self-Healing and Automation**: Automating recovery mechanisms (e.g., auto-scaling, automatic retries with backoff, circuit breakers) converts potential incidents into silent self-healing events, reducing paging alerts and manual response.
3.  **Error Budget Governance**: An [error budget](error-budget.md) acts as a buffer. When spent, the [error-budget policy](error-budget-policy.md) triggers a pivot in engineering priorities, forcing the team to focus on resolving the root causes of failure demand before the system falls into a severe reliability crisis.
