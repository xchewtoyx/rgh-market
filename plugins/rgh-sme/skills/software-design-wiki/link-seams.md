---
type: concept
title: Link Seams
description: >
  A link seam exploits whatever mechanism resolves cross-module references
  at link or load time — an explicit linker, or a classpath — to substitute
  a test stub for a real dependency, with the enabling point living outside
  the program text entirely.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 4"
---

In Java, classes are resolved by fully-qualified name via the classpath;
compiling alternate classes with the same names into a different directory
and pointing the test classpath there is a link seam. In statically-linked
C/C++, a graphics library that a class calls directly (`drawText`,
`drawLine`, ...) can be replaced at test time by linking against a stub
library with empty-bodied versions of those functions (returning a safe
default for functions with a return value) — an easier case when the real
API is mostly a "tell" interface (commands, not queries), since asking for
information back is harder when you can't always fabricate a meaningful
default.

[Sensing](sensing-and-separation.md) through a link seam is possible with
more work: pushing a record of each call onto a queue inside the stubbed
function, then asserting on the queue's contents after exercising the code
under test. Start with a very simple scheme and let it get only as
complicated as it needs to be.

**Link Substitution** names the general form of this for languages with no
object-oriented substitution mechanism at all (C is the primary example)
and no macro preprocessor option either: build a separate "dummy" library
containing alternate function bodies with the exact same signatures as the
ones you want to fake, and link the test build against that library instead
of the real one. For sensing, the fake bodies record their own invocations
(arguments, call order) into an accessible structure — a global list, a
file — that tests inspect afterward. This is especially practical for
faking external libraries that are mostly pure data sinks (call them, don't
care about return values) — graphics libraries are a canonical example. The
same substitution idea applies in Java too, without needing a linker:
create same-named, same-method classes and manipulate the classpath so
calls resolve to the fakes instead of the real dependency-laden classes.

Link seam enabling points always live **outside the program text** — a
build script, makefile, or IDE project setting — which makes them easy to
overlook and easy to lose track of. If you use link seams, make sure the
difference between the test and production environments is obvious, rather
than buried in build configuration nobody remembers exists.

**Severely tangled C++ classes**: unlike Java/C#'s `import`/`using` (which
reads only a compiled summary of a dependency), C++'s textual `#include`
reparses the full declaration every time, and transitive includes can
silently balloon a small file into compiling tens of thousands of lines —
"it's hard to point at any one particular file and understand why it is
taking so long to compile." To get a heavily-tangled class to compile
standalone in a test file, add `#include`s one at a time, driven by actual
compiler errors, rather than blanket-copying every include from the original
source file — copying everything risks pulling in far more transitive
dependency than actually needed. For a hard dependency baked into the
constructor, supply an **alternate definition** of just the offending method
directly in the test file, exploiting the fact that C++ requires only *one*
definition per program, not per compiler-visible declaration — a deliberate
link-seam-style substitution. This forces the test for this class onto its
**own separate build/executable**, since two definitions of the same method
can't coexist in one program; reusable fake definitions can be pulled out
into a shared header once several test files need the same substitution.
This does not remove any dependency at the language level — it's a
stepping stone that commits you to maintaining hand-written duplicate stub
definitions for as long as the tests exist, worth reserving for genuinely
huge, severely-tangled classes, ideally while the class is progressively
broken into smaller pieces that no longer need the workaround.
