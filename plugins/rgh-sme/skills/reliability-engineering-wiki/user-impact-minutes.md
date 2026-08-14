---
type: concept
title: User-Impact Minutes
description: A metric that quantifies the severity of an outage by multiplying its duration by the fraction of the user base affected.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 16"
---

User-Impact Minutes (UIM) is a metric used to quantify the magnitude of a production outage. It combines both the temporal duration of the incident and the scope of its impact on the user base.

## Calculation Formula

$$\text{User-Impact Minutes} = \text{Outage Duration (minutes)} \times \text{Fraction of Affected Users}$$

For example:
*   If a service experiences a complete outage (100% of users affected) lasting 10 minutes, the impact is:
    $$10 \text{ minutes} \times 1.0 = 10 \text{ user-impact minutes}$$
*   If a service experiences a partial outage (10% of users affected) lasting 100 minutes, the impact is:
    $$100 \text{ minutes} \times 0.1 = 10 \text{ user-impact minutes}$$

Both scenarios represent equivalent total customer-facing disruption, which this metric reflects accurately.

## Advantages over Simple Duration

Traditional outage tracking often relies on simple downtime duration (e.g., MTTR/MTTD). That approach is limited because:
1.  **Ignores Partial Outages**: A binary up/down model fails to distinguish between a minor subset of users experiencing slow loads and a total global system outage.
2.  **Miscalibrated Prioritization**: Using raw downtime duration might lead teams to prioritize a long-lasting but minor regional failure over a brief but catastrophic global failure.

## Connection to Service-Level Management

User-Impact Minutes serves as an intermediate metric that aligns with [time-based vs request-based availability](time-based-vs-request-based-availability.md). While request-based availability captures the raw percentage of failed requests, User-Impact Minutes allows organisations to translate those failures into a time-based duration that is easier for non-technical stakeholders to understand, facilitating [reliability burndown reporting](reliability-burndown-reporting.md) and assisting in [SLO-based reporting vs incident counting](slo-based-reporting-vs-incident-counting.md).
