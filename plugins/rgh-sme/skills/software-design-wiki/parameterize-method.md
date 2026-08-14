---
type: concept
title: Parameterize Method
description: >
  When a method creates an object internally that you want to substitute
  for sensing, pull the creation out and accept the object as a method
  parameter instead — the same move as Parameterize Constructor, applied to
  an ordinary method.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Not to be confused with the identically-named
[Parameterize Function](parameterize-function.md) refactoring, which merges
near-duplicate *logic* differing only by a literal — this technique is
about exposing a hidden construction dependency for testability, not
unifying duplicated behavior.

Direct sibling of [Parameterize Constructor](parameterize-constructor.md),
applied to an ordinary method rather than a constructor: a method creates an
object internally that you want to substitute for sensing or separation —
pull the creation out and accept the object as a method parameter instead,
preserving the original call signature via a thin forwarding overload so
existing callers see no change. Worked example: a method internally
constructing a result object is parameterized to accept that object
instead, with the original no-argument call reduced to a one-line forward
that supplies a fresh instance.

Naming note on overload collisions: many languages allow same-named methods
differentiated only by parameter list, which is convenient but "at times...
can be confusing" — when clarity matters more, name the new overload
explicitly after its added parameter type rather than reusing the bare
original name.

Same dependency-leakage caveat as Parameterize Constructor: exposing a
previously-internal type as a method parameter risks new external
dependencies on that type creeping in through the interface. If that risk
feels too high, use
[Extract and Override Factory Method](extract-and-override-getter.md)
instead, which doesn't widen the public interface at all.

Steps: copy the target method; add a parameter for the object being
replaced, remove its internal creation, and assign the parameter to the
relevant variable instead; strip the copied (original-signature) method's
body and replace it with a forwarding call to the new parameterized method,
passing the original creation expression as the argument.
