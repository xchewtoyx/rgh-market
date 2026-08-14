---
type: concept
title: User-Centric SLI Selection
description: >
  Reliability is defined by how a service appears to the user experiencing
  it, not by internal metrics, so SLIs must be chosen from the user's vantage
  point rather than from whatever is easiest to instrument.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 4"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 1, ch. 2"
---

Zero logged internal errors doesn't matter if users perceive the service as
unreliable. Reliability ≈ "is the service doing what its users need it to
do?" — and that judgment can only be answered by measuring from the user's
vantage point: successful HTTP 200 responses vs. 5xx errors, not
server-side CPU usage or other easy-to-measure proxies that happen to
correlate with reliability today but may not tomorrow.

"User" is broad: a human, a paying customer, another internal service, or an
automated caller — anything relying on the service counts.

This principle is why alerting built on internal/proxy signals tends to
degrade over time (see
[why simple threshold alerting fails](why-simple-threshold-alerting-fails.md)):
a proxy can drift away from what it originally stood in for without anyone
noticing.

A user's expectations aren't limited to whatever is formally promised —
[implicit SLOs form from past performance](implicit-slo-from-past-performance.md),
and [Hyrum's Law](implicit-slo-from-past-performance.md) means users will
come to depend on behaviors nobody intended to promise.

Practical consequence: for a complex, multi-component service, one internal
hop's error rate is not representative of the true end-to-end experience —
see [end-to-end vs per-component SLI measurement](end-to-end-vs-per-component-sli-measurement.md)
and [critical user journeys](critical-user-journey.md).

For a model-backed system, the same user-vantage-point principle argues for
scoping the SLO around the business outcome the system delivers rather than
around raw model statistics — see
[ML SLOs scoped to business outcome](ml-slo-scoped-to-business-outcome.md) —
and for treating a graded, confidence-scored prediction as something other
than a plain binary up/down signal, see
[ML prediction confidence as SLI](ml-prediction-confidence-as-sli.md).
