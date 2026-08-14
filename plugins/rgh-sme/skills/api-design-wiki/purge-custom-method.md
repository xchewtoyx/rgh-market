---
type: concept
title: Purge Custom Method
description: >
  A filter-driven bulk delete that previews matching resources by default and
  requires an explicit force flag before removing data.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 19"
---

**Criteria-based deletion** removes resources matching a filter without listing
ids first — avoiding paginated list plus [batch operations](batch-operations.md)
delete and the race where membership changes between list and delete.

The **purge** custom method combines list semantics with atomic delete: accept the
same `filter` string as standard list (see [list filter](list-filter.md)), delete
all matches in one call when forced.

## Safety defaults

Purge is dangerous — an empty filter matches **everything**, and a typo like
`fliter` silently matches all. Do not reject empty filters — that would break
filter consistency between list and purge.

Instead, default to **validation-only**:

- **`force` omitted or false:** no deletion; return `purgeCount` and `purgeSample`
  (ids of matching resources) so callers spot-check before committing.
- **`force: true`:** execute deletion; `purgeCount` is exact.

Do not reuse [validate-only request](validate-only-request.md) here — its default
is execute, which would make omitted flags catastrophic. Purge is one of the few
methods intentionally **crippled by default**.

## Response fields

- **`purgeCount`:** exact on live purge; may be an estimate on preview — avoid
  severe underestimates that surprise operators at execution time.
- **`purgeSample`:** enough ids to catch filter mistakes (≥100 for large sets, or
  full sample when cheap).

## Consistency

Preview and live purge may see different match sets — data changes in between.
Do not snapshot at preview time or fail on drift; that reintroduces list-then-delete
complexity. Follow the same consistency guarantees as list.

For resources with [soft deletion](soft-deletion.md), document whether purge
soft-deletes or [expunge custom method](expunge-custom-method.md)-style permanent
removal.

Avoid offering purge unless absolutely necessary — even with safeguards, mistakes
can destroy large datasets quickly.
