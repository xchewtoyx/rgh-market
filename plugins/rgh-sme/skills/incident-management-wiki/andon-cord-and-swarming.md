---
type: concept
title: Andon Cord and Swarming
description: Stopping work the moment a problem is detected and mobilizing whoever is needed to fix it immediately, rather than letting it queue or propagate downstream.
sources:
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 3"
---

Named for the physical cord above every Toyota assembly work center: any
worker can pull it the instant something looks wrong, which immediately
summons the team leader. If the problem isn't resolved within a short,
predefined window, the entire line stops and the organization mobilizes
until a countermeasure is found. Counterintuitively, when Andon pulls
*decrease*, plant managers tighten tolerances to provoke more pulls — the
goal is surfacing ever-weaker failure signals for continued learning, not
minimizing interruptions.

**Swarming** is the response behavior the cord triggers: mobilize whoever is
needed to contain and diagnose a problem immediately, rather than letting
the person who found it work it alone or file it for later. This matters
because in complex systems, the cost and difficulty of understanding a
problem grows the longer it's left — context decays, other changes pile on
top, and the conditions that caused it become impossible to reconstruct.
Swarming also blocks new work from entering until the problem is
understood, which prevents compounding it with a second failure layered on
top of the first.

The technology equivalent is a low-friction way for anyone to signal "I
found something wrong" (a chat command, a dedicated channel, a build
turning red) that reliably pulls in help *before* the problem escalates to
a formally [declared incident](early-incident-declaration.md) — swarming
is the fast, informal first response; the
[incident command system](incident-command-system.md) is what takes over
once a problem is big enough to need structured, multi-team coordination.
Making the cord genuinely safe to pull — with no penalty for false alarms —
is a precondition: teams under-pull when they fear disturbing others or
being wrong, which is itself a sign the surrounding culture isn't
[blameless](blameless-postmortems.md) enough yet.
