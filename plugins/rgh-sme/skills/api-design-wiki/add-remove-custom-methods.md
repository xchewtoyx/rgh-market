---
type: concept
title: Add-Remove Custom Methods
description: >
  Pair of custom methods that join or split a many-to-many relationship without
  exposing a third association resource, at the cost of relationship metadata.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 15"
---

When [association resource](association-resource.md) overhead is unwarranted — no
join metadata beyond existence — use **add** and **remove** custom methods on one
**managing** resource to hide the join row.

Example: users in groups — `AddGroupUser` / `RemoveGroupUser` on `Group`, not a
standalone `Membership` resource.

## Limitations

1. **No relationship metadata** — cannot store join time, role, or expiry on the
   association itself; store elsewhere if needed.
2. **One managing side** — pick whether groups add users or users add groups;
   the choice affects ergonomics but the pattern requires exactly one manager.

## Naming and requests

Name `Add<Managing><Associated>` / `Remove<Managing><Associated>`. Request carries
`parent` (managing resource id) and the **associated resource id only** — not the
full associated resource (that would imply simultaneous create/update).

HTTP example: `POST /groups/1/users:add {"userId": "users/1"}`.

## Listing

Provide two [association alias list methods](association-alias-list-methods.md) —
one per direction (`ListGroupUsers`, `ListUserGroups`) on implicit subcollections.
Do not inline unbounded member lists on the parent resource.

## Integrity

Duplicate add → **409 Conflict**; remove when not a member → **412 Precondition
Failed**. Callers who only care about end state may treat conflict on add as success
(already a member).

Trade-off: simpler surface than association resources; nonreciprocal and metadata-free.
