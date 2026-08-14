---
type: concept
title: Cumulative Exposure Scheduling
description: >
  Evaluate load and recovery across a sequence of demands, not as isolated
  blocks, because effects accumulate and late-sequence exposure is often
  higher risk than the same exposure early.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 6 (Philippe Cabon et al.)"
---

Scheduling or assessing demands one block at a time — "this shift looks
fine on its own" — misses cumulative wear. The same reduced-rest pattern
carries different fatigue risk depending on where it falls in a weekly
sequence: early-week exposure may be absorbable; the same pattern at the
end of a demanding sequence can push past a critical threshold. Treating
each block as isolated is a common planning failure.

When designing personal schedules, commitments, or control stacks, map the
**sequence**, not just individual events: stack recovery before predictable
peaks; avoid clustering high-cost items at the end of a run without
buffer. [Full calendar capture](full-calendar-capture.md) makes cumulative
load visible; [demand triage traffic-light
systems](demand-triage-traffic-light-system.md) help shed load when the
sequence is already overloaded. [Efficiency-flexibility control
tradeoff](efficiency-flexibility-control-tradeoff.md) applies here too: a
schedule optimized block-by-block can be brittle across the week.
