---
type: concept
title: Precision Escalation Trigger for Specifications
description: >
  Reach for a more formal specification notation than prose only when a
  description is genuinely too complex for natural language and the cost
  of being misunderstood is high — not as a default level of rigor.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 18"
---

Most requirements are well served by natural language — a short
[user story](user-story.md) or [scenario](scenario-for-business-use-case.md)
plus a conversation resolves ambiguity cheaply enough that formal notation
would be overkill. The trigger for reaching past prose into something more
formal — a [decision table](decision-table.md), a
[state transition matrix](state-transition-matrix.md), pseudocode, a
finite state machine, or a message sequence diagram — is not "this is an
important requirement," it's a conjunction of two conditions: the
behavior is genuinely too complex to state unambiguously in prose *and*
the business cannot afford the specification being misunderstood (a
cardiac-pacemaker algorithm, not a settings-page toggle).

This keeps formality proportional to actual risk rather than treating
precision as an across-the-board virtue: applying a decision table or FSM
to every trivial piece of logic wastes authoring effort on cases where
prose was never actually ambiguous, while skipping formal notation on a
genuinely complex, high-stakes behavior leaves exactly the kind of gap
[requirements completeness checking](requirements-completeness-checking.md)
exists to catch — prose can silently omit a combination of conditions that
a formal, exhaustive notation would have forced into the open.
