---
type: concept
title: Introduce Parameter Object
description: >
  Replacing a recurring group of parameters with one structure is a
  prerequisite enabling step, not just tidiness — it's what makes the group
  promotable into a first-class domain abstraction with its own behavior.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6"
---

The direct cure for [Data Clumps](data-clumps.md): groups of data items that
recur together across many function signatures. Replacing the clump with one
structure has three immediate, modest benefits — it makes the relationship
between the items explicit, shortens parameter lists, and enforces
consistent naming for the group's elements everywhere it's used. The real
payoff is what it *enables* afterward: once the group exists as a real
structure, shared behavior over that data can migrate onto it, reshaping the
conceptual model of the code by promoting a formerly-implicit group into a
first-class domain abstraction. **None of that deeper payoff is reachable
without first doing Introduce Parameter Object** — it's an enabling step,
not an end in itself.

**Mechanics**: if no suitable structure exists yet, create one — prefer a
**class** over a plain record specifically because it makes attaching
behavior later easy, and usually make it a value object (no update methods)
from the start. Use [Change Function
Declaration](change-function-declaration.md) to add the new structure as a
behavior-neutral extra parameter; test. Update each caller to construct and
pass the correct instance, testing after each. For each individual element
the function currently reads from the old separate parameters, replace
those reads with reads through the new structure; once every element is
migrated, remove the old parameters.

**The payoff step** happens once the structure exists as a real class:
behavior migrates onto it — a bundled min/max pair, for instance, gains a
`contains(value)` method that replaces scattered inline range checks
wherever that pair was used. Spotting one such pair worth promoting is
usually a signal to look for other structurally similar pairs elsewhere in
the codebase that the same new abstraction could absorb.
