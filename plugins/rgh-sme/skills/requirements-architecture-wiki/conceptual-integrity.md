---
type: concept
title: Conceptual Integrity
description: >
  An architecture has conceptual integrity when the same kind of problem
  is solved the same way everywhere in it — a property of the design
  itself, worth stating and checking for explicitly, not a side effect of
  competent individual decisions.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 14"
---

Conceptual integrity is the consistency of design choices across an
architecture: a small number of inter-component communication mechanisms
used everywhere rather than a different one per team; one approach to
error handling, logging, user interaction, and data sanitization, applied
uniformly instead of reinvented per module. It is a quality of the
architecture as an artifact itself, not of the running system or of the
development project the way a runtime quality attribute like performance
is.

Its payoff is indirect but real: a reader who has understood how one part
of the system solves a problem can correctly predict how every other part
solves the same kind of problem, which is what actually makes a large
architecture learnable and reduces confusion during implementation and
maintenance — "less is more" in the sense that fewer distinct ways of
doing the same thing means less to hold in your head. Because it's a
property of the whole design rather than of any single decision, it tends
to erode by accumulation — each individually reasonable local decision to
solve a familiar problem "slightly differently this time" degrades it a
little, the same incremental mechanism behind
[architecture debt](change-locality-classification.md) more generally —
which is why it's worth checking for deliberately in an [architecture
documentation review](architecture-documentation-review.md) rather than
assuming it falls out of individually sound decisions.
