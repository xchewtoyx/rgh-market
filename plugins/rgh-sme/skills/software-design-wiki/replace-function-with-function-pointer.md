---
type: concept
title: Replace Function with Function Pointer
description: >
  A lighter-weight, compile-time-only alternative to Link Substitution for
  procedural languages with function pointers — the resulting seam can
  double as a genuine production extension point, not just a testing
  convenience.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

For dependency-breaking in procedural languages that lack OO mechanisms
(where [Encapsulate Global References](encapsulate-global-references.md) and
[Subclass and Override Method](subclass-and-override-method.md) are
unavailable), this is a lighter-weight alternative to
[Link Substitution](link-seams.md) or
[Definition Completion](definition-completion.md) when those feel
like overkill for a smaller, localized substitution — specifically usable
in languages that support function pointers. Teams disagree about function
pointers' safety (corruptible, can jump through arbitrary memory if
misused, versus fine when "used with care"); this technique is offered for
teams comfortable with them.

Mechanism: declare a function pointer with the *same name* as the original
function, rename the original function's declaration and definition (a
`_production` suffix, say), and initialize the pointer to point at the
renamed production function during program startup. Once in place, tests
can install alternate function bodies through the pointer for sensing or
separation, exactly like an [object seam](object-seams.md) but achieved
through raw function-pointer indirection.

Practical advantage: "it happens completely at compile time, so it has
minimal impact on your build system" — contrasted with Link Substitution,
which can require restructuring libraries and produces seams "not the sort
you'd want [to] exploit to vary behavior in production code." Function-
pointer seams, unlike link seams, can double as genuine production
extension points (swapping database backends at runtime, say), not just a
testing convenience. If working in C this way, consider migrating toward
C++ incrementally, file by file, to unlock the fuller set of OO seams
elsewhere in the book — see
[migrating procedural code toward object seams](migrating-toward-object-seams.md).

Steps: find the declarations of the functions to replace; declare
same-named function pointers alongside them; rename the original function
declarations so they no longer collide with the new pointer names;
initialize each pointer to the corresponding renamed function's address
(commonly at program startup); build, locate the old function bodies via
the resulting errors, and rename them to match their new production names.
