---
type: concept
title: Service Discovery Mechanisms
description: The range of techniques applications and infrastructure use to find the current location of other services in a dynamic environment, from hardcoded addresses to a service mesh.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 10"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 7"
---

In a dynamic infrastructure environment where the location of a service can change — a rebuild, a scaling event, a failover — a service needs some responsive way to find where its dependencies currently are, since a known, static hostname (fine for static infrastructure) can't be assumed. Options, roughly from least to most dynamic:

- **Hardcoded IP addresses** — simplest, but any address change or multi-instance rollout requires rebuilding and redeploying every consumer.
- **Hostfile entries** — server configuration writes `/etc/hosts` (or equivalent) mappings; a messier workaround mainly seen where legacy DNS setups can't be changed easily.
- **DNS** — mature, well-supported, using managed entries or Dynamic DNS.
- **Resource tags** — services and their infrastructure are tagged with what they provide and their context (environment, etc.); discovery queries the platform API for matching tags. Care is needed to avoid coupling application code directly to the infrastructure platform's tagging API.
- **Configuration registry** — application instances publish their current connectivity details to a [configuration registry](configuration-registry.md) for others to look up; useful when consumers need more than just an address, such as health status.
- **Sidecar** — a companion process alongside each instance handles discovery (and often more) on its behalf; usually part of a [service mesh](service-mesh.md).
- **API gateway** — a centralized HTTP service defining routes and endpoints, providing similar capabilities to a sidecar (authentication, encryption, logging, monitoring) but centralized rather than distributed to each instance.

The right mechanism depends on how dynamic the environment is and how much infrastructure-level machinery a team wants to run: hardcoded addresses and hostfiles are essentially static-infrastructure holdovers, while a sidecar or API gateway commits to running dedicated infrastructure to handle discovery dynamically at scale.

Server configuration tools face the same discovery problem one layer down — before a service can be discovered by its consumers, the configuration tool itself first has to discover *which hosts exist to be configured*. Where a static, hand-maintained host list can't keep up with cloud/autoscaled/ephemeral infrastructure that creates and destroys hosts continuously, dynamic inventory addresses this: an executable script or plugin, invoked by the configuration tool itself, queries the platform (a cloud provider's API, resource tags, a custom internal service) at run time and returns the current set of hosts and their grouping/variables as data, so the tool's view of "what exists" is always freshly derived from the platform's own state rather than a document someone forgot to update. This is the same category of problem as application-level service discovery, just aimed at populating the configuration tool's own worklist rather than an application's runtime dependency list.
