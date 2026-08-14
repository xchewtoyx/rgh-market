---
type: concept
title: Efficiency-Flexibility Control Tradeoff
description: >
  Controls that maximize efficiency and predictability within the normal
  envelope can erode the autonomy, creativity, and reactivity needed when
  something genuinely unanticipated happens — the "irony of resilience."
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel, Pariès, Woods, Wreathall, eds.), ch. 2 (Jean Pariès)"
---

There is a standing tradeoff between **efficiency** (how well adapted the
system is to its usual conditions) and **flexibility** (how wide a band of
variation it can survive). Highly optimized routines, heavy
proceduralisation, and automation that removes decision points make the
normal envelope safer, cheaper, and more reliable — but they can erode
exactly the real-time competences needed at the sharp end when something
outside the script happens. Proceduralisation reduces uncertainty by
reducing variety, deviation, and instability; the side effect is reduced
room to improvise, reconfigure, and sacrifice intelligently under time
pressure.

When designing personal controls, notice when "more order" is buying
efficiency at the cost of **brittleness outside the standard envelope**.
Examples of the tradeoff in action: an engine certification optimized for
fuel efficiency cannot survive a flock of oversized birds; a life organized
so tightly that every hour is scheduled has no slack to absorb a surprise
crisis. Mitigations are not "abandon all structure" but deliberate
reserves: [layered defence in depth](layered-defence-in-depth.md) so
efficiency at one layer does not eliminate fallback; [operating envelope
control shift](operating-envelope-control-shift.md) so generic emergency
frameworks exist alongside detailed normal protocols; periodic drills or
rehearsals that keep improvisation skills from atrophying ([contingency
rehearsal scripts](contingency-rehearsal-script.md), [voluntary hardship
drill](voluntary-hardship-drill.md)). A resilient setup is both prepared
and prepared to be unprepared.
