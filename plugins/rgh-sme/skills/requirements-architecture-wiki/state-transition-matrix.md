---
type: concept
title: State Transition Matrix
description: >
  A grid enumerating every state against every possible event forces a
  finite state machine's behavior to be fully specified, surfacing edge
  cases an informal state diagram or prose description would let slide.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 18"
---

A finite state machine (FSM) diagram is already more precise than prose
for describing state-dependent behavior — natural-language attempts at
specifying even a simple stateful device ("after On is pushed but before
Off is pushed, the system is 'powered on'") get awkward fast. But a
drawn FSM diagram can still leave gaps: it's easy to draw the transitions
you thought of and simply not draw — and therefore never notice you
omitted — a transition for an event that occurs in a state where "nothing
should happen" wasn't actually decided on purpose.

A state transition matrix closes that gap by turning the diagram into a
grid: every state as a row, every possible event as a column, and every
cell filled in with that state's output and resulting transition for that
event — including the states where the "obvious" answer is that nothing
happens, which now has to be stated rather than merely implied by
omission. The forcing function is structural: because the matrix has one
cell per state-event pair, a genuinely unconsidered case shows up as a
visibly empty cell rather than as a diagram that merely doesn't happen to
mention it. This is the same completeness-by-exhaustive-enumeration
principle a [decision table](decision-table.md) applies to combinations of
input conditions, applied here to combinations of state and event instead.
