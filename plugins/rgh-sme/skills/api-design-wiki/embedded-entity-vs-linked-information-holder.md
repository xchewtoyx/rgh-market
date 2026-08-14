---
type: concept
title: Embedded Entity vs Linked Information Holder
description: >
  Two ways to expose related data in a message — inline nested representation
  versus a link to a separate information-holder endpoint — trading call count,
  size, privacy, and evolution cost.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 7"
---

References between elements (order → customer, order → product) can be modeled as:

**Embedded entity** — nest the target [parameter tree](parameter-tree.md) inside
the source representation, recursively until closure or a cycle stops traversal.
One response, fewer round trips, self-contained snapshot — but larger messages,
higher risk of leaking restricted fields, harder to remove fields later without
breaking clients, and wasted bandwidth when embedded parts change at different
velocities.

**Linked information holder** — place [link elements](link-element.md) pointing
at an [information holder resource](information-holder-resource.md); client
fetches on demand. Smaller messages, independent caching, finer access control,
modular endpoints — but more requests, link breakage when targets move, and
implicit promise that links remain followable.

Drivers:

- Homogeneous single consumer → embed aggressively (Backends for Frontends).
- Diverse public clients → link selectively; embed only what the UI needs
  immediately.
- [Operational data holder](operational-data-holder.md) → [master data holder](master-data-holder.md)
  references often link; same-type references may embed.

Combine both: embed hot paths, link the rest. [Wish list](wish-list.md) or
[wish template](wish-template.md)
can trim embed size. [Link lookup resource](link-lookup-resource.md) reduces
broken-link pain. [Two in production](two-in-production.md) can run both shapes
during migration.

Quality tensions: message size vs call count; bandwidth vs computation;
statelessness vs performance; ease of use vs latency — stakehold goals decide.
