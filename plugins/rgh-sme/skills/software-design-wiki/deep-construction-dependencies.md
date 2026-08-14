---
type: concept
title: Dependency-Breaking for Deeply Nested Construction
description: >
  When the object you need to fake is buried several constructors deep (a
  construction blob or an onion parameter), parameterizing the outer
  constructor alone doesn't reach it — peel one layer at a time, or swap
  the object after construction instead of during it.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 9"
---

Two related shapes of the same problem: a **construction blob**, where a
constructor builds several interdependent objects internally and the one you
actually need to sense or fake is buried several objects deep in that
sequence (making [Parameterize Constructor](parameterize-constructor.md)
alone require an unreasonably large parameter list); and an **onion
parameter**, where constructing object A needs object B, which needs object
C, and so on ("it seems like a big onion"). The chain must bottom out
somewhere — some class in the chain takes no other class as an argument, or
the system could never have compiled in the first place.

**For onion parameters**: ask what the test actually needs from the deeply
nested value. If nothing, [Pass Null](pass-null.md). If just rudimentary
behavior, apply [Extract Interface](extract-interface.md)/[Implementer](extract-implementer.md) to the *nearest* dependency —
the one directly in the outer constructor's parameter list — not to
everything it in turn depends on. You don't have to unwind the whole onion,
just peel the outer layer that's actually in view. This "peel one layer, not
the whole onion" strategy is broadly applicable in any language capable of
expressing interfaces or interface-like abstract classes.

**For construction blobs, when the object-you-need is created internally
rather than passed in**: **Extract and Override Factory Method** — extract
the internal creation into an overridable method, then override it in a
test-only subclass to return a fake. This has a sharp limitation: calling an
overridable method from within a constructor is unsafe in general, because a
derived-class override may read base-class fields the base constructor
hasn't finished initializing yet — and in some languages (C++) virtual calls
made from within a constructor don't even resolve to derived-class overrides
at all, making the technique unusable there regardless of the safety
concern.

See [Extract and Override Factory Method and Getter](extract-and-override-getter.md)
for the fuller treatment of these two techniques, including the C++-specific
lazy-getter workaround for exactly this constructor limitation.

**Fallback when Extract and Override Factory Method isn't available or
isn't safe**: [Supersede Instance Variable](supersede-instance-variable.md) —
add a setter that lets a
test swap in a fake collaborator *after* construction completes, discarding
the original. In unmanaged languages this shifts real responsibility onto
you: correctly disposing of the superseded object, understanding what its
cleanup does, and avoiding double-frees or dangling references. Even in
garbage-collected languages, where the cleanup burden disappears, never call
the superseding method from production code if the superseded object manages
a real external resource (a live connection, a lock) — the method exists for
tests, not runtime reconfiguration. Prefer Extract and Override Factory
Method where it's available and safe; reach for Supersede Instance Variable
mainly when the language or the constructor's shape closes that option off.
