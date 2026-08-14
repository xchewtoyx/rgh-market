---
type: concept
title: Infrastructure Platform Layering Model
description: A three-layer model — infrastructure platform, application runtime, and applications — used to reason about which tools and concerns belong at which level of a system.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 3"
---

It helps to group the parts of a cloud system into three layers:

- **Infrastructure platform** — the dynamic, API-driven platform (IaaS) that provisions compute, storage, and networking primitives: a public or private cloud, or a virtualization platform. Infrastructure as Code requires this layer to be dynamic — provisionable and changeable on demand through an API — since that is what makes applying code to reconcile infrastructure fast enough to be worthwhile.
- **Application runtime** — services and constructs assembled from infrastructure-platform resources that provide capabilities to applications: container clusters, serverless environments, application servers, operating systems, databases. Sometimes called Platform as a Service (PaaS). See [infrastructure stacks](infrastructure-stack.md) for how you assemble infrastructure-platform resources into this layer, and [application runtime layer](application-runtime-layer.md) for how the runtime layer relates to the applications it hosts.
- **Applications** — the software and services that provide value to the organization; everything else in the model exists to enable this layer.

The boundaries between layers are not absolute — the same construct (a database, a load balancer) can sit in different layers depending on how it's provided and consumed — but the model is useful for keeping a discussion of tools and practices anchored to which layer they operate at, and for noticing when a design mixes concerns across layers unnecessarily. A related concern at the platform layer is [multicloud strategy](multicloud-strategies.md) — how an organization spreads infrastructure across more than one platform.
