---
type: concept
title: List Filter
description: >
  A server-evaluated string expression on standard list requests that returns
  only resources matching criteria without client-side full scans.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 22"
---

Standard list returns collections; [standard method contract](standard-method-contract.md)
get returns one id. **List filter** closes the gap: add `filter: string` beside
`maxPageSize` and `pageToken` on list requests so the server evaluates criteria
server-side.

Client-side filter after paging wastes bandwidth and cannot prove completeness without
fetching everything.

## String vs structured filter

Prefer an **unstructured string** in a documented syntax (SQL-like `WHERE`, CEL,
AIP-160, storage-native subset) over a rigid structured query object:

- Server can extend syntax without client schema upgrades ([backward compatibility](backward-compatibility-policy.md)).
- Familiar to users who know SQL-like expressions.
- Stays readable as conditions compound.

Structured and string forms are convertible; the choice is ergonomics and evolution,
not capability.

## Evaluation rules

**Hermetic evaluation:** `evaluate(filter, resource) → boolean` using **only** fields
on the resource under test. No dereferencing other resources or external systems during
filter evaluation — `administrator.name = "Luca"` requires embedded name, not an id
lookup.

**Repeated fields:** treat arrays as unordered — test membership (`"new" in tags`),
not index positions (`tags[0]`). Positional filters imply ordering guarantees the API
should not make. Use explicit position fields when order matters.

**Strictness:** error on unknown field names and type mismatches — silent non-match
on typo (`ttile`) frustrates operators and is catastrophic when the same filter drives
[purge custom method](purge-custom-method.md). Do not be lenient "because reads are
safe."

**Custom functions:** extend via named helpers (`endsWith(title, "(new)")`,
`imageContains(profilePhoto, "dog")`) instead of bloating core grammar with wildcards
that need their own escaping.

## Adoption

Filtering costs server resources but beats pushing full scans onto clients and infrastructure.
Recommend filter support on list for collections that may reach hundreds or thousands of
rows. Same filter string must behave identically on list and purge.

Used by [list operations](list-operations.md) for operation discovery and
[association alias list methods](association-alias-list-methods.md).
