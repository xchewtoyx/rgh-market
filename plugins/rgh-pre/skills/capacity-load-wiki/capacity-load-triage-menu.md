---
type: concept
title: Capacity Load Triage Menu
description: >
  When demand approaches saturation, only three families of response
  exist — add capacity, adjust limits by removing stressors, or remove
  load — and the right mix depends on how close to yield the person
  already was.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 7 (Siemens Turbine Maintenance Case Study)"
---

Once overload is noticed, mitigating actions fall into three categories —
no fourth option:

1. **Add capacity** — bring in help, extend time, add people or tools so
   the same load spreads across more resource.
2. **Adjust capacity limits** — remove or reduce stressors so the same
   person can function nearer their normal ceiling (e.g. heaters, shorter
   shifts, fewer simultaneous demands, better site organization).
3. **Remove load** — defer, delete, or move work off the critical path so
   existing capacity is freed for what must stay.

Design questions for choosing among them:

- What unplanned events are consuming capacity right now?
- What help is needed to add capacity, remove stressors, or free existing
  capacity?
- Where was the person relative to their limits *before* this situation
  changed?

A menu of concrete tactics — stop and reassess the plan, reorganize roles
and communication, escalate for commercial or logistics help, institute
periodic stand-downs to check needs — implements these three families in
context. The point is not memorizing the list but recognizing that every
response is an instance of add, adjust limits, or remove load; pacing
plans that only suggest "try harder" omit two of the three levers.

See [capacity yield point](capacity-yield-point.md) for when this menu
should be invoked, and [precommitted demand
shedding](precommitted-demand-shedding.md) for a personal-scale version
of the remove-load option decided in advance.
