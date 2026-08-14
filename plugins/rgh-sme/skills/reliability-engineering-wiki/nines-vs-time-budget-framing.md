---
type: concept
title: Nines vs Time-Budget Framing
description: >
  Fixating on "the number of nines" as the only vocabulary for a target is
  limiting; deriving a percentage from an acceptable time budget is often a
  more useful starting point than picking a percentage first.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 4"
---

The nines vocabulary (99%, 99.9%, 99.99%, 99.999%) is limiting: it implies
only a handful of legitimate target values exist, and it can be arbitrarily
far from what users actually need. Non-nines targets (99.97%, 98.62%, 87%)
are completely legitimate SLO targets.

Because the jump between adjacent nines is wildly non-linear in time terms
(e.g. 99.9% ≈ 43m50s/month of allowed downtime vs. 99.99% ≈ 4m23s/month —
see [cost of nines](cost-of-nines.md) and [availability table](availability-table.md)),
it's often more productive to work in the other direction: decide on an
acceptable *time* budget first (e.g. "about two hours of unreliability a
month is fine for this service") and reverse-derive the percentage from that,
rather than picking a percentage and discovering only later what it costs in
practice.

Percentile-based latency framing carries the same lesson — see
[layered percentile SLO thresholds](layered-percentile-slo-thresholds.md).
As Charity Majors is quoted: "Nines don't matter if users aren't happy" —
the target vocabulary is a tool for the conversation, not the goal itself.
