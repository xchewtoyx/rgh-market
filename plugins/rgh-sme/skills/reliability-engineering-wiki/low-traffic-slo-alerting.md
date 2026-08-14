---
type: concept
title: Low-Traffic SLO Alerting
description: >
  Low event volume makes single failures look like enormous burn rates,
  requiring specific mitigations rather than tuning the alert threshold
  alone.
sources:
  - title: The Site Reliability Workbook
    resource: "The Site Reliability Workbook (Beyer, Murphy, Rensin, Kawahara, Thorne), ch. 5"
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 9"
---

At low request volume, a single failure can look like a huge
[burn rate](burn-rate.md) purely from statistics, not from any real
reliability problem — e.g. 1 failure out of 10 requests in an hour is a
1000x burn on a 99.9% SLO. A genuinely healthy 99.99%-reliable service will
still organically see occasional failures; at low enough traffic, a
naively-sized measurement window can trip the SLO alarm on a schedule that
has nothing to do with actual health.

Mitigations:

- Generate artificial or synthetic traffic to increase effective sample
  density (caveat: synthetic traffic isn't always representative of real
  customer traffic and can mask real customer-specific failures).
- Combine multiple low-traffic services into one alerting group (risk:
  individual 100% failures on one service may get masked by the aggregate).
- Modify the service or client to reduce the true impact of an individual
  failure (retry with backoff and jitter, fallback, queue-for-later).
- Simply lower the SLO target or widen the measurement window.

This is the alerting-side manifestation of the same underlying issue covered
in [metric attributes for SLO targets](metric-attributes-for-slo-targets.md)
(the "quantity" attribute) — low event volume constrains both what target is
achievable and what alerting can reliably fire on.
