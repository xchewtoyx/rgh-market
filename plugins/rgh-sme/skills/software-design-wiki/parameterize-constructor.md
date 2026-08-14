---
type: concept
title: Parameterize Constructor
description: >
  Move an object's internal construction of a collaborator out to a
  constructor parameter, so a fake can be substituted in tests, while a
  preserved no-arg constructor keeps existing production call sites working
  unchanged.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

A **hidden dependency** — a constructor that internally `new`s a
collaborator, connects it, and configures it, all invisible from the
constructor's own signature — can't be swapped for a test double no matter
how the object is called, because the concrete type is baked into the
constructor body itself.

**Parameterize Constructor**: move the internal allocation out of the
constructor and accept the collaborator as a parameter instead. On its own
this doesn't look like much, but combined with
[Extract Interface](extract-interface.md) on the collaborator's
type, it lets a [fake](fake-objects.md) implementation be substituted in
tests while the real class still does the real thing in production.

**Backward-compatibility trick** for existing callers of the old no-arg
constructor: extract the original constructor's body into a private
`initialize(collaborator)` method; keep a no-arg constructor that calls
`initialize(new RealCollaborator())` for existing callers, while a new
parameterized constructor calls `initialize(collaborator)` directly for
tests. This is safe to do even *without* tests already in place, because
it's a pure, mechanical application of
[Preserve Signatures](preserve-signatures.md) — no existing
call site's behavior changes. (Simpler still in languages where constructors
can chain-call each other directly, e.g. `this(new RealCollaborator())`.)

Parameterize Constructor is the default first reach for a hidden
construction dependency with no construction dependencies of its own — one
of the most frequently used dependency-breaking techniques, described as "a
very easy refactoring." When
the object to isolate is buried several objects deep inside the
construction sequence — not the immediate parameter but something *it*
constructs — see
[dependency-breaking for deeply nested construction](deep-construction-dependencies.md)
instead, since parameterizing the outer constructor alone doesn't reach that
far.

**Mechanical sequence**: copy the original constructor; add the new
parameter to the copy and remove its internal `new` expression, assigning
the parameter to the field instead; go back to the *original* constructor,
strip its body, and replace it with a delegating call to the new
constructor, passing a fresh `new` expression for the now-externalized
parameter. In languages supporting default arguments, the new dependency
can instead be added as a defaulted parameter directly on the existing
constructor rather than creating a second overload — with a real cost in
C++ specifically: a default-argument expression referencing another class's
constructor forces the header file to fully `#include` that class's header
rather than getting away with a lighter forward declaration, a compile-time
coupling cost significant enough that "I don't use default arguments often"
for this purpose.

**Honest tradeoff**: adding a constructor parameter for what used to be an
internal implementation detail can let other client code start depending on
that parameter's type in ways it couldn't before. This is judged a "rather
small concern" in practice relative to the technique's payoff. The same
tradeoff, applied to an ordinary method instead of a constructor, is
[Parameterize Method](parameterize-method.md).
