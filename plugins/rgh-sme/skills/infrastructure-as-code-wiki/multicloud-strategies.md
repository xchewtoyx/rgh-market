---
type: concept
title: Multicloud Strategies
description: Distinct terms for the ways organizations spread infrastructure across more than one platform — hybrid cloud, cloud agnostic, and polycloud — each with different motivations and trade-offs.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 3"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 8"
---

Organizations that host across more than one [infrastructure platform](infrastructure-platform-layers.md) tend to fall into one of a few patterns:

- **Hybrid cloud** — hosting a system across both private infrastructure and a public cloud, typically because legacy systems can't easily migrate (for example, mainframe-hosted services) or because requirements — such as data residency law — can't currently be met by a public vendor.
- **Cloud agnostic** — building systems so they can run on multiple public cloud platforms, usually to avoid vendor lock-in. In practice this tends to trade one lock-in for another: lock-in to whatever abstraction software promises to hide the platform differences, or a large amount of custom code to maintain that abstraction.
- **Polycloud** — running different applications or services on more than one public cloud platform, usually to exploit the differing strengths of each platform, rather than trying to make any one workload portable between them.

These are different strategies with different goals — hybrid cloud is about what you're forced to keep, cloud agnostic is about avoiding lock-in for a given workload, and polycloud is about picking the best platform per workload — so it's worth being explicit about which one a given multicloud decision is actually trying to achieve before evaluating whether it's paying off. A multicloud strategy usually also means maintaining separate [server images](server-image-as-code.md) per platform, since images aren't portable across infrastructure platforms.

Cleanly separating the code that provisions raw compute from the code that configures software on it is a concrete, lower-effort way to get most of the cloud-agnostic benefit without a full portability-abstraction investment: if the provisioning step's only job is to produce running hosts and populate an inventory with them, and every other step (installing and configuring software, deploying an application) consumes only that inventory, the configuration code is naturally portable across platforms already — it never references anything platform-specific. Swapping a local-VM provisioning step for a cloud API-driven one then only ever touches the provisioning layer, leaving the (usually much larger) configuration codebase completely unchanged. This is a narrower version of the same idea behind [separating cluster provisioning from workload deployment](separating-cluster-provisioning-from-workload-deployment.md) — provisioning and configuration change for different reasons and at different rates, so keeping them as separate stages (even without formally separate [stacks](infrastructure-stack.md)) pays off independent of any multicloud goal.
