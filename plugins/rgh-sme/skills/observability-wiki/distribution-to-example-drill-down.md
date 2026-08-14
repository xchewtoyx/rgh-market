---
type: concept
title: Distribution-to-Example Drill-Down Interface
description: An explorable telemetry UI lets a user go from a bucketed distribution over a chosen cost metric straight to a concrete example instance in that bucket, turning "why is this pattern slow" from a manual search for a representative case into one click.
sources:
  - title: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure"
    resource: "Dapper, a Large-Scale Distributed Systems Tracing Infrastructure (Sigelman et al.), §5.2"
---

A recurring shape for exploring a large collection of traces or events: first let the user pick a cost metric relevant to their investigation (latency, error rate) and a scope (service, time window); then show a distribution over that metric — a frequency histogram bucketed by cost — rather than a single collapsed summary number; then, for any bucket the user picks, surface a handful of **concrete example instances** that landed in it, ready to open directly.

This closes the gap between "I can see there's a cluster of slow executions around 800ms" and "here is one of them to actually inspect," without the user having to separately query for a matching example by hand. It's a specific, concrete instance of the shift [away from static dashboards toward open-ended exploration](dashboard-glanceability-constraint.md) — the histogram-plus-examples view only makes sense as an interactive drill path, not as a fixed panel — and it complements rather than replaces [automated outlier-field ranking](high-cardinality-outlier-isolation.md): ranking tells you *which field* explains an anomalous bucket, this pattern gets you *a real instance* to read once you've picked a bucket to investigate. Both depend on retaining per-event/per-trace detail rather than only pre-aggregated numbers — see [pre-aggregation is irreversible](pre-aggregation-is-irreversible.md).
