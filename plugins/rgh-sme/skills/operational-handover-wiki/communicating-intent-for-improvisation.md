---
type: concept
title: Communicating Intent for Improvisation
description: A handover or instruction that states only the steps to follow leaves the recipient unable to adapt correctly when reality deviates from the plan; stating the underlying purpose is what lets them improvise instead of guessing.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power (Klein), ch. 13"
---

No plan, procedure, or handover document can anticipate every situation its recipient will actually encounter. When conditions inevitably diverge from what was written, whether the recipient can adapt correctly depends on whether they understand *why* the plan called for what it called for — not just what it called for. A recipient who only has the steps has no way to tell whether an unexpected situation is one where the letter of the instruction still applies, or one where following it literally would defeat its own purpose.

## Two Failure Modes, Same Root Cause

- **Reasonable literal compliance that misses the point**: a request specifying *what* to do without *why* gets carried out in a way that technically satisfies it but fails the actual need — the requester is left protesting "you knew what I meant," to which the honest answer is that they didn't, because it was never said. A request for "the exact same part as this old order" without the underlying reason ("something inexpensive that's compatible with this machine") produces a wrong substitute the moment the original item is unavailable, because the fulfiller had no rationale to fall back on once the literal reference broke down.
- **Reflexive divergence from an unstated goal**: an instruction is followed but reinterpreted through the executor's own narrower frame because the requester's actual goal was never made explicit. A request to route all engines onto one fuel tank, given without explaining that the real goal is correcting a lateral weight imbalance (not fuel conservation), gets resisted or countermanded by someone applying their own default priority instead — not from insubordination, but because the instruction genuinely didn't communicate what it was for.

## What to Include Beyond the Steps

A request, order, or procedure communicates intent robustly when it covers, as needed for the situation:

- **Purpose** — the higher-level goal the task serves, not just the task itself. This is the single most commonly missing element even in organizations that formally require intent statements.
- **Objective** — a concrete image of what success actually looks like, not just an activity description.
- **Rationale** — why this particular plan was chosen, which both aids comprehension and invites a better plan from someone closer to the ground if conditions have shifted.
- **Key decisions and contingencies to anticipate** — the branch points where the plan is most likely to need adjustment, so the recipient recognizes them when they arrive instead of only realizing in hindsight that a decision was needed.
- **Antigoals** — outcomes to explicitly avoid, when there's a real risk of drifting into a plausible-but-unwanted alternative that satisfies the literal instruction while missing the point.
- **Constraints** — genuine limits or hazards the recipient should keep in mind but that don't belong in the main plan.

Deliberately not on this list: fully specifying the plan's every step. That is the element most instructions already over-invest in, often at the expense of the others — a fully detailed sequence of steps, absent purpose and rationale, is exactly the shape that produces both failure modes above.

## Calibrating How Much to Say

More intent-communication is not always better. How much of the above to spell out depends on:

- **The recipient's experience level** — a more experienced recipient needs only the higher-level goal and can be trusted to fill in the plan; a less experienced one needs more of the concrete steps spelled out because they lack the background to derive them from purpose alone.
- **How stable the situation is** — in a fast-changing situation, committing to specific antigoals or contingencies too early can be actively misleading if priorities are likely to shift before they're relevant.
- **How well-defined the goal itself is** — a genuinely ill-defined goal deserves more attention to the key-decision-points element, since the image of a successful outcome may itself change as work proceeds.

Shared history between the people involved substitutes for a lot of this: the more a recipient already knows how the requester tends to think, the less needs to be spelled out explicitly, because they can correctly infer the missing purpose and rationale from context alone.

## Why This Matters for Handover

This is the piece that [Playbook Required Content Elements](playbook-required-content-elements.md)'s "how" and "when" don't cover on their own: knowing the technical steps and the trigger condition for a procedure still leaves an operator unable to improvise when the actual situation doesn't cleanly match the documented trigger. A handover that hands over the steps without the purpose behind them produces an operator who can execute the runbook exactly as written and still make the wrong call the first time reality doesn't match the page — because they were never told what the runbook was actually for.
