---
type: concept
title: Multiple Data Lakes Rationale
description: >
  Why organizations split analytical storage into several physically separate
  data lakes rather than one, and the cross-lake query cost that trade-off
  buys.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 5"
---

One large [data lake](data-lake-architecture.md) is easier to find and
combine data in, but several concrete pressures push organizations toward
multiple physically separate lakes instead of zones inside a single one:

- **Ownership and organizational structure**: when domain teams own their
  own data end-to-end — the [data mesh](data-mesh.md) pattern — each domain
  is a natural candidate for its own lake rather than a shared one a central
  team administers. A related split is a **source-aligned** lake (minimally
  transformed, structured the way people already familiar with the source
  system understand it) versus a **consumer-aligned** lake (transformed for
  broader, non-specialist understandability) for the same underlying data.
- **Compliance, governance, and security**: data residency/sovereignty rules
  can legally require region-local storage (data generated in one
  jurisdiction that cannot leave it), and separating sensitive from
  less-sensitive data into different lakes lets stricter access controls
  apply only where needed, limiting the blast radius of any single
  elevated-privilege grant. Differing regulatory regimes (GDPR, HIPAA) are
  also easier to satisfy per-lake than as exceptions carved into one shared
  lake's policy.
- **Platform limits and policy granularity**: cloud providers cap resources
  per account/subscription (e.g., max storage accounts), and splitting lakes
  sidesteps those ceilings while also allowing different infrastructure
  policies (e.g., mandatory encryption on one lake but not another) and
  finer-grained cost attribution than tag-based billing alone provides.
- **Performance, availability, and disaster recovery**: placing a lake
  regionally close to its users cuts latency, and replicating across regions
  lets traffic fail over to an alternate lake if one becomes unreachable.
  This also allows differentiated service levels by data criticality — a
  highly available, replicated lake for critical data, a cheaper
  single-region lake for data that can tolerate more downtime or latency.
- **Environment and retention separation**: dev, test, and production lakes
  kept apart avoid lifecycle-stage interference (a test job's malformed data
  never lands anywhere production reads from), and separate lakes make it
  straightforward to enforce different [retention](data-retention-and-lifecycle-management.md)
  rules per data category where legal or regulatory requirements differ.

**The cost is real and compounding**: more lakes means more operational
surface, more required expertise, and extra integration tooling just to move
data between them while keeping it consistent. Combining data that lives in
separate lakes for a single query or report is the sharpest cost — it's
effectively a [data federation](data-federation-and-virtualization.md)
problem across lakes rather than across tables, worsened when the lakes are
geographically distant enough that copying everything to one location first
becomes the only practical option. Multiple lakes should be adopted for a
specific, named pressure from the list above, not by default — and where the
pressure is something like data sovereignty, there may be no real choice to
weigh at all.
