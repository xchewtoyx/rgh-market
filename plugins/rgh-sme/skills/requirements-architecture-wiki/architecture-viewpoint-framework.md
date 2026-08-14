---
type: concept
title: Architecture Viewpoint Framework
description: >
  Standard viewpoint frameworks (ISO/IEC 42010, Kruchten's 4+1, Rozanski
  and Woods) give a reusable starting vocabulary for architecture views,
  but still need to be adapted to the system and its actual stakeholders.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), Appendix E"
---

ISO/IEC 42010 formalizes the vocabulary this whole domain of documentation
uses: stakeholders, concerns, viewpoints, views, models, correspondences,
and rationale. A [viewpoint](view-and-viewpoint.md) establishes the
conventions; a view applies them to address a specific concern. Named
frameworks such as Kruchten's 4+1 or Rozanski and Woods' viewpoint set
give a starting vocabulary of common viewpoints — Rozanski and Woods, for
example, separate functional, information, concurrency, development,
deployment, operational, and security perspectives, treating "perspective"
as a crosscutting quality concern applied across views rather than as
another kind of diagram.

The value of adopting a named framework is a shared vocabulary for talking
about architecture across projects and organizations. The risk is treating
the framework as a mandatory checklist rather than a starting point:
frameworks must be adapted to the actual system and the actual
stakeholder questions (see [choosing architecture
views](choosing-architecture-views.md)), not applied mechanically.
Adopting a framework also requires an explicit mapping between its
terminology/products and your own documentation package, plus a plan for
keeping that mapping consistent as both evolve — a standard improves
communication, but it does not remove the need to explain local notation
and decisions on their own terms.
