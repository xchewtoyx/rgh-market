---
type: concept
title: Release Train Deadline Discipline
description: >
  A release train enforces hard submission deadlines so no single feature
  can delay the whole batch, and frequent trains make missing one cheap.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Release Train Deadline Discipline

A **release train** is a fixed-cadence batching mechanism: features must
board by a submission deadline or they wait for the next train. The rule
is strict: past the deadline, no amount of pleading gets a feature into
that release — rare true exceptions aside. This trades individual-feature
urgency for predictability of when *something* ships.

The discipline only works when trains run often enough that missing one
is cheap. If releases are weeks apart, a missed deadline costs weeks of
delay and developers panic; if trains leave every other day (or faster),
the next opportunity is hours away and the release engineer's work–life
balance improves because they aren't constantly negotiating exceptions.

Pair deadline discipline with [launch KPI
thresholds](launch-kpi-thresholds.md): imperfect binaries can still ship
when guardrail metrics are within agreed bounds, but lateness is never a
reason to hold the train.
