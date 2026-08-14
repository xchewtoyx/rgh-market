---
type: concept
title: Operating Envelope Control Shift
description: >
  Match control design to how far the situation has departed from normal:
  detailed protocols when within the normal envelope, predefined
  reconfiguration when abnormal, generic frameworks and satisficing when in
  the emergency region.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 2 (Jean Pariès)"
---

Not every situation calls for the same kind of control. Three envelopes,
from most to least predictable:

1. **Normal operation** — events stay on predefined tracks, parameters
   within design limits; intrinsic flexibility absorbs variation. Controls
   here are accurate, detailed routines and checklists the system is
   already adapted to.
2. **Abnormal operation** — departure from normal but in anticipated ways
   (a component fails, a parameter exceeds limits). Controls shift to
   specific procedural responses, built-in redundancy, and active
   reconfiguration — the system must re-adapt using predefined options.
3. **Emergency (open) region** — extreme, possibly unanticipated departure.
   Detailed protocols may not exist. Controls shift toward generic
   frameworks, sense-making under time pressure, creativity, ultimate
   backups, and **satisficing then sacrificing** solutions — stretching
   relevant capabilities quickly because full re-adaptation is no longer
   possible.

The design mistake is applying normal-envelope detail everywhere (brittle
under surprise) or relying only on emergency improvisation (no prepared
retreat path). Pair [layered defence in depth](layered-defence-in-depth.md)
with envelope-appropriate procedure: stock detailed scripts for the normal
and abnormal bands ([contingency rehearsal
scripts](contingency-rehearsal-script.md), [visual checklists for multistep
routines](visual-checklist-for-multistep-routines.md)), and generic
frameworks — "if the plan collapses, what is the minimum outcome to
protect?" — for the open region. [Premortem
procedure](premortem-procedure.md) is the advance work that maps which
failure modes stay abnormal versus which would land in the emergency region
with no script.
