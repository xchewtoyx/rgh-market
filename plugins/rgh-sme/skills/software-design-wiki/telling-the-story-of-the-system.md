---
type: concept
title: Telling the Story of the System
description: >
  Force yourself to describe a system's architecture using only its most
  essential concepts, as if to someone who knows nothing about it — the
  discomfort of leaving things out surfaces what's essential and can reveal
  new abstractions.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 17"
---

An exercise for at least two people: one asks "What is the architecture of
the system?" and the other must answer using only a handful of core
concepts, as if to someone who knows nothing about it, then progressively
add the next-most-important facts. The discomfort of leaving things out
("but it also gets rule sets from the working set!") is a feature, not a
flaw — it forces you to identify what's *essential* versus what's merely
*expedient*, and the simplified story becomes both a roadmap and a
confidence-builder: "it can also make a system a lot less scary."

Worked example using JUnit's own architecture: start with a deliberately
oversimplified two-class story, then explicitly enumerate each
simplification as it's peeled back (reflection-based construction, an
interface implemented by a concrete class, listener-based reporting instead
of direct queries, and so on). The takeaway: "when we force ourselves to
communicate a very simple view of a system, we can find new abstractions" —
and a system being more complicated than its simplest honest story isn't
inherently bad, since real systems accumulate necessary complexity. The
story's value is as **guidance**, not as a literal spec.

**Practical payoff**: when two implementation choices are otherwise
comparable, prefer the one that keeps the team's honest brief story of the
system truer. A worked comparison: bolting a report-building method directly
onto an existing class introduces an entirely new, unmentioned
responsibility, making the honest story harder to tell truthfully;
generalizing an already-existing reporting channel to carry the new data
requires only a small, defensible extension of a part of the story already
being told. Divergence between an implementation choice and the team's
honest story is itself a design smell worth weighing against other factors.

This connects to the broader claim that design work never actually finishes
— see [design is a continuous activity](continuous-design.md) — since
telling the story periodically is how a team catches its architecture
quietly drifting away from what everyone believes it to be.
