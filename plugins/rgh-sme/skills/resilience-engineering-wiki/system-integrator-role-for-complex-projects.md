---
type: concept
title: The System Integrator Role
description: >
  Once a project's core technology matures past the point where incremental
  engineering can keep delivering gains, resilience requires an explicit,
  dedicated role responsible for the coherence of the whole system across
  technical, managerial, and institutional domains — a role no single
  discipline's expertise covers.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 15"
---

Technology acts as the flywheel of progress early in a project or a
paradigm's life, but it eventually matures into a saturated state where
further gains require conceptual-level innovation rather than incremental
refinement of the existing approach — the same saturation point [the
master-coupling-paradigm life cycle](master-coupling-paradigm-life-cycle.md)
describes at the scale of an entire industry's core technology, here applied
to a single complex project.

At that saturation point, resilience stops being something any single
technical or managerial discipline can deliver on its own. A complex project
needs an explicit, dedicated **system integrator** (or system architect)
role: someone whose actual job is the coherence of the *whole* system —
technical, managerial, and institutional — rather than the excellence of any
one part of it. This is a deliberate organisational design choice, not a
title added after the fact to whoever happens to be senior; without it, no
one is actually responsible for the interfaces and interdependencies
*between* the technical, managerial, and institutional pieces, only for the
pieces themselves.

Building resilience proactively into a system at design time — rather than
letting it emerge, if it emerges at all, only once the system is mature and
operational — requires the system integrator role alongside a broadened
design solution space: moving analysis from form to function, from
performance to properties, from components to context, and from a single
artefact's design to the design of the overall system architecture around
it. Practically, this means combining technological innovation with
organisational and institutional reform together, rather than treating
technical redesign and organisational redesign as separate projects that
happen to run in parallel — exactly the multi-actor, multi-aspect
integration [three design phases of resilient
systems](three-design-phases-of-resilient-systems.md) argues has to span a
system's entire life cycle, not just its final assembly.
