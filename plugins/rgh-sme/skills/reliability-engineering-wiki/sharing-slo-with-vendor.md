---
type: concept
title: Sharing Your SLO with a Vendor
description: >
  Sharing your own SLO with a cloud provider or vendor, rather than relying
  solely on their published SLA, gives both sides better data during an
  incident.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 3"
---

A customer's regional footprint or specific workload can get "lost" inside
a vendor's global SLA rollup — the vendor might be meeting its overall SLA
comfortably while a specific customer is having a bad time. Sharing
dashboards built around the customer's own SLO lets the vendor give
customer-specific impact figures during an incident instead of generic
ones, and lets major incidents get appropriately urgent treatment jointly
rather than the customer having to escalate blind.

This is a concrete instance of a broader pattern: an
[SLA](sla-vs-slo.md) tells you what's contractually promised, but an SLO —
even one built and owned entirely on the customer's side of a vendor
relationship — is what actually drives useful, specific conversations about
real impact. Regular joint review meetings (e.g. monthly) and an agreed SLO
revision cadence (e.g. every 6 months) keep this working over time, without
so much churn that the relationship thrashes.
