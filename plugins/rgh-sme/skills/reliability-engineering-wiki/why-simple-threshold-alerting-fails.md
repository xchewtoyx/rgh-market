---
type: concept
title: Why Simple Threshold Alerting Fails
description: >
  Alerting on a fixed metric threshold is cheap to build but degrades
  predictably over time and structurally can't see slow, distributed, or
  emergent failure modes.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 8"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
---

Traditional threshold alerting — pick a metric, guess a bad number, alert
when it's crossed — fails for five compounding reasons:

1. **Thresholds don't stay relevant.** Even modest compound growth erodes a
   fixed threshold's meaning within about a year; thresholds are usually
   only revised reactively, after an outage exposes their staleness.
2. **Poor proxies for user experience.** Teams often alert on an
   easy-to-measure proxy (server-side CPU) instead of what actually matters
   (client-side latency), and over time forget the proxy was ever a
   stand-in. See [user-centric SLI selection](user-centric-sli-selection.md).
3. **Context loss in static thresholds.** A fixed constant behaves very
   differently at low vs. high traffic — over-sensitive when traffic is low,
   effectively noise-proof (and thus useless) at high traffic.
4. **Unclear correlation with actual bad behavior.** For continuous metrics
   with a large "maybe" zone between clearly-good and clearly-bad, absent
   better signal, thresholds tend to ratchet down after every complex
   outage ("to catch it next time"), degrading over time into
   false-positive-generating triggers untethered from real impact.
5. **Alert fatigue.** Repeated false positives erode a responder's ability
   to distinguish true from false signals over time — and organizational
   incentives (fear of being blamed for a missed outage) push thresholds to
   get *stricter*, not looser, worsening fatigue rather than curing it.

Modern distributed architectures are designed to tolerate component
failure and are inherently complex; threshold alerting on individual
internal metrics can't see emergent, multi-component failure modes, because
there's no single "smoking gun" metric to alert on.

**Evaluating any alerting approach** (including SLO-based alternatives) uses
four criteria: **precision** (proportion of alerts that were significant),
**recall** (proportion of significant events actually detected),
**detection time** (how fast the alert fires), and **reset time** (how long
the alert keeps firing after the underlying problem resolves — a long reset
time causes confusion and gets ignored). Threshold alerting scores poorly on
several of these depending on the exact variant chosen (a short window has
good detection time but poor precision; a long window improves precision at
the cost of reset time).

See [multiwindow multi-burn-rate alerting](multiwindow-multi-burn-rate-alerting.md)
for the alternative this critique motivates, and
[actionable alert philosophy](actionable-alert-philosophy.md) and
[symptom-based alerting](symptom-based-alerting.md) for the
underlying principles both approaches are trying to satisfy.
