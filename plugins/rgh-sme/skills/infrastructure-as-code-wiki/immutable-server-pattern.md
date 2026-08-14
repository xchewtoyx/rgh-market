---
type: concept
title: "Pattern: Immutable Server"
description: A server instance whose running configuration is never changed in place; every change is delivered by building a new instance from updated source and replacing the old one.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 12"
---

An immutable server never has configuration applied to it after it's created. Any change — a patch, an upgrade, a fix — is delivered by building a fresh instance from updated code and [images](server-image-as-code.md) and swapping it in for the old one, rather than reapplying configuration in place as with [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md). This trades the speed of in-place updates for a stronger guarantee: you can test the new instance before it takes traffic, and swap it back out if something's wrong, rather than debugging a partially-updated live server.

Immutability requires a solid automated process for building and updating [server images](server-image-as-code.md), favoring [baking over frying](baking-vs-frying-server-configuration.md), and it requires the wider system to support swapping instances without disrupting service — see [zero downtime infrastructure changes](blue-green-infrastructure-change.md). Despite the name, immutable servers do still change underneath — logs, memory, running processes — the immutability is about the managed configuration, not literal server state; the term is a useful metaphor rather than a literal claim.

Immutable servers can still drift if people log in and change them manually rather than going through the replace-the-instance process, so teams relying on this pattern should restrict or gate direct access (a "break glass" procedure for genuine emergencies) rather than assume immutability alone prevents [configuration drift](configuration-drift.md). Immutable servers are a specific instance of the broader idea of [immutable, disposable infrastructure](reproducibility-principle.md) applied at the server level, and pair naturally with [blue-green infrastructure changes](blue-green-infrastructure-change.md) as the mechanism for swapping instances in production.
