---
type: concept
title: Link Element
description: >
  A wire element carrying a dereferenceable address and local name for related
  information held at another endpoint.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4, ch. 6, ch. 7"
---

A **link element** is a network-accessible [id element](id-element.md) — href plus
relation semantics (`rel`/`href`, HAL, JSON-LD, IANA link relations). Used in
[linked information holder](embedded-entity-vs-linked-information-holder.md)
messages instead of inlining the target.

Links should convey **what following them means** — next step, pagination, compensating
action, detail drill-down — via relation type and optional [metadata elements](metadata-element.md)
(expected verb, media type). API clients cannot infer semantics from URL text alone;
document in [API description](api-description.md) and/or supply runtime metadata.

Collections of links model one-to-many references. Links to
[processing resources](processing-resource.md) support HATEOAS control flow and
[pagination](pagination.md) (`next`, `self`).

**Stability:** changing URI schemes after launch is costly — [link lookup resource](link-lookup-resource.md)
and redirects mitigate. Treat URIs as part of security design — malformed links must
not crash servers.

Clients must tolerate redirects and broken links when targets move or are deleted —
pair with [cross-reference field](cross-reference-field.md) semantics (dangling ids).

Often realized as [atomic parameters](atomic-parameter.md) or small
[parameter trees](parameter-tree.md) (for example `_links` trees in paginated list
responses). Not every id is a link — correlation ids and third-party keys may stay
non-invokable by design.

Do not confuse with `sources:` citations — links stay inside the API contract graph.
