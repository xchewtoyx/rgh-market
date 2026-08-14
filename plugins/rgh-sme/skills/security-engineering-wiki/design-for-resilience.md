---
type: concept
title: Design for Resilience
description: >
  Resilience is a system's ability to delay or withstand breakage from
  attack or overload — distinct from recovery, which fixes systems after
  they break — built from layered, prioritized, compartmentalized,
  automated, and validated defenses.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Design for Resilience

Resilience is the ability to hold out against major malfunction or
disruption — attacks and unusual stress alike — ideally continuing to run
through an incident, perhaps degraded, and recovering automatically.
Distinguish it from [recovery](design-for-recovery.md): recovery fixes
systems *after* they break; resilience *delays or withstands* breakage.
Systems designed for both need minimal human intervention. Plan early for
staying at least partially up under multiple simultaneous incidents.

Characteristics of a resilient design, each a concept of its own:

- **Independently resilient layers** —
  [defense in depth](defense-in-depth.md), so each layer covers the likely
  failures of the one before.
- **Prioritized features with known costs** — decide in advance what must
  survive any load and what can be throttled or dropped:
  [graceful degradation](graceful-degradation.md).
- **Compartmentalization along clear boundaries** —
  [blast radius control](compartmentalization.md), with
  [role](role-separation.md), [location](location-separation.md), and
  time ([rotation](credential-rotation.md)) separation.
- **Redundancy across [failure domains](failure-domains.md)** — and for
  global failures, compartments with *different* reliability and security
  properties ([component reliability tiers](component-reliability-tiers.md)).
- **Automated response** where safe, to beat human reaction time — with
  humans kept in the loop for judgment calls.
- **[Continuous validation](continuous-validation.md)** — exercising the
  resilience properties so they still work when needed.

Cost ordering for a smaller organization: failure domains and blast-radius
controls first (relatively static, lasting benefit — they make it
structurally harder to build coupled, fragile systems later);
high-availability instances next (cheap to try, cheap to abandon); then
load-shedding/throttling automation and DoS defenses
([DoS mitigation](dos-defense-in-depth.md)); low-dependency solutions
last — expensive, and only worth it if kept genuinely low-dependency.

The payoff frame: resilience buys *time* — degraded-but-alive
functionality extends the window responders have to organize, contain, and
recover, and blast-radius controls limit what an attacker who does get in
can reach. Because the benefit manifests as an absence of problems, budget
for it deliberately, and protect the validation spend that locks in the
value of everything else.
