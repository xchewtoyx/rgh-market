---
type: concept
title: Critical User Journey
description: >
  A multi-step sequence of user interactions (e.g. search → add to cart →
  purchase) that captures what actually matters to users even though it
  doesn't map 1:1 onto any single existing SLI.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 2"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 10"
---

Per-component SLIs (e.g. one microservice's error rate) can each look
healthy while the sequence of steps a real user actually cares about — the
journey — still fails or degrades. A critical user journey is identified by
walking the actual path a user takes through the system and instrumenting
that path directly, rather than assuming per-component health implies
journey health.

Once instrumented, a critical user journey is treated as just another
[SLI](service-level-indicator.md) — it doesn't need a separate framework,
only a deliberate choice to measure across component boundaries instead of
within one.

Architecting a system around its critical user journeys — rather than
retrofitting SLOs onto whatever components already exist — means letting the
journey's failure cost drive investment: two services can each claim "99.9%
availability" while the actual severity of failing differs enormously (a
joke site vs. a payments flow), so investment should track journey impact
severity, not the raw percentage.

See [end-to-end vs per-component SLI measurement](end-to-end-vs-per-component-sli-measurement.md)
for the measurement trade-off this implies, and
[measuring many things by measuring only a few](measuring-many-things-by-measuring-a-few.md)
for why a well-chosen critical-path metric often implicitly validates most of
what a journey depends on.
