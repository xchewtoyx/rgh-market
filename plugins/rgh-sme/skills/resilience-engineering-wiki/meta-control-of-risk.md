---
type: concept
title: Meta-Control of Risk
description: >
  Resilience engineering's leverage is not predicting the next accident or
  bolting on more external controls, but making an organisation sensitive
  to whether the risk model it is already using is still valid — control of
  the control of risk.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 7"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 12"
---

Incident databases in ultra-safe systems hit a double limit that better
analysis cannot fix. First, in systems where accidents genuinely emerge from
[normal people doing normal work](studying-normal-work.md), the everyday
practices that actually precede catastrophe are never flagged as incidents
in the first place, so the database is structurally blind to them — the
mechanism [Wald's bomber paradox](walds-bomber-paradox.md) and [the Heinrich
triangle myth](heinrich-triangle-myth.md) already establish. Second, even
where reports do accumulate, mature reporting systems (NASA's Aviation
Safety Reporting System is the canonical case) become victims of their own
success: report volume grows past the point where recombining and
cross-referencing them can extract meaningful intelligence, so counting
reports gets mistaken for the actual goal, which is risk anticipation and
reduction — a second-order instance of [the information paradox of
high-safety systems](information-paradox-of-high-safety-systems.md): the
system that replaced accidents as a source of learning can itself succeed
its way out of being useful. Linear extensions of the standard toolkit — more rules, more
standardisation, more proficiency checks, more incident reporting — hit an
asymptote for exactly this reason: they are all still trying to solve a
recombinant-prediction problem that the system's own maturity has already
made unsolvable.

**The reframe: safe and unsafe operation are not different kinds of work.**
If success and failure arise from the same everyday adaptive processes (the
premise [Safety-II](safety-i-and-safety-ii.md) is built on), then a
dedicated "accident model" applied only after something goes wrong has
limited leverage, because it studies a different population of behaviour
than the one that actually produces outcomes day to day. The useful object
of study is not accidents at all — it's the organisation's *model of its own
risk*, and specifically how sensitive that model stays to evidence that it
has stopped matching reality.

Commercial aviation is the sharpest illustration of the asymptote itself:
safety improved for decades to a baseline around one accident per million
flights (Boeing's 2005 figures — roughly 1.09 billion passengers on 18
million flights, 20 fatal accidents in 2000 — put flying some twenty-two
times safer per passenger-mile than driving), and then the improvement
curve went flat. Airlines individually lack the internal resources — time,
spare analytic capacity, a mandate outside daily operations — to originate
a new safety paradigm on their own; the asymptote is a structural ceiling on
what the existing paradigm's own toolkit can deliver, not a sign that
airlines have simply stopped trying.

This gives resilience engineering's leverage point a name: **control of the
control of risk**, or meta-control. Rather than adding another external
layer of risk control (another barrier, another rule, another audit), the
target is the validity of the risk-control apparatus the organisation
already has — does it still track how the organisation actually creates
safety, or has the world underneath it moved while the model stayed fixed?
Different industries default to structurally different risk paradigms —
nuclear power's barriers and defence-in-depth insulate the system behind
protective walls; aviation runs a largely reactive "fly-fix-fly" loop built
on overlapping event reports; military systems use proactive, top-down
hazard analysis aimed at an active adversary — and meta-control is
paradigm-agnostic: whichever paradigm an organisation runs, the question is
whether the organisation is watching its own paradigm's validity, not just
executing it.

**Safety boundaries are themselves a product of this same model, not an
independent physical fact.** They cannot be nailed down as hard,
deterministic lines that exist prior to an accident — they exist as
indeterministic probability patterns that shift with operational
conditions, and what gets mapped as "the boundary" at any moment is a
projection of the organisation's *current* risk model, not a
realist entity waiting to be discovered. This is why mapping a boundary
credibly requires sociological and ethnographic methods — surfacing
insiders' actual beliefs, perceptions, and daily adaptive behaviour — rather
than calculative engineering metrics alone; [Rasmussen's three-boundary
space](rasmussen-boundary-model.md) is the structural picture this fills in
epistemically.

**Predicting the next accident and managing the aftermath of one share the
same cognitive demand.** Both require retreating from the
organisation's existing understanding of its own system, confronting [the
gap between work-as-imagined and work-as-done](work-as-imagined-vs-work-as-done.md)
honestly, abandoning safety beliefs that have gone stale, and recalibrating
the risk model itself — which is exactly the meta-control move this note
describes. An organisation that only does this recalibration reactively,
after an accident forces it, is capable of the same work proactively; it is
choosing not to.
