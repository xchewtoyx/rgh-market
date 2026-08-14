---
type: concept
title: INVEST Criteria for User Stories
description: >
  A well-formed user story is Independent, Negotiable, Estimable, Small,
  and Testable — a checklist for catching a poorly scoped story before it
  enters an iteration rather than after it stalls mid-build.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 6"
---

INVEST is a checklist for judging whether a [user story](user-story.md) is
well formed enough to plan and build:

- **Independent** — the story can be built, tested, and potentially
  shipped on its own, and so can be independently valued. A natural
  sequence between stories (show a record, then a list, then filtering,
  then export) doesn't violate this, since the product can still ship at
  any point in that sequence; a *non-valued* dependency (one story is
  technically blocked on another with no independent value of its own) is
  the thing to find and eliminate.
- **Negotiable** — a story is not a contract for specific functionality;
  it's a placeholder for what gets discussed, developed, tested, and
  accepted through the [conversation](user-story.md) that follows the
  card. Negotiability requires reorienting the functional breakdown from
  horizontal slices (all of the UI layer, then all of the data layer) to
  vertical slices through the whole architecture, so each negotiated
  increment is something a user or stakeholder can actually see and react
  to.
- **Estimable** — if a team can't estimate a story, that's a diagnostic
  signal, not a scheduling inconvenience: either the story is too large
  (split it, see [story splitting patterns](story-splitting-patterns.md))
  or too uncertain (reduce the uncertainty with a [spike](spike-story.md)
  first). The value of the estimating conversation itself is usually more
  important than the resulting number — it surfaces hidden assumptions and
  missing acceptance criteria before they surface as mid-iteration
  surprises.
- **Small** — a story should fit inside a single iteration. Complexity
  scales non-linearly with size (most visibly in the number of test
  permutations), so shrinking a story reduces effort disproportionately
  more than its apparent size would suggest, and smaller stories increase
  throughput predictability and shorten feedback loops.
- **Testable** — an untestable story is usually a symptom of being
  ill-formed, overly complex, or wrongly coupled to other backlog items,
  not a property to fix after the fact. Writing the acceptance test (or
  criteria) before writing the code extends test-driven development's
  logic from the unit-test level up to the story level.

A story that fails INVEST is a scoping problem to fix before planning, not
a risk to carry into an iteration and hope resolves itself.
