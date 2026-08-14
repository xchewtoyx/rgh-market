---
type: concept
title: Silent Model Version Drift
description: A third-party model API provider can swap the model behind a stable endpoint without disclosing it, changing application behavior with no corresponding entry in your own deploy history — defeating ordinary change correlation and requiring active, dedicated drift monitoring instead.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering: Building Applications With Foundation Models (Chip Huyen), ch. 10"
---

[Change correlation in debugging](change-correlation-in-debugging.md) assumes the change responsible for a regression shows up in your own recent pushes, config edits, or flag toggles — that assumption breaks for a model API dependency. The API surface (endpoint, model name) can stay identical while the model actually serving requests changes underneath it, and providers don't always disclose this. Chen et al. (2023) found notable benchmark-score differences between the March 2023 and June 2023 versions of GPT-4 and GPT-3.5 despite no visible interface change; Voiceflow reported a 10% performance drop after their provider moved `gpt-3.5-turbo-0301` traffic to `gpt-3.5-turbo-1106`. (A milder, fully diffable sibling of this problem is an unannounced system-prompt-template edit — e.g. a coworker's typo fix — which simple text diffing catches; a vendor-side model swap has no equivalent diff to inspect.)

Because there is no deploy-log entry to correlate against, catching this requires monitoring output quality/behavior metrics over time and treating an unexplained shift as a drift hypothesis even when nothing in your own system changed — see [the eval/monitoring feedback loop](eval-monitoring-feedback-loop.md) for how production monitoring and evaluation metrics are kept coupled well enough to surface this kind of shift. Where a provider supports pinning a specific model version rather than a floating alias, pinning removes this failure mode at the cost of losing automatic access to improvements.
