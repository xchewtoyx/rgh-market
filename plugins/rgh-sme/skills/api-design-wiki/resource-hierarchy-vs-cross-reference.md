---
type: concept
title: Resource Hierarchy vs Cross-Reference
description: >
  When parent-child URLs imply ownership and cascade semantics versus when
  relationships are mutable associations stored as fields or link elements.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 5"
---

**Hierarchy** embeds parent segments in [resource identifiers](resource-identifier.md)
when children never reparent, deletes cascade, and security inherits —
`books/1/pages/2`. See [hierarchical resource identifier](hierarchical-resource-identifier.md)
and [resource layout](resource-layout.md) for when cascade semantics fit.

**Cross-reference** stores foreign keys or [link elements](link-element.md) when
associations change — shelf assignment on a book, customer on an order.
See [cross-reference field](cross-reference-field.md) for naming (`authorId`),
dangling-pointer policy, and dynamic `targetType` pairs.
Prefer fields or links over encoding mutable relationships in paths.

Avoid **deep hierarchies** without true cascade need — see
[resource modeling anti-patterns](resource-modeling-anti-patterns.md).

[Revision scope](resource-revision.md) usually excludes child hierarchies unless
a firm snapshot requirement exists.
