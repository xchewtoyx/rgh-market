---
type: concept
title: Data Fabric Architecture
description: >
  Layering unified access, governance, and real-time capability onto a modern
  data warehouse so any consumer inside or outside the organization can reach
  any data without knowing where it physically lives.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 11"
---

Data fabric is an evolutionary layer added on top of a
[modern data warehouse](modern-data-warehouse-architecture.md): rather than a
distinct storage architecture, it's a set of capabilities that "weave" access
to all of an organization's data — regardless of size, speed, or type —
into a single reachable surface for anyone authorized to use it. There's no
sharp line separating an MDW from a data fabric; it's a spectrum defined by
which of a cluster of governance and access capabilities have been added,
not a different storage technology.

The capabilities that mark the transition, several of which already have
their own treatment in this domain:

- **[Data access policies](data-access-policy-enforcement.md)**: centrally
  defined rules for who can access what, enforced at the point of access
  rather than left to convention.
- **[Metadata catalog](data-catalog.md)** and the
  **[lineage](data-lineage.md)** it carries, so a consumer can find a dataset
  and trust what it actually is before using it.
- **[Master data management](master-data-management.md)**, producing one
  authoritative version of shared entities like customer or product.
- **[Data virtualization](data-federation-and-virtualization.md)**, letting a
  consumer query across siloed sources without first copying everything into
  one place — genuinely useful, but only for the subset of access patterns
  that suit a live federated query, not a wholesale replacement for
  centralized storage.
- **[Real-time processing](batch-vs-streaming-ingestion.md)**, so the fabric
  isn't limited to whatever the last batch load produced.
- **APIs** fronting data access instead of raw connection strings: a
  consumer talks to a stable API surface, and if the underlying data moves or
  its storage technology changes, only the API's internal implementation
  needs updating — every caller is insulated from that change.

An architecture doesn't need every one of these to count as a data fabric in
practice; what distinguishes it from a plain MDW is that governed,
policy-enforced, catalog-discoverable access has become a first-class layer
rather than something bolted on ad hoc per consumer. The trade-off is real:
this layer is genuinely more complex to build, staff, and troubleshoot than
an MDW alone, and is worth adopting only once an organization's data volume,
source variety, or compliance surface has grown large enough that ungoverned,
ad hoc access has itself become the bottleneck.
