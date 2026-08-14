---
type: concept
title: Checklist Execution as Team Communication
description: Running an operational checklist as a spoken, team-led ritual rather than a silent solo paperwork exercise, including who has authority to invoke it.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 7"
---

A checklist's value depends heavily on *how* it is executed, not just what it contains. Two execution-design choices determine whether a checklist actually surfaces problems or becomes a box-ticking formality that an unfamiliar or junior operator is afraid to interrupt.

## Distributed Authority to Invoke the Checklist

Assign the authority to initiate and pace the checklist to a role other than the most senior or highest-authority person present (e.g. a supporting operator rather than the lead). This mirrors the aviation "pilot not flying" pattern:

- It empowers team members who would otherwise defer silently to a senior operator's judgment.
- It decentralizes the responsibility for catching a missed or skipped step — the person running the checklist is not the same person whose action is being checked.
- It signals, structurally, that the checklist outranks any individual's seniority.

## Oral, Team-Based Execution

Conduct checklist items as a verbal exchange among the assembled team, not as one person silently reading and marking a form:

- Each item is spoken aloud and confirmed aloud by the relevant role, not just checked off.
- This turns the checklist into a shared moment of situational awareness for everyone present, not just a record-keeping artifact for the person holding it.
- It creates a natural opening for anyone on the team to flag a concern, because the checklist has already established that speaking up mid-procedure is the expected behavior.

## Distributed Authority Requires an Explicit Duty to Speak Up

Granting a non-lead role the authority to invoke a checklist is not enough on its own — that role must also understand that flagging a concern is a *duty*, not just a permission they may choose not to exercise. Teams where a subordinate is technically allowed to raise a doubt but doesn't believe they are obligated to still suffer the same failure as teams with no distributed authority at all: a senior operator's mistaken assumption goes unchallenged because no one felt it was their place, or their job, to stop and say so.

## Structured Briefings Enable Rapid Team Formation

Operators who have never worked together before can still form an effective, coordinated team within minutes if they run a structured introduction and briefing before the work begins: each person states their name and role, and the team walks through the plan and its likely contingencies together. This matters directly for handover and on-call staffing, where the operators responding to a given event are often not a team that has worked together before — the structured briefing substitutes for the shared history a long-tenured team would otherwise rely on.

## State the Execution Mode on the Document Itself

Designing a checklist to be executed verbally and by a distributed authority is not enough if the document itself doesn't say so. Left ambiguous, operators default to whatever is most convenient — typically, one person silently completing the checklist alone on paper before or after the fact, rather than running it as a live team conversation. An early draft of the WHO surgical checklist failed a field test for exactly this reason: nothing on the page indicated it was meant to be a verbal, team-run exercise, so the nurse using it reasonably defaulted to silent solo completion. State the intended execution mode explicitly and visibly on the checklist itself (who calls it, that it is read aloud, that responses are spoken back) — don't rely on training or verbal handoff to convey a protocol the document doesn't state.

## Why Both Matter Together

Distributing invocation authority and requiring oral confirmation reinforce each other: a checklist invoked by a junior role only works if the team also has a norm of speaking answers aloud rather than deferring to the loudest or most senior voice in the room. Designing one without the other weakens both — a silently-executed checklist still lets a senior operator's assumption go unchallenged, and a verbal checklist invoked by the senior operator still centralizes authority in the same person being checked.

A related technique for hand-off-prone steps is mandatory verbal read-back: the receiving operator repeats the instruction back aloud (rather than just acknowledging it) before acting on it, catching transcription and mishearing errors at the cheapest possible point. This is one layer in a broader [Layered Checklist System](layered-checklist-system-design.md) built from several purpose-specific checklists rather than one comprehensive list.

For the format (DO-CONFIRM vs. READ-DO) and pacing constraints these conversations happen within, see [Runbook and Checklist Design](runbook-checklist-design.md). For how to decide which items warrant this kind of team-forcing treatment, see [Checklist Item Selection Trade-offs](checklist-item-selection-tradeoffs.md).
