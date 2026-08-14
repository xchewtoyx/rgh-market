---
type: concept
title: Fallback to a Safe Default
description: >
  When neither rollback nor roll-forward is fast enough or even possible,
  switch to a simpler, safe, non-optimal behavior instead — trading
  quality for a guarantee that the failure mode is bounded.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

# Fallback to a Safe Default

[Roll back vs. roll forward](rollback-vs-roll-forward.md) covers the usual
two mitigation options for a bad change. Both can be unavailable at once:
rollback can be blocked by the schema, format, or dependency hazards
described in [progressive rollout data-layer
isolation](progressive-rollout-data-layer-isolation.md), and roll-forward
(or, for a model, [retraining](retraining-as-roll-forward-for-models.md))
can simply be too slow for the incident at hand.

A third option in that case is falling back to a simpler, safe,
non-optimal behavior instead of either reverting or fixing forward: for
example, serving a generic, non-personalized top-10 list instead of a
broken personalized-recommendation model. It won't be the right answer for
anyone, but it also won't be badly wrong for anyone — trading away
quality in exchange for a bounded, predictable failure mode. This
generalizes past ML models to any component with an optimized primary path
and a cheap, well-understood degraded path — a cached last-known-good
response, a static default configuration, a generic fallback response —
whenever the primary path's specific failure is either unknown or too
costly to chase down live.

Unlike a per-feature [feature flag](feature-flag-blast-radius-isolation.md),
which turns a feature off entirely, a safe-default fallback keeps the
feature *on* in a deliberately degraded form — useful exactly when turning
the feature off entirely would be a worse user outcome than serving it
badly-but-safely. The fallback path itself needs to be built and exercised
before it's needed, not improvised during the incident it's meant to
contain.
