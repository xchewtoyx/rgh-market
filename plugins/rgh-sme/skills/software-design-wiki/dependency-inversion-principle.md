---
type: concept
title: Dependency Inversion Principle
description: >
  Depend on interfaces or abstract classes rather than concrete classes,
  because interfaces change far less often than the implementations behind
  them, so fewer changes trigger a recompile or ripple to dependents.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 7"
---

A class that depends directly on another concrete class is coupled to every
change made to that class — including changes that don't affect the
dependent's actual behavior, purely because the compiler must recompile
anything that references a changed type. Depending on an interface or
abstract class instead insulates callers: interfaces change far less often
than the implementations behind them, since an interface only needs to
change when the *contract* changes, not whenever internals do. Minimizing
how often "particular changes will trigger massive recompilation" is the
whole payoff. [Ports and Adapters architecture](ports-and-adapters-architecture.md)
is this same principle applied at the scale of a whole module's boundary
with its environment: the module owns the interface (port), and every
external technology it talks to supplies an implementation (adapter) that
depends inward on that interface rather than the module depending outward
on the technology.

This is a compile-time, dependency-management framing of the same idea
behind [interface and implementation inheritance](interface-vs-implementation-inheritance.md)
and [general-purpose modules being deeper](general-purpose-modules-are-deeper.md):
a stable interface in front of a changeable implementation reduces
[change amplification](change-amplification.md). Applied deliberately across
a whole package or cluster of classes, it produces a
[compilation firewall](compilation-firewall.md); applied to unblock a single
untestable class, it's one of the standard moves in
[dependency-breaking for testability](dependency-breaking-for-testability.md)
(there called [Extract Interface](extract-interface.md)). [Dependency injection](dependency-injection-pattern.md)
names the roles in this same mechanism when the concrete implementation is
supplied externally by an injector rather than looked up or constructed by
the dependent class itself.
