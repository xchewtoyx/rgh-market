---
type: concept
title: Atomic Parameter List
description: >
  A flat grouping of related atomic parameters whose co-location makes
  relatedness explicit in the contract and on the wire.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 4"
---

An **atomic parameter list** combines two or more [atomic parameters](atomic-parameter.md)
in one representation element — keyed or positional. Example address record:
`streetAddress*` (set), optional `postalCode`, required `city`.

Use when scalars belong together but should not nest deeply. Query strings like
`fields=city,postalCode` are positional lists — the basis of
[wish list](wish-list.md) field selection.

Order atoms logically; give representative examples in the API description.
Equivalent to a shallow [parameter tree](parameter-tree.md) in many mappings;
choose the pattern that matches the target technology's idioms.

When a platform transports only one flat parameter, wrap related atoms in a list
or tree — the structural choice is recursive for nested shapes. Prefer lists when
related scalars must stay simple but visibly grouped (salary figures without full
employee records).

[Link elements](link-element.md) in simple cases may be lists of href/rel pairs.
