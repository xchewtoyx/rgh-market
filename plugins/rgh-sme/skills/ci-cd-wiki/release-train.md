---
type: concept
title: Release Train
description: >
  A fixed, frequent release schedule with hard submission deadlines so every
  release ships on time and missed features wait for the next train rather than
  delaying the whole batch.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Release Train

A release train is a **predictable cadence** — daily, every other day, weekly —
backed by automation, submission deadlines, and a policy that **the train
leaves on time**. Past the deadline, no amount of pleading adds a feature to
that release; the feature waits for the next train, which arrives soon enough
that the wait is hours, not days.

Two trade-offs make this workable at scale:

**No binary is perfect.** With many developers shipping independently, fixing
every bug before every release is impossible. Clear
[key-performance-indicator thresholds](automated-release-fitness-gate.md) let
features launch when metrics stay within agreed bounds, reducing contentious
launch debates. Perfection is rarely the right goal — know how much error
budget remains and spend it deliberately on the velocity/stability trade-off.

**Meet your release deadline.** A missed train costs one interval of wait time,
not a cascade of slipped dates, developer panic, and release-engineer burnout.
Regular, frequent trains make abandoning any single release cheap and keep
divergence from a known-good state small — which in turn shortens
[release latency](release-latency-at-scale.md) when rolling out safely.

Building a release train typically means automating build and integration,
setting feature-submission cutoffs, and simplifying plug-in or data
integration so each cycle no longer consumes days of manual triage. The
Search case study at Google moved from unreliable weekly releases to a
consistent every-other-day cadence over several years of incremental
investment.

A release train pairs naturally with [trunk-based development](trunk-based-development.md)
— developers integrate continuously at head while the train provides a
predictable business-facing shipping rhythm — and with [feature toggles](feature-toggle.md)
so code merged before a deadline can still be held back from users until
product readiness.
