---
type: concept
title: Tactical/Strategic Decision Split with a Liaison
description: >
  When a decision's stakes outgrow one decision-maker's span of
  control, split it into a tactical layer that executes and a
  strategic layer that sets direction, connected by a liaison whose
  only job is shuttling information between them.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 5"
---

A single decision-maker can hold either the tactical detail needed to
execute or the cross-cutting business context needed to weigh
options against organizational priorities — but past a certain scale
of stakes, not both at once, and trying to do both slows both down.
The pattern that scales: split decision authority into two explicit
layers. A tactical layer keeps directing the people doing the work
and stays focused on execution. A strategic layer — convened only
once the decision's consequences cross into territory the tactical
layer isn't chartered to weigh (legal exposure, cross-team tradeoffs,
customer-facing commitments, reputational risk) — sets direction and
picks between options the tactical layer presents, without trying to
run the execution itself.

**A liaison, not a channel, connects the two layers.** The liaison's
job is narrow and specific: stay current enough on the tactical
picture to deliver a status briefing on demand, carry the strategic
layer's questions back down, and carry answers back up — without
ever making a decision on either layer's behalf. This matters because
it lets the tactical decision-maker stay fully engaged with execution
instead of context-switching into briefing mode themselves every time
the strategic layer needs an update, and it lets the strategic layer
get a consistent, single-sourced picture instead of noisy direct
access to everyone doing the work.

**The framing that makes the split land**: presenting the strategic
layer with a menu ("here are two viable paths, here are the tradeoffs
of each, which do you want") rather than a status report keeps the
division of labor honest — the strategic layer is choosing a
direction, not being asked to solve the technical problem, and the
tactical layer retains ownership of everything below that choice.

This is a scaling companion to
[sponsorship-versus-mandate](sponsorship-versus-mandate.md) and
[multi-party-decision-contracts](multi-party-decision-contracts.md):
those establish who must agree, be informed, or hold veto power over
a decision in general; this pattern is what to do once that set of
parties has grown too large or too senior for a single decision-maker
to brief and coordinate directly. It also gives
[escalating-unresolved-disagreements](escalating-unresolved-disagreements.md)
a durable structure to escalate *into*, rather than a one-time event —
the strategic layer, once convened, stays available for the rest of
the decision's lifetime, not just the moment it was first needed.
