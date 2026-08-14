---
type: concept
title: Adapt Parameter
description: >
  When a parameter's type is hard to fake and can't be narrowed via Extract
  Interface — typically a wide third-party interface — introduce your own
  minimal interface expressing only what the calling code actually needs,
  and accept that this is the one case where Preserve Signatures doesn't
  apply.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

Use when a method parameter's type is hard to fake and
[Extract Interface](extract-interface.md) can't be applied to
it — typically because it's a third-party or standard interface you can't
modify, or because it's low-level and implementation-specific with a wide
surface. Worked example: a method taking a servlet request type with
dozens of methods to fake if mocked directly. A third-party mock library
would work but leaves production code coupled to the wide original
interface regardless. The chosen fix: introduce a **new, narrow interface**
expressing only what the calling code actually needs (here, a single
lookup method), write a production wrapper delegating to the real type, and
a trivial fake for tests.

Design principle this illustrates: **"Move toward interfaces that
communicate responsibilities rather than implementation details. This makes
code easier to read and easier to maintain."** It directly addresses a
common legacy pattern where important logic sits intermingled with
low-level API calls with no abstraction layer at all — a narrow,
purpose-built interface both enables testing and improves readability by
hiding unused surface area. This is the same underlying move as
[skinning and wrapping an API](skin-and-wrap-the-api.md), applied to a
single parameter rather than a whole library surface, and it's the specific
technique behind [wrapping sealed or final third-party classes](wrapping-sealed-third-party-classes.md).

**Sharp exception to the catalog's general discipline**: "Adapt Parameter is
one case in which we don't [Preserve Signatures](preserve-signatures.md).
Use extra care." If the new simplified interface diverges too much from the
original parameter's actual interface, subtle bugs can creep in; bias toward
whichever version you feel more confident in, deferring ideal structure
(eliminating null-checks via the [null object pattern](null-object-pattern.md),
say) until after tests exist.

Steps: design the new, minimal interface, kept as trivial as possible while
requiring only trivial changes at the call site; write a production
implementer delegating to the real parameter type; write a fake implementer;
write a test passing the fake; update the method to use the new interface
type; run the test to confirm the fake works end to end.
