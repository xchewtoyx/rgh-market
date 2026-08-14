---
type: concept
title: Spike (Research Story)
description: >
  A spike is a story whose deliverable is reduced uncertainty rather than
  user-visible functionality, used sparingly and only after splitting has
  failed to make a story estimable.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 6"
---

A spike is a special-purpose [user story](user-story.md) whose output is
information — reduced technical or functional risk — rather than delivered
functionality. It exists for the case [story splitting
patterns](story-splitting-patterns.md) can't handle: a story that's too
uncertain to scope into smaller pieces at all, not just too large. A
**technical spike** researches an implementation question (how long does
propagating a data update actually take; what does a third-party
integration actually support); a **functional spike** builds a throwaway
prototype to gather user reaction to a design direction before committing
to it.

Because a spike doesn't deliver user value directly, it should be used
sparingly and only after ordinary splitting has been tried and failed —
treating uncertainty-reduction as a story is useful precisely because it
makes that work visible and estimable like everything else in the backlog,
not because it's a substitute for normal story decomposition. The output
of a spike is usually one or more newly-estimable stories, and those are
generally planned into a *later* iteration than the spike itself: planning
the spike and its resulting stories into the same iteration assumes the
spike's answer in advance, which defeats the purpose of doing it.
