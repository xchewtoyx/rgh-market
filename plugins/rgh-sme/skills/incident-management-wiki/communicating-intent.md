---
type: concept
title: Communicating Intent
description: Why telling a delegate the purpose behind a task, not just the steps, is what lets them improvise correctly when the situation stops matching the plan.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Gary Klein), ch. 13"
---

Delegating a task by specifying only the steps to follow works exactly as
long as conditions match what the planner anticipated — the moment they
don't, the person executing the steps has no basis for adapting, because
they were never told what the steps were *for*. A well-documented military
finding makes this concrete: when battalion commanders described how they
expected subordinates to react to an unforeseen development, the
subordinates' actual planned reaction matched only about a third of the
time — despite standardized intent-communication procedures both sides had
practiced for months. In a studied cockpit case, a captain gave a
correctly-worded instruction to rebalance fuel between tanks; the flight
engineer heard it clearly but, not understanding *why*, reinterpreted it
through his own narrower role (fuel conservation) and executed something
different — landing with a wing-weight imbalance five times the safe
maximum, in a version of the incident where the mismatch was never even
caught.

Klein's inventory of seven facets worth conveying when handing off a task
— useful as a checklist, not a mandatory script — names exactly the
information that's missing when delegation goes wrong this way:

1. **Purpose** — the higher-level goal this task serves. The single most
   commonly omitted facet in practice, and the one whose absence causes the
   most damage, because everything else can be reconstructed from it but
   it can't be reconstructed from anything else.
2. **Objective** — a concrete image of what "done" looks like, not just a
   restated task name.
3. **The plan** — the intended sequence of steps. Ironically the
   over-specified facet: teams tend to spell this out in the most detail
   while omitting purpose, which produces confident-sounding delegation
   that still fails the moment reality diverges from the plan.
4. **Rationale** — why this particular plan, not another. Sharing it does
   double duty: it builds understanding, and it invites the delegate to
   propose a better plan if they see one.
5. **Key decisions to anticipate** — contingencies and priorities the
   requester already expects might come up, including known weak points in
   the plan, so the delegate recognizes early signs of it breaking down
   rather than discovering that only in hindsight.
6. **Antigoals** — explicitly unwanted outcomes, worth stating specifically
   when there's a real risk of a plausible-but-wrong path (e.g., "do not
   get pulled into a side investigation" for a responder assigned to one
   narrow piece of an incident).
7. **Constraints** — real-world limits and extra considerations the
   delegate wouldn't otherwise know to weigh.

The right amount of detail to give depends on who's receiving it: an
experienced [SME](sme-conduct-during-incidents.md) needs mostly the purpose
and objective and can be trusted with the rest; someone less familiar with
the domain needs the plan spelled out more explicitly too. Over-specifying
for an experienced delegate reads as micromanagement and removes exactly
the room to improvise that communicating intent is supposed to create — a
delegate told the fixed sequence but not the goal can only ask "is this
what you wanted?" and wait for permission, rather than adapting on their
own when the field situation stops matching the plan.

This is the same gap a [CAN report](can-report.md) and a clear [incident
action plan](star-incident-action-plan.md) are meant to close during a
live response: a directive that only names the task ("run this rollback")
leaves a responder unable to judge whether a change in conditions still
serves the goal, while one that also states the objective and rationale
("we're rolling back because X is the suspected cause and we need to
confirm that before Y") lets them recognize on their own if the rollback
stops making sense partway through. The same principle applies to an
automated system reporting its own status: a system that silently
compensates for a problem without surfacing what it's doing leaves human
responders with no way to anticipate what happens when its compensation
capacity runs out — the same blindness a human delegate experiences when
never told the purpose behind an instruction.
