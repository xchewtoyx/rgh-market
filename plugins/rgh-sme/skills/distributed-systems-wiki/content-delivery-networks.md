---
type: concept
title: Content Delivery Networks
description: >
  A globally distributed edge-caching layer that serves content from
  wherever demand is, populated on first request rather than pre-replicated
  everywhere, colocated inside ISPs to cut transit cost.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 5"
---

# Content Delivery Networks

A CDN is a [caching tier](caching-tiers.md) turned into infrastructure: many
geographically spread cache nodes, each serving requests from whichever
users are nearest via the same geolocation-based routing a [global load
balancer](global-load-balancing.md) uses to pick a region. The distinguishing
design choice is **demand-driven population, not blanket replication** — a
CDN doesn't push every asset to every edge node up front; it tracks regional
request trends and populates a region's nodes when demand actually appears
there (and evicts accordingly), the same [cache-after-persist, populate-on-
miss](caching-tiers.md) pattern applied at planetary scale.

**Integration mechanic.** Content still has a canonical origin URL; enabling
the CDN means serving *CDN URLs that encode the origin URL* instead. The
first request for a given CDN URL is a cache miss the CDN resolves by
transparently fetching from the encoded origin and caching the result;
every subsequent request in that region is served from the edge. There is no
separate "upload to the CDN" step — the encoding does it implicitly on first
access. Because this is just URL substitution, it should sit behind a
runtime flag: falling back to origin URLs is the fastest recovery path
during a CDN outage or a misconfiguration on the operator's own side, and the
same switch lets pre-release or secret content stay off the CDN during
testing, or lets an operator change CDN vendors without a code change.

**Why it pays for itself.** CDN operators run far larger aggregate internet
bandwidth than a single site could justify buying, and commonly colocate
cache nodes directly inside ISP datacenters — traffic served from inside an
ISP's own network avoids the inter-ISP [transit
cost](cloud-regions-and-availability-zones.md) both the CDN and the ISP
would otherwise pay, which is why ISPs often host CDN nodes for free or at a
steep discount.

**Build versus buy.** Third-party CDNs are cost-effective for most
operators — even a young, small company can see a large uptime improvement
just from offloading static content to one. At very large scale, once an
operator already runs its own global [region and datacenter
footprint](cloud-regions-and-availability-zones.md), building a private CDN
on top of that existing footprint can be cheaper and more reliable than
paying a third party — the same build-vs-buy calculus that applies to any
other piece of shared infrastructure, just applied to the caching layer.
