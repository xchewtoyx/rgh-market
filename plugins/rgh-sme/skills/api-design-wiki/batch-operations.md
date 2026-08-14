---
type: concept
title: Batch Operations
description: >
  Custom collection-scoped methods that apply standard get, create, update, or
  delete semantics atomically across multiple resources in one request.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 18"
---

**Batch operations** provide limited transactional semantics without a generic
transaction API — named `BatchGetMessages`, `BatchDeleteMessages`, etc., targeting
the **collection** URL (`POST .../messages:batchDelete`), not the parent resource.

There is **no batch list** — use standard list with [list filter](list-filter.md)
for set retrieval with looser atomicity.

## Atomicity

If any item fails, the **entire** request fails — no partial success lists. Rationale:
atomic multi-resource updates are the point; partial-success responses are complex.
Includes batch delete when one id is already deleted (imperative delete semantics
from [standard method contract](standard-method-contract.md)).

For best-effort multi-read, use list with a filter on ids instead.

## Request shape

Two composable strategies:

1. **List of standard single-resource requests** — needed when items differ (per-item
   parents, per-item [field mask](field-mask.md) on update).
2. **Hoisted shared fields** — for example `ids: string[]` on batch get/delete;
   `parent` and blanket `fieldMask` hoisted on batch update.

If hoisted and per-item values conflict, **reject** — do not infer overrides. Use
parent wildcard `-` in the URL and per-request `parent` for cross-parent batches:

```
POST /chatRooms/-/messages:batchCreate
{ "requests": [
  { "parent": "chatRooms/1", "resource": { ... } },
  { "parent": "chatRooms/2", "resource": { ... } }
]}
```

Reject URL parent vs request parent mismatches the same way.

## Per-method notes

- **Batch get:** HTTP GET; ids in query string; optional hoisted `fieldMask`; preserve
  response order matching request order; document max batch size — **no pagination**
  inside batch.
- **Batch delete:** POST; void response; all-or-nothing including already-deleted ids.
- **Batch create:** hoisted `parent` plus `CreateMessageRequest[]`; order preservation
  critical for matching server-assigned ids to request items.
- **Batch update:** `UpdateMessageRequest[]`; hoisted `fieldMask` must match item-level
  mask or item mask must be blank.

Cross-parent wildcards may complicate future sharding — disallowing them later is
likely breaking; decide early.

Trade-off: atomicity over convenience; get/delete use raw id lists while create/update
use full request objects — simpler per verb than uniform indirection.

Pairs with [request deduplication and idempotency keys](request-deduplication-and-idempotency-keys.md)
when retrying large batch creates.
