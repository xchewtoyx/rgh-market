---
type: concept
title: Proactive Monitoring as a Control-Loop Redesign
description: >
  Classical safety control only updates policy after an outcome fails;
  proactive monitoring inserts intermediate process and environmental
  indicators directly into the feedback loop so control action can happen
  before the outcome is compromised.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 5"
---

Wreathall frames the difference between reactive and proactive safety
management as a difference in where a feedback loop's sensor sits, not just
a difference in attitude. The classical model runs: Process → Outputs →
Model of Process → Controller → Inputs. Its only sensor is the output
itself — accident and injury rates, "days without an incident" — so policy
stays static until a major output failure occurs, at which point management
investigates retrospectively and bolts on a new barrier. This has four
compounding weaknesses, independent of and additional to [why lagging
outcome metrics generally mislead](heinrich-triangle-myth.md): top-level
outcome events carry heavy stochastic noise, so a good or bad run is weak
evidence either way; an outcome event carries no diagnostic information
about *which* underlying process produced it; a long run of good outcomes
breeds complacency and pressure to underreport marginal occurrences rather
than "lose the game"; and because the organisation and its environment keep
changing, a historical outcome record is a poor basis for judging today's or
tomorrow's risk regardless of how good the record is.

The proactive model keeps the same loop but inserts **candidate
indicators** — data streams read directly off intermediate stages of the
process itself, and off shifts in the external environment (raw-material
costs, customer demand, regulatory change, credit conditions) — feeding
straight into the process model and controller, ahead of the output stage.
This is a structural change, not a philosophical one: it moves the sensor
from *after* the point where damage is done to *before* it. This is also
the mechanistic answer to what [resilience as
control](resilience-as-control.md) names as the "lack of time" constraint —
a purely output-driven loop is structurally always behind events by
definition; moving the sensor upstream is literally how that constraint gets
relieved.

The subtlest of these upstream signals are **faint signals** (Westrum,
1999): early, weak hints of emerging trouble — an uptick in customer calls
asking for clarification, say — that are almost never recognised as warnings
until after a failure has already made their significance obvious in
hindsight. Faint signals are this chapter's version of the same object
[ambiguous threats](ambiguous-threats.md) describes: whether one gets
investigated or dismissed depends on the organisation's operating mindset,
not on the signal's inherent strength, which is fixed and genuinely weak
either way.

A related but distinct sensor-integrity question is not *when* in the
process an indicator is read but *who controls* the party being measured:
see [segregation of duties as a control
barrier](segregation-of-duties-as-a-control-barrier.md) for what happens
when the same actor controls both the risky action and the report on it.

See [criteria for selecting safety
indicators](criteria-for-selecting-safety-indicators.md) for how a candidate
indicator is chosen and grounded once this architecture is in place, and
[leading and lagging indicators are level-relative](leading-vs-lagging-indicators-are-level-relative.md)
for why "proactive" and "reactive" turn out not to be fixed properties of a
given metric. Once the sensor sits upstream, a separate design question
follows: on what cadence does monitoring actually run — see [four monitoring
cadence modes](monitoring-cadence-modes.md) for continuous, probe,
proactive, and reactive tracking as distinct, complementary answers.
