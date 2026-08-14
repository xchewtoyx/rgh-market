---
type: concept
title: Custom Method Targeting
description: >
  Whether a custom method attaches to one resource, its parent collection, or a
  wildcard collection when acting on many related items.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 9"
---

[Custom methods](custom-method.md) must declare their target explicitly —
unlike standard methods, where create/list hit the collection and get/update/delete
hit one resource.

**Same collection, many resources** — bulk export or delete within one user's
emails → target the **collection**:
`POST /users/1/emails:export`, not `POST /users/1:exportEmails`.

**Parent resource focus** — export all user info (emails included) → target
the **resource**: `POST /users/1:export`.

**Multiple parents** — archive emails across several users → collection format
with parent wildcard `-`:
`POST /users/-/emails:archive` and list specific ids in the body.

Pairs with [import and export as contract](import-export-as-contract.md) for
collection-scoped bulk movement.
