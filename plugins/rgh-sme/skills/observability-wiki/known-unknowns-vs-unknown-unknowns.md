---
type: concept
title: Known-Unknowns vs. Unknown-Unknowns
description: Threshold and runbook-based tooling handles known-unknowns well — failure modes you can name and check for in advance — but distributed systems increasingly fail via unknown-unknowns, novel combinations of conditions nobody wrote a check for, which require exploratory investigation rather than a pre-built alert.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 3"
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 11"
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins, Beyer, Blankinship, Lewandowski, Oprea, Stubblefield), ch. 15"
---

**Known-unknowns** are enumerable, nameable risks: you know the failure mode exists, you just don't know if it's occurring right now (disk filling up, a dependency timing out). Traditional monitoring — threshold/cause-based alerts, runbooks keyed to specific symptoms — handles these well, because someone could write the check in advance.

**Unknown-unknowns** are emergent, novel interactions nobody anticipated — a "harmless" deploy that happens to tip a downstream cache into eviction churn, for instance. In distributed systems, failure modes multiply combinatorially as services and dependencies grow, so unknown-unknowns become the norm rather than the edge case; by definition, you cannot pre-write a threshold check for a failure you can't yet imagine. Many unknown-unknowns are not even a single broken component but an [emergent failure](emergent-failure-vs-broken-component-hunting.md) arising from several normally-functioning parts interacting in a way nobody designed for — in that case there is no "the" bug to pre-check for at all, only a combination to characterize after the fact.

This distinction is directly analogous to [horses vs. zebras](horses-vs-zebras.md): known-unknowns are horses (common, previously-seen, checkable in advance); unknown-unknowns are zebras (rare, novel, only findable through open-ended investigation). It's also the deeper argument for exploratory, high-[cardinality](cardinality.md) querying over static dashboards and pre-built alerts — see the [core analysis loop](core-analysis-loop.md) and [debugging from first principles vs. tacit knowledge](debugging-from-first-principles-vs-tacit-knowledge.md), which are the investigative techniques suited to unknown-unknowns specifically. It also motivates what makes an alert genuinely [helpful](helpful-alert-criteria.md): a threshold check can only ever catch a known-unknown, so an alerting strategy that leans entirely on thresholds has a structural blind spot for anything novel.

This is also why instrumentation coverage itself needs deliberate attention rather than organic growth: see [the streetlight effect in instrumentation priorities](streetlight-effect-in-instrumentation-priorities.md) for why the best-instrumented paths are usually the ones that matter least for finding the next unknown-unknown.
