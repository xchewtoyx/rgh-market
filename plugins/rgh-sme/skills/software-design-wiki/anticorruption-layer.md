---
type: concept
title: Anticorruption Layer
description: >
  A translation layer between your code's internal model and an external
  dependency's model, protecting your code from a foreign, unstable, or
  poorly designed vocabulary rather than adopting it directly.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 3 (term originates with Eric Evans, Domain-Driven Design)"
---

When code depends on an external system or library whose own concepts,
naming, or model don't match the vocabulary your code actually uses — or
whose model is poorly designed, unstable, or liable to change on someone
else's schedule — adopting that external model directly lets its problems
leak straight into your own code. An **anticorruption layer** is a
translation boundary that sits between the two: your code talks to the
external dependency only through this layer, in the external model's
terms, while everything on the inside stays expressed in your own model,
never directly touching the foreign vocabulary.

This is [skin-and-wrap-the-api](skin-and-wrap-the-api.md) generalized past
its original testability motivation: skinning an API for testability is
concerned with substitutability (can a fake stand in for the real thing);
an anticorruption layer is concerned with conceptual integrity (does the
external model's shape, naming, and assumptions match what your code
actually needs to express). The two often coincide in the same wrapper —
a translation layer built to protect your model also happens to be an easy
seam to fake in tests — but the anticorruption layer is worth reaching for
even when testability isn't the driving concern, whenever an external
dependency's model would otherwise distort how your own code has to think
about its problem.

The alternative — adopting the external model as-is, with no translation
layer — is a legitimate, lower-effort choice when the external model is
stable, well-designed, and already matches what your code needs. An anticorruption layer costs real
translation code to build and maintain; it's worth that cost specifically
when the alternative is letting a foreign or volatile model dictate the
shape of your own, or when the external dependency is itself poorly
structured (a legacy system with no clear internal boundaries) and direct
exposure would otherwise let that disorder propagate inward.
