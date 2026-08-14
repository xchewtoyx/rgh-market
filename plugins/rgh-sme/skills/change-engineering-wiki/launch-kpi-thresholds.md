---
type: concept
title: Launch KPI Thresholds
description: >
  Pre-agreed key-performance-indicator thresholds let imperfect releases
  ship when guardrail metrics are within bounds, instead of blocking on
  perfection.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Launch KPI Thresholds

At high release velocity with many independent contributors, **no binary
is perfect** — there will always be bugs whose fix-vs-ship trade-off is
judgment, not certainty (display shifts, readability edge cases, revenue
sensitivity). Without a decision framework, every launch becomes a
contentious debate.

Pre-agreed **key performance indicator thresholds** on health, revenue,
and user-experience guardrails convert those debates into threshold checks:
if metrics are within bounds, the feature or release proceeds even when
imperfect; if a metric crosses a threshold, escalation is warranted. This
reduces launch contentiousness and aligns with error-budget thinking —
perfection is rarely the right goal; know how much budget remains and spend
it deliberately on velocity.

Thresholds don't eliminate judgment calls on low-incidence, high-principle
issues (a bug affecting a tiny population may still warrant a delay), but
they keep the common case fast.

See [release train deadline discipline](release-train-deadline-discipline.md)
for the complementary rule that deadlines, not pleading, gate train
boarding.
