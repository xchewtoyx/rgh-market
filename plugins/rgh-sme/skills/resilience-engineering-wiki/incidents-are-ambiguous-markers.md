---
type: concept
title: Incidents Are Ambiguous Markers of Adaptive Capacity
description: >
  A recovered incident is simultaneously evidence a system successfully
  stretched to absorb disruption and evidence of how close it came to a
  fracture point — the same episode supports both readings at once.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 6"
---

Judging a system's resilience from its incidents runs into a structural
ambiguity that no amount of additional incident data resolves on its own.
Every finite system has boundary conditions on its adaptive capacity, so an
incident that gets absorbed without becoming a disaster is, at the same
time, both a demonstration that the system's adaptive capacity worked *and*
a data point on exactly how close that capacity came to running out. Reading
it as pure success story misses the second half; reading it as pure early
warning misses the first. And an incident that *does* reach breakdown does
not automatically prove the system is generally brittle — a sufficiently
large disruption can push any finite system past its ultimate limit without
that meaning the system's ordinary adaptive capacity was inadequate.

A hospital medication near-miss shows the pattern from the failure side:
a cross-checking mechanism broke down and an erroneous treatment plan nearly
reached a patient — a local failure of resilience by any account. But
analysing *why* it nearly failed surfaced the actual resilience mechanism
that had been quietly working in every other case: experienced frontline
staff with both the clinical knowledge and the organisational standing to
challenge a physician's order. The failure case is what made that mechanism
visible enough to design around deliberately, rather than leaving it as an
unexamined, undercredited habit.

A hospital pharmacy software outage shows the pattern from the recovery
side. A computer failure pushed inaccurate medication plans hospital-wide;
nurses recognised the error was systemic rather than a one-off, and
improvised a manual paper-and-fax workaround with pharmacy staff and
physicians that held for a 24-hour outage with zero patient harm. Read only
by its outcome, this is an unambiguous resilience success — human
adaptiveness, not any technological redundancy, is what actually recovered
the system. Read as a marker instead of an outcome, the same incident
exposed *growing brittleness*: management had been treating human staffing
buffers as pure inefficiency and pushing toward paperless operations, both
of which were quietly eroding the exact manual-fallback experience that had
just saved the day. The zero-harm outcome and the brittleness trend were
both true, from the same 24 hours.

**The practical implication is what to treat as the unit of analysis.**
Neither "did it succeed" nor "did it fail" is the right question on its own;
the useful unit is the system's *pattern of response* to a class of
disruption — which pools of adaptive capacity it drew on, how far into them
it had to reach, and what would have had to be different for the reach to
come up short. Building that picture requires an explicit model of the
adaptive behaviour in question (a cross-checking process, a
[decompensation](decompensation.md) signature) with stated operational
limits, not a running tally of successes and failures. This is the same
move [Safety-II](safety-i-and-safety-ii.md) makes at the level of everyday
work, applied specifically to the incidents an organisation already has
records of.
