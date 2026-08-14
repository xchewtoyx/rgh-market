---
type: concept
title: Architecturally Significant Decision
description: >
  A design decision is architectural, and worth documenting as such, when
  it must be bound to meet a behavioral, quality, development, or business
  goal — not because of how much implementation detail it involves.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan)"
---

Architecture is a subset of design, and the line between them is not the
amount of detail involved. A decision is architectural when it must be
bound early to meet a behavioral, quality-attribute, development-process,
or business goal — protocols and interfaces can be architectural even
though they are detailed, while an internal implementation choice with no
externally visible effect is not architectural even though it may be
consequential to the code.

This distinction matters for documentation practice directly: it tells you
what belongs in an [architectural decision
record](architectural-decision-capture.md) and what does not. A decision
is worth capturing formally — issue, decision, rationale, alternatives,
consequences — when reversing it later would require rebinding something
that other parts of the system, teams, or business commitments now depend
on. A decision that can be freely changed by one developer without
consulting anyone else, regardless of how intricate it is, does not need
that overhead.

The practical test is: does this decision constrain how a quality
attribute (performance, security, modifiability, availability...) can be
achieved, or does it commit the system's structure in a way that later
work depends on? If yes, treat it as architectural and document it as a
decision with rationale, not merely as a fact about the current code. See
also [requirement vs design decision](requirement-vs-design-decision.md)
for the analogous distinction on the requirements side, and [timing of
architectural decisions](timing-of-architectural-decisions.md) for why
these particular decisions tend to get made too early to reverse cheaply.
