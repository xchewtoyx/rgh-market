---
type: concept
title: Parameter Forest
description: >
  A top-level message payload comprising multiple sibling parameter trees,
  common when HTTP combines query params and body as one logical input.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4"
---

A **parameter forest** groups two or more top-level [parameter trees](parameter-tree.md)
by name or position — forests cannot nest forests. Example: upload customers
and products in one message with separate `customers` and `products` roots.

Semantically equivalent to a tree with an artificial root in many mappings; the
distinct pattern preserves technology differences (single DTO vs multiple method
parameters; HTTP query/path/header plus body as one forest).

JSON may render like a tree; service signatures differ:
`uploadForest(Forest)` vs `upload(List<Customer>, List<Product>)`.

Use at message top level only. For arbitrary complexity, recursive trees with
atomic leaves suffice theoretically — the four structure patterns exist to
model HTTP, SOAP, gRPC, and GraphQL idioms explicitly.

See [request bundle](request-bundle.md) for bundling multiple operations, not
just multiple trees in one message.
