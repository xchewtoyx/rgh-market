---
type: concept
title: Link Lookup Resource
description: >
  A specialized information holder that returns current link elements for
  referenced endpoints so messages stay decoupled from concrete URLs.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 3"
---

A **link lookup resource** is an [information holder resource](information-holder-resource.md)
whose [retrieval operations](retrieval-operation.md) return [link elements](link-element.md)
— single or collections — with up-to-date addresses of referenced endpoints.

Problem solved: representations refer to many or frequently changing targets
without baking brittle URLs into every message. Clients dereference via lookup
when content is needed; broken links can be retried against lookup instead of
immediate hard failure.

Trade-offs: smaller messages vs extra round trips compared to
[embedded entity](embedded-entity-vs-linked-information-holder.md); adds
coupling to the lookup service itself and endpoint count. Works best when
endpoint references can change dynamically at runtime.

Hypermedia evolution must coordinate [version identifiers](version-identifier.md)
across linked APIs — a backend may not know which downstream version the
ultimate client supports.
