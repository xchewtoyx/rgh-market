---
type: concept
title: Decision Table
description: >
  Enumerating every combination of input conditions as an explicit column,
  with its resulting action, replaces nested conditional logic that
  readers can't verify is actually complete.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 18"
---

Nested if-then-else logic over several conditions quickly becomes tangled
prose that non-technical stakeholders can't confirm they understand, and
that nobody can be confident actually covers every combination. A decision
table replaces the nesting with an explicit grid: one column per possible
combination of input conditions, with the resulting action listed at the
bottom of each column. Three boolean inputs produce 2³ = 8 columns, each
one forced into existence by the table's structure — there's no way to
silently skip a combination the way a paragraph of prose or a chain of
if-statements can.

A decision tree is the same information laid out as a branching diagram
instead of a grid — easier to follow when conditions are evaluated in a
meaningful sequence rather than all at once, at the cost of making the
"have we covered every combination?" check less immediate than counting
columns in a table. Use either specifically as a [precision
escalation](precision-escalation-trigger.md) once conditional business
logic gets complex enough that prose can no longer be trusted to be
complete — [state transition matrices](state-transition-matrix.md) apply
the same forced-completeness principle to state-dependent behavior instead
of to input conditions.
