---
type: concept
title: Leading and Lagging Indicators Are Level-Relative
description: >
  Whether a given metric counts as leading or lagging is not a fixed property
  of the metric — it depends on which control level is using it and over
  what response timescale, so the same number can be lagging locally and
  leading systemically at once.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 5"
---

The pragmatic definition of the leading/lagging distinction is functional,
not categorical: a **leading indicator** is one that arrives in time for
management or operators to act and forestall or mitigate an unwanted
outcome; a **lagging indicator** reflects a change in a core output that has
already happened. Framed this way, the classification is not a fixed label
a metric carries with it — it depends on the control level consuming it
(local operational versus system-wide) and the response timescale available
at that level.

The same number can be both at once, read from two levels simultaneously. A
spike in short-term fatigue-related injuries during a high-demand surge is a
**lagging** indicator at the fast, local operational level — the fatigue
already happened and the injuries already occurred; nothing at that level
can undo them. But the identical spike is a **leading** indicator for a
higher, slower control level whose response timescale is measured in
staffing cycles or process redesigns rather than shifts: it arrives in
plenty of time to expand baseline headcount or redesign the surge process
before the *next* comparable demand spike hits. Classifying an indicator
correctly requires specifying all three of the intended control action, the
organisational decision level it feeds, and the intervention timing
available at that level — not the indicator alone (Hopkins, 2009a, 2009b;
Hale, 2009; Wreathall, 2009).

The practical consequence for [selecting an
indicator](criteria-for-selecting-safety-indicators.md): a metric dismissed
as "merely lagging" at the level where it was first noticed may be exactly
the leading indicator a level above needs, and building a monitoring system
around a single fixed leading/lagging taxonomy will misclassify indicators
that are doing real anticipatory work one level up.
