---
type: concept
title: Mental Simulation as an Evaluation Tool
description: The technique of imagining a course of action playing out step by step to find its flaws before committing to it, including the premortem method for doing this deliberately.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 5"
---

**Mental simulation** is how a decision-maker evaluates a single option
without anything to compare it against (the mechanism behind [singular
evaluation in the recognition-primed decision
model](recognition-primed-decision-model.md)): imagine carrying the option
out as a sequence of steps, and let problems surface as imagined failure
points. A firefighter mentally walking through an unconventional car-rescue
method before ordering it, step by step, is doing this; so is an incident
commander silently running a rollback plan forward in their head before
calling it.

Empirically, people build these simulations like assembling a small
machine with a hard capacity limit: **around three moving parts and about
six transition steps**, rarely more — plausibly a working-memory
constraint. Two consequences follow directly:

- **Chunking** lets an experienced person compress several transitions into
  one step (treating "roll back the deploy" as a single unit rather than
  simulating every sub-step of it) — freeing capacity to simulate the parts
  that actually need scrutiny. This requires real domain familiarity;
  without it, people either omit real complexity or exhaust their capacity
  partway through.
- **Interacting parts cost more than independent ones**, because tracking
  an interaction means holding both parts and their relationship in mind at
  once. A plan is easier to mentally rehearse when its steps run in a
  straight line than when they interact with each other.

A simulation that completes without hitting a snag is not proof the plan is
sound — only that the imagined version of it works. The car-rescue example
this technique is drawn from succeeded; the earlier harness-rescue example
in the same source material failed for a reason the simulation never
surfaced (the rescue harness couldn't be cinched tight enough on a slight,
unconscious victim) — mental simulation reliably finds imaginable problems,
not unimaginable ones.

## The premortem: forcing the simulation deliberately

People who have just finished building a plan become invested in it and
review it for flaws half-heartedly. The **premortem** technique breaks that
attachment by reframing the task: assume the plan has already been carried
out and has failed, and ask participants to explain why — "of course it
wasn't going to work, because..." This turns plan review from a
defense exercise into a competence/creativity exercise (who can find the
smartest failure mode), and reliably surfaces problems that a straight
"any concerns with this plan?" review misses. It takes under ten minutes to
run and is well suited to a new-project kickoff, an [incident action
plan](star-incident-action-plan.md) before executing a risky mitigation, or
a [game day](preparedness-drills.md) scenario design session — a mission-
rehearsal study found that of twenty teams none had asked "what do we do if
we arrive early or late," a contingency a premortem specifically forces
into the open.

A related technique for building genuine buy-in to an unwelcome
possibility: present **three** distinct scenarios rather than one plan plus
one alternative. Two scenarios differing on a single dimension tend to get
"split the difference" rather than genuinely considered; a third,
structurally different scenario forces people to actually update their
mental model instead of averaging away the disagreement. This is the
technique Shell's planning department used to get executives to take a
coming oil-price shock seriously years before it happened, and it
generalizes directly to preparing an organization for possible incident
scenarios that don't fit its default assumptions.
