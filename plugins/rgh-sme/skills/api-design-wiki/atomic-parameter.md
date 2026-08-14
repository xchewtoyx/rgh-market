---
type: concept
title: Atomic Parameter
description: >
  A single scalar or binary value in a request or response — the simplest
  representation element with explicit type, cardinality, and meaning.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4"
---

An **atomic parameter** exchanges one unstructured value — string, number,
Boolean, encoded binary — as a path segment, query field, header, or body
property. Document name, type, cardinality (required, optional, set), value
range, and meaning (including units) in the [API description](api-description.md).

Set-valued atoms use JSON arrays; binary may use Base64. Internally structured
strings (regex, CSV-in-a-string) stay application-level — convenient but bypasses
schema tooling.

Stereotypes from the same shape: [data element](data-element.md),
[metadata element](metadata-element.md), [id element](id-element.md),
[link element](link-element.md). [Version identifiers](version-identifier.md)
are often atoms.

Maps to JSON primitives, XML simple types, protobuf scalars, GraphQL scalars.

When a platform allows only one return value, group related atoms in an
[atomic parameter list](atomic-parameter-list.md) or [parameter tree](parameter-tree.md).
