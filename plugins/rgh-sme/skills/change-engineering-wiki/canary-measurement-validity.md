---
type: concept
title: Canary Measurement Validity
description: >
  A canary verdict is only trustworthy if canary and control are measured
  at a fine enough granularity and aren't contaminating each other, and if
  the comparison is population-based rather than time-based.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
---

# Canary Measurement Validity

Three ways a [canary](canary-release.md)'s evaluation can be undermined
even when the [metrics chosen](canary-metric-selection.md) are correct in
principle:

**Aggregation hides the signal.** Monitoring must support fine-grained
breakdown by population (canary vs. control) — whole-service aggregate
monitoring can make a real defect statistically invisible. A 20% error
rate confined to 5% of traffic looks like a 1% error rate in an aggregate
view. Also, the metric aggregation window must be no longer than the
canary duration: a canary that runs for 30 minutes evaluated against an
hourly-computed "errors per hour" metric gets a muddied signal, because the
window mixes canary-period and non-canary-period data.

**Shared fate contaminates the comparison.** Canary and control usually
share backends, frontends, networks, and datastores — imperfect isolation
means a canary-triggered stop-and-investigate signal doesn't guarantee the
canary itself is at fault, and a misbehaving canary can leak into and
distort the control group's metrics too. Always also check absolute SLO
thresholds, not just the relative canary-vs-control comparison, since a
shared-fate problem can move both groups together and hide in the
relative delta.

**Time is not a substitute for population.** "Canarying in time-space" —
comparing before/after a release instead of a canary population against a
held-back control — is risky because time is a major confound (day-of-week
and time-of-day traffic shape differs on its own), and a full before/after
comparison exposes 100% of traffic to the bug being tested for, rather
than a small canary fraction. Prefer a population-based canary/control
split whenever one is possible.
