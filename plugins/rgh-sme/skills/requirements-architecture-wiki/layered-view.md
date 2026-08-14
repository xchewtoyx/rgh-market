---
type: concept
title: Layered View
description: >
  A layered view groups modules into layers that act as virtual machines,
  permitting dependencies only in one defined direction, and must state
  explicitly whether the layering is strict or relaxed.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A layered view groups cohesive modules into layers and permits dependency
only in one defined direction — each layer acts as a virtual machine built
on the layer below it. This is a special, direction-constrained case of a
[uses view](uses-view.md): all the uses relations in the system have been
constrained to point the same way across a fixed set of layers.

Documentation must state explicitly whether the layering is **strict**
(a layer may only use the layer immediately below it) or **relaxed** (a
layer may use any layer below it, skipping some) — this is not obvious
from a diagram of stacked boxes and materially changes what a reader can
assume about a given module's dependencies.

Dependency structure matrices (DSMs) are the practical tool for checking a
layering against reality: they expose actual dependencies in a form where
violations of the intended direction (a lower layer depending upward, or a
layer skipping a supposedly-strict boundary) are visible and can be
tracked down and fixed, rather than only being described as intent in
prose.
