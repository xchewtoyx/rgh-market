---
type: concept
title: Association Alias List Methods
description: >
  Convenience list methods on parent resources that imply a filter on the
  underlying association collection.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 14"
---

Filtered `ListMemberships({filter: "groupId: 2"})` answers "who is in this
group?" but dedicated **alias list methods** bake in the implied filter:

- `ListUserGroups({userId})` — groups for a user
  (`GET /{userId=users/*}/groups`)
- `ListGroupUsers({groupId})` — users in a group
  (`GET /{groupId=groups/*}/users`)

**Naming:** first segment (singular) = resource being queried by; second
(plural) = what is listed — `ListUserGroups`, `ListGroupUsers`.

Equivalent to filtered list on the [association resource](association-resource.md)
but clearer for common queries. Parent resources (`User`, `Group`) should not
inline full member lists — consumers use aliases or filtered association list.
