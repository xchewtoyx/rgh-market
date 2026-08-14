---
type: concept
title: Organize Modules by Business Concept, Not Technical Layer
description: >
  Grouping code into modules named after technical roles (controllers,
  services, repositories) rather than the business concepts they implement
  causes a single business-logic change to ripple across many modules.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 10"
---

A common way a codebase accumulates [change amplification](change-amplification.md)
is organizing top-level modules by technical layer — one module for
controllers, one for models, one for repositories, one for services — rather
than by the business concept each piece of code actually serves. Under this
layout, a change to one business concept (say, everything about how a quiz
works) isn't localized to one place; it's smeared across the controller
module, the service module, the model module, and the repository module,
each of which also holds the unrelated logic for every other business
concept in the system. This is [Shotgun Surgery](shotgun-surgery.md) at the
scale of top-level module boundaries: the layered grouping obscures which
files actually change together, and the technical-layer boundary
consistently cuts across the boundary that matters for change.

The fix is to invert the grouping: one module per business concept
(`classmanagement`, `contentcreation`, `coursestudies`, ...), each internally
free to have its own controller/service/model/repository pieces if that
internal structure is still useful. This groups by "what changes together"
rather than by "what technical role does this code play" — the same
heuristic behind [Feature Envy](feature-envy.md)'s cure, applied one level
up, at the granularity of whole modules rather than individual functions.
It also gives each business-concept module a natural home for its own
[information hiding](information-hiding.md) boundary: internal
representation choices (which technical layers exist, how they're wired)
stay private to that module instead of leaking into a shared, layer-wide
convention that every other business concept's code has to follow too.
