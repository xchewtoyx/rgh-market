---
type: concept
title: Decremental Drift in Maintenance Intervals
description: Repeatedly stretching a maintenance or inspection interval in small, individually-justified steps can silently erode a system's real safety margin, because each step looks locally reasonable and "nothing broke" is mistaken for proof the new interval is safe.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 1-2"
---

A maintenance interval — how often a part gets lubricated, inspected, or replaced — rarely gets relaxed in one large, scrutinized jump. It erodes through many small steps, each approved on its own reasonable-sounding grounds (a busier schedule, a cost target, "the last several checks all came back fine"). No single step looks like a violation, and each one is empirically "successful" in the sense that nothing broke afterward. But the interval a decade later can be an order of magnitude looser than the original, with no single decision point where anyone weighed that full cumulative change against the original safety margin.

## Why "Nothing Broke" Doesn't Mean "Safe"

Treating a stretched interval's apparent success as evidence it was a sound decision inverts cause and effect: the absence of failure so far may just mean the part hasn't yet reached the point where the missing margin matters, not that the margin was unnecessary. The real risk this creates is arithmetic as much as physical: missing one lubrication cycle on a part serviced every 300 hours is a minor gap; missing one cycle on the same part serviced every 2,500 hours is a much larger, more dangerous gap — the interval's own stretching is what manufactures the system's sensitivity to a single missed or degraded check, independent of any one person's competence or diligence.

## Why It's Invisible While It's Happening

Each individual extension is judged only against the interval immediately before it, not against the original baseline — so the gap between "yesterday's accepted practice" and "today's" is always too small to be worth flagging or investigating on its own. This is what makes the drift structurally undetectable from inside the process that's producing it: nobody experiences a moment of "we are now taking on much more risk than before," because no single step ever presented that choice explicitly.

## Implications for Maintenance Documentation

- **Track the interval's full history, not just its current value**: a maintenance schedule that only records the present interval loses the information needed to notice that it has drifted far from where it started. Record each revision alongside its stated justification, so a future maintainer reviewing the schedule can see the cumulative shape of the drift, not just its latest snapshot.
- **Re-anchor periodically to the original rationale, not just the previous value**: when a new relaxation is proposed, compare it against the interval's original basis (the design assumption or test data that justified the first number), not merely against whatever the interval happens to be today — the latter comparison is exactly what makes each step look reasonable in isolation.
- **Treat a long unbroken record of "no failures" on a loosened interval as inconclusive, not reassuring**: this is the same caution as [Rehearsing Rare Procedures with Deliberate Drills](rehearsing-rare-procedures-with-drills.md) — a procedure or interval that hasn't been tested against its real limit recently doesn't have confirmed margin, whatever its track record so far suggests.

This is a different failure mode from [Unauthorized Substitution Change Control](unauthorized-substitution-change-control.md): there, a single deviation silently violates a hidden design assumption. Here, every individual step is properly reviewed and approved — the danger is entirely in the accumulation across many separately-reasonable steps, none of which was ever evaluated against the full distance already traveled from the original baseline.
