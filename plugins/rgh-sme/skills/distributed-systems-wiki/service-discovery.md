---
type: concept
title: Service Discovery
description: >
  How callers find current, healthy instances of a service — from static
  config and DNS (with its caching traps) to dynamic registries and floating
  VIPs.
sources:
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 9"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Service Discovery

"Which addresses currently serve this service?" is the same moving-target
problem as [routing to partitions](request-routing.md), one level up.
Mechanisms evolve with scale: static config files → DNS → load balancers →
dynamic registries and meshes. Working knowledge of each rung:

- **DNS.** Round-robin A/AAAA records give crude discovery plus load
  spreading. The trap is **caching beyond TTL**: JVMs, OS resolvers, and
  intermediate recursive resolvers routinely hold records far longer than
  the TTL asks, so after a failure or IP change, clients keep sending
  traffic to dead addresses. DNS-based failover is therefore *slow* by
  construction — fine for coarse, rarely-changing routing (and for
  geographically informed global routing, where dynamic resolvers answer
  based on client proximity and datacenter health), wrong for
  instance-level liveness.
- **Migratory virtual IPs.** A floating VIP bound to the active host (VRRP,
  keepalived, or an orchestrated cloud IP move) migrates to a standby on
  failure — clients keep one stable address while the machine behind it
  changes. Instant failover for leader/standby pairs; beware the moment of
  migration, when a service making non-[idempotent](idempotency.md)
  requests can see one connection land on each host.
- **Dynamic registries.** Instances register on startup and deregister (or
  are health-checked out) on shutdown — Consul, etcd, Kubernetes
  DNS/kube-proxy — giving clients or [load
  balancers](l4-vs-l7-load-balancing.md) a near-real-time routing table.
  Registries built on [coordination services](coordination-services.md)
  inherit consensus's consistency and its availability behavior; the
  discovery layer is infrastructure whose own failure modes
  ([stale views, partitions](membership-services.md)) must be designed
  for.

The recurring judgment call: how *fresh* must routing knowledge be? Each
step up the ladder buys faster convergence on the true state at the price
of more moving parts.

## Scheduler indirection on managed compute

Hardcoding a hostname — even as a startup config parameter — breaks
[ephemeral compute](ephemeral-compute-instances.md): the scheduler moves
work. Callers refer to a **durable service identifier** the control plane
resolves to wherever instances currently run. Clients typically resolve that
address and open connections at **startup** (off the request critical path),
refreshing in the background — the same indirection pattern as dynamic
registries, but driven by the orchestrator rather than self-registration
alone.

Because backends may be taken down mid-request during rescheduling, callers
must [retry](retry-design.md); mutating operations need
[idempotency](idempotency.md). A subtler case: the scheduler loses contact
with a machine, presumes it dead, and starts a replacement — then the
original returns. Two instances briefly believe they are the same replica;
the address-resolution layer disambiguates (whichever is not registered
terminates), but in-flight work on both sides can duplicate effects until
convergence — another reason idempotency keys belong on mutating RPCs.
