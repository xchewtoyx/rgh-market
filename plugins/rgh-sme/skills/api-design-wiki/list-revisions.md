---
type: concept
title: List Revisions
description: >
  A custom list-style method that enumerates revisions of one resource rather
  than children of a parent, keyed by resource id with standard pagination.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

The standard [list method](standard-method-contract.md) lists children of a
parent; [resource revisions](resource-revision.md) need a separate custom
method such as `GET /resources/*:listRevisions`. The request uses an `id`
field identifying the target resource (not a `parent` field). Otherwise behave
like standard list, including [pagination](pagination.md).
