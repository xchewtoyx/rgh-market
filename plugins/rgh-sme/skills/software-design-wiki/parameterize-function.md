---
type: concept
title: "Refactoring: Parameterize Function"
description: >
  Merge two functions that carry out very similar logic differing only in
  a literal value into one function taking that value as a parameter,
  removing the duplication and widening the result's applicability at the
  same time.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 11 (formerly Parameterize Method)"
---

When two functions carry out very similar logic differing only in a literal
value, merge them into one function taking that value as a parameter — this
both removes the duplication and increases the resulting function's
applicability, since it's now usable anywhere the old literal-specific
versions weren't. Not to be confused with the identically-named but
distinct legacy-code technique of extracting an internally-constructed
collaborator out to a parameter (see
[Parameterize Method](parameterize-method.md) and
[Parameterize Constructor](parameterize-constructor.md)) — this refactoring
is about unifying near-duplicate *logic*, not exposing a hidden
construction dependency.

**Mechanics**: pick one of the similar functions as the starting point. Use
[Change Function Declaration](change-function-declaration.md) to add
parameters for the literals that need to vary, updating every call site to
pass the specific literal for that case; test. Update the function body to
reference the new parameters instead of the hardcoded literals, testing
after each individual literal is swapped in. For each other similar
function, replace its calls with calls to the now-parameterized function
(adjusting the parameterized function further if a case doesn't quite fit
yet, before moving to the next).

**When generalizing range-oriented logic** (several functions each handling
a different numeric band), start parameterizing from the *middle* case
rather than an edge case — it's the one most likely to generalize cleanly
to both neighbors. An open-ended edge case (no upper bound, say) can often
still fit the same generalized two-bound shape by using an infinite literal
as its bound, rather than needing a separate code path.

A guard clause that becomes logically redundant once several call sites are
unified under one general function is still worth keeping if it documents
how an edge case is meant to be handled — even when the unified logic would
technically still produce a correct result without it.
