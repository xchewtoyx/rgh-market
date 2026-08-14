---
type: concept
title: Architecture as Structures for Reasoning
description: >
  Software architecture is the set of structures needed to reason about a
  system — its elements, relations among them, and properties of each —
  and a system normally has several such structures at once.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Architecture is not a single diagram or a single decomposition. It is the
set of structures a system needs so that stakeholders can reason about it:
elements, the relations among those elements, and properties of both. A
system has several of these structures simultaneously — how it is divided
into modules is a different structure from how its runtime processes
communicate, which is different again from how its pieces are deployed
onto hardware. Treating threads, objects, source modules, and files as
interchangeable "the architecture" damages both the design work and the
documentation of it, because a decision that is sound in one structure can
be invisible or wrong in another.

This is why architecture documentation is organized around multiple
[views](view-and-viewpoint.md), each presenting one structure for one set
of stakeholder concerns, rather than one master diagram trying to show
everything. The three broad families of structure are module views (code-time
decomposition, see [module views](module-view.md)), component-and-connector
views (runtime structure, see
[component-and-connector views](component-and-connector-view.md)), and
allocation views (mapping software onto non-software structures such as
hardware or teams, see [allocation views](allocation-view.md)).

Architecture matters because it is what makes quality attributes possible
or impossible: performance depends on concurrency, communication, and
bottleneck choices; security depends on usage and communication
constraints; modifiability depends on separated concerns; incremental
delivery depends on untangled dependencies. Documentation exists to record
which structures were chosen, and the argument that those choices meet the
system's requirements — see
[architecturally significant decisions](architecturally-significant-decision.md).
