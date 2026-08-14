---
type: concept
title: Backward Compatible Infrastructure Transformation
description: Adding a new interface to a provider stack while temporarily keeping the old one pointing at it, so consumers can migrate to the new interface on their own schedule instead of all at once.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 21"
---

When a [provider stack](test-fixtures-for-infrastructure-stacks.md) changes what it exposes to consumers — for example, moving from a single shared VLAN to three — it doesn't have to force every consumer to update in lockstep. A backward compatible transformation adds the new resources and exports their new identifiers, while also keeping the *old* exported identifier pointing at one of the new resources (marked deprecated), so every consumer stack that hasn't updated yet keeps working unchanged against the old name. Consumers migrate to the new identifiers on their own schedule; once nothing depends on the old identifier anymore, it's removed from the provider's code.

This works well when the change is purely additive from the consumer's point of view — a rename or a split that can be bridged with an alias. It doesn't help when applying the *new* code to a *live* instance would itself require destroying or disrupting resources still in active use — most infrastructure platforms refuse an operation like that outright, or worse, apply it partway and leave the instance in an inconsistent halfway state. That harder case — changing infrastructure resources that are actually in use right now — needs either [infrastructure surgery](infrastructure-surgery-technique.md) or the [expand and contract pattern](expand-and-contract-pattern.md).

Backward compatible transformation is the [dependency-discovery](resource-matching-pattern.md) analogue of a [feature toggle](feature-toggles-for-infrastructure.md): a toggle lets one stack support two code paths at once, while this technique lets a provider stack support two sets of consumers — those on the old interface and those on the new — at once.
