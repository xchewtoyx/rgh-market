---
type: concept
title: Wrapping Sealed or Final Third-Party Classes for Testability
description: >
  Language features like sealed or final block the usual fake-substitution
  techniques for classes you don't control; loosen the parameter type where
  possible, and wrap the rest behind your own interface at the cost of an
  explicit adaptation step in production code.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 10"
---

Language/runtime restrictions on subclassing or external construction
(`sealed` in C#, `final` in Java) are well-intentioned — they prevent
malicious subclasses of sensitive types — but directly obstruct the usual
[Extract Interface](extract-interface.md)/[Extract Implementer](extract-implementer.md)
fake-object techniques when the
restricted class is a **third-party dependency you don't control**.

[Adapt Parameter](adapt-parameter.md): if the code only needs a narrower
capability than the full sealed type provides (e.g. just iteration) and the
sealed type happens to derive from an unsealed base with that capability,
loosen the method's parameter type to a custom subclass of that unsealed
base instead. Tests can construct and populate the looser type freely;
production code still passes the real sealed instance, since it satisfies
the loosened type. Made safe by
[leaning on the compiler](lean-on-the-compiler.md): change the type, then work through every
resulting compile error one at a time.

When individual instances of the sealed type still can't be constructed for
tests, escalate to [skinning and wrapping the API](skin-and-wrap-the-api.md):
extract an interface exposing just the members actually used, write a thin
wrapper implementing that interface around the real sealed class for
production, and a [fake object](fake-objects.md) implementing the same
interface for tests. Production code pays a real, acknowledged cost — it
must now manually wrap each real instance before passing it to the
refactored code. "That's the price of security."

The closing reframe matters as much as the techniques: **"the real fault
lies with us. When we depend directly on libraries that are out of our
control, we are just asking for trouble."** The practical rule this
motivates is proactive, not reactive: use `sealed`/`final`-style restricted
classes sparingly in your own code, and when you must depend on someone
else's, wrap them behind your own interface *before* the pain shows up, for
the "wiggle room" it buys later.
