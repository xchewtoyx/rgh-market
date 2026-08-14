---
type: concept
title: Hierarchical Resource Identifier
description: >
  When parent collection segments belong in an id because ownership is permanent
  and implies cascading delete or security — not for mutable associations.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
---

Embed hierarchy in a [resource identifier](resource-identifier.md) only when
the relationship is true **ownership**, not mere association.

**Anti-pattern:** `shelves/1/books/1` for "book 1 is currently on shelf 1."
Books move; embedding shelf id breaks [permanence](resource-identifier.md).
Store `shelfId` as a mutable field instead.

**Appropriate:** `books/1/pages/2` when pages never reparent, deleting the book
cascades to pages, and security inherits from the book. Child ids are meaningful
only with their parent segment; `pages/2` under different books are distinct
full strings (`books/1/pages/2` vs `books/9/pages/2`).

Identical local suffixes under different parents are expected and correct.

Contrast [cross-reference versus hierarchy](resource-hierarchy-vs-cross-reference.md)
when modeling relationships without embedding parent paths.
