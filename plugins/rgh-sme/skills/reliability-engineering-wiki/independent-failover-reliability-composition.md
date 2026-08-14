---
type: concept
title: Independent Failover Reliability Composition
description: >
  Adding one genuinely independent failover path lets each underlying
  component be orders of magnitude less reliable than the composite target,
  because independent failure probabilities multiply down.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 9"
---

If a frontend requires four-nines (99.99%) reliability and can automatically
fail over from one data center to a second, independent one on failure, the
*combined* system only fails if both independent data centers fail
simultaneously. Because independent-failure probabilities multiply,
`P(both fail) = P(fail)²` — so to keep the combined double-failure
probability under 0.01% (0.0001), each individual data center only needs to
be ≥99% reliable (`0.01² = 0.0001`).

This is the inverse of [dependency reliability composition](dependency-reliability-composition.md):
there, stacking components on a critical path multiplies reliability *down*;
here, adding a genuinely independent alternative path multiplies failure
probability *down*, letting each underlying component be two orders of
magnitude less reliable than the composite target.

**Practical caveat**: this is a different strategy from simply retrying the
same target twice. Retrying only helps for transient, load-independent
failures — during a real outage or overload, retrying the same target can
actively worsen things (adding load to an already-struggling system), whereas
failing over to a genuinely independent failure domain is far more likely to
actually succeed. In extreme availability systems, this alternative path is
often architected using a [low-dependency design](low-dependency-design.md)
to keep its own failure probability highly predictable. The entire argument
depends on true independence — see the shared-fate caveat in
[dependency reliability composition](dependency-reliability-composition.md).
