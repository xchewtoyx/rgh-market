---
type: concept
title: Acceptance Tests as Durable Behavior Record
description: The acceptance test written alongside a feature, not the requirement or story that prompted it, is the artifact a future maintainer should trust as the record of intended behavior.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Leffingwell), ch. 10"
---

A user story or feature request is deliberately written to be lightweight and disposable — a placeholder for a conversation, not a specification. Once the feature is built, the story itself is normally discarded. This creates an obvious hazard for a future maintainer: if the story is gone, where does "what is this supposed to do" now live?

The answer is the **acceptance test** written and automated during the same iteration the story was implemented. Because it is executable, it survives every subsequent change as a live, continuously-checked statement of behavior, in a way that a prose requirement document cannot: a stale prose doc silently drifts out of sync with the system, while a stale acceptance test fails loudly the moment its assumptions stop holding.

## Implication for handover

When a maintainer inherits a system and finds no design document or story backlog explaining a piece of behavior, check whether an acceptance or regression test covers it before concluding the intent was never recorded. The test suite, not the (likely discarded) original requirements artifact, is the place intended behavior was designed to persist. This also means a handover is incomplete if it hands over source code and a test suite but doesn't tell the incoming maintainer that the tests *are* the specification — without that framing, a new maintainer may treat a failing test as an obstacle to work around rather than as the authoritative constraint it was written to be.

This is a different situation from [Characterization Tests for Undocumented Behavior](characterization-tests-for-undocumented-behavior.md): a characterization test is written defensively, after the fact, to pin down what already-undocumented legacy code happens to do, with no claim that the behavior is correct. An acceptance test is written proactively, before or alongside the code, and does make that claim — it is what the story's author and the team agreed the behavior *should* be, not just a snapshot of what it currently is.
