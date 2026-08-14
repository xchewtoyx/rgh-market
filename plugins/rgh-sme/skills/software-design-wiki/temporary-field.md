---
type: concept
title: "Code Smell: Temporary Field"
description: >
  A field that's only populated under certain circumstances confuses readers
  who reasonably expect an object's fields to always matter — often better
  modeled as a distinct case than checked with conditionals.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

A Temporary Field is a field only populated under certain circumstances,
which confuses readers who reasonably expect an object's fields to always
be meaningful. Cure: Extract Class to give the orphaned fields a proper
home of their own, Move Function to relocate the behavior that concerns
them into that new class, and — where the "fields not valid" state itself
needs representing — Introduce Special Case to model that state as a
distinct alternative class rather than as conditional checks scattered
through client code. The [Null Object pattern](null-object-pattern.md) is
one concrete instance of Introduce Special Case, for the specific case where
the special state is "there is nothing here."
