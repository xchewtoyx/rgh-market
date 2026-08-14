---
type: concept
title: The Unit of Incrementality Should Be Abstractions, Not Features
description: >
  Agile's incremental development cycle is compatible with good design, but
  its bias toward deferring design decisions to ship features sooner can
  slide into tactical programming — the fix is to defer *when* you design an
  abstraction, not *how well* you design it once the need arises.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 19"
---

Agile is primarily a process methodology (team structure, scheduling,
testing, customer interaction) rather than a design methodology, but its
incremental/iterative cycle — small feature increments, each with design,
test, and customer feedback — is compatible with, and similar in spirit to,
[design as a continuous activity](continuous-design.md): you can't fully
visualize a complex system's best design up front, so building in increments
while continuously refining abstractions based on real experience is the
right general shape.

The risk is that agile's emphasis on shipping features can slide into
[tactical programming](strategic-vs-tactical-programming.md), because it
optimizes attention toward the next feature rather than designing good
abstractions, and can explicitly encourage deferring design decisions to get
working software out sooner — for example, building a minimal
special-purpose mechanism now and refactoring to something general-purpose
only once genuinely proven necessary. That advice makes sense to a degree,
but it works against the [investment mindset](strategic-vs-tactical-programming.md)
and nudges practitioners toward habits that accumulate complexity quickly.

The reconciling position: incremental development is good, but the right
unit of incrementality is *abstractions*, not features. It's fine to defer
even thinking about a given abstraction until a feature genuinely needs it —
but once that need arises, invest real time designing that abstraction
properly and cleanly, following the
["somewhat general-purpose" guidance](general-purpose-modules-are-deeper.md),
rather than bolting on the narrowest possible fix. This same principle
applies just as directly to [test-driven development](skepticism-of-test-driven-development.md).
