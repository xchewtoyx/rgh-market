---
type: concept
title: Cost/Efficiency as an SLI
description: >
  Cost per unit of business value is a commonly neglected SLI type worth
  tracking alongside latency, availability, and throughput.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
---

Cost/efficiency is best expressed per unit of business value delivered —
cost per page view, per subscription, per transaction — rather than as a raw
infrastructure spend figure, so it stays meaningful as traffic scales.

It's frequently left out of SLI sets entirely, even though it's a real
constraint on how far reliability investment can reasonably go: see
[cost of nines](cost-of-nines.md) for why reliability spend accelerates
non-linearly as targets tighten, which makes an explicit cost/efficiency
signal useful for grounding target-setting discussions in more than just
technical achievability.
