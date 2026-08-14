---
type: concept
title: Scheduling Isolated Blocks Underestimates Cumulative Load
description: >
  Planning each demand as a standalone block without modeling how
  deficits accumulate across a sequence systematically under-counts
  end-of-period fatigue and recovery need.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 6 (FRMS Structure and Implementation)"
---

Fatigue risk from a demanding block depends not only on that block's
intrinsic load but on **where it falls in the sequence**. Aviation roster
analysis found the same reduced-rest pattern produced widely different
fatigue-risk scores depending on whether it occurred early in the week or
after several prior shortfalls — a cumulative effect planners often missed
because rosters were scheduled as "isolated blocks," each evaluated on its
own merits without chaining prior deficits forward.

The personal-capacity parallel is familiar: a late-week social event, travel
day, or deadline crunch may be affordable in isolation but unaffordable
after three nights of short sleep and back-to-back masking. A calendar that
green-lights each entry without asking "what is already depleted going
into this?" will reliably overbook the end of a cycle and under-schedule
recovery. See [acute and chronic fatigue](acute-and-chronic-fatigue.md)
for how repeated small shortfalls compound, and [proactive recovery
scheduling](proactive-recovery-scheduling.md) for placing recovery gaps
before the sequence hardens rather than after collapse.

Fatigue factors also **interact**: reduced rest plus poor sleep environment
plus long duty is worse than any factor alone — the combination must be
evaluated, not summed as independent line items. The same logic applies
across dimensions in a [cross-dimensional saturation
cascade](cross-dimensional-saturation-cascade.md).

When people are already fatigued, compensatory strategies (extra
cross-checks, more automation, heightened vigilance) can add workload
rather than subtract it — raising total demand at the moment capacity is
lowest. That is a signal to prefer **suppression** (remove or defer the
exposure) over **barriers** (push harder through compensatory effort);
see [precommitted demand-shedding](precommitted-demand-shedding.md) for
deciding drops ahead of time while headroom remains.
