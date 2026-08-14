---
type: concept
title: "Refactoring: Replace Superclass with Delegate"
description: >
  Replace a subclass's inheritance from a superclass with a field that
  holds an instance of it plus forwarding methods for the operations that
  genuinely apply, fixing the classic mistake of inheriting an existing
  class purely to reuse its functionality.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 12 (formerly Replace Inheritance with Delegation)"
---

Inheritance is an easy way to reuse an existing class's functionality —
inherit, then override or add. That ease enables a classic modeling
mistake: making `Stack` a subclass of `List`, reusing `List`'s storage and
operations. The problem is that every `List` operation, including many that
make no sense for a stack, leaks onto `Stack`'s public interface. The
better model holds the list as a **field** of `Stack` and delegates only the
operations that genuinely apply. General diagnostic: if some of the
superclass's functions don't make sense on the subclass, that's a sign
inheritance is the wrong tool for reusing that functionality — a concrete,
mechanical instance of the
[Liskov Substitution Principle](liskov-substitution-principle.md).

A second, related error is the **type-instance homonym**: a "type" class
(a car *model*, with name and engine size) gets subclassed to represent an
*instance* of that type (a physical car, adding VIN and manufacture date),
when actually every instance of the subtype should be a valid instance of
the supertype in every sense — which a type/instance relationship never
really satisfies. Both mistakes are sidestepped by using delegation
instead — it makes explicit that the two things are related but distinct,
with only some functionality actually carrying over.

Even where the modeling *is* legitimate — every superclass function truly
applies, every subtype instance really is validly a supertype instance —
this refactoring can still be worth doing, because subclass/superclass
coupling is inherently tight: a subclass is easily broken by superclass
changes it didn't anticipate. The cost of switching to delegation is writing
a forwarding function for every shared operation — tedious, but such
forwarding functions are too simple to get wrong. As with
[Replace Subclass with Delegate](replace-subclass-with-delegate.md), the
guidance is not "never use inheritance": given the right semantic
conditions, inheritance remains simple and effective — mostly use it first,
and apply this refactoring only once it becomes an actual problem.

**Mechanics**: add a field on the subclass referencing an instance of the
(former) superclass, initialized to a new instance. For each element the
subclass actually uses from the superclass, add a forwarding method on the
subclass that delegates to that reference — testing after each *logically
consistent group* of forwarders (most can be tested individually, but a
getter/setter pair, for instance, can only be meaningfully tested once both
halves exist). Once every needed superclass element has a forwarder, remove
the inheritance link entirely.

**In practice this rarely arrives alone.** Fixing an inheritance-modeled
type-instance homonym typically also means turning the newly-introduced
delegate field from a private, per-instance copy into a properly shared
reference via [Change Value to Reference](change-value-to-reference.md),
reshaping constructor parameters via
[Change Function Declaration](change-function-declaration.md) to thread
through whatever identifier now locates the shared instance, and sometimes
accepting a deliberately temporary inconsistency (like a placeholder null
ID) as a known stepping stone on the way to the real fix rather than a
defect to avoid. A single real-world design fix is rarely delivered by one
named refactoring in isolation.
