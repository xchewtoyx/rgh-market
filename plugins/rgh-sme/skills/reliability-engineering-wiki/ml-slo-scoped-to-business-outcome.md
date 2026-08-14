---
type: concept
title: ML SLOs Scoped to Business Outcome
description: >
  SLOs for a model-backed system should be scoped around the business
  objective the system delivers, not around raw model-performance statistics,
  because model quality alone can't establish whether the system is
  fulfilling its purpose.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

Statistical model-quality metrics (AUC, log loss, accuracy) don't by
themselves capture the concrete business impact users experience when those
metrics degrade — model suitability can't be assessed from the model alone.
Best practice is to scope the SLO around the **business objective** the ML
system is meant to deliver rather than around raw model or ML-service
performance: framed this way, the system as a whole can tolerate temporary
model-quality degradation as long as overall user experience stays within
defined limits, which is a direct application of
[user-centric SLI selection](user-centric-sli-selection.md) to a model-backed
system.

Practical consequence: choose model-performance metrics that are as
representative of business impact as possible, since the more representative
the metric, the easier it is to connect a metric change to a real business
consequence — correlating available signals with business value is treated as
one of the highest-leverage things an ML-serving organization can do.

This is distinct from *how* a graded, non-binary model output gets turned
into a good/bad judgment for that SLI in the first place — see
[ML prediction confidence as SLI](ml-prediction-confidence-as-sli.md) — and
from the fact that, in practice, this business-objective scope usually can't
be drawn around the ML system in isolation — see
[ML system SLO entanglement](ml-system-slo-entanglement.md).

This business-outcome scope is one of three separations of concern worth
keeping distinct when setting ML SLOs generally — see
[ML SLO separation of concerns](ml-slo-separation-of-concerns.md) for how it
relates to the serving/training/application layer split and to the
golden-signals-vs-ML-internal-signals split.
