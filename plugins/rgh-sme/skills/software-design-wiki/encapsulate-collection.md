---
type: concept
title: Encapsulate Collection
description: >
  A getter that hands back the live collection object itself leaves
  membership changes uncontrolled even though the field reference looks
  properly encapsulated — the owning class needs explicit add/remove
  methods and a hardened getter.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 7"
---

Names a specific, common encapsulation mistake: a class properly wraps a
collection field behind a getter and setter, but the getter hands back the
**live collection object itself** — so the collection's *membership* can be
changed by any caller without the owning class ever getting a chance to
intervene, even though the *reference* to the field looks properly
encapsulated. "While the reference to the field is encapsulated, the
*content* of the field is not." Relying purely on team discipline not to
mutate the collection from outside is unwise — a slip here produces bugs
that are hard to trace.

**Fix**: add explicit `add`/`remove` methods on the owning class so
membership changes always route through it, preserving a future hook for
validation or side effects, and harden the getter itself so it can't hand
out a mutable view. Three ways to harden the getter, in order of
preference: **return a copy** — any modification to the returned copy
doesn't touch the encapsulated original, and is called the most common
approach, with the usual [measure-before-worrying](measure-before-modifying.md)
caveat about copy cost on large collections; a **read-only proxy** that
forwards reads and blocks writes; or, explicitly disfavored, **never
returning the collection at all** and replacing every usage with a bespoke
method — rejected because modern collection interfaces are rich and
composable, and replicating that composability behind hand-rolled methods
adds a lot of code for little benefit. Whichever mechanism is chosen, pick
one and use it consistently across the codebase, so callers can form a
single stable mental model of how every collection accessor behaves.

Stated personal habit worth generalizing: **"I find it wise to be
moderately paranoid about collections and I'd rather copy them
unnecessarily than debug errors due to unexpected modifications."** A
concrete trap this guards against: some standard-library operations (like
JavaScript's `Array.prototype.sort`) mutate their receiver in place rather
than returning a new collection, unlike what many callers assume.
