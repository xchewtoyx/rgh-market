---
type: concept
title: Premortem Risk Analysis
description: >
  Before executing a risky change, imagine it has already failed and work
  backward to explain why, which surfaces failure modes a straight review
  of the plan tends to miss because the plan's authors are invested in it
  succeeding.
sources:
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Klein), ch. 5"
  - title: "Thinking in Bets"
    resource: "Thinking in Bets: Making Smarter Decisions When You Don't Have All the Facts (Duke), ch. 6"
---

# Premortem Risk Analysis

Asking the people who built a change plan to review it for flaws tends to
get only half-hearted scrutiny: having just constructed the plan, they are
emotionally invested in its succeeding, and mental simulation of one's own
plan is prone to explaining away warning signs rather than surfacing them
(the same overconfidence that makes people "fall in love with" a
completed plan once it's built).

The premortem inverts the framing to break that attachment: instead of
asking "what could go wrong with this plan?", tell the group to assume
it's some time in the future, the change has already been made, **and it
has failed** — then ask each person to explain why, as if narrating a
postmortem that already happened. This reframes the exercise from
defending a plan (which people resist) to a creativity and competence
challenge (finding smart, specific failure stories), which people engage
with far more readily. It takes only minutes to elicit a first round of
imagined failure causes, though the resulting discussion can run much
longer, and it reliably surfaces risks a straight "any objections?" review
of the same plan would not.

This is a lightweight, general-purpose complement to the more structured,
checklist-driven review that a [launch readiness review](launch-readiness-review.md)
performs for major launches — a premortem can be run on any risky change
(a migration, a large batch release, an irreversible cutover) in a single
short meeting, without needing the full cross-team audit machinery a
launch review implies. It is also a natural exercise to run specifically
on the [rollback vs. roll-forward](rollback-vs-roll-forward.md) plan
itself: imagining the rollback has already been attempted and failed
tends to surface exactly the untested-rollback-path risk that plan
reviews otherwise miss.

The premortem is the negative-space complement to **backcasting**
(imagining the change has already succeeded and working backward to the
steps that got there): planning tends to over-represent the positive
case by default, and running a premortem alongside (or instead of) a
purely forward-looking rollout plan corrects that optimism bias.
Research on this pairing (Gabriele Oettingen's "mental contrasting"
studies, cited in *Thinking in Bets* ch. 6) found that people who
vividly imagined only a positive outcome performed measurably *worse*
at achieving it than people who also confronted concrete obstacles —
evidence that rehearsing failure modes in advance is not merely
reassuring but functionally improves execution, not only review
quality.
