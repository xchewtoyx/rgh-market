---
type: concept
title: Factor Combination Risk Matrix
description: >
  Identify contributing factors from a checklist, then evaluate risk from
  their combinations — not from any single factor in isolation — using a
  matrix that maps factor severity to situation criticality.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 6 (Philippe Cabon et al.)"
---

A single stressor often does not predict failure; combinations do. Reduced
rest alone may be manageable; reduced rest plus poor sleep environment plus
a long duty sequence is a different risk class. The control has two parts:

1. **Factor identification** — maintain an adapted checklist of intrinsic
   and contextual contributors (sleep, timing, workload, environment,
   commuting, personal factors). No universal weighting; tune the list to
   the person's actual failure modes.
2. **Combination evaluation** — estimate probability of reaching a harmful
   state from the *joint* profile, then map that to situation criticality
   (normal, abnormal, emergency per [operating envelope control
   shift](operating-envelope-control-shift.md)). High fatigue risk plus
   high-consequence context → highest priority for [suppression-reduction-
   barrier mitigation](suppression-reduction-barrier-mitigation-hierarchy.md).

Subjective scales and brief self-report instruments (sleep logs, validated
fatigue scales) weight model estimates when generic checklists miss
domain-specific load. Update the matrix after significant life or schedule
changes, not only after incidents.
