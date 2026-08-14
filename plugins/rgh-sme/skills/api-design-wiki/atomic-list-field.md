---
type: concept
title: Atomic List Field
description: >
  Treat inline list fields as wholes — replace entirely on update, never
  expose per-index mutation — to avoid dual entry points and ordering races.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

**Lists** are ordered collections (`categories: string[]`). Good for simple
primitive sets inherent to a resource. Storage need not mirror lists natively;
expose what remote clients need.

**Atomicity rule:** list fields are **atomic** — clients replace the entire
list on update, never patch individual indices. Positional addressing makes
order significant; concurrent inserts shift indices; dual edit paths (whole
list vs single row) create consistency hazards even with ETags.

Anti-pattern: normalizing a list into a child table with its own CRUD endpoint
for one row — opens the same race as editing one character inside a string
field. Mental model: a list is like a JSON blob you replace wholesale.

Keep lists **homogeneous** (one element type) to avoid ambiguity when numbers
serialize as strings for precision.

Bound maximum item count and per-item size; **reject** over-limit input, do
not silently truncate. If size is unbounded or hard to predict, model a
[subcollection resource](resource-hierarchy-vs-cross-reference.md) with
[pagination](pagination.md) instead of an inline list.

Default-value caveat: `[]` is often meaningful, so it cannot signal "pick a
default" the way empty strings sometimes do — restrict defaults to create time
or move to a managed subcollection.
