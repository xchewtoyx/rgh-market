---
type: concept
title: Generalization View
description: >
  A generalization view documents specialization relations between
  modules, recording commonality and variation to support reuse and
  product variants — and requires that substitutability respect the
  abstraction, not merely inheritance syntax.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A generalization view shows one module as a specialization of a more
general one, recording what is shared (commonality) and what varies
(variation) between them. It is the module-view counterpart of
inheritance, and it is valuable specifically for reuse and for building
product variants from a common base.

The documentation obligation this style creates is stronger than "class B
extends class A": a specialized module must be **substitutable** for the
general module wherever the general module's abstraction is relied upon.
Recording that a relation is "generalization" without also recording what
contract the general module promises — and confirming the specialization
actually honors it — gives a false sense that substitution is safe when it
may not be. This is why generalization documentation needs to state the
abstraction being specialized, not just the syntactic inheritance
relationship; see [module view](module-view.md) for what else to capture
about each element and relation.
