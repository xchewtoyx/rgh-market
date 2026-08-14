---
type: concept
title: Data Element
description: >
  A domain payload field in a message, distinct from metadata, identifiers, and
  links, usually carried as atomic parameters or parameter trees.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4, ch. 6"
---

A **data element** carries business-domain content in request or response
messages — customer name, order total, claim status. It implements the API's
**Published Language**: a vocabulary wrapping relevant parts of provider business
data without exposing internal persistence shapes wholesale.

Stereotypes specialize the same structural patterns: [metadata element](metadata-element.md),
[id element](id-element.md), [link element](link-element.md).

Expose as [atomic parameters](atomic-parameter.md) or nested
[parameter trees](parameter-tree.md). [Embedded entities](embedded-entity-vs-linked-information-holder.md)
are trees of data elements; [linked information holders](embedded-entity-vs-linked-information-holder.md)
replace embeds with [link elements](link-element.md).

**Variants:** *entity element* — includes an id implying object lifecycle; *query
parameter* — selects a subset in [retrieval operation](retrieval-operation.md), not
an owned entity.

Rules of thumb: expose fewer fields when possible — reduces attack surface, privacy
configuration, and [backward compatibility](backward-compatibility-policy.md) burden.
Full entity mapping is expressive but hard to secure and evolve. Optional deep nesting
hurts performance and testability.

Document meaning, constraints, and [missing versus null](missing-versus-null-policy.md)
behavior in the [API description](api-description.md). Different bounded contexts may
use different data element projections of the same domain entity.
