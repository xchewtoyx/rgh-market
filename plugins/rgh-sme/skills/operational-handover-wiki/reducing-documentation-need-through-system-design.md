---
type: concept
title: Reducing Documentation Need Through System Design
description: Treating the amount of explanatory prose a system requires as something to minimize by design, not just something to write more of.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 10"
  - title: "Infrastructure as Code"
    resource: "Infrastructure as Code (Morris), ch. 2"
---

The default response to "an unfamiliar operator can't safely run this system" is to write more documentation. A complementary and often more durable response is to change the system so it needs less explanation in the first place — treating the volume of necessary prose as a design metric to reduce, not just a gap to fill.

## Design Levers That Reduce Documentation Need

- **Error-proof interfaces**: An API or interface that makes the incorrect usage impossible or obviously wrong (rather than merely documented as incorrect) doesn't need a prose warning, because there's nothing unsafe left to warn about.
- **Consistency**: A system where every component follows the same conventions needs documentation for the convention once, not for every individual instance of it.
- **Replaceability**: A component that's easy to safely remove and rebuild needs less tribal knowledge about its specific quirks, because a confused maintainer's fallback is "replace it" rather than "understand every detail of why it's built this way."
- **Constrained behavior**: Deliberately narrowing what a component can be configured or used to do reduces the surface area that needs explaining, at the cost of flexibility.

A blunter version of the same instinct, applied specifically to operational procedures: "if it's worth documenting, it's worth automating" — a step someone judged important enough to write a careful runbook entry for is usually also a candidate to script, at which point the script is the documentation and it can't silently fall out of date the way prose can.

## Framing: A Design Challenge, Not Withheld Help

Pursuing this seriously requires outside judgment about what actually needs explaining, not just the author's own sense of clarity — see [The Author's Blind Spot for Complexity](authors-blind-spot-for-complexity.md) for why the person best positioned to reduce a system's obscurity is also the worst positioned to notice it unaided. Pursuing this is a genuine design challenge aimed at making the system itself safer to approach unprepared — it is not the same thing as simply not writing documentation and hoping the system is self-explanatory. Treat "how much explanatory prose does this component require" as a signal during design and review: a component that needs an unusually long runbook or an unusually detailed gotcha list is a candidate for redesign, not just better documentation of its current form.

This doesn't replace the documentation practices elsewhere in this domain — even a well-designed system needs some [runbooks](runbook-checklist-design.md) and [maintenance workflows](documentation-maintenance-workflows.md) — but it changes where investment goes: toward a system that needs less written explanation to operate safely, alongside writing the explanation that remains. See [Operability as a Design Property](operability-as-a-design-property.md) for the parallel case applied to day-to-day operational ease rather than explanatory need specifically, and [Infrastructure-as-Code Properties for Safe Change](iac-properties-for-safe-change.md) for the same idea applied specifically to what makes infrastructure code safe to modify.
