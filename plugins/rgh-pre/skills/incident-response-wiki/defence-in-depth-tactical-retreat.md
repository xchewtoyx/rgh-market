---
type: concept
title: Defence in Depth Tactical Retreat
description: >
  Layered fallback through successive lines of defence during an acute
  incident, each breach lowering ambitions and sacrificing less-critical
  goals to preserve what remains saveable.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 2 (Pariès, Hudson Ditching)"
---

When one response layer fails, a resilient system does not insist on the
original plan — it **tactically retreats** to the next line of defence.
Each move lowers sights: the situation becomes more improbable, less
controllable, more time-constrained, and less reversible; damage
probability and magnitude rise while options shrink. This is a shift from
adaptation toward de-adaptation, managed rather than denied.

Aviation's bird-strike defence illustrates five explicit lines:

1. Reduce strike frequency (wildlife control)
2. Absorb strikes without damage (engine/airframe certification)
3. Continue flight to an airport after losing one engine
4. Retain controllability after losing all engines long enough to reach
   somewhere survivable
5. Land on unprepared terrain or ditch with minimum damage and evacuate

Flight 1549 breached lines 1–3 simultaneously (flock strike, dual engine
failure). Lines 4–5 activated: APU and RAT preserved hydraulics and
electrical supply; ditching procedure and cabin preparation executed under
severe time pressure; outcome depended on daylight, water conditions, crew
familiarity, and luck within the last line.

Procedures **change character** across [operational mode
envelopes](operational-mode-envelopes.md): from detailed normal protocols
to specific abnormal responses to generic emergency frameworks requiring
sense-making and [sacrificing decisions](sacrificing-decisions.md) at the
open edge.

Personal application: identify your lines in advance (finish the critical
safety step, drop optional scope, accept partial delivery, ask for help,
stop entirely) so retreat is a chosen runbook step rather than unplanned
collapse. Pair with [acute stabilisation
procedures](acute-stabilisation-procedures.md) at each layer.
