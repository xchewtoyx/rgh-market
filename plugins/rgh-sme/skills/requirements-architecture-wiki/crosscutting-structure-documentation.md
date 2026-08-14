---
type: concept
title: Crosscutting Structure Documentation
description: >
  Combining or relating multiple architecture views is only justified when
  it serves a specific stakeholder task; the mappings between views are
  themselves architectural information that must be documented, not left
  to reader inference.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), ch. 6"
---

A system needs multiple [views](view-and-viewpoint.md) because no single
structure answers every stakeholder's question. But combining two views
into one diagram — overlaying a deployment view onto a component view, say
— is justified only when it demonstrably improves a specific stakeholder
task. Combined indiscriminately, an overlay obscures both structures
instead of clarifying either, because the reader can no longer tell which
lines belong to which structure.

The relationship between views is itself information that needs to be
documented, not left for the reader to infer: which module in a
[module view](module-view.md) implements which component in a
[component-and-connector view](component-and-connector-view.md), for
instance, is a mapping that has to be stated. **Refinement** — relating a
coarse architectural element to a more detailed representation of the same
thing — is a specific case of this, distinct from decomposition (breaking
an element into different sub-parts): refinement needs its correspondence
recorded explicitly so that a change to the detailed view can be checked
against the coarse one, and vice versa, keeping the views consistent with
each other over time rather than drifting apart unnoticed.
