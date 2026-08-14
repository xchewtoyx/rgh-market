---
type: concept
title: Web API Characteristics
description: >
  Network-exposed interfaces whose implementations stay remote, forcing immediate
  contract changes on all clients unlike locally versioned libraries.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 1"
---

An **API** defines how computer systems interact — in libraries, internal modules,
or over the network. **Web APIs** are built for remote use by many independent
clients. There is no local copy: when the provider changes behavior, algorithms, or
availability, **every consumer is affected immediately** — unlike a library where
each user chooses when to upgrade.

That loss of consumer control is the provider's gain: complete control over
implementation, IP protection (algorithms stay server-side), and hiding heavy
compute (many ML APIs). APIs also enable **composition** — reusable building blocks
assembled into larger systems that become blocks for later projects — which
motivates predictable, composable contract design.

Automation needs machine-oriented interfaces: GUIs conflate layout with data, and
"cosmetic" UI changes are breaking changes to scripts. APIs evolve in
[backward-compatible](backward-compatibility-policy.md) ways so clients are not
retaught on every release.
