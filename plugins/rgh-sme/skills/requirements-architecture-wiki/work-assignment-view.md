---
type: concept
title: Work-Assignment View
description: >
  A work-assignment view maps modules to the teams or individuals
  responsible for them, making organizational coupling visible so it can
  be planned for rather than discovered by accident.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

A work-assignment view is an [allocation view](allocation-view.md) that
maps software modules to the teams, organizations, or individuals
responsible for them, rather than to infrastructure. It exists because who
owns what is itself an architectural fact with consequences: Conway's Law
observes that a system's structure tends to mirror the communication
structure of the organization that builds it, so documenting the
work-assignment mapping surfaces where organizational boundaries and
module boundaries agree or disagree.

Where they disagree — one module owned by two teams, or one team owning
modules that depend heavily on another team's modules — that's exactly the
information a coordination view exists to expose: which groups need to
communicate because of dependencies the decomposition alone doesn't show.
Documenting this explicitly turns an implicit coordination cost into
something that can be planned for, rather than something a team discovers
only when a cross-team change turns out to need three meetings it didn't
budget for.

A [bounded context](bounded-context.md) is a natural unit for this
mapping: its ownership boundary is, by definition, meant to align with a
single team, so a work-assignment view built around bounded-context
boundaries is checking a design intention (one team, one context) against
reality, rather than assigning ownership after the fact.
