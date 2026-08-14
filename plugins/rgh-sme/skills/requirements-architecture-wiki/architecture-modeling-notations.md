---
type: concept
title: Architecture Modeling Notations
description: >
  UML, SysML, and architecture description languages (ADLs) are notations
  for architecture documentation, not methods — each still needs an
  explicit viewpoint, naming conventions, and defined relation semantics
  to be useful.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), Appendices A-C"
---

UML is a versatile notation, not an architecture-documentation method in
itself. The same UML construct can mean different architectural things in
different contexts — a package diagram can document a
[module view](module-view.md), a component diagram a
[component-and-connector view](component-and-connector-view.md), a
deployment diagram an [allocation view](allocation-view.md), and
sequence/activity/state/use-case diagrams
[behavior](behavior-documentation.md) — so each diagram needs a declared
architectural meaning, element types, relation semantics, and a legend or
profile; visual resemblance between two diagrams is not evidence they mean
the same thing.

SysML extends UML for systems engineering, adding blocks and internal
block diagrams for parts/connections, requirements diagrams with explicit
relations (satisfy, verify, derive, refine) that can trace requirements to
design, and cross-domain allocation covering hardware, software, and
people in one model. Architecture description languages (ADLs) go further
still, giving components, connectors, configurations, interfaces, types,
properties, and constraints explicit, sometimes formal semantics —
enabling analysis, consistency checking, and simulation, at the cost of
modeling discipline and tool-learning overhead.

None of the three substitutes for the rest of the documentation package:
an ADL model, like a UML or SysML diagram, still needs to sit inside a
package with context, rationale, and decisions explained in reader-facing
terms (see [architecture documentation
package](architecture-documentation-package.md)) — notational precision
alone does not provide sufficient explanation on its own.
