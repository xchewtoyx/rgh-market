---
type: concept
title: Supersede Instance Variable
description: >
  The C++ fallback for substituting a constructor-created object that's
  also used elsewhere in the constructor — add a supersedeXXX method that
  destroys and replaces the value after construction, since the language
  won't dispatch a virtual override during the base constructor at all.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 25"
---

The C++-specific fallback for constructor-time object substitution when
[Extract and Override Factory Method](extract-and-override-getter.md) is
blocked, specifically when the object being replaced is actually *used*
elsewhere in the constructor (not just created) — so
[Extract and Override Getter](extract-and-override-getter.md) doesn't apply
either.

**Root cause**: even a method declared `virtual` will not dispatch to a
derived-class override when called *from within the base class's own
constructor* in C++ — a `TestingSubclass` overriding a virtual method to a
no-op still ends up executing the real base-class implementation during
construction, because C++ resolves the call statically at that point in the
object's lifecycle. This is a deliberate language guarantee, not an
oversight: if a base constructor's call to an overridden method *did*
dispatch to the derived override, and that override touched a
derived-class-only member, it would operate on a member that hasn't been
constructed yet — C++ blocks this entire class of use-before-init bug at the
language level. Java, by contrast, does allow overridden methods to be
called from constructors — with a direct recommendation even there: "I
don't recommend doing it in production code."

**Mechanism**: rather than fighting the constructor-call restriction, add a
dedicated `supersedeXXX(...)` method that destroys the current instance and
installs a new one, callable *after* construction completes. Tests
construct the real object normally, then call the supersede method to
inject a sensing object before exercising it. This is judged "on the
surface... a poor way of getting a sensing object in place," but it's the
best choice specifically in C++ when
[Parameterize Constructor](parameterize-constructor.md) would be too
awkward due to tangled constructor logic; in languages permitting virtual
constructor calls, Extract and Override Factory Method remains the better
default.

A general design caution attaches directly to this technique: "it is poor
practice to provide setters that change the base objects that an object
uses. Those setters allow clients to drastically change the behavior of an
object during its lifetime... you have to know the history of that object
to understand what happens when you call one of its methods." Supersede
Instance Variable is a deliberate, test-only exception to this otherwise
sound advice — a practical naming discipline that keeps the exception from
leaking into production is choosing the unusual word "supersede" as the
method-name prefix, making it trivially easy to grep the codebase later and
confirm no production code has started calling it.

Steps: identify the instance variable to supersede; add a `supersedeXXX`
method named after it; inside it, properly destroy the old value and assign
the new one, checking carefully for any *other* references elsewhere in the
class to the object being replaced, which may need additional handling to
stay safe.
