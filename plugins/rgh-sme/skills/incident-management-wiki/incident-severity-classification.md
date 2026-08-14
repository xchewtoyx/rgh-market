---
type: concept
title: Incident Severity Classification
description: Tiering alerts and incidents by urgency and impact so response effort, escalation, and paging are proportionate rather than uniform.
sources:
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 8"
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 3"
---

Not every alert deserves a page, and not every incident deserves the same
response. Two paired classification schemes keep response effort
proportionate to actual impact:

**Alert priority** determines how an alert is delivered:

- **P1**: immediately actionable, pages the on-call engineer, SLO-impacting.
- **P2**: actionable but not urgent — handled the next business day,
  non-customer-facing.
- **P3**: informational only, surfaced on dashboards, never pages anyone.

**Incident severity** determines how the response is structured once an
alert becomes an incident. A simple Sev1–Sev3 scale, with predefined,
unambiguous escalation criteria for the top severity, avoids the delay and
disagreement of deciding severity from scratch mid-incident. Every P1 or P2
alert should open a tracked incident ticket, so pager load and incident
history stay linkable and analyzable later — see
[pager load management](pager-load-management.md).

Escalated incidents (typically Sev1) get roles assigned per the
[incident command system](incident-command-system.md) — an incident
commander, a scribe, and a communications lead — while lower-severity
incidents can be handled by an individual engineer without standing up the
full structure. Defining these criteria and role thresholds in advance,
before an incident occurs, prevents the criteria themselves from becoming a
point of contention while the system is down.

An alternative, coarser scheme tiers incidents by how well-understood the
fix is rather than by customer impact alone: **green-box** (solution is
well known — "see it, fix it," like changing a flat tire), **yellow-box**
(a bounded set of possible causes requiring a specialist's diagnosis, like a
mechanic diagnosing a car that won't start), **red-box** (a novel or complex
issue needing trial and error with no obvious playbook, where an [incident
commander](incident-command-system.md) becomes most valuable), and
**black-box** (disaster-scale, potentially redefining the organization's
"new normal"). The point of naming the tier out loud — "we are working a
serious red-box incident" — is that it lets a commander cut off unproductive
debate quickly by giving everyone the same frame for how much uncertainty
they should expect. This tiering is the **Triage** step of the [STAR
incident action plan](star-incident-action-plan.md).
