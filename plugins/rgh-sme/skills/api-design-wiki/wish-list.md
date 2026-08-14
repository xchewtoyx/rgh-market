---
type: concept
title: Wish List
description: >
  Client-supplied flat enumeration of desired response fields so retrieval
  returns only listed elements without per-client operation variants.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 7"
---

A **wish list** lets clients shape responses at runtime: enumerate desired
[data elements](data-element.md) in the request (for example
`?fields=customerId,birthday,postalCode` as an
[atomic parameter list](atomic-parameter-list.md) or flat
[parameter tree](parameter-tree.md)). The provider returns only listed fields —
reducing over-fetch when network capacity is limited.

**Variants:** verbosity level as a single [atomic parameter](atomic-parameter.md)
(`minimal`/`full`); wildcards (`*`, `customer.*`); response expansion — terse
first response lists expandable fields for a follow-up wish.

**Implementation:** translate wish to data-source filter (SQL `WHERE`) or
fetch-and-post-filter; may pass through to downstream APIs that support the same
pattern.

**Risks:** misspelled names error or silently omit fields; API renames break
stale wishes; exposes internal data model and increases coupling; comma-separated
lists need clear error semantics.

Combines with [pagination](pagination.md), [field mask](field-mask.md) (similar
Google/protobuf sparse fieldsets), and [rate limit](rate-limit.md) savings.
Document allowed fields in the [API description](api-description.md).

For nested selection, use [wish template](wish-template.md) instead.

**Security:** letting clients enumerate arbitrary fields can expose sensitive
[data elements](data-element.md) or enable denial-of-service via huge wish lists —
validate names against an allowlist and error on unknown fields rather than silently
omitting when strictness prevents data leaks.
