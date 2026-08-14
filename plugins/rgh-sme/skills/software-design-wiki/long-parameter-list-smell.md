---
type: concept
title: "Code Smell: Long Parameter List"
description: >
  A long parameter list is confusing to callers even though the historical
  alternative it replaced — global data — was worse; several targeted cures
  each remove a different reason a parameter ended up in the list.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Long parameter lists are confusing even though the historical alternative —
threading state through global variables instead — is worse. Distinct cures
address distinct causes: **[Replace Parameter with
Query](replace-parameter-with-query.md)** drops a parameter that's
derivable from another parameter already present;
**[Preserve Whole Object](preserve-whole-object.md)** passes the source
structure instead of several pulled-out fields;
**[Introduce Parameter Object](introduce-parameter-object.md)** bundles parameters that consistently travel
together into their own type; **[Remove Flag
Argument](remove-flag-argument.md)** eliminates a boolean or enum parameter
used only to select between behaviors. Compare
[pass-through variables](pass-through-variables.md), the related smell of a
parameter threaded through many intermediate calls that never use it
themselves — often fixed the same way, by routing the value through a
[context object](context-object-pattern.md) instead of a parameter list.

When several functions share several of the same parameters, that's usually
a stronger structural signal: [Combine Functions into
Class](combine-functions-into-class.md) turns the
shared values into fields shared across the whole group, described in
functional terms as "a set of partially applied functions."
