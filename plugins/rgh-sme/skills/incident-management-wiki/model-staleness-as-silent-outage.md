---
type: concept
title: Model Staleness as a Silent Outage
description: A model-training pipeline can fail in a way that produces no error at all, only a model that silently stops updating, so incident readiness needs a direct check on model age rather than trusting pipeline health signals.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

In a documented case, a search-ranking model's click-through rate dropped
steadily for three weeks before anyone noticed. The cause: log-feeder
processes reading raw customer logs had been crash-looping from
out-of-memory errors the entire time — each crash restarted the process on
a new machine, the training job retried, read a few bytes, and crashed
again, so no training run ever completed. The crash loop itself was
visible in infrastructure logs, but nothing about it looked like a
top-level outage — no service was down, no request was erroring — it just
silently prevented the model from ever refreshing. The only end-to-end
symptom was a slow quality decline that took three weeks to become
undeniable, and the retraining pipeline's own daily golden-set stability
(which should show minor day-to-day drift as the model absorbs new signal)
had actually gone suspiciously *flat*, which in hindsight was the tell:
constant golden-set results meant the model itself hadn't changed at all.

The general lesson: a training or refresh pipeline that fails upstream of
its own output doesn't necessarily fail loudly. Monitoring the pipeline's
internal health (is it running, is it erroring) is not the same as
monitoring what it's supposed to produce. The direct, harder-to-fool check
is model age itself — both wall-clock age since last successful training
and data age (how recent is the data the current serving model was
actually trained on) — alerted on past an explicit staleness threshold,
independent of whether any pipeline stage is currently reporting an error.
Defining that threshold up front, and budgeting how much of it is spent in
each pipeline stage (extraction, training, evaluation, deployment), turns
"the model must be fresh within 48 hours" from an aspiration into
something an alert can actually enforce — the same pre-negotiated-threshold
discipline described in [ML pre-negotiated outage
thresholds](ml-pre-negotiated-outage-thresholds.md), applied to freshness
specifically rather than only to quality metrics.
