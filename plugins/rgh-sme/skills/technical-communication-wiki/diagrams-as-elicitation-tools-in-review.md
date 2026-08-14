---
type: concept
title: Diagrams as Elicitation Tools in Stakeholder Review
description: >
  A structural diagram shown live to mixed stakeholders often surfaces
  unclear or missing requirements that prose specs never provoked,
  simply by being concrete enough for a non-technical reader to ask
  "but what happens when..." — treat that derailment as the review
  working, not as scope creep.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice (Bass, Clements, Kazman), ch. 2"
---

A diagram doesn't have to be about behavior to provoke a behavioral question. Showing a structural diagram (boxes, arrows, redundant elements, a runtime topology) to a room of mixed stakeholders — some technical, some not — routinely produces a moment where a non-technical participant asks something like "what happens when this button is pushed while that's happening?" A prose specification describing the same system, read silently, rarely produces this moment, because a reader working alone tends to accept ambiguity and move on rather than stop and interrupt; a diagram presented live, with an audience and a presenter both looking at the same concrete artifact, invites exactly the kind of pointing-and-asking that surfaces a gap neither the diagram's author nor its other readers had noticed.

When this happens, it can feel like a derailment — a 45-minute detour into a requirements question that "should have" been settled earlier, in a meeting that was supposed to be about something else. The more useful frame is that the diagram did its job: it was the first artifact concrete enough to make an unstated assumption visible to someone who didn't share it. Resist the urge to defer the question to protect the meeting's agenda; an unclear or missing requirement is far cheaper to catch here, provoked by a diagram, than later when it's discovered as a bug or a field failure. This is a reason to build room for open-ended questions into any review of a structural artifact shown to a mixed audience, rather than treating the review as a one-way presentation to be gotten through — the value of showing the diagram live, to people who will ask what it doesn't already answer, is precisely what a written document circulated for silent comment doesn't reliably produce.
