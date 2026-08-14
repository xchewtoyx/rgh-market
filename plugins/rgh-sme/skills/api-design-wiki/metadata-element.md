---
type: concept
title: Metadata Element
description: >
  A representation element carrying contextual facts about the message or
  payload — version, timestamps, units — distinct from core domain data.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4, ch. 6"
---

A **metadata element** annotates a message or [data element](data-element.md) with
non-domain facts: [version identifier](version-identifier.md), creation time, units,
correlation ids, pagination cursors, delivery status on
[data transfer resources](data-transfer-resource.md).

Populate thoroughly and consistently — sparse or stale metadata breaks interoperability.
Define a **freshness policy**: some metadata is immutable (original creator); counters
and estimates should expire or be labeled as estimates.

**Variants** (may overlap on one field):

- **Control metadata** — flags, filters, security tokens, hypermedia controls steering
  processing.
- **Aggregated metadata** — summaries of other elements ([pagination](pagination.md)
  totals, statistics).
- **Provenance metadata** — origin, timestamps, message ids, location.

Separate metadata structurally from domain [parameter trees](parameter-tree.md) where
possible so clients can ignore or validate context independently. HTTP `ETag` and
`Content-Type` are metadata realized in [conditional request](conditional-request.md).

Adding metadata that changes semantics of existing fields (currency on a price assumed
USD) is an evolution hazard — coordinate with
[backward compatibility policy](backward-compatibility-policy.md).

Stereotype of [data element](data-element.md); often an
[atomic parameter](atomic-parameter.md) or small tree. Alternative: metadata-only
[retrieval operation](retrieval-operation.md) or dedicated metadata holder endpoint.

Clients should treat metadata as optional convenience unless the contract marks it
required — though pagination links and rate-limit headers often become de-facto
required in practice.
