---
type: concept
title: Error Budget Policy
description: >
  A written, specific document defining who owns error-budget enforcement
  and exactly what actions trigger at different levels of budget consumption.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 5, Appendix A"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2, Appendix B"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3"
---

An error budget policy formalizes what happens as an
[error budget](error-budget.md) is consumed, so the response is agreed in
advance rather than negotiated mid-incident. Required elements:

- **Owners/stakeholders** — a person, team, or (for large composite
  services) managers-of-managers up to VP/CTO/CEO level for the whole
  product. Someone must be explicitly empowered to trade off [initial vs.
  sustained velocity](initial-vs-sustained-velocity.md) against reliability
  — at a small org this might be the CTO, at a larger one a product
  owner/manager.
- **Burn policies** — graduated responses tied to percentage of budget
  consumed (e.g. 33% burned → 2 of 6 engineers pivot to reliability work;
  66% → 4 of 6; 100% → whole team) or tied to burn *rate* rather than only
  absolute consumption — see [burn rate](burn-rate.md).
- **Exceeded policies** — typically stricter, more urgent responses once
  budget is fully exhausted: e.g. halting all changes/releases except P0
  issues and security fixes until back within SLO, a mandatory incident
  retrospective, and defined communication obligations to downstream teams.
  See [feature freeze as a first error budget policy](feature-freeze-as-first-error-budget-policy.md)
  for a concrete starting pattern.
- **RFC 2119-style language** (must/should/may/required) to distinguish hard
  rules from guidance, leaving room for judgment.
- **Justification and a revisit schedule** — document *why* thresholds were
  chosen and when they'll next be reviewed (monthly if new/unproven,
  quarterly/yearly once mature).
- **Non-goal**: an error budget policy is explicitly not a punishment
  mechanism — it exists to give a team explicit, legitimate permission to
  focus purely on reliability when the data says that's what's needed, not
  to penalize anyone for an outage.

**Edge case — a dependency causes the miss.** When a team's SLO is missed
because of another team's dependency rather than their own change, there are
two defensible policy stances, and the choice should be documented
explicitly rather than left ambiguous: don't halt releases (the team wasn't
at fault) versus freeze anyway (to minimize repeat risk regardless of fault).
A common resolution: a team *may* keep shipping if the outage was caused by
a company-wide problem, another team's already-frozen service, or explicitly
out-of-scope traffic (load tests, pen testers) — but *must* shift to
reliability work if a postmortem reveals a hard-dependency issue that could
be softened, since that's within the team's own control.

See [error-budget-driven prioritization](error-budget-driven-prioritization.md)
for how consumption data is used day to day, beyond the binary freeze/no-
freeze decision this policy formalizes.
