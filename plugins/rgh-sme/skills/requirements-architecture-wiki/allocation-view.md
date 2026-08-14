---
type: concept
title: Allocation View
description: >
  An allocation view maps software elements onto non-software structures
  such as hardware, file systems, or organizations, making explicit
  constraints that code and runtime diagrams alone conceal.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 1"
---

Allocation views map software elements onto structures that are not
themselves software: hardware, file systems, build/configuration units, or
organizations. Where [module views](module-view.md) show code-time
structure and [component-and-connector views](component-and-connector-view.md)
show runtime structure, allocation views show what the software depends
on or is assigned to in the world outside the software itself.

The most common allocation view is **deployment**: mapping software
elements to hardware/execution nodes. Document the nodes, the network
links between them, their capacities, which software is allocated to
which node, whether and how it's replicated, and any constraints on that
placement — this is what lets you reason about performance, availability,
security zones, and operational concerns from the architecture rather than
from the running system alone. **Install** views map software to
file-system or installable units, supporting release, deployment, and
upgrade planning. An **implementation** view is the code-time counterpart:
it maps modules to the file/directory structure across development,
integration, test, and configuration-control environments, and is what
build and configuration management actually depend on. See [work
assignment views](work-assignment-view.md) for the case where software is
mapped to teams or individuals rather than infrastructure.

Allocation relations are typically many-to-many (one node hosts several
components; one component may be replicated across several nodes), so
document the mapping's cardinality and the rationale behind it explicitly
— a diagram showing lines between software and infrastructure boxes
doesn't by itself say whether that's a 1:1 dedicated allocation or a
shared, load-balanced one.
