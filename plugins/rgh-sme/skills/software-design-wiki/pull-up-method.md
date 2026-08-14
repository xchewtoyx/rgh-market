---
type: concept
title: "Refactoring: Pull Up Method"
description: >
  Relocate an identical method duplicated across sibling subclasses up
  onto their shared superclass, removing the standing risk that a future
  edit to one copy won't be mirrored in the others.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12"
---

A straightforward application of "eliminate duplicate code" to the
inheritance case: duplicate methods across sibling subclasses are stable
today but a standing risk that a future edit to one copy won't be mirrored
in the other(s). The clean-cut case is two subclass methods with literally
identical bodies — a tell-tale sign of copy-paste. When it's less obvious,
actually inspect for behavioral differences rather than doing the move and
seeing if the tests fail — differences found this way often reveal a test
gap that would otherwise go unnoticed.

This often arises as the second half of a two-step move: two methods that
are *almost* the same get first unified via
[Parameterize Function](parameterize-function.md), making them truly
identical, and only then pulled up. The most awkward complication: if a
method body references fields or methods that live only on the subclass,
not the superclass, pull those dependencies up first (via
[Pull Up Field](pull-up-field.md) or Pull Up Method on them) before
attempting the method itself. Compare
[Pull Up Feature](pull-up-feature.md), a similarly-named but differently-
motivated legacy-code technique aimed at test isolation rather than
removing duplication.

**Mechanics**: confirm candidate methods are truly identical, or refactor
them until they are. Confirm every reference inside the method body —
calls and field accesses — resolves to something reachable from the
superclass. If the methods differ in signature, use
[Change Function Declaration](change-function-declaration.md) first to
unify them. Create the new method on the superclass, copying one
subclass's body over. Run static checks. Delete one subclass's copy at a
time, testing after each deletion, until every subclass copy is gone.

When a shared method depends on a field or accessor that genuinely can't
(or shouldn't yet) be pulled up to a real implementation on the
superclass, adding a **trap method** on the superclass that throws — a
"subclass responsibility error," in Smalltalk convention — makes the
expectation explicit to future subclass authors, rather than leaving an
undefined reference as an implicit assumption.

This is the inverse of [Push Down Method](push-down-method.md).
