---
type: concept
title: Cloud Regions and Availability Zones
description: >
  A region groups nearby datacenters for latency and data-residency reasons;
  its availability zones are engineered so a failure in one has negligible
  chance of also taking down another.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 17"
---

# Cloud Regions and Availability Zones

A **region** is a logical and physical grouping of geographically nearby
datacenters. Choosing which region(s) to run in is an explicit architectural
decision, driven by two separate concerns that don't always point the same
way: proximity to users (lower request latency the closer a region is to
where traffic originates) and **data residency** — regulation such as GDPR
that restricts moving certain data across borders, which can force a region
choice regardless of where users actually are.

## Routing to where the user's data actually lives

Picking the *nearest* region gets a user to a datacenter quickly, but
nearest-DC selection happens at the DNS/network level, before anyone knows
*which* user is asking — so it can't guarantee that DC actually holds that
user's data, especially once a user's data was pinned to one region at
signup and the user later travels, or a region gets decommissioned.
Two complementary fixes: replicate each user's data across more than one
region so a nearest-DC guess is more often right by construction, and — the
mechanism that actually closes the gap — have the frontend that lands the
connection query a lookup service for which region holds this specific
user's data, then forward the application-layer request there. This keeps
the outer routing layer generic (any frontend can receive any user) while
pushing the data-aware decision to a second hop, the same
[request-routing](request-routing.md) shape used for
[partition placement](request-routing.md) generalized to whole regions as
the unit being routed to.

## Private inter-region backbone

Once an organization runs enough regions, it's common to link them with an
owned or leased private WAN rather than routing inter-region traffic over
the public internet — avoiding **transit ISPs** (third parties that carry
traffic between networks you're not directly peered with, at a latency and
reliability cost) and giving the operator direct control over inter-region
paths. This isn't all-or-nothing: an operator can deliberately split traffic
by sensitivity, sending small, latency-critical request/response traffic
over the fast private backbone while routing bulky, latency-tolerant payloads
(large assets fetched asynchronously) over the cheap public path — trading
the backbone's operating cost against per-request latency, differentiated by
traffic class rather than applied uniformly. A **point of presence (POP)** —
a small facility with little or no compute, existing purely to peer directly
with local ISPs a main region can't reach efficiently — extends this control
to places too small to justify a full region; a POP with a modest amount of
compute added (enough to terminate connections and proxy onward, or cache
hot content) is sometimes called a satellite.

Within a region, datacenters are grouped into **availability zones**, each
with independent power and network connectivity, engineered so that a
failure knocking out one zone has a vanishingly small chance of also taking
out another zone in the same region. This is the same blast-radius logic as
[control plane vs. data plane isolation](control-plane-vs-data-plane.md)
applied at the facility level: spreading redundant instances across zones
buys protection against a shared-infrastructure failure (power, cooling, a
single network fabric) that spreading them across racks in one facility
doesn't. Placing standbys in a different zone from the primary is the
zone-level instance of the same [redundant spare](redundant-spare-tiers.md)
tradeoff — the more zones (or regions) a system spans, the more independent
its failure domains, and the more it also has to pay in cross-zone/
cross-region latency and coordination cost to keep those spread-out
instances consistent (see [coordination
avoidance](coordination-avoidance.md) for how systems that need multi-region
write availability sidestep synchronous cross-region coordination
entirely).

**The isolation promise is only as good as what actually stays independent
per zone.** Despite this physical-infrastructure independence, a real
pattern in major cloud outages is a "regional" failure that isn't caused by
any zone's infrastructure failing at all — it's a bad code or configuration
change rolled out to every zone in the region near-simultaneously by the
provider's own [control plane](control-plane-vs-data-plane.md). Zone
isolation defends against independent physical faults; it does nothing
against a single control-plane action correlated across every zone it
touches — the same fleet-wide blast-radius risk control planes pose in
general, just at the scale of an entire region instead of one operator's own
fleet.
