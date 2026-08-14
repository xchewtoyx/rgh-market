---
type: concept
title: Change Correlation in Debugging
description: Because most outages stem from a recent change, inspecting recent code pushes, configuration changes, flag toggles, and environment changes should be an early, default hypothesis-generation step in any investigation.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 12"
---

Roughly 70% of outages stem from a recent change. When generating hypotheses for an unexplained failure, checking what changed recently — deployments, configuration edits, feature-flag toggles, dependency version bumps — is one of the highest-yield first moves, and can often be automated (a "change correlator" tool inspecting recent pushes against the failure timeline).

Two related traps to be aware of when applying this heuristic:

- It's necessary but not sufficient: correlation with a deployment doesn't guarantee causation — see [correlation vs. causation in debugging](correlation-vs-causation-in-debugging.md) for a worked counterexample where an outage was correlated with, but not caused by, a deployment.
- Overlaying deployment events directly onto metric graphs makes this correlation visible at a glance rather than requiring a separate lookup — see [deployment markers and settling period](deployment-markers-and-settling-period.md).
