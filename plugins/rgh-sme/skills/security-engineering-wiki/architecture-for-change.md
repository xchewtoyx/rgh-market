---
type: concept
title: Architecture for Change
description: >
  Current dependencies, frequent rebuilds and releases, immutable
  containers, and microservice choke points make patching routine instead
  of exceptional.
sources:
  - title: Building Secure and Reliable Systems
    resource: "Building Secure and Reliable Systems (Adkins et al.), ch. 7"
---

# Architecture for Change

Structural choices determine whether a security patch is an emergency
project or a routine rollout.

- **Keep dependencies current; rebuild frequently.** Up-to-date
  references to fast-moving projects (OpenSSL, the kernel) mean a
  critical patch applies directly instead of arriving with a backlog of
  merges. Patches reach production only when you rebuild — frequent
  rebuild/redeploy keeps the emergency path warm.
- **Release frequently with automated testing.** Many small releases →
  each contains less, rolls back easier, and diagnoses faster; automated
  validation pushes good releases and blocks bad ones, giving confidence
  when a critical fix must move quickly.
- **Containers.** Decouple app dependencies from the host OS (patch a
  kernel vulnerability without touching app containers). Immutability
  means you never patch live containers — you patch images in the
  registry and redeploy through the same monitored, canaried pipeline as
  code, so patching inherits your release cadence. Content-addressability
  tells you exactly what's running: find vulnerable versions in the
  registry instead of scanning production. Enforce freshness both ways:
  monitor container age in production, and allow only recently built
  images to deploy (blocking redeployment of old unpatched ones).
- **Microservices.** Independent scaling, load balancing, and rollout
  per service; naturally suited to
  [zero-trust](zero-trust-networking.md) segmentation (heterogeneous
  trust inside the perimeter, down to per-service segmentation); and
  security tooling converges — common crypto libraries, monitoring, and
  critical security services maintained as separate microservices by
  small responsible teams. The Google Front End shows the choke-point
  payoff: services aren't directly internet-exposed; GFE terminates
  TLS, provides [DDoS countermeasures](dos-defense-in-depth.md), load
  balances globally, and absorbs protocol/security evolution — when an
  SSL renegotiation vulnerability appeared, one control at GFE protected
  every service behind it; integrating ALTS into the shared RPC library
  rolled encryption out fleet-wide without burdening product teams
  ([secure-by-construction frameworks](secure-by-construction-frameworks.md)).
  The generalization is separating the *data plane* from the *control
  plane* (service mesh): request processing configured by a manageable,
  scalable policy surface. Restraint required: the security advantages
  hold only while services stay simple.

These are the same structural properties that make
[recovery fast](decouple-rollout-speed-from-policy.md) — architecture for
change is preparation for both proactive improvement and emergency
mitigation.
