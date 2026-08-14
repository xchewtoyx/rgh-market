---
type: concept
title: Definition Completion
description: >
  In languages that separate declaration from definition, supply your own
  alternate method bodies in the test file and exclude the real
  implementation from the test build — powerful but costly enough to
  reserve for the worst dependency situations, as a temporary bridge only.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Applies to languages that separate declaration from definition — chiefly C
and C++, where a method's header declaration and its actual body are
physically distinct files. Mechanism: `#include` the class's header in the
test source file, but exclude the class's real implementation file from the
test build, then supply alternate (often no-op or sensing) bodies for its
methods directly in the test file — exploiting the fact that the linker only
needs *one* definition per built program, and nothing requires it to be the
real one. This is a variant of a [link seam](link-seams.md), operating at
the level of an entire class's method bodies rather than a single free
function.

**Real, foregrounded costs**: because a program can only have one definition
of each method, Definition Completion forces a wholly separate test
executable just for these tests (the real and fake definitions would
otherwise clash at link time); it creates two divergent sets of method
bodies to maintain long term — a genuine, ongoing maintenance burden — and
can confuse debuggers if the test environment isn't set up carefully. An
unusually strong caveat for this catalog: "I don't recommend using
Definition Completion except in the worst dependency situations. Even then,
I recommend doing it just to break initial dependencies" — treat it as a
temporary bridge to get a class under test properly, after which the
duplicate definitions should be removed.

Steps: identify the class whose definitions need replacing; confirm those
definitions live in a source file, not the header; include the header in the
test source; exclude the real source file from the test build; build and let
errors surface every missing definition; supply test-only definitions until
the build succeeds.
