---
type: concept
title: Parameter Tree
description: >
  A hierarchical message structure nesting atoms, lists, and subtrees to mirror
  containment in the domain model.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4"
---

A **parameter tree** has a root and named or positional children — each child
an [atomic parameter](atomic-parameter.md), [atomic parameter list](atomic-parameter-list.md),
or nested tree. Cardinalities: one, optional, one-or-more, zero-or-more.
Recursive definitions model deep domain graphs (customer with address and move
history).

JSON objects and XML complex types realize trees; set-valued nodes become
arrays of objects. Natural for [embedded entities](embedded-entity-vs-linked-information-holder.md)
and rich [information holder](information-holder-resource.md) responses.

Separate domain data from [context representation](context-representation.md)
via structural branches. Explicit optionality avoids oversharing that hurts
format autonomy.

Trade-offs: more processing than flat lists; risk of oversized payloads on deep
recursion — cap depth and breadth in the contract.

Deep nesting may not map cleanly to query/path parameters (OpenAPI "deepObject"
behavior is undefined for deep trees).

**Choosing structure:** match domain containment when possible — tree-shaped domain
data maps to trees; a single frequent IoT reading maps to an
[atomic parameter](atomic-parameter.md). When security or correlation metadata must
stay separate from payload, prefer a [parameter forest](parameter-forest.md) with
distinct content and metadata trees rather than folding metadata into the content
tree. Splitting into many small messages saves per-message memory but raises round-trip
count and session-state cost; batching related atoms in lists or trees reduces chatter.
Overspecifying optionality hurts [backward compatibility](backward-compatibility-policy.md);
underspecifying risks interoperability on missing-vs-null semantics — see
[missing versus null policy](missing-versus-null-policy.md).
