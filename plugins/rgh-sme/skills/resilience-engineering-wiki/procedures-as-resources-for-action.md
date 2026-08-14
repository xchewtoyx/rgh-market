---
type: concept
title: Procedures as Resources for Action
description: >
  The New View of procedures — not the safest prescribed way to work but
  flexible resources whose safe application is itself a complex cognitive
  skill, resting on design assumptions real work routinely violates.
sources:
  - title: The Field Guide to Understanding 'Human Error'
    resource: "The Field Guide to Understanding 'Human Error' (Dekker), ch. 4"
  - title: The DevOps Handbook
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 3"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 12"
---

Procedural design quietly assumes three things about work (Loukopoulos et
al., 2009), all routinely false:

1. **Linearity/seriality** — tasks occur sequentially, without parallel
   demands or interruptions.
2. **Predictability** — all information a step needs is fully and
   unambiguously available when the step executes.
3. **Controllability** — operators control task timing, pacing, and
   attentional focus.

Because real work violates these assumptions, following a procedure is never
simple IF–THEN execution. The two models of procedures:

| Model 1 (Old View) | Model 2 (New View) |
| :-- | :-- |
| Procedures are the safest, best-designed way to work | Procedures are flexible resources for action |
| Procedure-following is simple IF–THEN execution | Applying a procedure is a complex cognitive skill |
| Safety comes from strict compliance | Safety comes from skill in judging when and how rules apply |
| Enforce compliance to improve safety | Monitor and understand the gap between rules and practice |

Model 2 explains why compliance and safety are not the same thing: the
substantive safety work is the judgment that adapts written guidance to the
actual situation — the standing gap between
[work-as-imagined and work-as-done](work-as-imagined-vs-work-as-done.md).
Perfectly literal compliance can itself be unsafe (work-to-rule actions
paralyse operations precisely by withdrawing this adaptive judgment), while
sensible adaptation is invisible until an outcome invites hindsight to
rename it "violation".

Consequences:

- The management response to rule/practice gaps is to *monitor and
  understand* them, not to enforce them away — enforced-but-unworkable rules
  drive practice underground and feed [procedural
  drift](procedural-drift.md).
- After an incident, a "procedure not followed" finding is a description of
  normal work, not an explanation of the outcome; ask what the procedure's
  false assumptions left the operator to handle ([local
  rationality](local-rationality-principle.md)).
- Rigid stop-rules read by operators as negotiable parameters (altitude
  gates in [plan continuation](plan-continuation-bias.md)) are Model 1
  artefacts colliding with Model 2 reality.

Dekker states the underlying reason Model 1 cannot be rescued by writing
better checklists: in a genuinely [complex system](complicated-vs-complex-systems.md),
doing the same thing twice will not predictably yield the same result. Static
checklists and best practices stay valuable, but they are insufficient *alone*
to prevent or manage failure, because no fixed sequence of steps can be
written in advance for a situation whose relevant conditions have not
recurred identically before — the skill Model 2 locates in the practitioner
is exactly the judgment that compensates for that non-repeatability.

**A regulatory instance of Model 1 baked into policy**: airline quality
management regimes (e.g. JAR-OPS) formally assume that auditing compliance
against the manual — inspecting whether procedures were followed — is
equivalent to auditing safety itself. The assumption is premised on an
idealised world of perfect procedures, full operational certainty, and zero
unexpected conditions, and it ignores that complex, dynamic operations
routinely require sharp-end operators to improvise and make goal trade-offs
as normal work. A regulator built on this assumption cannot see the Model 2
work that actually produces the airline's safety record, because its audit
instrument is designed to measure Model 1 conformance only.
