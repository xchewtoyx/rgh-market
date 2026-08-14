---
type: concept
title: SLO Definition Document
description: >
  A standard written artifact capturing an SLO's ownership, approvers,
  definitions, rationale, and revisit schedule, so the target is
  understandable and defensible beyond the team that created it.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 15, Appendix A"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2, Appendix A"
---

A recurring template structure across sources:

- **Ownership** — who's responsible, and who can mandate change based on
  error-budget status; a whole team for single-team services, a single named
  stakeholder or director/VP for cross-cutting ones.
- **Approvers** — never a single person or team; include senior engineers
  from *outside* the owning team (teams go blind to their own dependents),
  representatives of dependent teams, and members of the operating team
  itself.
- **Definition status** — original proposal date, last-updated date
  (incremented on every revisit even with no changes, so "reviewed recently"
  is distinguishable from "untouched"), approval/implementation date, and
  next scheduled revisit date.
- **Service overview** — plain-language summary of what the service does,
  from the user's perspective.
- **SLI/SLO definitions** — both a plain-language sentence ("We will serve
  200 responses within 500ms to 99.9% of requests") and a precise
  query/formula version, plus a live link to a dashboard, never a
  manually-maintained static number.
- **Rationale** — document *why* these SLIs/SLOs/targets were chosen,
  including how they were derived from historical data (see
  [choosing SLO targets from historical data](choosing-slo-targets-from-historical-data.md)),
  and honestly flag if a target is not strongly evidence-based, so future
  readers know how much validation work is still warranted. Otherwise this
  institutional knowledge disappears.
- **Revisit schedule and error budget policy** — see
  [error budget policy](error-budget-policy.md); a starting point for
  discussion at first, though strict rules are fine once a team has earned
  trust in them.
- **External links** — one consolidated section listing deep-dive docs,
  dashboards, and source repos.

This document is the concrete artifact that makes
[SLO discoverability](slo-discoverability.md) possible — being technically
correct but undiscoverable only delivers value to the team that wrote it.
