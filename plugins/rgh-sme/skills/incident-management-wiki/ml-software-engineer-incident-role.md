---
type: concept
title: Software Engineer Incident Responsibilities (ML Systems)
description: How the engineer who builds the glue code around ML pieces should prepare to be a rarely-paged escalation point rather than a routine incident participant.
sources:
  - title: "Reliable Machine Learning: Applying SRE Principles to ML in Production"
    resource: "Reliable Machine Learning: Applying SRE Principles to ML in Production (Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood), ch. 11"
---

The software engineer implementing the systems software that glues ML
pieces together and moves data should aim to be an escalation point who is
rarely paged, not a routine incident participant — that outcome is a
function of preparation done beforehand, not luck. Two preparation choices
matter most for reducing incident load:

- Keeping model and binary rollouts separate and separable. Inference
  binaries and the models they read should ship to production
  independently, each with its own quality evaluation, because either can
  subtly affect quality on its own. Coupling the two rollouts makes
  troubleshooting an incident harder — a responder can no longer tell
  whether a regression tracks the binary or the model without first
  untangling a joint deploy.
- Keeping feature handling consistent between training and serving.
  Differences between the two — training-serving skew — are one of the
  most common ML failure sources: a quantization difference, or worse, a
  feature's meaning silently changing (a field switching from income to
  zip code, say). This is the kind of failure that manifests as an
  unexplained quality drop with no obvious error, which is exactly the
  hardest incident to triage.

When this role is paged, failures can originate across model servers, data
synchronizers, data versioners, model learners, training orchestration, or
the feature store — but a well-architected system reduces that surface to a
handful of large systems (a feature store, a training pipeline, a
model-quality analytics system, and a serving system), each only slightly
harder to reason about during an incident than its non-ML equivalent. Better
exporting of software state for monitoring, and resilience to large data
shifts, are the improvements this role most commonly identifies after an
incident.

See also [model developer incident
responsibilities](ml-model-developer-incident-role.md).
