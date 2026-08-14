---
type: concept
title: Reversible Architectural Decisions (One-Way vs. Two-Way Doors)
description: >
  Sorting a decision by how expensive it is to undo — a one-way door versus
  a two-way door — determines how much evaluation it deserves before
  committing, and architecting so more decisions land as two-way doors is
  itself a design goal.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Joe Reis, Matt Housley), ch. 3"
---

Jeff Bezos's distinction, adopted directly into architecture practice:
a **one-way door** decision is nearly impossible to reverse once taken
(shutting down a platform other products depend on); a **two-way door**
decision is cheap to undo if it turns out wrong (adopting a particular
database for one new service). The two kinds warrant different amounts of
up-front evaluation — pouring the same careful, slow deliberation into
both wastes time on the reversible ones and risks under-scrutinizing the
irreversible ones.

The practical consequence for architecture is not just to classify
decisions this way but to *design toward more two-way doors*: break a
large, seemingly all-or-nothing initiative into a sequence of smaller,
individually reversible steps rather than committing to it as one
irreversible leap. This is the same instinct behind [architectural
scaffolding](architectural-scaffolding.md) and behind treating [large-scale
refactors](large-scale-architecture-refactor-cases.md) as a genuine design
choice among incremental, occasionally-interrupted, and non-incremental
cases — the incremental case is preferred largely *because* each step
inside it is closer to a two-way door than the whole initiative taken at
once.

A concrete way to operationalize the same judgment for speculative
flexibility specifically (an extra parameter, an abstraction layer "we'll
probably need someday"): estimate how much harder it would be to add that
capability later, once it's actually needed, than to add it now. Only build
it now if that gap is substantial — otherwise the guessed-at flexibility is
itself the two-way door, safely deferrable, and building it early only
costs present understandability for a future need that may never arrive in
the form anticipated. This is the same reversibility judgment applied one decision at a time,
continuously, rather than as a single up-front architecture commitment —
it only holds up if the system stays cheap enough to restructure later
that deferring really does leave a two-way door open, rather than quietly
converting into a one-way one by the time the need actually arrives.

This reframes what [documenting trade-offs](documenting-trade-offs.md)
needs to capture for a given decision: alongside the options considered
and the reasoning for the one chosen, record which kind of door it is. A
decision recorded as a two-way door that later turns out to be one-way in
practice (a dependency nobody accounted for makes it prohibitively
expensive to reverse) is exactly the kind of gap [architectural
runway](architectural-runway.md) tracking exists to surface before it
becomes a forced, high-pressure decision.
