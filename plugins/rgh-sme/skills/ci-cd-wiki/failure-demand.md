---
type: concept
title: Failure Demand
description: >
  Demand for work created by not doing something correctly the first time —
  rework, incident response, hotfixing — as opposed to value demand, and a
  lens for why investing in pipeline quality frees up capacity rather than costing it.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
---

# Failure Demand

A term from John Seddon: failure demand is work generated purely because
something wasn't done right the first time — rework after a defect, incident
response, hotfixing a bad release. It competes directly with value demand
(building the features and improvements that were actually planned) for the
same engineering capacity.

The practical relevance to pipeline design: every mechanism that catches a
defect earlier — the [commit stage](commit-stage.md),
[automated acceptance testing](automated-acceptance-testing.md), a
[nonfunctional test gate](nonfunctional-test-gate.md) — converts what would
have been expensive failure demand (a production incident, an emergency
[hotfix](hotfix-through-pipeline.md)) into cheap, fast, in-pipeline feedback.
Investment in pipeline quality isn't a tax on feature velocity; it reduces the
failure demand that would otherwise consume that same capacity later, at
higher cost. This is the mechanism behind
[the speed vs. stability trade-off myth](speed-stability-tradeoff-myth.md):
high performers aren't trading tempo for stability, they're reducing the
failure demand that would otherwise eat into both.
