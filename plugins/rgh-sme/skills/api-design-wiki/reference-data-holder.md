---
type: concept
title: Reference Data Holder
description: >
  A read-only information holder serving immutable, widely shared lookup data
  such as country or status codes, designed for cache-friendly retrieval.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3, ch. 5"
---

A **reference data holder** is a specialized [information holder resource](information-holder-resource.md)
for **reference data** — inert, shared values (country codes, postal formats,
delivery statuses). Long-lived, simple, not client-writable.

Expose [retrieval operations](retrieval-operation.md) only — no create, update,
or delete from clients. Caching improves performance but introduces staleness
trade-offs; hardcoding reference values client-side violates DRY and breaks when
codes change.

Other endpoints embed reference ids or codes in requests/responses; clients
fetch definitions from the reference holder when needed.

See [string instead of enumeration](string-instead-of-enumeration.md) for wire
encoding of code values.
