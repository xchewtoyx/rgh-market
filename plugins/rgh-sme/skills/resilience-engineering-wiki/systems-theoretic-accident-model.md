---
type: concept
title: Systems-Theoretic Accident Model
description: >
  Control-theoretic models (Leveson's STAMP, Perrow) treat safety as an
  emergent property of the whole system and accidents as erosion of control
  over component interactions, not as component failures.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 5"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 3"
---

Systems theory abandons the search for broken parts. Its core principles:

- **Emergence**: safety is an emergent property of the entire system in
  operation — no individual component "has" safety, so inspecting components
  one by one (as the [Swiss cheese model](swiss-cheese-model.md) does) cannot
  establish whether the system is safe. See [emergence](emergence.md) for the
  formal resultant-vs-emergent distinction this rests on.
- **Control and constraints**: accidents result from an *erosion of control*
  over the safety constraints that govern component interactions, under
  dynamic [goal conflicts](goal-conflicts-and-production-pressure.md). This is
  the basis of Leveson's STAMP (Systems-Theoretic Accident Model and
  Processes): safety management is a control problem — enforce constraints and
  make goal trade-offs visible — not a failure-prevention problem.
- **Normal accidents (Perrow, 1984)**: in systems that are both interactively
  complex and tightly coupled, system accidents occur *without any component
  failing* — they are a normal by-product of unforeseeable interactions. The
  founding case is Perrow's own analysis of Three Mile Island: no single
  investigator, however expert, could fully predict the reactor's behaviour
  across circumstances, and once the partial meltdown began, the failure
  cascaded unpredictably along whichever path of least resistance the tightly
  coupled plant happened to offer — not along a path any designer had
  anticipated or any single fix could have interrupted. The emblematic
  domestic-scale example: a cracked coffee-maker water tank leaking until a
  flight engineer's outflow valve froze. **Interactive complexity** specifically means
  component interactions that are non-linear, unfamiliar, or unplanned, and
  not immediately comprehensible to the people running the system — contrast
  linear interactions, which are expected and visible even when unplanned.
  Software is what most reliably pushes a system from merely [complicated
  into genuinely complex](complicated-vs-complex-systems.md): a
  collision-avoidance system with on the order of 10^40 possible states, or a
  radiation-therapy machine (Therac-25) whose fatal timing-dependent state
  mismatch involved no single out-of-spec component, are both cases where
  nothing had to "break" for the accident to occur.

**Concurrence** is the systemic view's alternative to a causal chain:
catastrophic outcomes typically arise from several individually ordinary
events or conditions simply co-occurring in time, rather than from one event
propagating along a traceable path. This is why [tree-based risk-assessment
tools](structural-limits-of-tree-based-risk-assessment.md) — built to
represent a fixed structural path from cause to effect — cannot represent
the systemic view even when the analyst wants them to; the co-occurrence a
systemic model needs to capture is not known in advance, so it cannot be
drawn into a tree ahead of time. The moment-to-moment version of "control
held or lost" is [dynamic stability](dynamic-stability-and-damping.md):
whether the ordinary variability behind concurrence gets damped locally or
allowed to compound.

Leveson's own hierarchical control model gives this erosion a concrete
measurement method: take sequential snapshots of the control structure as
designed versus the control structure as actually operating, at intervals
over time, rather than a single before/after comparison at the point of an
accident. Compared serially, these snapshots expose the gradual erosion of
control loops directly — which oversight relationships have quietly stopped
functioning — making visible the same process [drift into
failure](drift-into-failure.md) describes qualitatively, but as a trackable
structural record rather than a narrative reconstructed only after the
fact.

Consequences for investigation and design:

- Asking "which component failed?" (or "which human erred?") is the wrong
  question; ask which constraints stopped being enforced and how the control
  structure lost the ability to see that.
- Systems exist to deliver goods, services, and profit — not to be safe — so
  constraint erosion under production pressure is the default trajectory, not
  an anomaly. NASA's 1990s "Faster, Better, Cheaper" era eroded launch checks
  and lost both the Mars Climate Orbiter and the Mars Polar Lander.
- The temporal version of this erosion — how a system migrates toward its
  safety boundary over years while everything looks fine — is [drift into
  failure](drift-into-failure.md).

STAMP's own internal machinery for describing how control is exercised and
lost goes deeper than the principles above: see [STAMP's hierarchical
control structure](stamp-hierarchical-control-structure.md) for the
downward reference channel and upward measuring channel between levels,
[flawed process models](flawed-process-models-in-control-theoretic-accidents.md)
for how a controller's own working model of the system can silently diverge
from reality, and [asynchronous evolution and boundary
overlaps](asynchronous-evolution-and-boundary-overlaps.md) for how parts of
a control structure fall out of sync with each other.
