---
type: concept
title: Staged Percentage Rollout
description: >
  Progress a change through a fixed sequence of environments and traffic
  percentages — dry run, staging, canary, then an increasing percentage of
  production — instead of jumping straight from testing to full deployment.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook: Practical Ways to Implement SRE (Google SRE series), ch. 13"
---

# Staged Percentage Rollout

A concrete pattern for taking a change from "written" to "fully deployed"
through a sequence of widening stages, each of which must pass before the
next begins:

**Prototype → 1% dry run** (small-scale test against production data in a
non-production environment) **→ Staging** (full-stack test against
production-like data, catching integration issues unit tests miss;
compares newly generated output against previously known-good output)
**→ Canary** (partial production deployment with monitoring — see
[canary release](canary-release.md); may need [two-phase mutation testing](two-phase-mutation-testing.md)
to validate real writes without committing them) **→ Partial deploy**
(feature-flagged rollout by percentage of accounts or data: roughly 1% →
10% → 50% → 100%) **→ Full production**.

This is [canary release](canary-release.md) and
[rolling deployment](rolling-deployment.md) composed into one named
sequence rather than two separate techniques — each stage is itself a
canary evaluation gating the next, larger stage. Multihomed or replicated
pipelines may not support clean single-cell canary progression through
this exact sequence; dry-run mode or partial data substitutes for the
canary stage in that case.

Progression between stages can be automatic (based on
[canary metrics](canary-metric-selection.md) crossing a threshold) or
gated by a human — see [manual approval release gates](manual-approval-release-gates.md)
for when the latter is warranted.
