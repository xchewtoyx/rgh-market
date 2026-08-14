---
type: concept
title: Use Case as a Source of Contextualized Stories
description: >
  A use case gives a set of related user stories shared situational
  context and a systematic way to surface edge-case complexity that
  writing stories directly, without a use case behind them, tends to miss.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 19"
---

Alistair Cockburn's critique of writing [user stories](user-story.md)
directly off a backlog, with no use case behind them, is that stories
alone give a designer no situational **context**: when is the user doing
this, what's the surrounding operating context, what's their larger goal
at that moment? A use case supplies that context, and does two further
things a story card can't do on its own:

- Its **main success scenario** gives everyone — customer, developer,
  tester — shared agreement on what the system will and won't do, in a
  way that's hard to reach any other way once a system is genuinely
  composed of multiple actors or subsystems.
- Its **extension conditions and scenarios** are a systematic look-ahead
  device for surfacing "all the little, niggling things that somehow take
  up 80% of the development time and budget" — the edge cases that
  normally get discovered mid-implementation, met with "I don't know,
  I've never thought about that case," instead of being found early
  enough to matter.

A use case has an **actor** (the person or device that initiates it), and
must deliver a **result of value** to that actor — "the resident pushes
the opt-in button" isn't a use case (no observable system response); "the
resident pushes the opt-in button and the system starts to shed load" is.
Beyond the actor and result of value, a use case is named, briefly
described, and has a **flow of events**: this is the same normal/exception
flow and precondition/postcondition structure as a [scenario for a
business use case](scenario-for-business-use-case.md) — a "basic flow" is
a normal flow, an "alternate flow" is an exception flow, and the
**success guarantee** / **minimum guarantee** split is the same
postcondition idea split by whether the use case succeeded or failed.

The practical payoff for an agile team: a single use case commonly spawns
dozens of individual stories, but it spawns them within one coherent,
shared usage context, rather than as isolated cards with no visible
relationship to each other. Those stories then get sliced progressively
across iterations — a thin slice of the main scenario first, then
progressively more of the main scenario and each alternate scenario in
later iterations — so the use case functions as a standing source that
[just-in-time elaboration](just-in-time-requirement-elaboration.md)
draws stories from over time, not as something implemented all at once in
a single iteration. See [use case identification
process](use-case-identification-process.md) for how to derive the actors
and use cases themselves.
