---
type: concept
title: "Refactoring: Remove Flag Argument"
description: >
  Replace a parameter whose only job is selecting which of several
  distinct behaviors to run with one explicit, intention-revealing
  function per behavior, so an API's real shape is visible from its list
  of functions instead of hidden behind a runtime flag value.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11 (formerly Replace Parameter with Explicit Methods)"
---

A **flag argument** is a parameter whose only job is telling the called
function which of several distinct behaviors to run — `bookConcert(aCustomer,
true)`, or the enum/string equivalents. This obscures an API's real shape:
scanning a list of available functions is usually the first way anyone
explores an API, and a flag argument hides genuinely different behaviors
behind one signature — once a caller has picked the function, they still
have to go dig up what legal values the flag accepts. Boolean flags are the
worst offenders, since a literal `true`/`false` at a call site conveys
nothing about what it actually means without checking the definition. The
fix is an explicit, intention-revealing function per behavior:
`premiumBookConcert(aCustomer)`. This is one of the targeted cures for the
[Long Parameter List](long-parameter-list-smell.md) smell.

**Precise scoping of what counts as a flag argument** (both conditions
required): the caller must be passing a **literal value**, not data flowing
through the program from elsewhere; and the implementation must be using
the argument to **steer its own control flow**, not merely passing it along
as data to some other function. A caller that computes the flag from real
data and passes that through is not misusing the parameter as a flag
argument, and that call site's signature can legitimately stay as-is. When
some callers pass literals and others pass computed data, both interfaces
can coexist: apply this refactoring for the literal-passing callers, and
leave the data-driven callers and the original signature untouched.

Removing flag arguments has a practical side-benefit beyond readability:
static analysis can now cleanly distinguish "callers of the premium path"
from "callers of the regular path," which it couldn't do when both were
buried behind one shared signature and a runtime flag value.

**Named exception**: flag arguments can be reasonable when a function
genuinely has more than one such flag, since replacing them all with
explicit methods would require one method per *combination* of flag
values. But a function juggling multiple flags is usually a function doing
too much — the better fix is decomposing it into smaller composable
functions rather than accepting the combinatorial explosion of explicit
methods.

**Mechanics**: create one explicit function per legal value of the flag
parameter. If the function already has a clean top-level dispatch
conditional on the parameter, use
[Decompose Conditional](decompose-conditional.md) to derive the explicit
functions directly from its branches. If the flag is instead woven through
multiple nested conditions rather than sitting behind one clean top-level
branch, untangling it may not be worth the effort — layer thin wrapper
functions directly over the untouched original instead (each wrapper is
conceptually a partial application of the original function, just expressed
as an ordinary named function). For every caller currently passing a
literal flag value, redirect it to call the matching explicit function
instead. If, after migration, no caller is left using the original
parameter as genuine data, restrict the original function's visibility or
rename it to signal "don't call this directly," since it now exists purely
as an implementation detail behind the explicit entry points.
