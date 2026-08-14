---
type: concept
title: Strangler Fig Pattern
description: >
  A technique for replacing a legacy system incrementally: build the
  replacement alongside the original and redirect calls to it piece by
  piece, so the old system can be retired once nothing depends on it.
sources:
  - title: "Architecture for Flow: Adaptive Systems with Domain-Driven Design, Wardley Mapping, and Team Topologies"
    resource: "Architecture for Flow (Kaiser), ch. 10"
---

Named for the strangler fig vine, which grows around a host tree and
gradually replaces it. Applied to legacy systems, the steps are: (1) identify
one piece of functionality to extract; (2) implement it as a new component
running alongside the old system, not inside it; (3) if the new component
still needs functionality the old system owns, expose that as an API from
the old side rather than reaching in directly; (4) route incoming calls
through a facade that dispatches each call to whichever of old or new
implementation currently owns it. Repeat per piece of functionality until all
traffic goes to the new system, at which point the old one can be retired.

The pattern's value is that it never requires a big-bang cutover: each
extracted piece is verified independently, in production, while the rest of
the legacy system keeps running unmodified. This is the large-scale, whole-
system counterpart to working [incrementally rather than in refactoring
binges](incremental-extraction-over-refactoring-binges.md) inside a single
codebase — the same principle of shrinking risk by making the replaced
surface small and independently checkable, just applied at the scale of an
entire running system rather than a single function or class. It pairs
naturally with [characterization tests](characterization-tests.md) on the
piece being extracted, to pin down the legacy behavior the replacement must
preserve before cutting traffic over. [Branch by abstraction](branch-by-abstraction.md)
is the same move applied within a single codebase on mainline: a dispatching
layer routes between old and new implementations linked into the same
build, rather than between two running systems.

**The pattern only delivers its benefit if the new code stays genuinely
decoupled from the old system** — it must reach the old system only through
a clean API, never by bypassing it to read the old system's internals or
database directly. If the piece being replaced doesn't already expose a
clean API to migrate against, either build one on the old side first, or
wrap the messy interaction inside a small client library that exposes a
clean interface to the rest of the new code — either way, the mess gets
contained rather than propagated into the replacement.

**Choosing what to extract first**: a straightforward, effective heuristic
is prioritizing by business value — extract the highest-value or
highest-risk piece of functionality first, and stop once further
extraction effort isn't justified by the return, rather than treating full
migration as an all-or-nothing commitment made up front.

**A rewrite's biggest risk is silently expanding scope.** It's tempting,
mid-migration, to reproduce every quirk of the old system's behavior
verbatim in the new one — but a legacy system's business processes are
often more convoluted than the underlying business goal actually requires,
purely from years of accumulated legacy idiosyncrasy; researching what
users actually need can reveal a substantially simpler replacement than a
literal port would produce. Martin Fowler's caution on this: "You would
think such a thing is easy — just make the new one do what the old one
did. Yet they are always much more complex than they seem, and overflowing
with risk... old stuff has to remain. Even old bugs often need to be added
to the rewritten system." The corrective discipline is the same one that
makes the pattern work in the first place: identify the smallest piece of
work that usefully achieves a real outcome in the new architecture, ship
it, and iterate — rather than trying to fully specify the replacement's
scope before starting.
