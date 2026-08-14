---
type: concept
title: Service Mesh
description: >
  A sidecar proxy co-deployed with every service instance to handle
  interservice communication, splitting a fleet-wide control plane for
  routing/security policy from a per-instance data plane that enforces it.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th ed. (Bass, Clements, Kazman), ch. 9"
---

# Service Mesh

A service mesh moves cross-cutting communication concerns — service
discovery, retries and timeouts, mutual TLS, load balancing, and
observability — out of each service's business logic and into a **sidecar**
proxy co-deployed alongside every instance (typically in the same pod).
Every outbound and inbound call passes through the local sidecar instead of
the application talking to peers directly.

This is a concrete, widely-deployed instance of [control plane versus data
plane](control-plane-vs-data-plane.md) separation: the sidecars scattered
across every instance *are* the data plane, forwarding and enforcing
traffic rules on the request path; a separate control plane (e.g. Istio's
istiod) computes routing, security, and traffic-splitting policy centrally
and pushes it out to every sidecar. The same blast-radius asymmetry
applies here as anywhere else this split shows up: a data-plane sidecar bug
affects the instance it rides with, but a bad control-plane policy push can
reconfigure every sidecar in the mesh at once.

Benefits: cross-cutting networking code can be built and operated by a
specialist platform team once, instead of every service team reimplementing
retry/TLS/discovery logic; co-locating the proxy with its service keeps the
extra hop cheap (loopback, not a network call); centrally pushed policy
makes fleet-wide changes — a canary rollout, a traffic-splitting
experiment, a security policy change — a control-plane update rather than a
per-service redeploy. Tradeoffs: every call now pays a sidecar hop, adding
latency and per-instance resource overhead; a sidecar typically bundles
functionality beyond what any single service actually needs; and the mesh
introduces exactly the fleet-wide control-plane risk described above.
