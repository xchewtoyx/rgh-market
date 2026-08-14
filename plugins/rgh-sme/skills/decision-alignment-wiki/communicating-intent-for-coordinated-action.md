---
type: concept
title: Communicating Intent for Coordinated Action
description: >
  State the underlying purpose behind a decision or instruction,
  not just the plan, so the people carrying it out can improvise
  correctly when reality departs from what was anticipated.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 13"
---

A decision or instruction that specifies only the plan — what to
do, step by step — leaves the executor unable to do anything except
follow the plan literally, which fails the moment reality departs
from what the plan anticipated. Two people can hear the identical
instruction and act on it completely differently once conditions
change, because only the instruction's *literal content* transferred,
not its underlying purpose: a cockpit crew told to move fuel between
tanks "for balance" complied only when the engineer eventually
understood *why*, and in one recorded case never did understand it,
producing a landing far outside safety limits despite the crew
having heard and technically complied with every word said to them.
The fix is not more precise wording of the plan — it is stating the
**purpose** underneath it, so the plan itself becomes something the
executor can adapt rather than something they can only obey or fail.

A contrasting pair makes the mechanism concrete: asked to order a
replacement part, one requester cited an old purchase order to
remove all ambiguity about which item was wanted — and still got
the wrong part, because the fulfiller, lacking domain knowledge,
filled the literal gap (the same *vendor*) rather than the actual
need (a part *compatible with this machine*) once the exact original
item was unavailable. Another request, given with almost no explicit
instruction at all but to someone who already understood the
requester's priorities, was carried out correctly including a
judgment call the requester never anticipated needing. Specifying
the plan more tightly does not substitute for the executor
understanding *why* — if anything, it invites literal compliance
with a plan that no longer fits.

**Seven facets worth checking when stating intent for a decision or
instruction meant to drive action** (used as a checklist, not a
mandatory template — some facets legitimately don't apply):

1. **Purpose** — the higher-level goal this serves, and why it
   matters. The single most commonly omitted facet in practice, and
   the one whose absence causes the most damage, because everything
   else can be reconstructed from it but it cannot be reconstructed
   from anything else.
2. **Objective** — a concrete image of what success looks like when
   complete, not just the category of action ("defend this
   position") but the actual completed state.
3. **The plan** — the intended sequence of steps. This is the facet
   people habitually over-specify, often at the direct expense of
   purpose and rationale — a fully detailed plan with no stated
   purpose is precisely what produces literal, brittle compliance.
4. **Rationale** — why this plan, specifically, was chosen. Sharing
   it does double duty: it aids comprehension, and it invites the
   executor to propose a better plan when they notice something the
   planner didn't (see
   [walk-stakeholders-through-the-reasoning](walk-stakeholders-through-the-reasoning.md)
   for the same effect applied to a whole recommendation, not just an
   instruction).
5. **Key decisions and contingencies to anticipate** — where the
   plan is most likely to need a judgment call, or to start breaking
   down, flagged in advance so the executor recognizes it happening
   rather than discovering it only in hindsight.
6. **Antigoals** — outcomes to explicitly avoid, stated only where a
   real, plausible-but-unwanted alternative exists (restating the
   main goal in negative form adds nothing).
7. **Constraints** — other conditions or considerations that bound
   how the plan can be adapted.

Calibrate depth to three things: how experienced the executor is
(more experience needs less plan detail and more purpose); how
stable the situation is (a fast-changing situation makes antigoals
and contingencies premature to fix in detail); and how well-defined
the goal itself is (an ill-defined goal needs more attention to
anticipated decision points, since the target image may itself keep
evolving).

This is the mechanism that makes
[line-ownership-of-implementation](line-ownership-of-implementation.md)
actually work in practice: an owner who understands the intent
behind a decision can adapt it to field conditions the decision
document's authors never anticipated, rather than either freelancing
disconnected from the goal or stalling for clarification at the
first surprise. It also supplies the missing half of
[implementation-context-in-recommendations](implementation-context-in-recommendations.md):
naming the organizational context a recommendation must navigate is
necessary but not sufficient if the recommendation still fails to
say why the specific recommended path was chosen over the
alternatives.
