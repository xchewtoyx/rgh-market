---
type: concept
title: "Pattern: Stack Data Lookup"
description: A consumer stack discovering a provider stack's resource by reading the provider stack management tool's own state data, such as a Terraform remote state file.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 17"
---

Stack data lookup (also known as remote statefile lookup, stack reference lookup, or stack resource lookup) finds a provider [stack's](infrastructure-stack.md) resources using the data structures the stack management tool itself maintains for that instance — Terraform and Pulumi remote state, or CloudFormation's stack output export/import. The provider stack explicitly declares which values it publishes for others to consume, which discourages consumers from silently depending on resources the provider never intended to expose.

The pattern is convenient because most stack tool vendors build this capability in, but it ties a system to a single stack management tool across every stack that participates in the lookup, and it can break across tool version upgrades — an upgrade that changes the provider's state structure can leave older consumers unable to read it until they upgrade too, which can force a disruptive coordinated upgrade rather than a gradual, stack-by-stack one. It's possible to extract stack data lookup values via a script and hand them to other tools, which loosens this coupling somewhat.

Compared to [resource matching](resource-matching-pattern.md), stack data lookup is more reliable within a single-tool environment but locks in that tool choice; compared to [integration registry lookup](integration-registry-lookup-pattern.md), it avoids running a separate registry service but ties consumers to the provider's specific tooling rather than a general-purpose store.
