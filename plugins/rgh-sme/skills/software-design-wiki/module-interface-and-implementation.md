---
type: concept
title: Module Interface and Implementation
description: >
  Modular design splits a system into relatively independent modules, each
  with an interface (what other modules must know to use it) and an
  implementation (the code that fulfills the interface's promises).
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 4"
---

"Module" here is broad: a class, a function (even in non-OO languages), or a
higher-level subsystem or service whose interface might be a set of kernel
calls or HTTP requests. Full independence between modules is unachievable —
modules must call each other, and every call creates a
[dependency](dependencies-as-a-cause-of-complexity.md) (a method's parameter
list, for example, is a dependency between the method and every call site).
The design goal is to minimize how many such inter-module dependencies exist.

An interface is two-way: it includes not only what a module *provides* to
its callers, but what it *requires* from its environment to function —
missing or misbehaving required resources break a module just as surely as
a broken provided operation would, so both directions belong in the
interface, not just the outward-facing half.

A developer working in a module must understand that module's interface *and*
implementation, plus the *interfaces* — never the implementations — of any
modules it calls. This is the leverage point: the best modules have interfaces
much simpler than their implementations, for two reasons. First, a simple
interface minimizes the complexity the module imposes on the rest of the
system. Second, if a module's implementation changes without changing its
interface, no other module is affected — the bigger the gap between
implementation and interface, the more can change safely later. This gap is
what [depth](deep-modules.md) measures directly. A published interface is
also a standing commitment over time — see [interface evolution:
deprecation, versioning, and
extension](interface-evolution-deprecation-versioning-extension.md) for how
to change one without breaking everything that already depends on it, and
[Hyrum's Law](hyrums-law.md) for why that commitment extends further than
the documented contract alone.
