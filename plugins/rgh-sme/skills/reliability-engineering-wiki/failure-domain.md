---
type: concept
title: Failure Domain
description: >
  The bounded scope beyond which a given failure has no impact; deliberately sizing and aligning failure domains is what keeps a local failure local instead of letting it cascade.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 6"
---

A **failure domain** is the boundary beyond which a failure has no effect —
a car breaking down closes a lane, not the whole highway. A domain can be
**prescriptive** (an explicit design goal, e.g. deliberately placing two
server replicas on separate racks and power circuits so a rack failure
can't take both down) or **descriptive** (worked out after the fact, e.g.
discovering what a machine's failure domain actually became after it was
moved to cover a different failure). Every domain boundary is scoped to an
assumed disaster size — off-site backups kept a safe distance away accept
that a disaster spanning that distance is either an acceptable residual
risk or catastrophic enough that data availability stops being the primary
concern anyway.

Rack and datacenter are the two most common failure-domain granularities in
practice, and each has two opposite deliberate placement strategies:

- **Diversity** — spreading a service's replicas across multiple domains
  (racks, datacenters) so one domain's failure can't take the whole service
  down. This is the mechanism behind [independent failover reliability
  composition](independent-failover-reliability-composition.md): two
  domains are only simultaneously down if *both* fail independently, which
  is why a system with a genuinely independent failover path can tolerate
  each individual domain being far less reliable than the composite target.
- **Locality** — deliberately keeping a component *self-contained* within
  one domain to exploit that domain's abundant internal bandwidth or
  simplicity (e.g. a rack's top-of-rack switch gives any two machines in
  the rack full simultaneous bandwidth, far more than the shared,
  comparatively scarce inter-rack uplink). Locality trades resilience for
  performance or cost, so it's the right choice only for components whose
  loss is genuinely tolerable or covered by redundancy at a coarser
  granularity.

**Alignment is the design hazard.** A failure domain is only as clean as
its least-aligned shared dependency: a datacenter can have power, cooling,
and network domains that are each individually well-partitioned yet still
overlap unexpectedly — for example, a power bus shared across 6 racks while
network connectivity spans 8-rack groups drawing from the first rack of
each group, so a routine 6-rack power maintenance can cascade into a
13-rack network outage. Worse, two domains can share a single hidden joint
dependency (e.g. the building's only two external network uplinks happen
to sit inside two of ten otherwise-independent domains), silently
collapsing what looked like ten-way redundancy into two points of failure.
Auditing failure-domain alignment — do power, cooling, network, and
software/cluster-manager boundaries actually coincide, and is there a
shared dependency underneath all of them — is what keeps
[dependency reliability composition](dependency-reliability-composition.md)'s
independence assumption honest instead of merely assumed. Because rare
joint-dependency failures like this typically only surface at scale, [game
day exercises](game-day-exercises.md) that actually take a domain down are
the reliable way to find a misalignment before it finds you.

A common concrete target for critical, user-facing services is **N+2
datacenter diversity**: enough independent datacenters that one can be
taken down deliberately for planned maintenance while a second, unrelated
datacenter also fails unexpectedly, without user-visible impact — the
[N+M redundancy](n-plus-m-redundancy.md) model applied at datacenter
granularity.
