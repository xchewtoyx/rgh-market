---
type: concept
title: Service Mesh
description: A decentralized network of per-instance sidecar processes that dynamically manages connectivity, security, and observability for a distributed system, moving these concerns out of the infrastructure layer and into the application runtime layer.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 3, ch. 14"
---

A service mesh dynamically manages connectivity between the parts of a distributed system, typically by giving every application instance a *sidecar* process that handles communication on its behalf. This moves networking capability from the [infrastructure platform layer up into the application runtime layer](infrastructure-platform-layers.md).

A mesh commonly provides: dynamic routing to the current healthy instance of a service (which enables progressive deployment strategies such as blue-green and canary — see [zero downtime infrastructure changes](blue-green-infrastructure-change.md)); availability controls like circuit breakers and rate limiting; encryption and certificate management; peer authentication rules governing which services may talk to which; and observability, recording connections and events so requests can be traced through a complex distributed system. Examples include HashiCorp Consul, Envoy, Istio, and Linkerd; sidecars are also one of several [service discovery mechanisms](service-discovery-mechanisms.md) infrastructure can rely on.

A mesh pairs naturally with an [application cluster](application-cluster-as-code.md), since the same scheduler that deploys and configures application instances can deploy and configure their sidecars alongside them — but it doesn't remove complexity, only relocates it from application code into infrastructure, which the organization needs to be ready to operate and troubleshoot. Keeping clear boundaries between what's managed at the infrastructure-networking level and what's managed by the mesh matters: without that discipline, concerns duplicate and intermingle across the two layers, making the system harder to understand, change, and debug.
