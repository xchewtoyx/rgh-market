---
type: concept
title: Alerting Response-Time Floor
description: >
  A practical minimum human response time of roughly five minutes bounds how
  tight an SLO can be before human-in-the-loop paging stops working at all.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
---

An alert must fire *after some* budget is spent but *before all of it* is
gone — alerting exactly at exhaustion is useless (no time left to react),
and alerting at the first sign of any loss is oversensitive.

Assume a practical minimum ~5-minute human response floor (paging delay +
device pickup + getting to a laptop). Below roughly four nines (99.99%,
about 4.38 minutes of budget per month), there usually isn't enough budget
left for a human to meaningfully react in time — tighter targets than that
require auto-remediation instead of paging a person.

At the extreme, very high availability targets with high traffic volume push
the allowed downtime so low (fractions of a minute per year) that the
time-to-exhaustion for a full outage can be smaller than the metric
collection interval itself — alerting can't defend the SLO fast enough at
any human-response speed. See
[extreme availability alerting limits](extreme-availability-alerting-limits.md)
for what actually defends a target that tight.

This floor is a hard input to
[SLO window selection](slo-window-selection.md) and to
[choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md):
a target that requires faster-than-floor response isn't really achievable
through alerting-driven human response at all, regardless of how carefully
the alert is tuned.
