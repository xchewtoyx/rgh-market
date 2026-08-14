---
type: concept
title: Testing Private Methods
description: >
  Prefer testing a private method through its public callers; if that's not
  practical and making the method public feels wrong, that discomfort is a
  design smell pointing at excess responsibility, not a reason to reach for
  reflection.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 10"
  - title: Unit Testing Principles, Practices, and Patterns
    resource: "Unit Testing Principles, Practices, and Patterns (Khorikov), ch. 11"
---

The first question when a method that needs testing is private: **can you
test it through a public method instead?** This is usually preferable, not
just easier — it guarantees the private method is exercised the way it's
actually used in production, and it caps scope creep, since "each method has
to be just functional enough to support the callers that use it," not
maximally general in anticipation of a test calling it directly. If a private
method later genuinely needs a public caller of its own, that first external
caller should be the one to write the tests documenting its correct usage.

When testing through the public surface genuinely isn't practical: **"If we
need to test a private method, we should make it public."** Discomfort with
that move is itself diagnostic, not a testing problem to route around: "If
making it public bothers us, in most cases, it means that our class is doing
too much and we ought to fix it." Two distinct reasons it might bother you —
(1) it's just an internal utility clients don't care about (mild,
"forgivable"); (2) clients calling it directly could corrupt state the
class's other methods rely on (more serious) — point to different fixes. For
(2), move the method to a new class where it can be legitimately public, with
the original class holding an internal instance of that new class. Where a
full responsibility split is too risky given release timing, a pragmatic
middle path is to loosen the method to `protected` and re-expose it as public
only on a test-only subclass — a small, acknowledged encapsulation violation
("getting the tests in place is a fair trade") that may itself become the
trigger for the fuller refactor next time the class is touched.

This is also a class-decomposition heuristic in its own right: many
private or protected methods on a class often signal "another class dying
to get out" — the urge to test one directly is itself the signal that it
belongs to a *different* responsibility and should become a public method
on a **new** class instead, not a public method bolted onto the original.
Making such a method public on the original class would look odd to its
existing clients; making it public on a newly extracted collaborator is
natural, and the original class's own encapsulation isn't weakened at all,
since it still only *uses* the collaborator's public methods privately. See
[grouping methods to find hidden responsibilities](group-methods-heuristic.md)
for this in the context of decomposing an oversized class more generally.

**Avoid reflection-based tricks** that read or call private members directly
from tests, even where technically available. The concern isn't mechanical —
it's that such subterfuge "quietly launders the pain of bad design out of
view," preventing a team from noticing how bad the code is getting. The
discomfort of legacy code is a useful, motivating signal; suppressing it with
reflection just delays the bill until the eventual cost of fixing it has
grown "too ridiculous."

Khorikov adds: don't expose private methods solely for testing — that violates
testing [observable behavior only](observable-behavior-vs-implementation-details.md)
and damages [resistance to refactoring](four-pillars-of-a-good-unit-test.md).
If coverage through the public API is insufficient, the private method is either
dead code (delete it) or a **missing abstraction** to extract (e.g. complex
`GetPrice()` logic → standalone `PriceCalculator`). Rare exception: private
constructors forming an ORM reconstruction contract — test via reflection or
make public if the contract itself is what matters. Don't expose private state
for tests; assert what production consumers actually use (e.g. discount after
`Promote()`, not internal `_status`).
