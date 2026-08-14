---
type: concept
title: The Author's Blind Spot for Complexity
description: Whoever built a system is a poor judge of how confusing it will be to someone inheriting it, because familiarity has already erased the difficulty for them.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (Ousterhout), ch. 2"
---

Complexity is not a property of a system in the abstract — it's what a specific person experiences trying to understand or change it. That makes it fundamentally more visible to readers than to the original author: by the time someone has built a system, they've internalized every quirk and workaround well enough that none of it feels complicated anymore. If the person who wrote a handover document thinks the system is simple and clear but the person receiving it finds it confusing, the discrepancy should be resolved in the reader's favor — they are the one experiencing the complexity that matters.

## Why This Matters for Handover

This is a direct argument against trusting your own sense of "this is obviously documented well enough" when writing a handover package — the outgoing owner is structurally the worst-positioned person to judge whether their own explanation is adequate, precisely because they no longer notice which parts require explaining at all. Practical countermeasures:

- **Get a genuinely fresh reader**, not just another reviewer already familiar with the system, to walk through the handover material before treating it as done — the same instinct behind rotating newcomers through on-call and asking what looks strange to them before telling them what's "normal" (see [System Baseline for Troubleshooting](system-baseline-for-troubleshooting.md)).
- **Treat a reader's confusion as data, not a comprehension failure on their part.** If a competent recipient of a handover gets stuck on something the author considered obvious, that's a gap in the material, not a deficiency in the reader.
- **Watch for the same effect during live handover conversations**: an outgoing owner who says "that part's straightforward" about something the incoming owner visibly struggles with is exhibiting exactly this blind spot, not being unhelpful.

This blind spot is also an argument for [Reducing Documentation Need Through System Design](reducing-documentation-need-through-system-design.md) over relying on the author's own account of what needs explaining: a design that is *obscure* to outsiders but feels obvious to its builder cannot be reliably identified as obscure by that same builder, so the safer fix is to reduce actual obscurity in the system rather than trust the author's judgment about how much prose it needs.
