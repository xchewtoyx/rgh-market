---
type: concept
title: Placebo Deployment A/B Test
description: >
  Compare a real update against a placebo re-shipment of the old version
  to separate deployment-induced metric shifts from genuine quality change.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Placebo Deployment A/B Test

Canarying to a small traffic fraction reveals crash and stability signals
but says little about whether the new version is actually *better* — and
pushing *any* update, even with no functional change, can itself cause a
statistically significant shift in user metrics unpredictably.

A **placebo deployment A/B test** ships two versions simultaneously to
large, similar user populations: the real update and a **placebo** that
re-ships the old version (same bits, new deployment event). Comparing
metrics between the two isolates whether observed shifts come from the
change itself or from the act of updating (install friction, reboot
behavior, cache invalidation, user attention).

With sufficient userbase, statistically significant results can arrive
within hours or days; an automated metrics pipeline can promote the
release to more traffic as soon as guardrail metrics show no harm. This
requires population-based comparison — see [canary measurement
validity](canary-measurement-validity.md) — not a before/after time
comparison.

The technique has overhead and needs scale; where userbase is too small,
fall back to a [change-neutral release](change-neutral-release.md).
