---
type: concept
title: Training-Serving Skew
description: Training-serving skew is any difference between a model's measured training-time performance and its actual serving-time behavior, commonly caused by feature-definition drift, gaps in the serving data, or a feedback loop between the model and the task — and because skew detection is inherently model-specific, the monitoring system must stay general-purpose while the actual skew checks are implemented per model.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

"Skew" in ML production covers a cluster of related data problems: biased distribution shifts, unexpected outliers, semantic violations in how data is interpreted, missing feature values (especially when the missingness is asymmetric across features), and loss of correspondence between two data streams that are supposed to stay in sync. The production-critical variant is **training-serving skew**: any difference between how a model performed during training and how it actually behaves in serving. Common causes:

- A feature's definition changing between the training pipeline and the serving path (the same feature name computed two different ways).
- Gaps or changes in the underlying data itself between when the model was trained and when it's serving live traffic.
- A feedback loop between the model's own predictions and the task it's predicting on (the model's outputs change the population of future inputs it sees).

**Key limitation, with a direct implication for how to build monitoring**: there is no known general-purpose function that detects "skew" for an arbitrary model — skew checks are inherently model-, architecture-, or purpose-specific. You can detect that training and serving performance differ without knowing why or whether it matters; you can't detect a coverage gap in a dataset without already knowing what the expected domain/coverage should have been. That means the monitoring *system* (the pipeline, storage, and query tooling) should stay general-purpose and flexible, but the actual skew checks for a given model have to be implemented jointly by the production engineers and the ML engineers who understand that model's specific inputs and failure modes — a monitoring platform can't ship this out of the box the way it can ship a latency histogram.

This is distinct from, and a broader category than, [silent model version drift](silent-model-version-drift.md) (a third-party provider swapping the model behind a stable API) and [user behavior adaptation as a drift cause](user-behavior-adaptation-as-drift-cause.md) (the input population itself changing over time) — those are two specific, well-characterized *causes* of the more general skew problem this note describes.
