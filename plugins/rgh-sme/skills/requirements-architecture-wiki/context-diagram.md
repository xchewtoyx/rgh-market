---
type: concept
title: Context Diagram
description: >
  A context diagram fixes the boundary of a system or business area under
  study, showing the external entities it interacts with and the precise
  meaning of each interaction crossing that boundary.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 6"
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 3"
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 7"
---

A context diagram identifies the boundary of the thing being studied — a
business area (a **Work Context Diagram**, in requirements work: a central
oval representing "the Work," with terminators for adjacent systems,
departments, and external entities, connected by arrowed data flows) or a
software system (an architectural context diagram: external entities,
external interfaces, and the system boundary). Both are the same
underlying technique applied at different stages: fix what is inside the
boundary before trying to describe or decompose it, and make every
crossing of that boundary explicit.

The arrows are the part that carries the actual information, and they
require precise semantics — a line between two boxes that doesn't state
what kind of interaction it represents (a data flow, a dependency, a call)
is decoration, not documentation. See [descriptive
completeness](descriptive-completeness.md) for the general principle this
follows from.

A context diagram drawn once and then left alone goes stale as the system
evolves. A **living services diagram** — discovered automatically from
which services are actually running and their declared metadata, rather
than hand-maintained — is one concrete way to keep a context/component
view current with deployment instead of trusting a drawing that was
accurate on the day it was made; see [code as architecture
documentation](code-as-architecture-documentation.md) for the broader
technique and its limits. For requirements elicitation specifically, the
Work Context Diagram is produced during [project
blastoff](project-blastoff.md) and is the starting point for identifying
[business events and business use cases](business-event-and-use-case.md).
