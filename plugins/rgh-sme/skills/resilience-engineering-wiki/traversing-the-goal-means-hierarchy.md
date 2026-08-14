---
type: concept
title: Traversing the Goal-Means Hierarchy Under Resilient Performance
description: >
  Routine work stays at the concrete, low-abstraction level of Rasmussen's
  goal-means hierarchy where goals rarely conflict; a resilient response to
  sudden demand requires traversing upward to resolve conflicts, deliberately
  sacrificing lower-level goals to preserve the system's top-level viability.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson), ch. 13"
---

Rasmussen's goal-means hierarchy (Rasmussen, 1986; Rasmussen et al., 1994)
arranges a system's activity from concrete, low-level means (specific
actions, specific procedural steps) up through progressively more abstract
levels toward high-level purposes. In ordinary, routine operation, cognitive
performance stays down at the concrete end of that hierarchy — the level
where individual goals rarely conflict with each other, so a practitioner
never needs to reason explicitly about trade-offs between them.

A sudden, unanticipated resource demand changes this. It registers as a
threat at a *high* level of the hierarchy — to overall system viability, not
to any single task — and resilient performance requires the practitioner to
traverse *upward*, out of the concrete level where they normally operate, to
resolve the conflict that has now appeared between goals that used to
coexist without friction. Once at that higher level, they redefine what
success means for the current situation and deliberately sacrifice
lower-level goals to protect it: abandoning non-essential paperwork,
accepting a procedural delay, deferring routine cases — trades that would be
indefensible measured against the original, concrete-level goal but are
exactly right measured against the higher-level purpose that goal always
served. A hospital's mass-casualty response shows this upward traversal
concretely: severely injured casualties get routed directly to operating
rooms, bypassing standard trauma-room evaluation, and administrative
paperwork is systematically abandoned except for the one item
(blood type-and-cross match) that is still safety-bound at the higher level
— while non-emergency cases resume as quickly as possible, because the
higher-level goal was never "suspend routine work," only "protect viability
during the surge."

This traversal is the cognitive-level analogue of [matching response
abstraction to uncertainty](matching-response-abstraction-to-uncertainty.md):
that concept describes how the *usefulness of pre-written guidance* shifts
from action-level to goal-level as uncertainty rises; this one describes the
same shift happening inside the practitioner's own reasoning, which is why
generic, goal-level guidance is what remains applicable once a situation has
escalated past what concrete procedures anticipated. It is also the
mechanism underneath a [sacrifice judgement](sacrifice-judgements.md):
choosing to relax an acute, lower-level goal to protect a chronic,
higher-level one is only possible for someone who has already traversed up
the hierarchy far enough to see the higher-level goal the trade actually
serves.

The events that provoke this traversal are, in the practitioners' own
framing, **unusual but not unknown** — deep domain knowledge lets an
experienced practitioner anticipate operational tempo, predict where
bottlenecks will form, and identify alternative pathways without waiting for
real-time instruction, precisely because they have encountered the shape of
the demand before even if not this specific instance of it. The same
cognitive mechanism operates at every scale, from a single anaesthesia
coordinator quietly renegotiating an operating-room schedule between two
surgeons to a hospital-wide response to a mass-casualty event involving
hundreds of people — the traversal itself is qualitatively the same act,
just multiplied across more actors and more goals.
