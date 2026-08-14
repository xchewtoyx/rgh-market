---
type: concept
title: Cross-Specialist Communication Schedule
description: A schedule that specifies who must consult whom, and by when, to resolve issues at the boundaries between specialties, as a companion to a process checklist.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 3"
---

For [complicated operational work](problem-complexity-taxonomy.md) that spans multiple specialties or system components — where each specialist's individual task is well understood, but issues emerge at the boundaries between them — a process checklist alone is not enough. A second, complementary document is needed: a schedule of who must talk to whom, and by when, to resolve issues that no single specialist's checklist could anticipate.

## What It Specifies

- **Who talks to whom**: For each class of boundary issue (e.g. a change to a shared interface, a resource both components depend on), name the specific roles or owners on each side who must be looped in — not a general "notify the team" instruction.
- **By when**: Attach an enforced resolution window to each required consultation (e.g. a fixed number of days), so a raised issue cannot silently stall without anyone noticing it never got resolved.
- **Decentralized resolution, not centralized approval**: The schedule's job is to force the right experts into a room together, not to route the decision up to a central authority — the specialists closest to each side of the boundary are best placed to resolve the conflict once they're actually talking. This is the same [decentralized authority](decentralized-authority-for-complex-operations.md) pattern applied specifically to cross-boundary technical decisions.

## Automating Detection of Boundary Issues

Where the components or specialties involved have machine-readable models (e.g. infrastructure-as-code definitions, API schemas, architecture diagrams), tooling can automatically detect a class of boundary conflict — such as two components independently claiming the same resource, or an interface change that breaks a downstream consumer — and automatically generate the communication task that routes it to the right owners, rather than relying on a human noticing the conflict first. This turns a class of complicated-problem coordination failure into something closer to a simple, checkable step.

For what happens when a boundary change is made without going through this consultation process, see [Unauthorized Substitution Change Control](unauthorized-substitution-change-control.md).
