---
type: concept
title: Operational Requirements as First-Class Requirements
description: >
  Naming operational needs "non-functional" invites treating them as
  optional extras, when a system that cannot be configured, upgraded,
  drained, or degraded gracefully in production is not a lesser version
  of the product — it is an unfinished one.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration, 2nd Edition (Limoncelli, Chalup, Hogan), ch. 2"
---

Most of a service's life is spent operating it, not building it, yet the
needs of the people who will operate it are conventionally bundled under
the "non-functional requirements" label — a name that itself signals they
are secondary to the "real," functional ones. Reframing them as
**operational requirements** is a deliberate rhetorical move: features
like configuration management, startup/shutdown behavior, queue draining
before maintenance, live software upgrades, backup/restore while running,
redundancy, feature toggles, [graceful
degradation](feature-complete-vs-production-ready.md), access control and
rate limits, monitoring, auditing, and debug instrumentation are essential
to the service's existence, not optional polish layered on afterward. A
system missing them does not do less of what it's supposed to do — it is
harder or impossible to run safely at all.

This is the same underlying gap that [feature-complete vs.
production-ready](feature-complete-vs-production-ready.md) names from the
delivery-pipeline side and that [non-functional
requirement](non-functional-requirement.md) names from the general
requirements-taxonomy side: conventional practice systematically elicits
and tests what a system *should* do while leaving what it must not do
(crash under load, lose data on upgrade, block on a full disk) to be
discovered in production. Naming a standing checklist of these needs and
treating it as no less real than a feature backlog — see [quality
attribute checklist vs. catalog](quality-attribute-checklist-vs-catalog.md)
for the equivalent discipline applied to quality attributes generally — is
the concrete countermeasure. Getting them built in practice follows the
same path as any requirement competing for engineering time: request them
as identified, framed around the operational problem and its business risk
rather than a prescribed implementation, so they can be prioritized
alongside — not below — user-facing work.
