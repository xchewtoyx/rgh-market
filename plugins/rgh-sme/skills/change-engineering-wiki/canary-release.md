---
type: concept
title: Canary Release
description: >
  Deploy a change to a small, time-limited subset of production capacity or
  traffic and evaluate it against the unchanged rest of the fleet before
  deciding whether to roll it out further.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 13"
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 16"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16"
---

# Canary Release

Canary release routes a small fraction of live traffic, or deploys to a
small subset of instances (e.g. 1-5%), to the new version — the "canary" —
while the rest of the fleet — the "control" — keeps running the previous
version unchanged. It is effectively A/B testing applied to releases: the
goal is to detect defects on a small population before they reach
everyone, because of [pre-production fidelity
limits](pre-production-fidelity-limits.md) — pre-production tests never
achieve full production fidelity.

A canary process needs three things:

1. A way to deploy the change to a population subset (the canary fraction
   should scale with total population size) — preceded by a
   [pre-canary artifact smoke test](pre-canary-artifact-smoke-test.md) to
   rule out a structurally broken artifact before spending any canary
   population on it.
2. An evaluation process that classifies the canary as "good" or "bad" —
   see [canary metric selection](canary-metric-selection.md) and
   [canary measurement validity](canary-measurement-validity.md).
3. Integration of that evaluation into the release process itself —
   automatic pause/rollback, or escalation to a human — often implemented
   via [production prober testing](production-prober-testing.md) canary
   analysis (prober assertions plus metric divergence vs baseline).

Why it matters more than testing alone: a full rollout of a bug that
induces a 20% error rate produces a sustained 20% platform-wide error rate
with no rollback path already in place. The same bug, canaried to 5% of
traffic, produces roughly a 1% overall error rate, and per-version metric
breakdown (see [canary measurement validity](canary-measurement-validity.md))
makes the release candidate's failure obvious — enabling automatic
rollback before the rest of the fleet is ever touched.

How large the canary should be and for how long is a separate design
question — see [canary population and duration selection](canary-population-and-duration-selection.md).
For batch and streaming pipelines rather than request-serving services, see
[canarying pipeline systems](canarying-pipeline-systems.md). Compare with
[blue-green deployment](blue-green-deployment.md) (binary cutover between
two full environments), [rolling deployment](rolling-deployment.md)
(sequential in-place update with no held-back control population), and
[traffic teeing](traffic-teeing.md) (duplicating real traffic to a system
whose responses are discarded, rather than serving real responses to a
real subset of users).
