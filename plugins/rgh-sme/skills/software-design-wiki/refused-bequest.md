---
type: concept
title: "Code Smell: Refused Bequest"
description: >
  A subclass that inherits a superclass's methods and data but only wants
  part of what it's given — usually too faint to be worth fixing, unless the
  subclass refuses the superclass's interface itself.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 3"
---

Refused Bequest is a subclass that inherits a superclass's methods and data
but only wants part of what it's given. The "traditional" prescription —
push the unused parts down to a new sibling class via Push Down Method or
Push Down Field, leaving the superclass strictly common — is explicitly
*not* endorsed as a default: Fowler and Beck say they use subclassing for
behavior reuse constantly, and consider the resulting faint smell usually
not worth cleaning, "nine times out of ten this smell is too faint to be
worth cleaning."

The stronger, genuinely worth-fixing version is when a subclass refuses the
superclass's *interface*, not just its implementation — that's a [Liskov
Substitution Principle](liskov-substitution-principle.md) violation, where
callers holding a base-class reference can get silently wrong behavior. That
version calls for Replace Subclass with Delegate or Replace Superclass with
Delegate rather than reshaping the inheritance hierarchy.
