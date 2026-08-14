---
type: concept
title: Why Big Classes Are a Problem
description: >
  A class grows too big through repeated path-of-least-resistance tweaks,
  then costs a team through reading confusion, concurrent-edit contention,
  and internals that rot unseen behind too much encapsulation.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 20"
---

Class bloat has a mundane root cause: a small feature tweak naturally gets
bolted onto whatever existing class already holds the relevant data, because
that's the path of least resistance. Repeated many times, this produces long
methods and large classes — "a swamp." A team can have a clean-looking UML
architecture on paper while every class in it, in reality, wants to be split
into roughly ten smaller ones.

Three concrete costs: **confusion** — with fifty or sixty methods and many
instance variables, it's hard to know what any given change actually
touches; **task-scheduling contention** — a class with many responsibilities
gives many people many independent reasons to touch it in the same
iteration, causing concurrent-edit thrashing; **testability** — big classes
"hide too much." [Encapsulation](information-hiding.md) is valuable when it
helps reasoning, but over-encapsulation lets internals rot and fester
unseen, pushing developers back toward
[edit and pray](edit-and-pray-vs-cover-and-modify.md) — which shows up later
as either slower changes or more bugs. "You have to pay for the lack of
clarity somehow."

**Immediate defensive tactic** while working inside an already-too-big class
(damage control, not a fix): prefer [Sprout Class](sprout-class.md) and
[Sprout Method](sprout-method.md)
for new work rather than adding directly to the class. Sprout Class avoids
growing the class at all beyond one delegation call; Sprout Method at least
*names* a new discrete thing the class does, which can itself later hint at
a decomposition. See
[seeing responsibilities via method grouping](group-methods-heuristic.md)
for the actual decomposition technique this buys time toward.
