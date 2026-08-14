---
type: concept
title: Exception Collection as an Automation Health Signal
description: >
  Centrally capturing every severe program-exiting failure keeps automated
  self-healing from silently hiding recurring crashes, and turns exception
  volume into a stop-the-rollout signal for automated deployment.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 2"
---

# Exception Collection as an Automation Health Signal

Automatic process restart is a basic form of [self-healing](self-healing-overload-response.md):
a crashed component comes back up on its own, without paging anyone. Left
alone, this is also a trap — a component that crashes and auto-restarts
every few minutes produces no user-visible outage and pages no one, so the
underlying bug can recur indefinitely with nobody aware it exists. The
self-healing mechanism, by successfully hiding the symptom, removes the
only signal that would normally prompt someone to fix the cause.

A central exception collector closes this gap by capturing every severe,
program-exiting failure independently of whatever recovery mechanism
handles it, giving three distinct benefits:

- **Makes invisible failures visible** — a crash that auto-restart would
  otherwise fully absorb still shows up in aggregate exception data, so a
  team can see a recurring crash even though no human ever had to respond
  to any single instance of it.
- **Serves as a rollout health signal** — a spike in exception volume
  during a gradual, automated rollout is a natural automatic stop
  condition: it means the new version is failing in ways the rollout
  process should halt on, before it reaches more of the fleet.
- **Supports trend analysis** — correlating exception volume and type
  against specific releases distinguishes a genuinely improving system
  (trending down) from one accumulating a worsening root cause (trending
  up), which a simple "is it up" health check can't tell apart.

This makes exception collection a cheap, general-purpose complement to the
explicit [safeguards against runaway automation](safeguards-against-runaway-automation.md)
built into an automated rollout: those safeguards bound what a bad change
can do, while exception collection is what notices the change was bad in
the first place, even when the immediate symptom was already absorbed by
self-healing.
