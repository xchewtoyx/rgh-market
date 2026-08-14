---
type: concept
title: Global Load Balancing Tiers
description: >
  The frontend traffic stack at global scale: geo-DNS steers coarsely,
  anycast plus consistent-hashing L4 balancers spread packets, and L7
  proxies route requests with capacity-aware overflow between datacenters.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 19"
---

# Global Load Balancing Tiers

No single mechanism can route planet-scale traffic; production frontends
stack three tiers, each correcting the previous one's bluntness (Google's
stack as the reference):

1. **Geo-DNS.** Resolve each user's DNS query to a nearby datacenter's
   address. Coarse and slow to change: resolver location is a weak proxy for
   user location, and [DNS caching ignores TTLs](service-discovery.md), so
   it cannot react to sudden overload or failure. Treat it as a first
   approximation only.
2. **Anycast + L4 balancing.** The same VIP is BGP-announced from many
   points of presence, so the internet delivers packets to the nearest one.
   There, a software [L4 balancer](l4-vs-l7-load-balancing.md) (Maglev, on
   commodity Linux) spreads packets across L7 proxies using **consistent
   hashing** — any balancer instance maps a given connection's packets to
   the same backend *without shared connection state*, so balancer
   instances can fail or be added without breaking established connections.
3. **L7 proxies with global capacity control.** The frontend proxy tier
   (GFE) terminates TCP/TLS, parses HTTP, multiplexes HTTP/2, and forwards
   over RPC to backend clusters. A central controller (GSLB) watches
   cluster capacity worldwide and instructs proxies to **overflow traffic
   to other datacenters** when the local cluster is full — the reaction
   speed that DNS cannot provide, placed at the layer that can see
   requests.

The design pattern to reuse: put slow, coarse steering at the outermost
layer, fast precise decisions closest to capacity, and give every tier a
way to spill to an alternative — the same
[yield-preserving](yield-and-harvest.md) philosophy applied to traffic.
Within the datacenter, the [backend-selection
problem](datacenter-load-balancing.md) takes over. A [content delivery
network](content-delivery-networks.md) applies the same geolocation-routing
idea to serving cached content directly from the edge, bypassing the
origin's own tiers entirely for cache hits.
