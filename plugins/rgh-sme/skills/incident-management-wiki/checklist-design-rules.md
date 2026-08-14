---
type: concept
title: Checklist Design Rules
description: How to design a checklist that survives actual use under stress — the format constraints, the two execution modes, and how to choose which items make the list.
sources:
  - title: "The Checklist Manifesto"
    resource: "The Checklist Manifesto: How to Get Things Right (Atul Gawande), Introduction, ch. 1, ch. 2, ch. 3, ch. 4, ch. 5, ch. 6, ch. 7, ch. 8"
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 13"
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan), ch. 2"
---

To be effective under stress, a [runbook or checklist](runbooks-and-checklists.md) must be:
* **Concise and Focused**: Limit items to **5 to 9 "killer items"**—high-impact safety steps that are easily forgotten but catastrophic to omit.
* **Time-limited**: Taking no more than **60 to 90 seconds** to execute. If it is longer, operators will skip it.
* **Simulation-tested**: Iteratively refined and verified in staging, simulators, or drills.
* **Visually Ergonomic**: Easy to read under night or high-stress emergency conditions (uncluttered, sans-serif font).

## Execution Modes
Checklists are executed in one of two modes:
1. **DO-CONFIRM**: Operators perform tasks from memory and experience independently, then pause at a designated threshold to confirm that all critical safety checks were completed.
2. **READ-DO**: Operators read the steps aloud and execute them sequentially (the "recipe" model).

DO-CONFIRM is generally preferred where the operator already knows the
workflow (it preserves speed by only interrupting to verify, not to
dictate each step); READ-DO fits situations where sequence itself is
unfamiliar or error-prone enough that reading each step aloud matters more
than speed. Whichever mode is chosen, checks should be a spoken team
exchange, not a silent solo read of a paper form — the verbal
call-and-response is itself a communication forcing function, not just a
memory aid.

## Selecting Which Items Make the List
A checklist's real design work is deciding what to leave out, not what to
include — brevity is what keeps it inside the 60-90 second budget. Weigh
each candidate item on frequency **and** severity together, not either
alone: a low-frequency but high-severity, fast-to-check item (e.g.,
confirming the correct patient and surgical site) earns its place despite
rarely triggering, because the cost of a miss is catastrophic and the
check itself is nearly free. An item that would meaningfully slow the
checklist down for a failure mode that's both rare *and* geographically or
organizationally irrelevant to the team using it is a reasonable cut, even
if it has some plausible benefit in the abstract — checklists that try to
cover every possible failure stop getting followed at all. The WHO Safe
Surgery Checklist's global pilot (8 hospitals, ~4,000 patients before/after)
found a 36% reduction in major complications and a 47% reduction in
mortality from applying this kind of disciplined 19-item list — evidence
that a short, well-chosen checklist beats a longer, more exhaustive one in
practice.
