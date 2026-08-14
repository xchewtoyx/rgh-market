---
type: concept
title: Exhaustive Matrices for Unambiguous Logic
description: >
  When conditional or state-dependent behavior has enough interacting
  cases that nested prose can hide a gap, replace the prose with a
  table that forces every combination to be filled in explicitly.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Dean Leffingwell), ch. 18"
---

Nested conditional prose ("if A and not B, unless C also holds...") degrades fast as the number of interacting conditions grows: a reader can't easily confirm they've understood every branch, and the writer can't be sure every combination was actually considered — some case quietly never gets a sentence. The fix is to stop describing the logic in prose and instead build a matrix that has one cell for every possible combination, so an unconsidered case shows up as a visibly empty cell rather than a silent gap in a paragraph.

**Decision tables** apply this to conditional logic: list every input condition as a row (or column) and enumerate all combinations explicitly — with three independent boolean conditions, that's a fixed 2³ = 8-column table, not an open-ended set of prose sentences the writer has to remember to keep exhaustive. **Decision trees** are the same content in graphical form, branching through each condition in turn; choose whichever form makes the specific case count easier for the intended reader to scan — a table for a compact, review-at-a-glance layout, a tree when the path structure itself is the useful part.

The same principle extends to specifying behavior over time rather than a single conditional outcome: a **state transition matrix** enumerates every system state down one axis and every possible event or stimulus across the other, with each cell recording what happens to that state under that event. This format forces a question nested prose would never surface on its own — "what happens if the user presses the On switch and the device is already on?" — because the corresponding cell has to be filled in with something, even if that something is "no effect."

Reach for this technique specifically when the combination count is large enough that a reader can't hold "have I seen every case" in their head from prose alone, and when the cost of a missed case is genuinely high — not as a default replacement for ordinary explanatory prose, which still communicates the *why* behind a rule better than a bare matrix cell can. A decision table or state transition matrix is a diagram-adjacent structure in the sense of [using visuals effectively](using-visuals-effectively.md): it earns its place by passing the same comprehension test, not by looking more rigorous than the prose it replaces.
