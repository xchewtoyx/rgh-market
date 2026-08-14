---
type: concept
title: Layered Defence in Depth
description: >
  Stack multiple independent preventive and mitigating controls so a breach
  at one layer triggers tactical retreat to the next rather than total
  failure, with each deeper layer accepting more damage but saving what can
  be saved.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 2 (Jean Pariès)"
---

A single control — one reminder, one routine, one environmental fix — leaves
no answer when that control fails under stress. **Defence in depth** stacks
independent layers, each addressing the same hazard at a different point:
reduce frequency, absorb impact without damage, continue with degraded
function, retain enough control to reach a safe outcome, and finally
minimize harm at the end. Moving through the layers is a **tactical
retreat**: sights are lowered, sacrificing decisions are made to save what
can be saved. Each step is more improbable, more variable, less
controllable; damage probability rises, response options shrink, and
choices become harder to reverse — a shift from adaptation toward
de-adaptation.

Design layers explicitly rather than hoping one strong control covers
everything. Examples in personal reliability: [environmental sensory
accommodation](environmental-sensory-accommodation.md) plus a [launch pad
bag](launch-pad-bag.md) spare; [importance-urgency triage
criteria](importance-urgency-triage-criteria.md) plus a [demand triage
traffic-light system](demand-triage-traffic-light-system.md) plus
[pre-stocked low-energy fallback](pre-stocked-low-energy-fallback.md);
[premortem procedure](premortem-procedure.md) plus [contingency rehearsal
scripts](contingency-rehearsal-script.md) for what the premortem surfaces.
Each layer should work even if the one above it failed.

No stack eliminates tail risk — some events exceed every designed layer
(simultaneous engine failure in the aviation source). The goal is not
perfection but **strategic resilience**: enough depth that routine and
anticipated failures are absorbed, and rare extremes still have a last line
rather than nothing.
