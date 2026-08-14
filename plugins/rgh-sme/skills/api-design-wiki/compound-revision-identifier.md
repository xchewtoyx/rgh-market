---
type: concept
title: Compound Revision Identifier
description: >
  A resource id combined with a revision id using an @ separator so the
  standard get method can retrieve a specific revision without changing its
  request shape.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

To fetch one [resource revision](resource-revision.md), extend the standard
[get method](standard-method-contract.md) by interpreting a compound
identifier: resource id, `@`, revision id — for example
`/chatRooms/1/messages/2@1234` for revision `1234`. Filtering via list works
but is awkward for a single-item fetch; compound ids reuse get unchanged.

**Invariant:** `GetResource({id}).id == id`. The response `id` field must
exactly match what was requested. A request without `@` returns an `id`
without a revision suffix (even though `revisionId` is populated on the
resource). A request with `@revisionId` returns that exact compound string.
