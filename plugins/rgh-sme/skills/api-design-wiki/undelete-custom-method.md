---
type: concept
title: Undelete Custom Method
description: >
  A custom method restoring a soft-deleted resource by clearing its deleted
  flag, with explicit errors when the resource is not deleted.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 25"
---

**Undelete** restores a [soft-deleted](soft-deletion.md) resource:

`UndeleteChatRoom({id}) -> ChatRoom` as
`POST /{id=chatRooms/*}:undelete`.

Clears `deleted` (and resets `expireTime` when expiration is used). Undelete on
a resource that is **not** soft-deleted → error (412 Precondition Failed) — same
imperative-vs-declarative rationale as duplicate delete: did *this request*
restore the resource?

Complements [expunge custom method](expunge-custom-method.md) for the opposite
extreme — permanent purge.
