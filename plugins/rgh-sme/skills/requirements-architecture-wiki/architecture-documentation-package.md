---
type: concept
title: Architecture Documentation Package
description: >
  A complete architecture documentation package bundles individual view
  packets with system-level material — overview, goals, driving
  requirements, decisions, and cross-view mappings — organized for actual
  navigation and use.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 10"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 8"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (ed. Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 13"
---

A single [view](view-and-viewpoint.md) is documented as a **view packet**:
a primary presentation, an element catalog, a context diagram, variability
information, background/rationale for the view's architecture, and
whatever else is needed to interpret it — a view packet can also record
the incremental steps by which the design was reached, not just its final
state.

Above the level of individual views, the package as a whole needs: a
system overview, goals and constraints, the driving requirements behind
the architecture, a glossary, an explanation of notation, the
[architectural decisions](architectural-decision-capture.md) that shaped
the system, and mappings among views — including requirement-to-element
and CRUD-style mappings that make correspondences inspectable rather than
left to reader inference (see [crosscutting structure
documentation](crosscutting-structure-documentation.md)).

A worked real-world instance of this shape is a living design-doc template
used for database architecture decisions: executive summary, goals and
anti-goals, background, design, constraints, alternatives considered, and
launch details — kept tied to configuration management rather than a
static wiki page, so it evolves with the system it describes rather than
freezing at the moment it was written. For an operational system such as a
data pipeline, the equivalent minimal package is three linked artifacts:
system diagrams (with links into live monitoring), process documentation
for both routine and rare/manual tasks, and playbook entries reachable
from the alerts that reference them.

Package the whole thing for navigation, not just completeness: a table of
contents, a road map for finding things, consistent templates across
views, traceability between package parts, an explicit revision strategy,
and an architecture overview presentation for onboarding. A wiki can host
this, but only with governance, a fixed structure, and a clear
authoritative version — a wiki without those properties is exactly the
"stale, uncertain source" this package is meant to replace. Tooling should
support multiple representations, links and mappings between them, change
management, search, and consistency checking; presentation quality is not
cosmetic — it determines whether stakeholders can actually use the
architecture, not just whether it was written down.
