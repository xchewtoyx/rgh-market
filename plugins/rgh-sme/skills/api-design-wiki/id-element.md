---
type: concept
title: Id Element
description: >
  A data element stereotype whose value identifies a resource or entity for
  lookup, update, or linking.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 6"
---

An **id element** is a specialized [data element](data-element.md) whose value
identifies endpoints, operations, or message parts — path parameter, DTO field, or
filter token. Use consistently in [API description](api-description.md) and
implementation; document global vs API-local uniqueness scope.

Common schemes: UUIDs (RFC 4122 — note v1 is guessable), human-readable generated
strings, surrogate database keys (couples consumers to storage — avoid when possible).
Usually an [atomic parameter](atomic-parameter.md) or tree leaf.

**Security:** ids should be hard to guess when authorization relies on obscurity;
always enforce proper auth regardless. Include ids in threat modeling.

**Scope:** uniqueness may be bounded by time (pagination cursor valid for session
lifetime) or space (API-local vs global). [Link elements](link-element.md) add
network addressability ids lack — REST maturity level 3 needs dereferenceable URIs,
not bare ids alone.

Returned by [state creation operations](state-creation-operation.md) for later
[state transition](state-transition-operation.md) calls. [Link lookup resources](link-lookup-resource.md)
map id elements to current link elements.

Follow [resource identifier](resource-identifier.md) design: permanence,
[checksum](identifier-checksum.md) when applicable. Distinct from [link element](link-element.md)
(which carries invokable addresses) and from correlation ids (may not be client-facing).

Embedding entire related records instead of ids wastes bandwidth — prefer id plus
optional [embedded entity](embedded-entity-vs-linked-information-holder.md) when
justified.
