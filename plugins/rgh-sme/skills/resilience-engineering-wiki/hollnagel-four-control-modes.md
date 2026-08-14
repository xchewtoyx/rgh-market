---
type: concept
title: Hollnagel's Four Control Modes (COCOM)
description: >
  How much time and predictability an actor has determines which of four
  qualitatively different control modes they operate in — strategic,
  tactical, opportunistic, or scrambled — and each mode change downgrades
  planning horizon and effectiveness together, not independently.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 15"
---

Hollnagel's Contextual Control Model (COCOM) names four modes an actor —
an individual, a team, or an organisation — can be operating in, ordered by
shrinking planning horizon and predictability:

| Mode | Planning horizon | Characteristic behaviour | Condition |
| :-- | :-- | :-- | :-- |
| **Strategic** | Wide | Considers higher-level goals, task interdependencies, multi-goal trade-offs; runs on feedforward models of what's coming. | High predictability, ample time |
| **Tactical** | Mid-range | Follows known rules and procedures; planning is bounded and ad hoc rather than forward-looking. | Moderate predictability |
| **Opportunistic** | Short | Action selection driven by whatever context feature is most salient right now; minimal anticipation; heavy trial and error. | Low predictability, high stress |
| **Scrambled** | None | Action selection is effectively irrational or random; situation assessment is paralysed. | Severe disturbance, loss of control |

**The modes are not independent design choices — they are what deteriorates
together as time and predictability shrink.** An actor does not choose
scrambled mode; they are pushed into it by [lack of
time](resilience-as-control.md) and a collapsing predictive model, the same
"lack of time" constraint that mechanism names as one of the four ways
control is lost generally. Moving down the mode ladder is what [running out
of the abstract, goal-level guidance a fixed procedure cannot
supply](matching-response-abstraction-to-uncertainty.md) looks like from
inside the actor doing it: strategic and tactical modes can still use
goal-level and process-level guidance, while opportunistic and scrambled
modes have degraded past the point where any pre-written guidance, however
abstractly written, still applies.

**A concrete organisational state-transition case ties the mode ladder
directly to [the healthy/unhealthy/catastrophic state
triad](state-space-model-of-organizational-functioning.md).** Barings plc's
1995 collapse traces cleanly onto the four modes at organisational scale:
the firm's healthy state ran on strategic and tactical control; its slide
into an unhealthy state (ignored balance-sheet warnings, escalating margin
calls approved without inquiry, missing data going unaudited) showed a mix
of tactical and opportunistic control, where recovery was still possible
if external conditions stayed favourable; and its catastrophic collapse
into insolvency was accompanied by fully scrambled control — situation
assessment paralysed, funds transferred without any coherent plan, right up
to the point recovery became impossible. The mapping matters diagnostically:
an organisation's control mode at a given moment is itself a leading
indicator of which state it is sliding toward, readable before the state
transition itself completes — see [decompensation](decompensation.md) for
the mechanism by which a system can look stable on its output right up
until a mode collapse like this becomes visible.
