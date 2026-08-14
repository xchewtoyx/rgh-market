---
type: concept
title: Rollback and Roll-Forward
description: >
  A release strategy needs a tested, automated way to either revert to the
  previous known-good version (rollback) or rapidly ship a corrective fix
  (roll-forward) when a release turns out to be bad.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
---

# Rollback and Roll-Forward

Two distinct recovery paths for a release that turns out to be bad:

- **Rollback**: revert production to the previous known-good version.
  Zero-downtime deployment patterns provide this almost for free —
  [blue-green deployment](blue-green-deployment.md) rolls back by switching
  the router back to the old environment; [canary release](canary-release.md)
  rolls back by routing traffic away from the canary; a
  [rolling deployment](rolling-deployment.md) rolls back by rolling the
  previous version back out across the fleet.
- **Roll-forward**: rather than reverting, push a corrective fix through the
  pipeline as a new release. This is the same mechanism as any other change —
  see [emergency fixes follow the same pipeline](hotfix-through-pipeline.md).
  Roll-forward is only safe when it can move as fast as the incident does:
  it depends on the same automated testing and fast, reliable pipeline that
  make any other change safe to ship, plus enough telemetry in place to
  confirm the fix actually worked. This is the basis for the maxim "optimize
  for MTTR, not MTBF" — favoring the ability to recover fast over trying to
  prevent every possible failure.

Rollback is not always available for free: if the release included a
database migration that isn't backward-compatible, rolling the application
back without also reversing the migration can break it against the old code
path — see
[backward-compatible schema migration](backward-compatible-schema-migration.md).
This is why a rollback plan has to be designed and tested alongside the
release itself, as part of
[release strategy components](release-strategy-components.md), not assumed to
always be "just redeploy the old version."

## Why rollback is not actually risk-free

"True" rollback is a myth in a live system: everything around the release —
other services' versions, in-flight data, accumulated state — has moved on
since the previous version last ran, so reinstalling the "known good" build
is itself an under-tested production change, just one made under worse
conditions, during an active incident, with risk tolerance at its lowest.
This is the deeper argument for preferring roll-forward whenever the pipeline
is fast enough to support it: shipping a real fix through the same tested
path every other change goes through is a more controlled action than
reverting to a state the rest of the system no longer fully matches. Where
roll-forward genuinely isn't fast enough, a narrowly-scoped, deliberately
under-tested emergency hotfix is a legitimate middle ground between the two —
provided it's tracked and followed up with a project to close the gap that
made the hotfix necessary.

## Applied to ML models: retraining as roll-forward

For a deployed ML model, **retraining** is the roll-forward equivalent: build
a new model and ship it, rather than reverting to a previous one. It has two
weaknesses roll-forward for ordinary code doesn't share:

- Retraining over exactly the same data reproduces exactly the same
  behavior — the fix has to come from a deliberate change to the training
  data itself (a new or corrected corpus, a different date range, adjusted
  example weighting), not just re-running the same job.
- There is no inherent guarantee a retrained model is actually *better* — an
  arbitrarily different training window (e.g. one that happens to span an
  atypical period like a holiday) can produce a worse model than the one
  being replaced. Without validation automation comparable to a code
  pipeline's automated tests, retraining pays both compute and staff-review
  cost on every attempt with no guaranteed payoff, which is a strong
  argument for building automated [pre-rollout model comparison
  testing](pre-rollout-model-comparison-testing.md) rather than relying on
  manual review of each retrained candidate.

**Rollback** for a model means reverting to a previous versioned model
binary — which requires actually keeping old model binaries around and
tracking which version is live; see [model provenance and snapshot
retention](model-provenance-and-snapshot-retention.md) for what a training
pipeline needs to retain, beyond the general
[artifact repository](artifact-repository.md) discipline for code builds,
to make that rollback actually possible.
Model rollback has its own hazard beyond the general one above: if a feature
store, feature-transformation logic, or upstream data schema changed between
model versions — e.g. one version defaults a missing input to "last seen
value" while a newer version defaults it to "closest saved value" — reverting
the model without also reverting whatever produces its inputs can leave the
old model receiving inputs shaped for the new one. This is the same
expand/contract discipline [backward-compatible schema
migration](backward-compatible-schema-migration.md) describes for databases,
applied to the feature pipeline a model depends on, and it can block rolling
*forward* just as easily as it blocks rolling back, until the mismatch itself
is understood.

**Fallback to a simpler, hardcoded response** is a third recovery option
specific to models, sitting outside the rollback/roll-forward pair: instead
of serving either the old or new model, serve a deliberately non-personalized
default (e.g. top-10 most popular items instead of broken personalized
recommendations). It won't be optimal for anyone, but it bounds how wrong the
response can be, and it's a useful last resort precisely when both rollback
and roll-forward are blocked by the hazards above.
