---
type: concept
title: Time-Based vs Request-Based Availability
description: >
  Availability can be computed as a fraction of uptime over total time, or as
  a fraction of successful requests over total valid requests, and the two
  formulas capture different failure modes.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3"
---

**Time-based**:

```
Availability = uptime / (uptime + downtime)
```

**Request-based (yield)**:

```
Availability = successful requests / total valid requests
```

Request-based metrics are generally preferred: they capture degraded states
and partial outages that a binary up/down time-based metric misses entirely.
At the implementation level, this distinction is closely related to
[event-based vs. metric-based SLOs](event-based-vs-metric-based-slo.md),
where evaluating individual request events directly avoids the distortion
of grouping them into arbitrary time windows.

Time-based framing remains useful for reporting and human communication —
error budgets are often expressed in minutes even when the underlying SLI is
request-based, because "we have 17 minutes of budget left" is more
immediately graspable than a raw event ratio. Similarly, tracking
[user-impact minutes](user-impact-minutes.md) provides a structured way to
express partial outages in time-based terms. See
[error budget](error-budget.md) for both calculation styles, and
[reliability burndown reporting](reliability-burndown-reporting.md) for why
time-based framing tends to win for stakeholder-facing reporting regardless
of which framing drives the underlying SLI.
