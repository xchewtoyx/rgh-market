---
type: concept
title: L4 vs. L7 Load Balancing
description: >
  Transport-level balancers push packets cheaply but blindly; application-
  level balancers see requests and can route on content — the throughput
  versus intelligence trade at every tier.
sources:
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 9"
---

# L4 vs. L7 Load Balancing

Load balancers spread incoming traffic over a pool of instances found via
[service discovery](service-discovery.md). The layer they operate at fixes
what they can and cannot do:

- **Layer 4 (transport):** balances on IP/port at TCP/UDP level. Very high
  packet throughput and low CPU cost, but it cannot see HTTP headers,
  paths, methods, or cookies — every connection is an opaque byte stream,
  so routing decisions can't use request content, and a "healthy" backend
  is just one that accepts connections.
- **Layer 7 (application):** terminates the protocol (HTTP/gRPC/TLS) and
  balances *requests*. Enables content/path-based routing, [cookie sticky
  sessions](stateless-services-and-session-affinity.md), TLS termination,
  rate limiting, and richer health semantics — at meaningful CPU/memory
  cost per connection. (The same L4/L7 split governs [database
  proxies](database-proxies.md).)

**Software vs. hardware:** software balancers (HAProxy, NGINX, Envoy)
configure dynamically via API and fit cloud/autoscaled environments;
hardware appliances (F5) offer raw throughput but static, ticket-driven
change. The industry direction is software L7 at the edge and between
services.

Two adjacent roles often colocated with the balancer:

- **Ingress demand control:** edge proxies/WAFs enforce rate limits,
  payload caps, TLS policy, and DDoS absorption *before* traffic reaches
  internal networks — the outermost defense against
  [cascade-triggering surges](cascading-failures.md).
- **Health-based eviction:** removing failing instances from rotation is a
  [failure-detection](timeouts-and-failure-detection.md) decision, with all
  its false-positive hazards — a balancer that evicts aggressively under
  load can amplify a [chain reaction](cascading-failures.md).
