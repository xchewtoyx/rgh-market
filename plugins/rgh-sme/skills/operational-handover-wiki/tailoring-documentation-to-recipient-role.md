---
type: concept
title: Tailoring Documentation to Recipient Role
description: Different recipients of a handover need different subsets of the same material, so a single all-purpose document under-serves everyone rather than serving any of them well.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 22"
---

"Know your reader" applies to a handover package the same way it applies to any other documentation: a maintainer, a tester, an end user, and a future owner reading the same material six months from now each need a different slice of it, and each is poorly served by a document written for someone else's needs.

- **A maintainer** needs what a regular developer needs (the pieces they're responsible for, the constraints on them) plus specifically a way to localize [the scope of a change](change-scope-classification.md) before making it and a way to trace what else depends on the piece they're about to touch.
- **A tester or integrator** needs black-box behavior and interface specs for the pieces they must fit together — not the internal reasoning behind them.
- **Someone taking over ownership entirely** (the closest analogue to "the future architect") is the most avid reader of all: they want the full, candid picture, including why past alternatives were rejected, because they cannot be expected to reconstruct today's reasoning from memory the way the outgoing owner still can.
- **Infrastructure or platform support staff** need to know what will actually run where, not how it was decided to be built that way.

## Why This Matters for Handover

A single "the architecture" document tries to serve all of these audiences at once and typically ends up too shallow for the maintainer who needs to trace an impact and too heavy with irrelevant deployment detail for the person who just needs to consume an interface. Treating the handover package as several purpose-built slices — even if they draw from the same underlying source material — is what lets each recipient find exactly what they need without wading through what they don't. This is a role-based application of the same instinct as [Structural Views for Onboarding](structural-views-for-onboarding.md): different questions need different views, and different *people* asking different questions need different combinations of those views handed to them up front rather than discovered by trial and error.
