---
type: concept
title: "Code Smell: Alternative Classes with Different Interfaces"
description: >
  Classes that should be substitutable for each other but expose mismatched
  method signatures defeat polymorphic substitution even though the classes
  are otherwise interchangeable.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Alternative Classes with Different Interfaces are classes that should be
substitutable for one another — they play the same conceptual role — but
expose mismatched method signatures, defeating polymorphic substitution.
Cure: [Change Function Declaration](change-function-declaration.md) to align
the signatures; [Move Function](move-function.md) to relocate behavior until
the two classes' protocols genuinely match. If
aligning the interfaces surfaces duplicated implementation between the two
classes, [Extract Superclass](extract-superclass.md) unifies the shared
parts.
