---
type: concept
title: Design Around the Critical Path
description: >
  When a genuinely hot, high-impact piece of code has no algorithmic fix
  available, sketch a structurally-unconstrained "ideal" for the common case
  and then find a real, cleanly-structured design that gets as close to it
  as possible — usually by stripping special-case checks out of that path.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 20"
---

A last-resort, relatively rare technique, applicable once
[measurement](measure-before-modifying.md) has identified a genuinely slow,
genuinely impactful piece of code and no fundamental algorithmic or
structural fix (a new algorithm, added caching) is available or has already
solved it.

**Method**: imagine discarding the current code structure entirely and ask
"what is the smallest amount of code that must execute to handle the common
case?" Deliberately ignore all existing special cases in this exercise;
imagine collapsing what might currently span several method calls into one;
consider only the data genuinely needed for the common case, using whatever
layout best serves it, even merging several variables into one if that
helps. Call the resulting minimal, structurally-unconstrained sketch "the
ideal" — not necessarily practical or compatible with existing class
boundaries, but a genuine ceiling on how fast and simple the code could ever
be.

Then search for a real design that gets as close as possible to the ideal
while remaining cleanly structured, applying the usual design techniques
under the added constraint of keeping the ideal's critical path largely
intact. Small additions to the ideal are fine if they preserve clean
abstraction (accepting one extra method call into a general-purpose hash
table class, say). It's almost always possible to find a design that's both
clean and very close to the theoretical ideal — and a small deliberate
deviation from the ideal is sometimes the right call when it clearly serves
the overall goal better; see the
[worked Buffer example](ramcloud-buffer-critical-path-example.md) for an
instance of exactly that trade-off.

The core performance-relevant insight: **removing special cases from the
critical path** is usually the single biggest lever. Code handling many
situations tends to accumulate conditional checks and extra calls to
accommodate all of them, and each addition taxes the common case even though
it exists for an uncommon one. The target structure is ideally a *single*
upfront check that detects "is this a special case at all?" — if it passes
(the common case), the rest of the critical path runs with zero further
special-case checks; if it fails, branch off to separate, non-critical-path
code to handle the special case, where simplicity, not speed, is once again
the priority, since special cases are by definition rare.
