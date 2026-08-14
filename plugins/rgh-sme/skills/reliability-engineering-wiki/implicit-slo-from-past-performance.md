---
type: concept
title: Implicit SLOs from Past Performance
description: >
  Users come to expect continuity of whatever reliability level they've
  already experienced, whether or not it was ever formally promised, and will
  depend on any observable behavior of a system regardless of what its
  contract says.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 2"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann, Stocker, Lübke, Zdun, Pautasso), ch. 3"
---

Even without a formal SLA or stated SLO, users form an *implicit agreement*
based on the service level they've actually experienced. A reliability
target should acknowledge this history, even though the implicit agreement
isn't binding — quietly regressing from a historically-better level will read
to users as a real reliability failure regardless of what was ever formally
promised.

**Hyrum's Law** (Hyrum Wright, Google): "With a sufficient number of users of
an API, it does not matter what you promise in the contract: all observable
behaviors of your system will be depended on by somebody." Practical
implication for SLO work: expect measurement needs to change as you learn
about real usage, because users will build dependencies on things the team
never intended to guarantee.

This is part of why [SLOs should not be hidden](slo-discoverability.md) — if
users can't see the stated target, they can't distinguish "the system
behaves this way by design" from "the system happens to behave this way
today," and will silently anchor on the latter.

Consistently overperforming a published SLO compounds this effect further —
see [too reliable is a cost](too-reliable-is-a-cost.md).

Quality objectives left **implicit or vague** — no published
[SLA](sla-vs-slo.md), no stated [SLO](service-level-objective.md) — are
common when documentation and operations overhead outweigh the business
benefit, especially for free or low-criticality offerings. That choice is
reasonable, but clients may still form expectations from actual experience
that do not match what the provider can sustain; making targets explicit
when clients pay for or depend on specific QoS is how those expectations
get aligned before integration rather than discovered in production.
