---
type: concept
title: Complicated Systems Become Complex Once Fielded
description: >
  A complicated system (many parts, but exhaustively describable by its
  designer) turns complex (not exhaustively describable even in principle)
  the moment it is released into an open, changing operating environment.
sources:
  - title: "Drift into Failure: From Hunting Broken Components to Understanding Complex Systems"
    resource: "Drift into Failure (Dekker), ch. 6"
---

**Complicated** systems — an airliner, a piece of certified software — have
huge numbers of interacting parts but are, in principle, exhaustively
describable. They typically have a designer who tested and specified every
interaction (even if imperfectly), so reductionism remains a workable
strategy for understanding them: open it up, trace the parts, you get the
whole. **Complex** systems cannot be exhaustively modelled even in
principle, because their behaviour depends on an open, changing environment
no designer can enumerate in advance.

The line between the two is not fixed to a type of artefact — it moves with
context. A system engineered as merely complicated becomes complex once it
is fielded, because fielding exposes it to interactions its design process
could never have enumerated:

- **Software state-space explosion**: a collision-avoidance system with a
  million lines of code can have on the order of 10^40 possible states —
  formally designed, yet no longer exhaustively testable against every
  real-world scenario it will encounter.
- **Regulatory and organisational drift**: a part's physical wear might be
  fully predictable from materials science, but the maintenance interval
  actually applied to it over decades depends on deregulation,
  reorganisation, and [decrementalism](decrementalism.md) that could never
  have been modelled at design time.
- **Cross-cultural fielding**: a cockpit or control-room interface embeds
  the language and hierarchy assumptions of its designers; deployed into a
  different culture's communication norms, the same artefact produces
  behaviour its designers never anticipated and could not have tested for.
- **Undocumented design assumptions outliving their documentation**: a
  hard-wired design choice (which sensor feeds which subsystem) made for
  reasons specific to an earlier hierarchy or technology generation can
  persist for decades after training materials stop mentioning it, becoming
  an invisible trap for anyone reasoning from current, incomplete
  documentation.

The practical consequence: certification, testing, and specification
compliance establish that a system is complicated and well-understood at the
point of design — they say nothing about whether it will stay well-understood
once operating, because operating is exactly what converts it into a complex
system. This is why [unruly technology](unruly-technology.md) and [sensitive
dependence on initial conditions](sensitive-dependence-on-initial-conditions.md)
keep surfacing in systems that passed every design-time check: the checks
were checking the complicated system, not the complex one it became.

A related but distinct taxonomy sorts *tasks* rather than *artefacts* into
[simple, complicated, and complex problems](simple-complicated-complex-problem-taxonomy.md):
where this note tracks one system's migration across the complicated/complex
line over its lifetime, that taxonomy diagnoses which of three difficulty
tiers a given task belongs to right now, and warns against applying a
technique matched to the wrong tier.
