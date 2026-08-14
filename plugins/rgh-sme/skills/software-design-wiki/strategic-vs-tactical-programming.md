---
type: concept
title: Strategic vs. Tactical Programming
description: >
  Tactical programming optimizes for getting the current task working as
  fast as possible; strategic programming treats a great design that also
  works as the actual goal, because complexity accumulates incrementally and
  tactical shortcuts are its main source.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 3"
---

**Tactical programming** focuses on getting a feature or bug fix working as
fast as possible, without prioritizing long-term structure. It feels
reasonable in the moment — what could matter more than working code? — but it
makes good design nearly impossible over time, because
[complexity accumulates incrementally](incremental-accumulation-of-complexity.md):
each tactically-completed task adds a few small compromises that each seem
individually fine. Once accumulated complexity starts causing visible
problems, a proper cleanup looks like more time than the schedule can absorb,
so developers apply quick patches instead — which add more complexity,
requiring more patches. A **tactical tornado** is the archetype of a
programmer who ships faster than anyone else this way; management sometimes
lionizes them as a hero, but they leave a wake of complexity that other
engineers must clean up, which perversely makes the cleanup engineers look
slower even though they're the ones doing the sustaining work.

**Strategic programming** reframes the goal: "working code isn't enough." Most
of the code written over a system's life extends an existing base, so
facilitating future extension is a developer's most important job, not a
nice-to-have on top of shipping the current task. This requires an investment
mindset — accepting some short-term slowdown for long-term design payoff (see
[how much to invest in design](design-investment-level.md)) — expressed as two
kinds of investment:

- **Proactive**: exploring a couple of design alternatives before picking the
  cleanest one (see [design it twice](design-it-twice.md)), imagining
  plausible future changes and designing for them, writing documentation that
  carries design intent.
- **Reactive**: when a design mistake becomes apparent — and mistakes are
  inevitable regardless of how much upfront investment you make — taking the
  time to actually fix it rather than patch around it.

Strategic programmers continually make small design improvements; tactical
programmers continually add small complexities. The difference compounds in
opposite directions over the life of a codebase.
