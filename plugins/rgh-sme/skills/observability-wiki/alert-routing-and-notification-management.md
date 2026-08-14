---
type: concept
title: Alert Routing and Notification Management
description: A notification manager sits between alert rule evaluation and human responders, aggregating, silencing, and routing firing alerts to the right destination so responders aren't paged redundantly or during known maintenance.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 10"
---

Once a [time-series alert rule fires](time-series-alert-rule-evaluation.md), a separate notification-manager layer handles what happens next:

- **Aggregation** — group related firing alerts so a single underlying problem doesn't generate a flood of separate pages.
- **Silencing** — automatically suppress alerts during scheduled maintenance windows, so expected disruption doesn't page anyone.
- **Routing** — dispatch to the appropriate target (paging system, chat channel, ticketing system) based on the alert's labels/ownership.

This layer is where much of the practical defense against [alert fatigue](alert-fatigue-and-normalized-deviance.md) lives: a technically-correct alert rule can still overwhelm responders if its output isn't aggregated and routed sensibly.
