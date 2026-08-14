---
type: concept
title: Coordination Dimensions of Resilience
description: >
  System resilience rests on coordinating distributed action across vertical,
  lateral, and longitudinal axes, and the tools built for routine coordination
  are exactly what strain or break first under crisis conditions.
sources:
  - title: "Resilience Engineering in Practice"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Wreathall), ch. 16"
---

Coordination in a sociotechnical system is two complementary movements:
**distributing** actions and decisions across agents, and **integrating**
those distributed actions back together across time and space (Savoyant &
Leplat; Pavard). Resilience depends on the dynamic interaction pattern
between agents across time and space — not on any single agent's individual
adaptive skill in isolation.

Organisations structure this coordination along three axes, each with its
own conventional tools and its own characteristic failure mode:

- **Vertical coordination** — information flowing up and down a hierarchy of
  decision-making roles. Conventional tools: task allocation by expertise
  level, call cascades, and "sentry markers" (thresholds that trigger a call
  for senior help). Vulnerability: novices routinely misjudge sentry markers
  — overestimating their own competence, underestimating how fast a
  situation is deteriorating, or fearing the loss of face that escalating
  implies — so the call for help arrives late.
- **Lateral coordination** — integrating specialised, autonomous units with
  their own subcultures and only a partial view of the situation into one
  shared picture. Conventional tools: multi-scale scheduling, workload
  tracking, standardised procedures.
- **Longitudinal coordination** — continuity of the same work across shift
  handovers and round-the-clock operation. Conventional tools: transition
  briefings and case records that serve as static external memory of a
  case's history and trajectory.

**Sector matters.** High-risk domains with formal crew training, like
aviation's Crew Resource Management (mandatory call-outs, explicit role
splits between Pilot Flying and Pilot Non-Flying), enforce common ground
directly. Domains without that training — healthcare is the studied case —
rely almost entirely on the static management tools above, with no formal
communication training to fall back on when those tools fail.

Four situational factors determine whether coordination holds or breaks
down in a given episode:

1. **Goal compatibility** — cooperating agents can hold different sub-goals
   (a surgeon wanting to operate immediately, an anaesthetist wanting the
   patient stabilised first) that create tension precisely when an
   unexpected event forces a fast joint decision. This is the same
   structural tension as [goal conflicts and production
   pressure](goal-conflicts-and-production-pressure.md), instantiated
   between roles rather than between management and the sharp end.
2. **Resource sharing** — competing demands on the same limited people and
   equipment require continuous re-alignment, not a one-time allocation.
3. **Agent skill and communication mode** — repeated cooperation between the
   same people builds implicit communication and automatic synchronisation;
   but under crisis, the demand for explicit, task-centred information rises
   sharply exactly when there is least time to produce it.
4. **Interaction type** — coordination can be **synchronic** (same time and
   place, real-time dialogue) or **asynchronic** (different time and place,
   relying on accumulated records rather than live exchange). Technology
   that removes the need for co-presence — electronic records, remote
   consultation — shifts coordination toward the asynchronic end, trading
   real-time dialogic synthesis for information accretion in a shared
   record.

The asynchronic mode is the weaker one under stress: a static record that
each new party reads in isolation, without dialogue, tends to produce
repeated restarting of diagnostic reasoning rather than genuine integration
— see [sharp-end myopia](sharp-end-myopia.md) for what this looks like when
several agents each handle the same unfolding situation as if it were a
fresh, local event. It is also one more channel through which uncoordinated,
locally rational adjustments by different units can undermine the whole,
the pattern [working at cross-purposes](working-at-cross-purposes.md)
describes at the level of adaptation rather than information flow.
