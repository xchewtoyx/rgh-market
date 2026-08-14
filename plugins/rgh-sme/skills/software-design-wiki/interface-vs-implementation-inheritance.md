---
type: concept
title: Interface Inheritance vs. Implementation Inheritance
description: >
  Interface inheritance, where a parent only declares signatures, is pure
  upside; implementation inheritance, where subclasses inherit shared
  method bodies, creates tight two-way dependencies across the whole
  hierarchy and tends to produce high complexity.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 19"
---

**Interface inheritance** — a parent class declares method signatures
without implementing them, and each subclass provides its own implementation
(a common I/O interface implemented separately for disk files versus network
sockets) — lets knowledge learned from one implementation transfer to
others, the same benefit as any
[interface with multiple implementations](interface-duplication-when-ok.md).
The more distinct implementations an interface supports, the
[deeper](deep-modules.md) that interface effectively becomes, since a widely
implementable interface must, by construction, capture only the essential
shared behavior while omitting implementation-specific detail.

**Implementation inheritance** — the parent also supplies default method
bodies that subclasses may inherit as-is or override — has a real upside
(avoiding duplicate implementations across subclasses, directly reducing
[change amplification](change-amplification.md)) but a serious downside: it
creates tight two-way dependencies between parent and every subclass. Parent
instance variables are often touched by both parent and child code, producing
[information leakage](information-leakage.md) across the whole hierarchy. A
developer changing the parent may need to audit every subclass for breakage,
and a developer overriding a method in a subclass may need to study the
parent's implementation to override it correctly. In the worst case,
modifying any class in the hierarchy requires full knowledge of the entire
hierarchy beneath the parent — hierarchies leaning heavily on implementation
inheritance tend to have high complexity.

Use implementation inheritance cautiously. Before reaching for it, consider
**composition** as an alternative — factoring shared functionality into small
helper classes that multiple otherwise-unrelated classes can build on,
rather than inheriting from a shared parent. If implementation inheritance is
unavoidable, cleanly separate which state belongs to the parent versus the
subclasses — keep certain instance variables entirely parent-managed, with
subclasses only reading them or accessing them exclusively through
parent-provided methods, applying
[information hiding within the class
hierarchy](information-hiding-within-a-class.md) itself to cut cross-class
dependencies.

OOP mechanisms in general — classes, inheritance, private members — are
enablers of good design, not guarantors of it: classes built with them can
still be shallow, carry complex interfaces, or leak internal state, and will
still produce high complexity if so.
