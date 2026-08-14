---
type: concept
title: View and Viewpoint
description: >
  A view is a representation of a set of system structures documented for
  a specific set of stakeholder concerns; a viewpoint is the set of
  conventions used to construct and interpret that view.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A **view** represents one structural aspect of a system — the set of
elements and relations relevant to a particular concern, such as how the
system is divided into modules or how its processes communicate at
runtime. A **viewpoint** is the set of conventions that governs how a
category of view is built and read: what kinds of elements and relations
it uses, what notation it employs, and what questions it is meant to
answer. The viewpoint is the reusable rulebook; the view is one
system-specific application of it.

Views are grouped into **styles** — module styles, component-and-connector
(C&C) styles, and allocation styles — each classifying a family of
structures that share a vocabulary of element and relation types. See
[module views](module-view.md), [component-and-connector
views](component-and-connector-view.md), and [allocation
views](allocation-view.md). A fourth category, the [quality
view](quality-view.md), cuts across all three when a stakeholder's
concern doesn't align with any single structure.

Because a system needs several structures simultaneously (see
[architecture as structures for reasoning](architecture-as-structures-for-reasoning.md)),
no single view is "the architecture." Which views to actually produce for
a given system is a deliberate choice driven by stakeholder concerns, not
a fixed checklist — see [choosing architecture
views](choosing-architecture-views.md). Combining two views into one
diagram is justified only when it demonstrably helps a stakeholder task;
indiscriminate overlay of structures obscures both of them rather than
clarifying either — see [crosscutting structure
documentation](crosscutting-structure-documentation.md).

ISO/IEC 42010 formalizes this vocabulary — stakeholders, concerns,
viewpoints, views, models, correspondences, rationale — and named
viewpoint sets such as Kruchten's 4+1 or Rozanski and Woods' set offer
starting vocabularies for common concerns; see [architecture viewpoint
frameworks](architecture-viewpoint-framework.md).
