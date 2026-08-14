---
type: concept
title: API Wire Naming
description: >
  Conventions for expressive, simple, predictable names on the public API
  surface — methods, resources, fields — including grammar, units, and case.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 3"
---

Unlike compiled identifiers, **API names are permanent and client-visible** —
renaming is like changing a phone number ([backward compatibility](backward-compatibility-policy.md)
cost).

**Good names** mirror API quality minus operational:

- **Expressive** — convey what is named; disambiguate overloaded domain words
  (`messagingTopic` vs `modelTopic` when both exist).
- **Simple** — add qualifiers only when they earn their place (`UserPreferences`
  beats `UserSpecifiedPreferences` or bare `Preferences`).
- **Predictable** — same name for the same concept everywhere; inconsistent
  synonyms (`topic` vs `messagingTopic`) force re-learning.

**Language and grammar:**

- **American English** on the wire (`color`, `BookStore`); docs may localize.
- **Imperative RPCs** — `<Verb><Noun>` (`CreateBook`); avoid indicative names
  like `isValid()` whose response shape is ambiguous — prefer `GetValidationErrors()`.
- **Prepositions** in resource names often signal combinatorial RPC sprawl
  (`BookWithAuthor`) — use [field masks](field-mask.md) or views instead.
- **Pluralization** — singular resource types (`Book`); plural collection paths
  (`/books/1234`); handle irregular plurals deliberately.
- **Case** — match spec conventions (Protobuf: UpperCamel messages,
  snake_case fields; OpenAPI: camelCase fields); consistency beats any one choice.
- **Reserved keywords** — avoid `string`, `from`, etc.; prefer domain terms
  (`sender`/`recipient`).

**Units and types:** primitive fields need units in the name when ambiguity hurts
(`sizeBytes` vs `sizeMegapixels`). Prefer structured types (`Dimensions` with
`lengthPixels`/`widthPixels`) over string-encoded composites when structure
matters.

**Naming vs guarantees:** [pagination](pagination.md) uses `maxPageSize` because
the API returns *at most* that many items — `pageSize` wrongly implies an exact
count and causes premature stop when fewer items return.

**Context** shapes interpretation — `Book` as resource vs action depending on
domain; names rarely stand alone.

See [boolean field conventions](boolean-field-conventions.md) for flag naming.
