---
type: concept
title: Strangler Pattern for Legacy Migration
description: >
  Replacing a legacy system piece by piece, with the new system growing
  around the old one until nothing is left to deprecate, keeps every step
  of a migration reversible and impact-assessable — unlike a big-bang
  rewrite.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Joe Reis, Matt Housley), ch. 3"
---

Named by Martin Fowler after the strangler fig, which grows around a host
tree until the tree is no longer needed: a legacy system is replaced by
building new components alongside it and incrementally routing
functionality to them, one piece at a time, until the legacy system is
fully superseded. This is the brownfield counterpart to [architectural
scaffolding](architectural-scaffolding.md) — temporary structure that
exists specifically to make a transition safe — and is the concrete
technique that makes [large-scale
refactoring](large-scale-architecture-refactor-cases.md)'s "Case A: big,
but incremental" achievable for a legacy system rather than merely
aspirational.

The alternative — an all-at-once "big bang" rewrite — is popular precisely
because it sounds simpler, but is a [one-way
door](reversible-architectural-decisions.md): it is high-risk, costly, and
offers no way back once substantially underway, with no way to validate
the new system against real usage until the whole thing is finished.
Strangling instead keeps each migration step small, flexible, and
individually reversible, which is what [reversible architectural
decisions](reversible-architectural-decisions.md) argues for as a general
design goal, not just a migration-specific one.

Full deprecation of the old system is not guaranteed to be achievable —
a large legacy system generating real revenue is not simply "technical
debt to pay off," and an organization may rationally choose to leave part
of it running indefinitely once it no longer blocks anything new. Where
full deprecation is the goal, the practical sequence is to demonstrate
value on the new platform incrementally, service by service, and only then
follow an explicit exit plan for retiring what's left of the old one —
mirroring how a [bubble context](bubble-context-for-legacy-architecture.md)
keeps the relationship between a target design and the legacy system it
replaces explicit throughout, rather than treating the old system as
something to simply ignore until the rewrite is "done."
