---
type: concept
title: A/B Testing via Release Routing
description: >
  Reusing the same traffic-routing mechanism that powers canary releases to
  run a controlled business-metric experiment between two live variants,
  rather than to detect defects.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 5"
---

# A/B Testing via Release Routing

A/B testing sends different user segments to different live variants of a
feature (a font size, a checkout flow, a pricing display) using the same
DNS- or discovery-service-based routing mechanism a
[canary release](canary-release.md) uses to split traffic. The mechanism is
identical; the purpose is not.

## How it differs from canarying

[Canary release](canary-release.md) exists to catch **defects** before they
reach the full fleet — its evaluation criteria are operational (error rates,
latency, log anomalies) and a clean canary is promoted to 100% as fast as
confidence allows. A/B testing exists to compare **business outcomes**
(conversion rate, revenue per user, engagement) between two variants that are
each presumed non-defective — its evaluation criteria are product metrics,
not SLIs, and both variants may legitimately keep running side by side for
the full length of the experiment rather than converging toward one winner
quickly.

Because the evaluation question is different, an A/B test needs its own
metric plumbing (conversion funnels, revenue attribution) separate from the
operational telemetry a canary reads — reusing canary dashboards for an A/B
test, or vice versa, answers the wrong question.

## Cost

Unlike a canary, which is disposed of as soon as the new version is fully
promoted, an A/B test requires building and maintaining **both** variants for
the duration of the experiment, plus a plan for discarding the losing variant
afterward. User segments and targeting characteristics have to be defined
up front, same as the power-user targeting a canary or
[dark launch](dark-launching.md) needs.

A [feature toggle](feature-toggle.md) is the usual mechanism for holding both
variants in the same deployed codebase and switching between them per
request, rather than actually deploying two different builds.
