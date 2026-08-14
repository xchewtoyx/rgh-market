---
type: concept
title: Per-Model Self-Service SLOs
description: >
  In environments with many models or high model churn, letting ML engineers
  define and enforce their own per-model or per-model-class SLOs through
  self-service infrastructure scales better than a central team hand-rolling
  each one.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

When an organization runs many models, or replaces/retrains models
frequently, a central team defining every model's
[SLO](service-level-objective.md) by hand doesn't scale. A promising pattern:
build self-service infrastructure that lets the ML engineers who own a model
define and enforce an SLO for that specific model or for a whole class of
similar models — typically evaluated by comparison against a golden dataset
— while the reliability/platform team builds and supports the underlying
measurement service rather than authoring each target itself. Where the
relevant use-case tagging can be done deterministically, the same pattern
extends further, down to per-use-case SLOs within a single model.

This is an organizational/tooling pattern for *scaling how many* ML SLOs get
defined and maintained, distinct from the question of what should count as
the underlying good-event signal for any one of them — see
[ML prediction confidence as SLI](ml-prediction-confidence-as-sli.md).
