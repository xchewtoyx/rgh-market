---
type: concept
title: "Code Smell: Data Clumps"
description: >
  The same two-to-four data items keep recurring together as fields or
  parameters — a test for whether they're crying out to become an object of
  their own is whether deleting one would make the others meaningless.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Data Clumps are the same two-to-four data items recurring together as
fields or parameters across many places. Test: "would deleting one of the
values make the others meaningless?" — if yes, they're crying out to be an
object. Cure: Extract Class when the clump appears as fields, or [Introduce
Parameter Object](introduce-parameter-object.md) / Preserve Whole Object when it appears as parameters (see
[long parameter list](long-parameter-list-smell.md)). Even partial
replacement — only some fields of the clump used at a given call site — is
still a net win as long as two or more fields are replaced together.

The book deliberately recommends a real class over a bare record or struct:
the class becomes a magnet for [Feature Envy](feature-envy.md)-driven
behavior migration later, which can remove significant further duplication
once the clump has a proper home to receive that behavior.
