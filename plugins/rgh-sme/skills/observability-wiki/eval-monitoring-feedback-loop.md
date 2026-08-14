---
type: concept
title: Eval/Monitoring Feedback Loop
description: Evaluation and production monitoring for an AI/LLM system should be tightly coupled in both directions — eval metrics should predict what monitoring will see in production, and issues monitoring detects in production should feed back into the eval pipeline — rather than treated as separate pre- and post-deployment concerns.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
---

Evaluation and monitoring share the same underlying goal — mitigate risk from application failures, security issues, and drift, and surface opportunities for improvement — but applied at different points in the lifecycle. Treating them as coupled rather than separate stages of a pipeline matters in both directions:

- **Eval metrics should predict monitoring performance.** If an eval suite scores a change as safe but production monitoring later catches a regression the eval never would have, the eval pipeline has a blind spot, not just the monitoring.
- **Monitoring-detected issues should feed back into the eval pipeline.** A failure mode discovered in production telemetry should become a case the offline eval suite checks for going forward, so the same class of failure gets caught before the next deployment rather than only after.

One diagnostic signal for whether this loop is actually working: **change failure rate (CFR)** — the percentage of changes/deployments that cause a failure requiring a fix or rollback. Not knowing your CFR at all is itself a sign the system needs to be redesigned for observability. A high CFR is not automatically a monitoring failure, though — it can equally mean the eval pipeline needs rework so that bad changes are caught *before* deployment rather than relied on monitoring to catch them after.

This coupling is also why sampled manual review of production data stays valuable even once automated metrics and dashboards exist: developers' sense of what counts as a good or bad output shifts as they see more real production data (Shankar et al., 2024), and that recalibration is exactly what should be flowing back into both prompt/system revisions and the eval pipeline's own checklist criteria — the human judgment underlying the eval pipeline is itself a thing that drifts and needs refreshing from live telemetry. See [explicit vs. implicit feedback signals as telemetry](explicit-vs-implicit-feedback-telemetry.md) for the online-monitoring side of this loop specifically, and [silent model version drift](silent-model-version-drift.md) for one concrete failure class this loop needs to be sensitive enough to catch.
