---
type: concept
title: Library Design Constraints vs. Testability
description: >
  Language features that enforce a library's design intent (singleton
  enforcement, non-virtual methods) often make testing nearly impossible;
  prefer a team convention that gets the same design benefit without the
  lockout.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 14"
---

"Library designers who use language features to enforce design constraints
are often making a mistake. They forget that good code runs in production
*and* test environments. Constraints for the former can make working in the
latter nearly impossible." Two recurring tensions:

**The "once" dilemma** — a library assuming there's only ever one instance
of a class system-wide (singleton-style enforcement) blocks the usual
fake-substitution techniques (see
[breaking singleton dependencies](breaking-singleton-dependencies.md)),
sometimes leaving [wrapping](skin-and-wrap-the-api.md) as the only escape
when you don't control the library's source.

**The restricted-override dilemma** — a convention or language feature
pushing toward non-virtual methods, sometimes recommended as a design best
practice, makes it hard to introduce
[sensing and separation](sensing-and-separation.md) via subclassing. Plenty
of very good code has historically been written both with this discipline
(parts of the C++ world) and entirely without it (Smalltalk, where every
method is effectively overridable) — it isn't a settled question of good
design, just a tradeoff.

**The practical compromise**: treat public methods as non-virtual *by
convention* in production code, while still declaring them virtual or
overridable so tests can selectively override them — "you can do very well
just pretending that a public method is non-virtual in production code...
you can override it selectively in test and get the best of both worlds."
The general principle this illustrates: **"Sometimes using a coding
convention is just as good as using a restrictive language feature. Think
about what your tests need."** Prefer team discipline over language-level
lockdown when design integrity and testability are in tension — the
discipline gets you the same intent without foreclosing the escape hatch
tests need.
