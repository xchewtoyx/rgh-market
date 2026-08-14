---
type: concept
title: Joint-Ownership Decision Budget
description: >
  Converting a recurring cross-team disagreement into a
  pre-agreed, quantitative threshold turns each future
  occurrence into an automatic, defensible decision instead
  of a fresh negotiation.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Beyer, Jones, Petoff, Murphy), ch. 3"
---

Some decisions recur constantly between the same two parties
with structurally opposed incentives — one side wants to move
fast, the other wants to hold the line on quality or risk.
Renegotiating that trade-off case by case is expensive and
produces inconsistent, hard-to-defend outcomes.

The fix is to jointly own a single quantitative budget that
both parties agree to in advance, then let it decide future
cases automatically: an explicit ceiling on how much of the
contested resource (downtime, spend, risk exposure) may be
consumed before the decision flips from "proceed" to
"freeze and redirect effort to fix the underlying problem."
Because both parties negotiated and accepted the threshold
before any specific case existed, neither party is imposing
its will on the other when the threshold triggers — the
budget itself made the call.

This differs from
[desired-result-as-decision-criterion](desired-result-as-decision-criterion.md)
in scope: that concept judges alternatives against a target
for a single decision, while a joint-ownership budget is a
standing policy that pre-resolves an entire recurring class of
decisions, the same way
[judgment-pre-commitment](judgment-pre-commitment.md)
pre-resolves a single meeting's judgments. It also sidesteps
[consensus-driven-paralysis](consensus-driven-paralysis.md):
the parties reach consensus once, on the rule, rather than
attempting it anew on every instance the rule will ever cover.

**Graduated override, not a free exception.** A budget policy
still needs a release valve for genuinely urgent cases, but a
free, ad hoc exception ("just this once") erodes the whole
mechanism — the next request feels equally urgent, and the
threshold stops meaning anything. A **thaw tax** keeps the
valve without that erosion: an override is allowed, but it
costs more of the budget than it saves — e.g. one day of early
unfreeze costs one and a half days added back to the freeze
period. This forces whoever wants the exception to weigh its
urgency against a real, quantified cost, rather than treating
"just this once" as free, and preserves the policy's teeth
through its first real test (see
[stakeholder-buy-in-sequencing](stakeholder-buy-in-sequencing.md)
on why that first test matters more than the sign-off that
created the policy).
