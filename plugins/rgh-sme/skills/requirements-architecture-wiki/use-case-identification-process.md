---
type: concept
title: Use Case Identification Process
description: >
  Deriving a system's use cases in a fixed order — actors first, then use
  cases, then their relationships, then flows — keeps each step answerable
  from what the previous step already established.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 19"
---

Deriving a system's [use cases](use-case-as-story-source.md) works best in
a fixed four-step order, because each step depends on the one before it:

1. **Identify and describe the actors** — partition the world into "the
   system being built" and everything that interacts with it. Guiding
   questions: who uses the system, who gets information from it, who
   provides information to it, where is it used, who supports or
   maintains it, and what other systems or devices use it?
2. **Identify the use cases** — one per actor goal, each with a short,
   action-verb-led name and a one- or two-sentence description. The names
   alone, listed together, communicate the system's scope even before any
   flow is written.
3. **Identify actor and use-case relationships** — only one actor
   typically *initiates* a use case, but several may participate in it.
   Cross-check each actor's expected behaviors against the use cases they
   should appear in; a use case with no plausible actor, or an actor with
   no use case, is a sign the partition from step 1 is off.
4. **Outline the flow of each use case** — for the basic flow: what event
   starts it, how does it end, how does it repeat? For alternate flows:
   what else can the actor do, how does the actor react to optional
   situations, what variants or exceptions might occur?

Working the steps out of order tends to produce use cases with unclear
boundaries or actors invented to justify a use case someone already wanted
to write, rather than use cases that fall naturally out of who actually
needs something from the system.
