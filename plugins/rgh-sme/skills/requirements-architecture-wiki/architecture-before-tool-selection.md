---
type: concept
title: Architecture Before Tool Selection
description: >
  Architecture is the what, why, and when; tools are the how — picking
  tools before the architecture that motivates them inverts a sequencing
  discipline, not just a style preference.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Joe Reis, Matt Housley), ch. 4"
---

Architecture is strategic — it states what a system needs to do, why, and
on what timeline, in terms of the [requirements](non-functional-requirement.md)
and [trade-offs](documenting-trade-offs.md) driving it. Tools are tactical:
they are *how* an architecture gets realized, chosen only once the shape
they need to fill is already known. Teams that pick tools first, and only
later try to rationalize an architecture around them, reliably end up with
components that don't cohere — because nothing was choosing them against a
shared set of drivers in the first place. Two named failure modes produce
this inversion: **shiny object syndrome** (adopting a tool for its
novelty, unconnected to any actual requirement it serves) and
**resume-driven development** (choosing a stack to look impressive rather
than to serve the project). Neither is a technology problem — both are a
sequencing problem, solved by insisting architecture and its trade-offs
get decided first.

This is [design concept selection](design-concept-selection.md) at the
level of the overall technology stack rather than a single design
decision: the drivers (requirements, constraints, quality attributes) have
to exist before candidate solutions are compared against them, or the
comparison has nothing real to be measured against. The practical test for
whether a prospective tool choice is premature is simple: can you state
the requirement it satisfies before naming the tool? If not, the
architecture work isn't finished yet, and picking a tool at that point is
guessing dressed up as a decision.
