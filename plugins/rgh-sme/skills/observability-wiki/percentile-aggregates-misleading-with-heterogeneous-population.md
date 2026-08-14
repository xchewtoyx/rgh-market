---
type: concept
title: Percentile Aggregates Can Mislead With a Heterogeneous Population
description: A percentile like p50 is only informative about "what to expect" when the population behind it is relatively homogeneous; across a wildly heterogeneous population (thousands of device/OS/network combinations), p50 or even p99 can look fine while a real, severe problem affects a small slice invisibly.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 19"
---

[Tracking percentiles instead of averages](latency-percentiles-not-averages.md) is generally the right instinct — but a percentile is only a useful summary of "what a typical user experiences" when the population contributing to it is reasonably homogeneous. Backend systems under normal load are close enough to homogeneous that p50 is informative for capacity planning and general health.

Mobile and frontend telemetry breaks this assumption: the population spans thousands of device/OS/browser/network combinations with enormously different baseline performance (a nine-year-old phone next to a brand-new one). In a population this heterogeneous, p50 tells you little about what any specific slice of users is actually experiencing — and a problem affecting only 1% of users can be entirely invisible in both p50 and p99 aggregates while being severe, even life-or-death for that 1% (at 100M daily active users, 1% is a million people).

The practical response is not to abandon percentiles but to pair them with segment-aware analysis (comparing across device tiers, versions, cohorts explicitly, as in the [core analysis loop](core-analysis-loop.md)) or to reach for a metric that isn't a technical aggregate at all — see [outcome-completion rate as a UX proxy](outcome-completion-rate-as-ux-proxy.md) for one such alternative.
