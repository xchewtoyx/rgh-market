---
type: concept
title: Architectural Runway
description: >
  A system has architectural runway when its existing or planned
  infrastructure can absorb current and anticipated requirements without
  excessive refactoring, and running out of it is a documentable, foreseeable
  failure mode rather than a sudden surprise.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 5"
---

Architectural runway is the amount of existing or planned infrastructure a
system has available to absorb current and anticipated requirements without
excessive refactoring. It reframes architecture work as inventory to be
maintained ahead of demand, not a one-time decision made at project start:
the operative question is what technology initiatives need to be underway
*now* so that future increments of functionality can still be delivered
reliably later.

This distinguishes two kinds of large-scale work competing for the same
backlog: ordinary feature work that delivers user-visible value directly,
and **architecture epics** — structural changes (potentially spanning
millions of lines of code and years of effort) undertaken purely to extend
the runway so that future features remain deliverable. Architecture epics
still need to be defined, prioritized, and communicated like any other
requirement; they are distinguished from a [requirement vs. design
decision](requirement-vs-design-decision.md) boundary case only by whose
need they satisfy — the system's own future capacity to change, rather than
an end user's.

Running out of runway has two distinct failure modes, both traceable to
treating architecture as a decision made once rather than a stock
maintained continuously: release dates slip because infrastructure work
that should have been incremental now has to happen just-in-time, under
schedule pressure; or the system becomes so brittle that no new feature can
be added without a rewrite. Because the runway is consumed by ordinary
feature delivery and only replenished by deliberate investment, its
maintenance is everyone's responsibility — architects, developers, and
whoever owns requirements — not a task delegable to a single architecture
function. This is the forward-looking complement to [timing of
architectural decisions](timing-of-architectural-decisions.md): that note
covers documenting the constraints a past decision was made under; runway
is about documenting, ahead of time, how much room the current architecture
has left before the next decision becomes forced rather than chosen.

Once an architecture epic is large enough to span releases or teams, how
it gets implemented is itself a decision with real options — see [three
cases for large-scale architecture refactoring](large-scale-architecture-refactor-cases.md).
