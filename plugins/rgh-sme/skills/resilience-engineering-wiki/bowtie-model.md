---
type: concept
title: The Bowtie Model of Resilience
description: >
  A risk diagram centred on a single loss-of-control event, with threat
  detection and avoidance on one side and recovery, mitigation, and
  containment on the other — used to show that resilience spans both
  directions, not just post-event recovery.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 3"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 18"
---

The bowtie model (Visser, 1998) diagrams risk as two triangles meeting at a
single central node: a loss-of-control event. The **left-hand side** fans
out backward from that event into the threats and pathways that could lead
to it, and the barriers meant to detect and avoid each one before it
happens. The **right-hand side** fans out forward from the same event into
its possible consequences, and the barriers meant to recover, mitigate, or
contain them once the event has already occurred.

The diagram's usefulness for resilience specifically is what it makes
visually unavoidable: resilience is not only what happens on the right-hand
side. A definition of resilience that stops at "bouncing back" — restoring
production after a fire, rebuilding trust after a leak, mobilising
emergency crews after an outage — only covers the recovery half of the
bowtie. The left-hand side (dynamic boundary control, active threat
detection, avoidance before the central event occurs) is resilience too,
and arguably the more valuable half, since it is what keeps the central
loss-of-control event from happening at all. This maps directly onto
[Rasmussen's boundary model](rasmussen-boundary-model.md): the left side of
the bowtie is the ongoing work of staying clear of the safety boundary, and
the central event is what crossing it looks like.

The bowtie's structure is also a useful diagnostic for which of [the four
abilities of resilient performance](four-abilities-of-resilient-performance.md)
a given organisational effort actually addresses: anticipation and
monitoring live entirely on the left-hand side, response lives on the
right, and an organisation that has invested heavily in one side while
neglecting the other has an asymmetric bowtie — strong at avoidance and weak
at recovery, or vice versa — that an aggregate safety-record metric will not
reveal, for the same reason [Woods's eight
criteria](eight-criteria-of-organizational-resilience.md) score an
organisation criterion by criterion rather than producing one number.

**A barrier on either side of the diagram is only a barrier if it is
functionally complete.** Hale, Guldenmund & Goossens define a barrier as a
dynamic control device that must perform three linked steps — **detect,
diagnose, act** — not as a static object drawn on the diagram. A warning
sign, an alarm, or a readout is only a *barrier element*; it becomes an
actual barrier only once coupled to a response capable of interpreting it
and acting on it in time. Auditing "is the barrier present" therefore has
to mean auditing whether all three steps are functioning together, not
whether the detecting element exists — an alarm nobody is positioned to
diagnose or act on in time is, functionally, no barrier at all, even though
it will show up as present on an inventory of safety equipment.
