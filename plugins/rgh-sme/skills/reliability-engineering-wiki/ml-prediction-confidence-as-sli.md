---
type: concept
title: ML Prediction Confidence as SLI
description: >
  A model-backed service's "availability" isn't binary up/down the way a
  plain request/response system's is, because predictions carry graded
  confidence and can be individually correct but still below a usable
  quality threshold.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning (Chen, Murphy, Parisa, Sculley, Underwood), ch. 9"
---

An ordinary [SLI](service-level-indicator.md) reduces each event to a binary
good/bad judgment — a page load was fast enough or it wasn't. A model's
output doesn't fail this cleanly: predictions typically carry a graded
confidence score (0.0–1.0), and a prediction can be individually
"correct" yet still fall below the confidence level needed for the
prediction to be useful. Treating the service as simply up or down misses
this — an ML SLI needs a quality/confidence threshold baked into the
good-event definition, not just a request-succeeded/request-failed check.

At the request-response service level specifically, this motivates alerting
on symptoms beyond plain errors: inability to produce a prediction at all,
predictions landing at drastically lower confidence than expected, and the
rate of falling back to an algorithmic (non-ML) default rising above its
normal baseline are all worth treating as SLI-relevant events in their own
right, alongside the [request-driven SLI](sli-types-by-service-category.md)
basics of latency, traffic, and errors.

This is the mechanism by which choosing *which* model-quality signal counts
as "good" becomes an SLI-selection decision in its own right, the ML analog
of picking the right good-event definition described in
[user-centric SLI selection](user-centric-sli-selection.md) — see also
[ML SLOs scoped to business outcome](ml-slo-scoped-to-business-outcome.md)
for how the target built on top of this signal should be framed.
