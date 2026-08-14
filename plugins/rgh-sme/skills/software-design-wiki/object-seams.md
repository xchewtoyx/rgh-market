---
type: concept
title: Object Seams
description: >
  An object seam relies on polymorphism — a call site doesn't determine by
  itself which method body runs, so if the runtime type can be varied
  without touching the call site, that call is a seam — and it's the
  workhorse and best available option in object-oriented languages.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 4"
---

A call like `cell.Recalculate()` doesn't by itself determine which method
body runs: polymorphism means the actual method depends on the runtime type
of `cell`. If that runtime type can be varied without touching the call
site, the call is an [object seam](seam.md).

**Not a seam**: if a method both constructs the object
(`Cell cell = new FormulaCell(...)`) and calls it in the same place, there's
no enabling point — the class is fixed by that same method, so it can't be a
seam without editing the method itself. **Made into a seam by
parameterization**: changing the method to accept `Cell cell` as a parameter
instead of constructing it internally makes `cell.Recalculate()` a seam, with
the enabling point being the caller's choice of argument — in a test, pass a
fake or test-specific `Cell` subclass.

Seam *existence* and seam *exploitability* are sometimes separate: a call to
a `private static` method from within the same class is technically still a
seam (you're not editing the call site), but only becomes usable for testing
once `static` is removed and visibility loosened to `protected`, at which
point a test subclass can override the method to substitute test behavior.
That's a small, mechanical, behavior-preserving edit that unlocks an
otherwise inert seam.

The same call site can often have multiple available seams at once — a
[preprocessing seam](preprocessing-seams.md), a
[link seam](link-seams.md), and an object seam can all apply to the same
buried call in different languages or configurations. Where a choice exists,
**object seams are the best option in object-oriented languages**: they're
the most explicit, and the resulting tests are easiest to maintain.
Preprocessing and link seams are useful but less explicit, and tests
depending on them can be hard to maintain — reserve them for pervasive
dependencies with no better alternative.
