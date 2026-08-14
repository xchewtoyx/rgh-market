---
type: concept
title: Symptom-Based vs. Cause-Based Alerting
description: Alerts should fire on evidence of actual user-facing impact (a symptom), not on a presumed underlying cause, because cause-based conditions generate false positives whenever the system absorbs them gracefully.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 6"
---

Two ways to define an alerting condition:

- **Symptom-based (preferred)**: alert on actual user impact, e.g. "HTTP 500 error rate > 1%" or "99th percentile latency > 500ms." This directly reflects whether users are being hurt right now.
- **Cause-based (discouraged for paging)**: alert on an underlying potential cause, e.g. "MySQL CPU utilization > 90%" or "server X disk space > 80%." Cause-based alerts fire even when the system handles the condition gracefully with no user-visible effect, generating false positives and contributing to [alert fatigue](alert-fatigue-and-normalized-deviance.md).

The distinction maps onto a "what" vs. "why" split: symptom-based alerting answers *that* something is degrading the user experience, while diagnosing *why* is a separate, subsequent investigation — see the [core analysis loop](core-analysis-loop.md) for how that investigation proceeds once a symptom-based alert fires.

Cause-based signals (CPU, disk, queue depth) are still valuable as [saturation](four-golden-signals.md) telemetry for diagnosis and capacity planning — they are just poor material for paging decisions specifically.
