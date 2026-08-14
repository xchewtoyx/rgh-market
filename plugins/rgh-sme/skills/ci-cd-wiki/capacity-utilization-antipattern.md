---
type: concept
title: Capacity Utilization and Lead Time
description: >
  As a team or system's resource utilization approaches 100%, queuing theory
  predicts lead time approaches infinity — so driving utilization up is
  counterproductive to reducing delivery lead time, unlike in manufacturing.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 2"
---

# Capacity Utilization and Lead Time

Manufacturing management practice optimizes machine utilization, because idle
machinery is pure waste. Applying the same instinct to software delivery
teams is a mistake: queuing theory says that as utilization (U) approaches
100%, lead time (L) approaches infinity. A fully utilized team has no slack
to absorb variability — an urgent bug, an unplanned production incident, a
blocked teammate needing help — so any new arrival has to queue behind
everything already committed, and queue time dominates
[cycle time](cycle-time.md).

The practical implication for pipeline and team design: preserving slack
capacity is not waste, it's what keeps lead time bounded. This is directly
relevant to [value stream mapping](value-stream-mapping.md): a bottleneck
stage running near 100% utilization (a shared test environment everyone
queues for, a single reviewer who's the sole approver) is a lead-time problem
even if that stage's own "utilization" metric looks efficient.
