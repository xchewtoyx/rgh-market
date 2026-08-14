---
type: concept
title: Extracting a Class Without Tests
description: >
  When Extract Class can't be done under test, a conservative manual
  procedure — moving methods and fields into a same-class staging area
  under a MOVING prefix before relocating them — protects against silently
  breaking inheritance-based overrides and variable shadowing.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Before extracting a responsibility, inventory exactly which instance
variables and methods must move, and check which of them can get real tests
around them — private methods are testable indirectly through the
containing class's public surface (see
[testing private methods](testing-private-methods.md)), falling back to
[dependency-breaking techniques](dependency-breaking-for-testability.md) if
the class resists instantiation or method-level testing altogether.

**If tests are achievable**, use the standard
[Extract Class](extract-class.md) refactoring directly. **If they aren't**,
a conservative manual procedure protects
against mistakes with no safety net to catch them:

1. Identify the responsibility to separate out.
2. Physically relocate (still within the same class) any instance variables
   that need to move, into their own section of the declaration.
3. For whole methods to be moved, extract their bodies into new methods with
   a unique `MOVING`-prefixed name, rather than moving or renaming the
   originals directly, applying [Preserve Signatures](preserve-signatures.md) if doing this by
   hand, and place these new methods in the same separated section.
4. For partial methods, extract just the relevant parts using the same
   `MOVING` prefix convention.
5. **Manually search-verify** — explicitly *not* relying on the compiler or
   [leaning on the compiler](lean-on-the-compiler.md) here — that
   none of the variables slated to move are used anywhere outside the
   methods slated to move. This step exists specifically because of
   **shadowing**: a subclass can declare a variable with the same name as
   one in a base class, and compiler-driven renaming can silently miss uses
   of the *other*, shadowed variable, changing behavior invisibly.
   (Practical tip: commenting out a shadowed declaration temporarily reveals
   the previously-hidden uses of the variable it was shadowing.)
6. Once isolated, move the flagged variables and `MOVING`-prefixed methods
   to the new class outright; create an instance of the new class inside the
   old one, and *this time* lean on the compiler to find and fix every call
   site that now needs to go through that instance.
7. Once it compiles, strip the `MOVING` prefixes back off, again leaning on
   the compiler to catch every reference that needs updating.

**Why the indirection matters**: moving a method or variable directly risks
the single most dangerous class of bug in tests-free class extraction —
inheritance-related breakage. Moving a method that happens to override a
base-class method silently changes which method callers on the original
class now resolve to (falling through to the base class's version instead);
moving a variable that shadows a base-class variable makes the previously-
hidden base variable visible again, with real behavior implications. The
`MOVING`-prefix-plus-manual-search discipline exists specifically to surface
and avoid these failure modes when no tests exist to catch them
automatically. Explicit final caution: **"It is possible to make mistakes
with this. Be very careful, and do it with a partner."**
