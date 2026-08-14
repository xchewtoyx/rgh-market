---
type: concept
title: "Refactoring: Replace Conditional with Polymorphism"
description: >
  Turn conditional logic that divides into distinct high-level cases into a
  class hierarchy, so each case is expressed as its own polymorphic
  override instead of a branch repeated across every place that switches
  on it.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 10"
---

Complex conditional logic is hard to reason about; when it can be understood
as dividing into distinct high-level cases, classes and polymorphism can
make that division more explicit than the conditional structure itself. Two
scenarios call for it:

1. **A genuine set of types**, each handling shared logic differently —
   most visible when several separate functions each `switch` on the same
   type code. This is the cure for the
   [Repeated Switches](repeated-switches-smell.md) smell: creating one class
   per case removes the duplicated switch logic across those functions,
   replacing it with per-type polymorphic methods.
2. **A base case with variants** — a common/default behavior with one or
   more special-case departures from it. The base case goes on a
   superclass, so it can be understood in isolation without needing to hold
   every variant in mind at once, and each variant becomes a subclass
   expressed purely in terms of its *difference* from the base.

This is not a call to replace *all* conditional logic with polymorphism —
most conditional logic is better left as plain if/else or switch/case;
polymorphism is reserved for cases matching the two patterns above.

**Mechanics**: if the needed classes don't exist, create them along with a
factory function that returns the correct instance for a given input (see
[Replace Constructor with Factory Function](replace-constructor-with-factory-function.md)
for the general form of this step); route calling code through the factory
instead of direct construction. Move the
conditional-containing function onto the superclass, using
[Extract Function](extract-function.md) first if it isn't already a clean,
self-contained function — often preceded by
[Combine Functions into Class](combine-functions-into-class.md) when the
conditional logic is spread across several functions sharing the same
switched-on data. For each leg of the conditional, in turn: create an
overriding method on the matching subclass, copy that leg's body into it,
and adapt it to fit — testable and committable one leg at a time. Leave a
default-case implementation on the superclass, or, if the superclass is
meant to be abstract, make the method throw or otherwise signal that it's a
subclass's responsibility.

**A variant that's a clean modification of the base value** can override by
calling `super.method() - adjustment` — no duplication of the base logic
needed, since the subclass value is expressible purely as a delta from the
superclass's. **A variant that isn't a clean superset or modification** —
where the special-case branch and the base-case branch are structurally
different, not one a delta of the other — needs the whole conditional block
extracted into its own method first (both branches together) so that the
superclass keeps only the base-case logic in its own body while the
subclass overrides the same method name with only its own branch's logic. A
method left with an awkward, two-purpose name at this intermediate stage
(a strong sign, if it needs an "and" to describe it, that two concerns are
still bundled together) can be split into two independently named,
independently overridable methods afterward as a follow-up cleanup, rather
than blocking the polymorphic split on finding the perfect name first.

Even in languages without a static type hierarchy — where polymorphism only
requires the right-named method to exist on the object — a superclass can
still earn its place purely for documenting the conceptual relationship
between the variant types, even where the language doesn't structurally
require it.

Once variant logic is fully isolated in a subclass, the superclass's logic
becomes simpler to read and reason about on its own terms, and each variant
only needs attention when specifically working on its subclass — expressed
entirely in terms of its difference from the base, rather than re-derived
from scratch each time it's read. Compare
[Replace Type Code with Subclasses](replace-type-code-with-subclasses.md),
which sets up the class hierarchy this refactoring's first scenario
dispatches into.
