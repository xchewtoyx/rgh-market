---
type: concept
title: Cluster Immune System
description: >
  Extending a canary release by wiring production monitoring directly into
  the release process, so a deviation in user-facing metrics triggers an
  automatic rollback rather than waiting for a human to notice and act.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 12"
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 8"
---

# Cluster Immune System

A [canary release](canary-release.md) relies on someone or something
watching telemetry and deciding whether to keep promoting or roll back. A
cluster immune system automates that decision: production monitoring is
linked directly to the release process itself, and if a key user-facing
metric moves outside a predefined expected range — the example given is a
new-user conversion rate dropping below its historical 15–20% norm — the
system triggers an automatic rollback without waiting for a human to notice.

## Compare against a live baseline, not a historical threshold

A fixed threshold ("conversion rate below 15%") is vulnerable to whatever
else is varying at the same time — time of day, current load, an unrelated
upstream incident — any of which can trip the threshold on a perfectly good
release, or mask a real regression that happens to land during a low-traffic
period. A more robust version runs a matched baseline group on the current
stable version concurrently with the canary, and compares the canary's
metrics statistically against that live baseline rather than against a
fixed historical number — isolating the effect of the new version itself
from whatever else is happening in production at that moment.

## Why this catches what tests can't

Some defects are essentially invisible to automated pre-deployment testing —
the example given is a CSS change that silently hides a critical page
element, which no functional test asserting on the DOM structure would
necessarily catch, but which shows up immediately as a drop in a business
metric like conversion rate. A cluster immune system catches this class of
problem specifically because it watches *outcomes* rather than *behavior*,
and reacts faster than a human monitoring a dashboard would.

Because canary releases already require running multiple software versions
in production simultaneously, minimizing that version count (often via the
[expand-contract pattern](backward-compatible-schema-migration.md) for any
accompanying schema change) matters just as much here as it does for a plain
canary — the automated rollback has to be safe to execute at any moment,
which depends on the same backward-compatibility discipline.
