---
type: concept
title: Just-in-Time Requirement Elaboration
description: >
  A requirement should be elaborated to full detail close to when it will
  actually be built, not as early as possible — elaborating too far ahead
  wastes work when priorities shift before the work is picked up.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 11"
---

There is a recurring failure pattern in iterative delivery: "we failed to
deliver the stories that weren't understood before we committed." The
obvious fix — elaborate every backlog item to full detail as early as
possible — creates its own waste, because a requirement elaborated too far
ahead of when it's actually built can be trumped by a higher-priority item
before its turn comes, or the underlying need can simply change in the
meantime. Both failure directions are real: too little elaboration before
commitment risks building the wrong thing or stalling mid-build; too much
elaboration too early risks throwing away detailed work that never gets
used.

The resolution is to time elaboration deliberately: detail a requirement
close to, but not too far ahead of, the point where it will be built. In
practice this means elaboration happens in a recurring cadence tied to the
upcoming work boundary (an iteration or release), with items further out
in the backlog deliberately left coarse. This is a timing discipline
applied to individual requirements, distinct from [requirement revisit
triggers](requirement-revisit-triggers.md), which govern reopening a
requirement that has *already* been finalized and later drifted — here the
requirement was never finalized in detail yet, on purpose. It is also the
requirements-side mirror of [good-enough
requirements](good-enough-requirements.md): the same trade-off between
premature precision and useful-enough understanding, applied specifically
to the question of *when* to invest elaboration effort rather than *how
much* to invest overall.
