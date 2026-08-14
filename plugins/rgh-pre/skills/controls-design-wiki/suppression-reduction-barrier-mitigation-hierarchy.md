---
type: concept
title: Suppression Reduction Barrier Mitigation Hierarchy
description: >
  When designing controls for a hazard, prefer removing exposure first,
  then reducing exposure, and only then adding barriers that block harm
  after exposure has already occurred.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 6 (Philippe Cabon et al.)"
---

Risk mitigation works best in priority order:

1. **Suppression** — remove exposure to the hazard at the source (e.g.
   design the roster so reduced-rest patterns are a last resort, not the
   default; refuse to take on a commitment that would guarantee overload).
2. **Reduction** — when suppression is not fully achievable, lower exposure
   (better accommodation after a hard day, scheduler training, life-hygiene
   practices that protect sleep).
3. **Barriers** — when exposure may still occur, block the negative effect
   (automation, extra cross-checks, task rotation, [layered defence in
   depth](layered-defence-in-depth.md) at the sharp end).

Barriers are necessary but last-resort: they manage consequences of
exposure rather than preventing it. Personal examples: suppression =
declining the meeting series; reduction = shortening it or adding recovery
time; barrier = a checklist used while depleted. Pair with [operating
envelope control shift](operating-envelope-control-shift.md) — suppression
and reduction dominate in normal and abnormal envelopes; barriers matter
most when already in the emergency region.
