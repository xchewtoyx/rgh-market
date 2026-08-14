---
type: concept
title: Acute Stabilisation Procedures
description: >
  Immediate runbook actions to hold steady during an active incident:
  stop-and-assess, stand-down check-ins, and rapid risk reassessment before
  load compounds further.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 7 (Siemens Turbine Maintenance Case Study)"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 13 (Cook & Nemeth)"
---

Stabilisation is minimum viable functioning until the acute phase passes —
not solving everything, but stopping degradation and buying time for
clearer decisions. Three procedure families apply once [incident detection
thresholds](incident-detection-thresholds.md) have fired:

**Stop and reassess.** Pause the current plan. Identify where issues
cluster. Reorganise roles, communication, handoffs, and the work
schedule before resuming. A coordinator facing competing urgent demands
may deflect anxious repeated queries ("do the scheduled case") while
searching for a non-disruptive alternative rather than immediately invoking
the most disruptive option they are formally entitled to use.

**Stand-down check-ins.** Periodic pauses between leadership and front line
to refocus on safe, quality work and assess whether people need warmth,
hydration, shorter hours, or other load relief. Weather-driven incidents
illustrate why: foul conditions raise stress and degrade functioning even
when no single task changed; slowing work, adding warm-up stops, adjusting
hours, or adding people are stabilisation moves, not luxuries.

**Rapid risk assessment.** Convene whoever holds relevant experience —
operations leadership, subject-matter experts, people who have seen similar
situations — to list risks, mitigating actions, and who owns each risk
decision. Clarify decision ownership before improvising further.

Under acute mass-casualty load, stabilisation also means **routing and
triage**: bypassing usual intake when severity warrants direct path to
definitive care, preserving scarce slots for others, deferring non-critical
paperwork while keeping safety-critical documentation (e.g. blood
cross-match) intact, and provisioning family/support space before arrivals
peak.

Every stabilisation move is an instance of add capacity, adjust limits, or
remove load — the three families described in capacity engineering — but
chosen under time pressure with an incident already underway. See
[incident escalation path](incident-escalation-path.md) when stabilisation
requires help beyond the local envelope.
