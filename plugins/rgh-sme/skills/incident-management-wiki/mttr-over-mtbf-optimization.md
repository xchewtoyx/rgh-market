---
type: concept
title: MTTR-over-MTBF Optimization
description: A resilience strategy shift, enabled by cheap and fast infrastructure change, from optimizing to prevent failure (MTBF) toward optimizing to detect and recover from it quickly (MTTR).
sources:
  - title: "Infrastructure as Code"
    resource: "Infrastructure as Code, 2nd Edition (Kief Morris), ch. 21"
---

When changing a system is slow and expensive, the rational response is to
prevent failure: heavy up-front design, thorough review, and infrequent,
tightly controlled changes, all aimed at maximizing **Mean Time Between
Failure (MTBF)**. This works when the cost of a mistake is also high and slow
to fix — but it has a hidden failure mode of its own: it optimizes for a world
where changes are rare, so when a failure does happen, the organization is
poorly practiced at recovering from it, and the incident runs long.

When changing a system is cheap and fast, the more effective strategy
inverts: optimize for **Mean Time to Recover (MTTR)** instead. Accept that
failures are inevitable, invest in detecting and correcting them quickly, and
let a track record of fast, reliable recovery be the thing that produces
stability — not the absence of failure. This is not a trade-off against
MTBF; organizations that focus on deployment frequency, change lead time,
and MTTR tend to end up with strong MTBF as a side effect, because the same
practices that make recovery fast (small changes, continuous testing, loose
coupling) also make failures less likely to begin with.

The trap is assuming this means abandoning prevention — "move fast and break
things" is not the point. The point is "move fast and fix things": keep
investing in preventing errors, but stop treating prevention as the *only*
lever, and stop assuming that fast recovery must come at prevention's
expense.

This mirrors the [Safety-I vs. Safety-II](safety-i-vs-safety-ii.md) shift at
the level of infrastructure change practice: Safety-I-style prevention
constrains variability to avoid the rare bad outcome, while an MTTR focus
treats frequent, well-practiced recovery as the actual source of system
resilience. Recovery speed is only real if it's measured — see
[outage tracking metrics](outage-tracking-metrics.md) for the TTD/TTM/TTR
breakdown — and only trustworthy if it's exercised continuously rather than
assumed, which is the argument for treating recovery and disaster-recovery
processes as routine, frequently-run automation rather than a rarely-tested
annual failover exercise (see [preparedness drills](preparedness-drills.md)
and [chaos engineering experiment design](chaos-engineering-experiment-design.md)).
