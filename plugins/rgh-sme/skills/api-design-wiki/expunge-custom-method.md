---
type: concept
title: Expunge Custom Method
description: >
  Permanent hard removal via a dedicated custom method when standard delete
  performs soft deletion only.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 25"
---

When [soft deletion](soft-deletion.md) repurposes standard delete, permanent
removal needs a separate **[custom method](custom-method.md)** — not a query
flag on delete. HTTP DELETE rarely carries a body; `?expunge=true` on standard
delete reshapes method semantics and complicates access control (soft vs hard
becomes parameter-level permission instead of per-method).

**Preferred:** `ExpungeChatRoom({id}) -> void` as
`POST /{id=chatRooms/*}:expunge`.

Callable on **any** resource whether or not it was soft-deleted first — requiring
two steps adds friction without benefit.

Regulated contexts requiring immediate exact removal may skip soft deletion
entirely; contexts forbidding permanent deletion should omit expunge and
expiration.

Pairs with batch expunge when bulk hard removal is needed alongside batch soft
delete.
