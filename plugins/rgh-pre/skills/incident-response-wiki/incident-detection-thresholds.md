---
type: concept
title: Incident Detection Thresholds
description: >
  Observable signs that distinguish an acute incident from ordinary strain,
  including stacked minor failures, stalled progress, and mismatches between
  declared urgency and actual risk.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 7 (Siemens Turbine Maintenance Case Study)"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 13 (Cook & Nemeth)"
---

An incident is not the same as a bad day. Detection thresholds are the
observable cues that the situation has crossed from manageable load into
something requiring a runbook response — stabilise, escalate, or shift
operating mode.

**Pinging signs** (proactive probing for risk-profile change) include:
multiple issues competing for attention, progress stalling, schedule
slipping, specialty help staying longer than planned, sudden need for more
people, personnel churn, higher-than-usual emergent work, a cluster of
minor safety or quality incidents even when each alone seems trivial,
common tasks performed late or skipped, communication dropping off
(unreturned calls, emails), and environmental stressors (severe weather,
holiday-period staffing). Project mood shifting is another field signal.
These signs are easiest to read from slightly outside the hot zone — when
you are inside overload, you may not know you have reached the overload
point, much like being too sick to judge when to call a doctor.

**Near-limit behavioral signs** at the sharp end include forgetfulness,
missing steps, anger outbursts, and visible fatigue or stress — the
individual-level complement to organisational pinging.

**Soft emergency** is a third threshold pattern: a situation declared
urgent by someone with standing to declare it, but that does not match
observable high risk — delayable but not indefinitely deferrable. A
coordinator who can read personalities, case types, and resource pace may
classify a declared emergency as "soft," search for alternatives that
avoid disruptive escalation, and adjust directives as the arrangement
evolves. The threshold question is not "did someone say emergency?" but
"does declared urgency match actual risk given what I can see right now?"

When several pinging signs cluster, treat that as crossing a detection
threshold even if no single event looks catastrophic. Human dormancy during
crisis — numb hopelessness that feels like being dead inside — is another
threshold pattern; see [signs of life detection](signs-of-life-detection.md)
for the diagnostic that distinguishes dormancy from giving up. Highly resilient
organisations treat **noticing** risk-profile change as a learnable skill
that triggers improvised response even before a prescribed menu exists —
the first of four behaviors (anticipate, notice, plan, adapt) that structure
acute response once load approaches the yield point. See
[error-likely climate signals](error-likely-climate-signals.md) for
environmental precursors and [envelope trespass escalation
trigger](envelope-trespass-escalation-trigger.md) for the moment a
prepared response envelope is left behind.
