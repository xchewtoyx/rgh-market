---
type: concept
title: Lean on the Compiler
description: >
  Deliberately trigger compiler errors to generate a worklist of every call
  site a change ripples to — powerful in statically typed languages, but
  inheritance can silently swallow errors it should have raised.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 23"
---

In a statically typed language, a compiler's type-checking can be used as a
**navigation tool**, not just a translation step: deliberately alter a
declaration in a way that breaks compilation, then navigate to and fix each
resulting error one at a time. Worked example: wrapping two bare global
variables inside a new class; recompiling surfaces every call site that
referenced the globals directly as a compile error, each mechanically
rewritten to go through the new object instead. A second common use: change
a variable's declared type from a concrete class to an interface, then use
the resulting errors to determine exactly which methods the new interface
actually needs to declare.

Practicality caveat: not always worth it if the build is slow — see
[lag time](lag-time.md) — in which case searching for call sites manually
may beat waiting through repeated slow recompiles.

**Sharp caution: inheritance is the biggest source of false confidence when
leaning on the compiler.** Commenting out a concrete method in a class
produces **zero compile errors** if a same-named concrete method exists in a
superclass — callers silently start resolving to the inherited version
instead of surfacing as an error. The same silent-fallback risk applies to
shadowed instance variables (see
[extracting a class without tests](extract-class-without-tests.md) for the
manual-search discipline this motivates when no tests exist to catch it).
"Lean on the Compiler is a powerful technique, but you have to know what its
limits are; if you don't, you can end up making some serious mistakes."
