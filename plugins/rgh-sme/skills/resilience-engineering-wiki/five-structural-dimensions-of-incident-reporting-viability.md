---
type: concept
title: Five Structural Dimensions of Incident Reporting Viability
description: >
  Whether reactive incident reporting can actually work in a given domain is
  set by five structural characteristics of that domain, not by how well the
  reporting programme itself is designed — and where they're absent, the fix
  is a different kind of system, not a better version of the same one.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 17"
---

A comparison of two large, well-funded incident reporting systems shows the
same programme design can succeed or fail for reasons that have nothing to
do with programme execution. Aviation's ASRS (established 1975, run by NASA
independently of the regulator, confidential but not anonymous, expert
analyst screening with follow-up) is the benchmark success. Healthcare's
NRLS collected over 700,000 reports a year yet was found, by the UK
Department of Health's own review, to deliver essentially no actionable
learning about patterns or root causes of harm — despite comparable
institutional investment.

Pasquini et al. trace the difference to five structural characteristics of
the domain itself, independent of the reporting system's own design:

1. **The pass criterion** — how easily a reportable incident can be
   factually distinguished from a non-event or normal operation, without
   subjective judgment. Aviation operators share a clear consensus on
   severity and event boundaries. Healthcare cannot cleanly separate harm
   caused by the care process from harm caused by the underlying disease
   itself — the same fact requires complex clinical judgment to classify at
   all, before it can even be reported consistently.
2. **Degree of standardisation** — using Kenneth Burke's pentad (act, agent,
   scene, means, purpose) as a description checklist: in a highly
   standardised domain, scene, tools, and operational context can stay
   implicit in a report because every reader shares the same background
   assumptions. In an unstandardised domain — emergency care looks nothing
   like elective surgery — scene, tools, and rationale all have to be
   spelled out explicitly for a report to be interpretable at all, which
   raises the burden on every single reporter.
3. **Visibility** — whether front-line operators are actually positioned to
   observe the full event sequence and its contributing factors. Invisibility
   arises from how the process itself is designed, from work being spread
   across shifts and locations, and — in healthcare specifically — from the
   patient's own internal physiological dynamics being invisible to anyone
   outside the patient. Where visibility is structurally low, routine safety
   surveys that actively elicit front-line risk perception are recommended
   to complement (not replace) incident reporting.
4. **Characteristics of the community of practice** — a homogeneous
   professional community (aviation pilots and controllers) shares
   standardised language, definitions, and mutual trust, which is what makes
   one nationwide reporting scheme with one analyst body workable at all.
   Healthcare's diverse micro-communities, each with its own terminology and
   priorities, instead require localised reporting systems, multidisciplinary
   analyst teams with domain-specific clinical expertise, and feedback loops
   tailored to each micro-culture rather than one generic loop for
   everyone.
5. **Safety culture** — evaluated across [Westrum's five culture
   levels](westrum-typology.md). Higher levels of safety culture can support
   open, confidential systems with named reporting and active follow-up
   investigation. Lower levels require strict confidentiality or full
   anonymity specifically to protect reporters from punitive action — the
   same mechanism [blame suppresses reporting](blame-suppresses-reporting.md)
   describes generally, here determining which *design* of reporting system
   a given culture can even sustain, not just how much reporting happens
   within a fixed design.

**Two further, independently-stated prerequisites cut across all five
dimensions.** Citing ASRS co-founder C. O. Billings: a reporting scheme only
works where there is a demonstrated, tangible, and widely *agreed-upon need*
for better safety information across every stakeholder group, and where
there is genuine *mutual consensus* among the professional communities
involved about what the system's goals are, how the data will be used, and
what its operational definitions actually mean. Both are properties of the
domain's culture and cohesion, not features that a well-written reporting
form can manufacture on its own.

**The design implication is a decision rule, not just a diagnosis.** Where a
domain scores well on the pass criterion and standardisation — factual
distinction between reportable and non-reportable events is clear — reactive
incident reporting on the accident-risk continuum works as designed. Where
outcomes are ambiguous, contexts are unstandardised, or visibility is low,
the same reactive design will underperform regardless of investment, and the
domain needs to shift toward eliciting subjective operator risk perception
directly and continuously instead — the move [proactive risk
monitoring](safety-control-upward-and-downward-forces.md) and [pinging](pinging-proactive-risk-probing.md)
both make. Practically, this reframes reporting-system design along three
continua rather than as a single fixed choice: from accidents toward risks
as the outcome focus, from specific events toward contextual scenes as the
descriptive scope, and from localised/departmental toward domain-wide as the
organisational scale — where a given domain sits on all three should track
its scores on the five dimensions above, not be decided independently of
them.
