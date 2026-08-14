---
type: concept
title: Sustainable On-Call Design
description: Principles for structuring on-call rotations to balance system reliability with engineer health, well-being, and operational sustainability.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 11"
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 8, ch. 21"
---

Sustainable on-call rotations protect team well-being while ensuring rapid system defense against outages. Key design guidelines include:
* **Rotation Caps**: Rotations must maintain a minimum of 6-8 engineers. This ensures reasonable shift frequencies and prevents cognitive fatigue.
* **Page Volume Limits**: Shifts should average a maximum of 2 actionable pages per 12-hour shift — see [pager load management](pager-load-management.md) for how to actively drive that number down rather than just monitor it.
* **Actionable Alerting**: Pages must require human intelligence and immediate action. Alerts that require no action or routine reboot scripts are noise and must be automated or silenced.
* **On-Call Shadowing**: New SREs must shadow primary on-callers for several rotations before taking independent shifts, ensuring a gradual onboarding path.
* **Compensation & Safety Nets**: Engineers must be compensated for availability. They must also have a clear escalation path to backup engineers or Dev managers if overwhelmed.

On-call sustainability supports team health, reducing cognitive fatigue during incident triage and response. See [burnout risk factors](burnout-risk-factors.md) for the underlying organizational conditions these design choices are meant to counteract.

### Shift structure and staffing

Shift length should be capped at 12 hours, with a preference for daytime
coverage; a single person covering a full 24 hours continuously is
unsustainable — better to split day and night between two people, shorten
the rotation cycle (e.g., 3 days on, 4 off), or — for organizations large
enough to staff it — hand off the pager between geographically distributed
teams so that no one is ever on call overnight ("follow the sun"). Scheduling shouldn't stay
manual once a team grows: an automated tool should rebalance load across
constraints like vacations and stated preferences, and must never silently
change an already-published schedule. A documented short-term swap policy
lets people trade shifts for illness or commitments, and teams with strict
response-time SLOs need to plan for on-call commute time in that policy.

Minimum staffing to sustain a rotation without burning anyone out: roughly
6 engineers per site for multisite 24/7 coverage, or 9 engineers per site
for single-site 24/7 coverage (a bare minimum of 5-8, plus one buffer for
someone stepping out of rotation for a long-term break). Part-time work is
compatible with on-call if planned for explicitly — shorten the shift to
match working days, split shift hours between two engineers, or restrict a
part-timer's on-call to only the days they already work — with pager load
reduced proportionally to hours worked.

### Team dynamics under pager stress

Stress and pager load push engineers toward intuition and heuristics over
careful reasoning, so team dynamics matter as much as process design. A
common anti-pattern is a rotation mixing feature developers with dedicated
operations staff: developers deprioritize on-call follow-up in favor of
feature work, alerting decisions become contentious, and morale erodes.
Two complementary fixes: give the operations role real, explicit ownership
of reliability and monitoring (rather than leaving it as an unglamorous
rotation feature developers tolerate), and invest directly in team
relationships (shared space, shared time) so mutual accountability for
finishing on-call follow-through develops socially, not just procedurally.
