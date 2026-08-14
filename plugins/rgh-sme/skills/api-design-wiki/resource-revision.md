---
type: concept
title: Resource Revision
description: >
  A timestamped snapshot of a resource that shares the resource's primary id
  but is distinguished by a unique revision identifier.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

A **resource revision** is a point-in-time snapshot of a resource, labeled
with a unique revision identifier and stamped at creation time. Revisions are
not a separate interface: they extend the existing resource shape with
`revisionId` and `revisionCreateTime`. Multiple stored records share the same
resource [identifier](resource-identifier.md) but differ in `revisionId`.

Retrieving a resource by its plain identifier returns the **latest** revision
— the one with the most recent `revisionCreateTime`. The resource identifier
therefore acts as an alias for the current revision.

Use revisioning when history must be preserved for auditing, rollback, or
compliance (documents, contracts, purchase orders, legal filings). Avoid it
when a single present-moment snapshot suffices: revisioning adds storage,
complexity for designers and clients, and operational burden.

Revision scope should stay on the resource itself. Including child resources
in each snapshot makes restore a true full-tree rollback but costs far more
storage and implementation effort; prefer scoping revisions to direct fields
unless a firm business requirement demands hierarchy-aware snapshots and
alternatives such as [export](import-export-as-contract.md) do not suffice.
