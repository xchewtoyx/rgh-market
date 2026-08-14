---
type: concept
title: Pre-Rollout Model Comparison Testing
description: >
  Comparing a candidate model against the current production model on the
  same inputs before any real traffic is at risk, using preproduction
  sandbox runs and a hybrid local-vs-production comparison to catch both
  behavioral regressions and training/serving skew.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

# Pre-Rollout Model Comparison Testing

Before a new or retrained model reaches any real traffic, two questions need
answering: does it actually improve on the metric it's meant to improve
(business validation against a baseline), and does it behave differently
from the current production model in ways that matter? Answering the second
question well requires comparing the candidate against the incumbent
directly, not just against a static historical benchmark.

## Preproduction / sandbox comparison

Run the candidate and the current production model — in parallel or in
series — over the same input data entirely outside production, and diff
their outputs. This is the cheapest and lowest-risk comparison technique
because no production traffic or infrastructure is involved at all; its
limit is exactly that isolation — it can't catch anything that only
manifests under real production load, concurrency, or infrastructure
configuration.

## Hybrid local-vs-production comparison: catching training/serving skew

Send the same test requests to both a local copy of the candidate model and
the live production model (the local copy never takes real production
traffic), and compare results. Because the local copy runs outside the
production serving stack, a difference between the two outputs on identical
input isolates a specific class of bug: divergence between how the model
behaves in its modeling/training environment versus how it's actually
invoked in production — feature computation differences, configuration
drift, or serialization mismatches between the two environments, rather
than a difference in the model itself. This is a targeted way to catch
[training-serving skew](training-serving-skew.md) before it reaches any
real user, distinct from comparing the two model *versions'* behavior.

## Where this fits relative to production-traffic techniques

Sandbox and hybrid comparison both run before any production traffic is
involved, which is exactly what they can't validate: real user data shapes,
real concurrency, and real infrastructure contention. The techniques that
pick up after this point use actual production traffic instead of
synthetic/replayed test data:

- **Shadowing**: send real production traffic to the candidate model but
  discard its output rather than serving it to users, exercising most of
  the serving path under genuine load without any user-facing risk. This is
  the model-rollout instance of the general [dark
  launching](dark-launching.md) pattern.
- **Canary testing**: give the candidate a small slice (typically 1-5%) of
  real production traffic and actually serve its results, which additionally
  exposes how the model performs under genuine user *reaction* — see [canary
  release](canary-release.md) for the general mechanism, which overlaps with
  [A/B testing](ab-testing-via-release-routing.md) once the comparison is
  business-metric-driven rather than defect-driven.

Together these form an escalating-risk sequence — sandbox, hybrid,
shadow, canary — each stage catching a class of problem the previous one
structurally can't, at the cost of moving progressively closer to real user
exposure. See [ML dependency regression gate](ml-dependency-regression-gate.md)
for a related but distinct comparison: evaluating a model against a fixed
eval dataset when an *upstream* dependency changes, rather than comparing
two versions of the model itself.
