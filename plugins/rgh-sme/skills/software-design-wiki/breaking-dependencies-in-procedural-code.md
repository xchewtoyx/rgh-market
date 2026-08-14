---
type: concept
title: Breaking Dependencies in Procedural Code
description: >
  Procedural languages lack the natural seams OO offers, so the practical
  strategy shifts from isolating small pieces to finding a pinch point for a
  whole area and separating pure logic from the dependency-laden calls
  around it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 19"
---

Safe change is possible in any language, but procedural languages (C, COBOL,
FORTRAN, Pascal, BASIC — still, as of writing, more widespread in the field
than any other non-OO paradigm) lack the natural seams OO or functional
languages offer, making the testing dilemma pandemic. Skilled developers
manage around this with disciplined dependency management — plenty of good C
exists — but the failure mode is easy: an incrementally unverifiable snarl
where the fallback becomes "think really hard, patch the system, and hope."

**Default strategic guidance**: since breaking individual dependencies is
hard in procedural code, prioritize finding a [pinch point](pinch-point.md)
for a whole area and using a [link seam](link-seams.md) (or, in C, a
[preprocessing seam](preprocessing-seams.md)) to get a large chunk under
test at once, rather than trying to isolate small pieces one at a time.

**Adding new behavior**: prefer adding new functions over extending existing
ones, since a new function can be given its own tests from the start.
[TDD](test-driven-development-loop.md) works identically well in procedural
code, and often nudges better decomposition simply by forcing you to imagine
how a piece would be tested.

**Separate pure logic from the dependency-laden call**: when a function
builds some result *and* immediately passes it to an untestable external
call in the same body, the only way to observe its work is at that exact
call site. Split out a pure function that just computes and returns the
result (directly assertable in a test), leaving the original as a thin
wrapper that calls the pure function and then the external dependency. "We
put all of the pure logic into one set of functions so we can keep them free
of problematic dependencies... we end up with little wrapper functions...
which bind our logic and our dependencies. It's not perfect, but it's
workable when the dependencies aren't too pervasive."

**When the sequence of external calls *is* the logic** (interleaved
database reads/writes carrying little separable pure computation), this
split doesn't apply — the pragmatic fallback for most procedural languages
is to skip test-first for that function, write it as carefully as possible,
and settle for testing it, if at all, at a higher level.

**C-specific alternative — function pointers as a seam**: bundle related
external operations into a struct of function pointers, pass that struct
into functions that need those operations, and point the fields at real
implementations in production and at fakes in tests. Explicitly generalized
beyond C: "this technique isn't C specific. It can be used in most languages
that support function pointers."

See [encapsulating global references](encapsulate-global-references.md) for
the class-based alternative to a bare link seam when the global dependency
itself is the obstacle, and
[migrating procedural code toward object seams](migrating-toward-object-seams.md)
for the further step of introducing genuine objects once a language's OO
extension is available.
