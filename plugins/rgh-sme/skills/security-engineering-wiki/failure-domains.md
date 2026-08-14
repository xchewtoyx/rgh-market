---
type: concept
title: Failure Domains
description: >
  Partitioning a system into equivalent, completely independent copies
  provides functional and data isolation, limiting how far a bad change,
  bug, or attack can propagate.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 8"
---

# Failure Domains

A failure domain is a [blast-radius](compartmentalization.md) control that
achieves *functional* isolation: the system is partitioned into multiple
equivalent, completely independent copies. Each partition looks like the
whole system to clients and can take over during an outage (at a fraction
of capacity). Unlike role/location/time separation, failure domains
require ongoing operational effort to keep isolated — in exchange they
protect against a single event taking everything down (though extreme
events can still hit all domains at once).

**Data isolation matters as much as functional isolation** — the security
half of the design:

- **Gate what data enters a domain.** Accept new data only after
  validation checks for typical, safe changes; escalate exceptions for
  justification, with [breakglass](breakglass.md) as the exception path.
  This blocks both attacker moves (a "permit all" clause slipped into an
  ACL) and bugs (ACL-generating software emitting an empty ACL that
  denies everyone). Rate-limit global changes (per-application quotas;
  prohibit actions touching many applications at once or changing
  capacity too fast).
- **Keep a last-known-good config on disk** so losing the configuration
  API doesn't take the system down, and retain recent old data in case
  the newest is corrupted — [defense in depth](defense-in-depth.md) for
  configuration.

Even *two* domains pay off: A/B regression capability with one domain as
canary (policy: never update both at once); geographic separation against
natural disasters; different software versions so one bug can't break all
servers or corrupt all data. During incident response, isolation delays
propagation — buying detection time — and lets you push multiple candidate
fixes to distinct domains in parallel instead of rushing one global
"fix" that makes things worse.

Costs: consistent per-domain configuration keyed by domain identifier,
protection against simultaneous corruption of all configs, hiding the
partitioning from clients (to prevent coupling to one domain), and
potentially partitioning all dependencies — one shared dependency can
propagate to every domain. And a domain still dies if one of *its*
critical components dies; mitigating total failure of all domains takes
alternative components with different reliability properties
([component reliability tiers](component-reliability-tiers.md)).
