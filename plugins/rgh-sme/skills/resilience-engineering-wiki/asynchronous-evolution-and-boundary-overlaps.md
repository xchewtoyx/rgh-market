---
type: concept
title: Asynchronous Evolution and Boundary Overlaps
description: >
  Two structural ways a control system's parts fall out of sync with each
  other — overlapping control zones producing ambiguous or conflicting
  authority, and one subsystem changing without a corresponding update to
  the controllers and assumptions built around it.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 8"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 15"
---

Two distinct ways a [STAMP control
structure](stamp-hierarchical-control-structure.md) can fall out of internal
sync, beyond any single controller holding [a flawed process
model](flawed-process-models-in-control-theoretic-accidents.md):

- **Boundary overlaps**: when two or more decision-makers' control zones
  overlap without a clear resolution rule for which one governs, the
  ambiguity itself produces conflicting actions — not because either
  decision-maker acted unreasonably within their own zone, but because
  nobody's process model of the boundary matched the other's.
- **Asynchronous evolution**: one subsystem changes — a trajectory
  parameter, a hardware procedure — without a corresponding update to the
  controllers, assumptions, or related subsystems built around the old
  version. The change is often entirely correct and well-justified in
  isolation; the accident lives in the gap between the part that changed and
  the parts that were never told.

**Ariane 5**'s destruction on its maiden flight is the canonical asynchronous-
evolution case: guidance software reused from Ariane 4 assumed a trajectory
profile within Ariane 4's flight envelope, and Ariane 5's genuinely
different, faster trajectory produced a horizontal-velocity value the
software's numeric range could not represent, triggering an overflow that
was handled as a processor shutdown. The software was not defective relative
to the assumptions it was written under — the rocket's own dynamics
evolved out from under it. The **SOHO** spacecraft's loss followed the same
shape from a procedural direction: a gyroscope spin-down procedure was
changed as part of a calibration sequence, and a related safeguard built
around the old procedure was not updated to match, leaving the spacecraft
without protection during a manoeuvre the new procedure made newly risky.

Both failure shapes point to the same design implication: a control
structure's safety is not a static property to certify once, because any
change to one part of a coupled system can silently invalidate an
assumption baked into another part that nobody thought to revisit — the
sociotechnical-system analogue of [structural secrecy and cross-unit
practical drift](structural-secrecy-and-practical-drift.md), where here the
un-reconciled divergence is between an engineering artifact and its
surrounding assumptions rather than between two human work groups.

**A third pattern is the mirror image of a boundary overlap: a boundary
gap**, where no decision-maker's control zone covers an interface at all,
rather than two zones covering it in conflict. The Dutch High Speed Line
signalling project shows this concretely: under a public-private
partnership, competing industrial consortia developed interoperating
signalling components concurrently rather than sequentially, and no actor
was ever designated as **systems integrator** responsible for the overall
system's coherence. Interfaces across hardware, software, and contractual
boundaries went structurally unmanaged — not overlapping and contested, but
simply nobody's job — and the gap surfaced downstream as concrete technical
failure: deploying one contractual signalling-software version while a
newer one became the de facto standard elsewhere in the system, and
cross-border interfaces between different consortia's systems requiring
expensive custom gateways built after the fact to bridge a compatibility
gap nobody had owned preventing. A boundary overlap and a boundary gap are
opposite failures of the same underlying requirement — that every interface
in a coupled system needs exactly one party accountable for it — and a
control structure has to be checked for both, not just the overlap case.
