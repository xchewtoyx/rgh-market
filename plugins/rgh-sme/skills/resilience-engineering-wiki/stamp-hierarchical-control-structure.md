---
type: concept
title: STAMP's Hierarchical Control Structure
description: >
  Leveson's STAMP models a sociotechnical system as two parallel control
  hierarchies (development and operations) linked by a downward reference
  channel and an upward measuring channel — and shows how severing the
  upward channel blinds the higher levels even while operations continue.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 8"
---

Under [STAMP](systems-theoretic-accident-model.md), a sociotechnical system
is built from two parallel control hierarchies — one governing system
development, one governing system operations — with safety constraints
imposed downward from each higher level onto the level below it. The link
between any two adjacent levels always runs both ways: a **reference
channel** carries policies, standards, and safety constraints down from the
higher level, and a **measuring channel** carries feedback — status reports,
incident logs, evidence of whether the constraints are actually being met —
back up. Control between levels is exercised both **directly** (management
oversight, direct intervention) and **indirectly** (policies, procedures,
shared values, culture) — the indirect channel is what lets a large
hierarchy scale without every constraint being enforced by direct
supervision at every level.

**Control structures degrade over time**, not just in a single dramatic
break. The Walkerton, Ontario water-contamination accident is the case: a
privatisation decision replaced government water-testing labs with private
ones, and the private labs were not mandated to report bacterial
contamination findings to the public-health oversight authority. This
severed the *upward* measuring channel specifically — the reference channel
(regulations, standards) stayed formally intact, but the feedback that would
have told regulators the standards were being violated simply stopped
arriving. Regulators were not overruled or defied; they were blinded,
continuing to operate on a process model that assumed reporting was still
happening. This is a concrete, structural instance of the same erosion
[drift into failure](drift-into-failure.md) describes narratively and
[Rasmussen's boundary migration](rasmussen-boundary-model.md) describes
spatially: here it is specifically the measuring channel of a hierarchical
control structure that eroded, which is why Leveson's own remedy is to track
the control structure as designed against the control structure as actually
operating at intervals over time, rather than inferring its health from
whether the reference channel (the rules) still looks intact on paper.
