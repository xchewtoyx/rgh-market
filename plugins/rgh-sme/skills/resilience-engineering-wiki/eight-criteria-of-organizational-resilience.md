---
type: concept
title: Woods's Eight Criteria of Organisational Resilience
description: >
  A checklist for auditing whether an organisation is actually resilient, as
  distinct from merely currently safe — each criterion names a specific way
  resilience is absent even where accident rates look fine.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 9"
---

Eight criteria (Woods, 2003) for auditing organisational resilience
directly, rather than inferring it from an accident rate that [Wald's bomber
paradox](walds-bomber-paradox.md) and [the Heinrich triangle
myth](heinrich-triangle-myth.md) both show is a poor proxy:

1. **Defences do not erode under production pressure** — margin holds even
   when schedule, cost, or throughput demands rise (see [goal
   conflicts](goal-conflicts-and-production-pressure.md)).
2. **Freedom from complacency** — past good performance is not treated as
   proof of future safety (the trap [chronic unease](chronic-unease.md)
   guards against).
3. **A shared, explicit risk model** — the organisation's various parts
   operate from a common, articulated understanding of its hazards, not an
   implicit or fragmented one that dissolves under organisational change.
4. **Dynamic revision of risk assessments** — new evidence actually updates
   the risk model, rather than being filed against a static assessment
   that never moves (see [getting stuck in outdated
   behaviours](getting-stuck-in-outdated-behaviors.md)).
5. **Communication and coordination across boundaries** — organisational
   seams (between departments, contractors, or levels) do not block
   information flow (see [upward and downward
   resilience](upward-and-downward-resilience.md) and [structural
   secrecy](structural-secrecy-and-practical-drift.md)).
6. **Operational flexibility** — the system can respond adaptively to
   changing demands and genuinely unexpected situations, rather than
   relying on one fixed response pattern regardless of the situation.
7. **Genuine devotion to safety** — safety is a real organisational value,
   not a slogan competing unsuccessfully against commercial targets.
8. **Safety built into the system inherently** — protection comes from
   design choices made at the infrastructure or architecture stage, not
   bolted on afterward as compensating procedure.

The criteria are useful precisely because a system can score well on some
and fail badly on others simultaneously — passing "inherent design safety"
through decades-old hardware while failing "shared risk model" after an
organisational restructuring fragmented it, for instance. Scoring an
organisation criterion by criterion, rather than assigning one aggregate
resilience verdict, is also what exposes cases like [command-and-control as
an alternative to resilience](command-and-control-alternative-to-resilience.md):
a system can fail most of these criteria and still be extremely safe,
because it is being protected by a different mechanism entirely.

A separate, independently-derived checklist built from different source
material for a different purpose is [the seven core themes of resilient
organizations](seven-core-themes-of-resilient-organizations.md) — the two
overlap in substance but are worth holding side by side rather than merged.

Whether these eight criteria can actually be audited, rather than merely
listed, depends heavily on which criterion is in question: see [structural
audits vs culture assessment for
resilience](structural-audits-vs-culture-assessment-for-resilience.md) for
which of the eight a formal management-system audit can reach and which it
structurally cannot.
