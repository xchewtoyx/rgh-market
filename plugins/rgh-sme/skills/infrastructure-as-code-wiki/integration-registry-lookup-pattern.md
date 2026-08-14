---
type: concept
title: "Pattern: Integration Registry Lookup"
description: A consumer stack and a provider stack both reading and writing values in a shared configuration registry, decoupling stack integration from any specific stack management tool.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 17"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 7"
---

Integration registry lookup has both sides of a [cross-stack dependency](resource-matching-pattern.md) read and write through a shared [configuration registry](configuration-registry.md) at a known path, rather than the consumer reading the provider's own tool-specific state (as in [stack data lookup](stack-data-lookup-pattern.md)) or matching against naming conventions (as in [resource matching](resource-matching-pattern.md)). The provider explicitly publishes values to the registry; the consumer explicitly reads them from it.

This decouples the stack tools used on either side of the dependency — different teams can use different tooling as long as they agree on the registry and its naming conventions — and it lets each side of the dependency upgrade its tooling independently, avoiding the coordinated-upgrade problem stack data lookup can create. The registry itself becomes a critical service, though: if it's unavailable, dependent stacks may not be provisionable or recoverable, which is a real concern to weigh for anything on a disaster-recovery critical path.

This pattern is especially useful for larger, multi-team, multi-tool organizations, or where a [configuration registry](configuration-registry.md) is already in use for other purposes such as the [stack parameter registry pattern](stack-parameter-registry-pattern.md) — reusing that same registry avoids introducing a second one. A clear naming/hierarchy convention (often organized by service, environment, and region) is essential once multiple teams write into a shared registry namespace.

A [dynamic inventory](service-discovery-mechanisms.md) script backed by an application's own metadata API is a real-world variant of this pattern applied to host discovery specifically: rather than the configuration tool talking to a cloud provider's API directly, it calls back to a private, purpose-built registry that already holds per-host metadata for another reason (in one documented case, a content-management system's own database of server records, populated by the provisioning process itself), and passes the returned data straight through as the tool's inventory. This couples the configuration tool's view of "what to configure" to the same registry other automation (DNS updates, deployment metadata) already reads and writes, at the cost of centralizing real operational power in that registry and its API — which the source explicitly flags as demanding careful hardening (encrypted transport, a properly authenticated and audited API) proportional to how much automation now depends on it.
