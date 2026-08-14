---
type: concept
title: The Law of Stretched Systems
description: >
  Every system is operated at the limit of its current capacity, so any gain
  from a technological or organisational improvement gets consumed by
  increased tempo, scope, or complexity rather than banked as slack.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 2"
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 11"
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 18"
---

Woods's law of stretched systems: every system is stretched to operate at
its capacity, so any advance — a faster tool, a process improvement, an
efficiency win — gets consumed by doing more, doing it faster, and doing it
in more complex ways, rather than being kept as reserve capacity. The gain is
real but it never shows up as slack; it shows up as a new, higher baseline of
throughput and complexity that the system is now stretched against in turn.
This is the mechanism behind the observation in [resilience as adaptive
capacity](resilience-as-adaptive-capacity.md) that resilience is routinely
traded away for measured productivity without anyone deciding to make that
trade: the trade is not a decision at all, it is what happens automatically
to any freed-up capacity under standing [production
pressure](goal-conflicts-and-production-pressure.md).

**NASA's "Faster, Better, Cheaper" (FBC) programme** is the canonical case.
Investigated after the loss of the Mars Climate Orbiter and related mission
failures, FBC combined resource cuts, compressed schedules, organisational
restructuring, and skill erosion under sustained external stakeholder
pressure. Each individual efficiency gain was real; none of it accumulated as
margin, because the programme's mandate consumed every gain as license to
take on more mission scope at the same or lower cost. The result was rising
system brittleness and increasingly risky decisions that the organisation was
not tracking as a trend, because no single decision looked different from the
ones that had "worked" the year before — the same invisible-until-crossed
dynamic as [Rasmussen's boundary migration](rasmussen-boundary-model.md).

The practical implication for monitoring resilience: a metric of current
throughput or efficiency will never show this erosion, because the law
guarantees throughput looks fine right up to the point capacity is
exceeded. What must be tracked instead is the *margin* left after the
system's normal operating stretch — see [buffering capacity, margin, and
tolerance](buffering-margin-and-tolerance.md) — not the efficiency gain
itself.

Fujita's commentary names the same dynamic an **"evil chain"**: a drive for
long-term performance optimisation (yield, speed, reliability) introduces
incremental changes — added technical complexity, tighter operating
tolerances, thinner safety margins — that quietly implant hazards nobody
decided to accept. What keeps the chain invisible is that front-line
practitioners proactively adapt to compensate for each hidden hazard behind
the scenes, so the system keeps working and the hazard never surfaces as a
problem report; the compensation is itself unrecognised risk-taking,
consuming exactly the buffering capacity the law of stretched systems
predicts will be consumed. Breaking the chain requires actively hunting for
these hidden hazardous side effects before they trigger failure, rather than
waiting for the compensating adaptation to eventually run out of margin.

**This produces a genuine interpretive ambiguity, not just a hidden risk:
skilled improvisation at the sharp end can be read as evidence of
resilience or as a symptom of macro-level under-resourcing, and both
readings can be correct about the same behaviour at once.** A cross-cultural
comparison of aviation maintenance makes the ambiguity concrete: in
resource-constrained environments, technicians facing chronic parts and
tooling shortages develop genuine problem-solving skill and constant
vigilance ("we don't have everything, but we get the job done anyway")
that, examined on its own, looks like exactly the kind of adaptive capacity
resilience engineering values. But if that micro-level skill exists
*because* the macro system routinely stretches resources too thin to
operate any other way — the law of stretched systems consuming margin as
described above — then the skill is not adding resilience to an otherwise
adequate system; it is quietly substituting for resourcing the organisation
should have supplied and is compensating for the organisation's own
brittleness. Total system resilience is not improved by this arrangement
even though the front-line population inside it has visibly become more
individually adaptive — the same compensation-masks-exhaustion structure
[decompensation](decompensation.md) names at the level of a single
escalating incident, here operating as a standing organisational condition
rather than a one-off event.
