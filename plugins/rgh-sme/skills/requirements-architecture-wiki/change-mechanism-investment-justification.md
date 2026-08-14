---
type: concept
title: Change-Mechanism Investment Justification
description: >
  Whether to build a flexibility mechanism for an anticipated change, or
  just wait and hand-edit the system when the change actually arrives, is
  a cost comparison that depends on how many times the change is expected
  to recur.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 8"
---

Building a [variation point](variation-point-documentation.md) — a
config flag, a plug-in interface, a parameterized abstraction — has a
cost of its own, separate from the cost of actually using it later. A
proposed mechanism is worth building only if, over N anticipated
occurrences of the change it is meant to serve:

> N × (cost per change with no mechanism) ≤ (cost of building the
> mechanism) + N × (cost per change once the mechanism exists)

This makes explicit what "build it flexible, just in case" usually leaves
implicit: N is a prediction, not a fact, and a mechanism built for a
change that recurs less often than expected can end up costing more than
the hand-edits it was meant to avoid. The inequality also omits two things
that still belong in the decision even though they don't fit the formula:
opportunity cost (money and time spent building the mechanism isn't
available for anything else), and time-to-availability (a mechanism with
a better long-run total cost is still the wrong choice if it won't be
ready before the change is actually needed).

This is the same reasoning [documenting trade-offs](documenting-trade-offs.md)
asks for generally, specialized to the recurring case of "should this be
made configurable" — and it's worth writing down explicitly in the
variation point's own rationale, because the answer can flip if N turns
out to be wrong, which is exactly the kind of assumption a later reader
needs to be able to check. Consistently skipping this justification and
defaulting to "no mechanism" is also what accumulates as
[architecture debt](change-locality-classification.md): the option was
available and cheaper in expectation, but nobody weighed it against the
alternative.
