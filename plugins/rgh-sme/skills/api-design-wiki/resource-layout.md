---
type: concept
title: Resource Layout
description: >
  How resources, fields, and relationships are arranged in an API — analogous
  to schema design — with purposeful references and shallow hierarchy.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 4"
---

**Resource layout** is the entity-relationship model for an API: which
resources exist, their fields, and how relationships connect them. Relationships
are bidirectional even when only one direction is declared.

**Reference** — one resource points at another via a field (foreign key). Many-to-one
from the pointed-to side.

**Many-to-many** — model via [association resource](association-resource.md)
join rows, not ad hoc arrays when relationship metadata matters.

**Self-reference** — same-type pointers (org charts, social graphs). Only when
fundamental to product purpose — fan-out on delete can touch millions of edges.

**Hierarchy** — reference implying **ownership**: delete and access cascade like
folders. Child has one parent; reparenting is usually a bad idea. Coexist with
non-owning references (company owns chat rooms; room **references** shared
retention policy).

**Choosing relationships:** connect only what is **purposeful and fundamental** —
rich graphs impose performance cost at scale. Given a needed link, choose
[embedded entity vs linked information holder](embedded-entity-vs-linked-information-holder.md):
inline for single-call common case; reference when data is large, shared, or
rarely needed. Use hierarchy when cascade delete/access match product semantics.

See [resource hierarchy vs cross-reference](resource-hierarchy-vs-cross-reference.md)
for URL encoding and [resource modeling anti-patterns](resource-modeling-anti-patterns.md)
for common mistakes.
