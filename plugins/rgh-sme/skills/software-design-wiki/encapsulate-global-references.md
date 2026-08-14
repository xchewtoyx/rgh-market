---
type: concept
title: Encapsulate Global References
description: >
  Wrap problematic globals in a new class rather than leaving them as bare
  data or reaching only for a link seam — a cleaner, more explicit seam
  that deliberately defers moving any logic onto the new class until more
  tests exist.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

For code depending on problematic C/C++-style global variables or free
functions, three broad options exist: make the globals behave differently
under test, link to different globals (a [link seam](link-seams.md)), or
**encapsulate them into a class** for a cleaner, more explicit seam. Simpler-
looking fixes often fail on inspection: making a global a plain member of
whichever class most obviously uses it breaks when *other* classes also
touch it; [Parameterize Method](parameterize-method.md) alone forces
threading the global as a
parameter through every downstream method that also treats it as global.

**Design guidance embedded in the technique**: "if several globals are
always used or modified near each other, they belong in the same class."
Naming the new encapsulating class is a real design act — think about what
methods will eventually migrate onto it, even though you won't move that
logic yet. On naming pressure: "the name should be good, but it doesn't have
to be perfect. Remember that you can always rename the class later."

**Mechanical procedure for data**: create a new class holding copies of the
global variables, initially keeping their original (ugly) names to ease the
transition; declare one global instance of the new class; comment out the
original bare global declarations; recompile and
[lean on the compiler](lean-on-the-compiler.md) to find every now-broken
reference; prefix each with the new global instance's name. The result is
deliberately uglier in the short term but fully behavior-preserving — a
first step, not a finished design.

**Deliberate restraint is the point, not a shortcut**: "when we don't have
tests in place and we are trying to do the minimal work we need to get
tests in place, it is best to leave logic alone as much as possible...
later, when we have more tests in place, we can move behavior from one
class to another with impunity." Start with data or small methods; defer
moving substantial methods until more tests exist — see
[designs emerge from zealous duplication removal](duplication-removal-as-emergent-design.md)
for the same incremental-commitment discipline applied once tests do exist.

**Variant for free functions**: create an abstract interface class with one
virtual method per free function, a concrete production subclass whose
methods do nothing but delegate to the real global functions, and a fake
subclass for tests holding whatever test data structure is convenient. "To
encapsulate references to free functions, make an interface class with fake
and production subclasses. Each of the functions in the production code
should do nothing more than delegate to a global function." This is
preferred over plain delegating free functions or static methods, because
those would still require falling back on
[link or preprocessing seams](preprocessing-seams.md) to substitute
behavior, whereas the class-plus-virtual-method approach yields an explicit,
easily managed [object seam](object-seams.md) via ordinary parameterization
instead. See
[migrating procedural code toward object seams](migrating-toward-object-seams.md)
for this technique as the first step of a larger C-to-C++ migration.
