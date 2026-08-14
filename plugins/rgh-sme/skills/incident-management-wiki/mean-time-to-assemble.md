---
type: concept
title: Mean Time to Assemble (MTTA)
description: The time to get the right responders engaged and ready to act, framed as the one part of incident response fully within an organization's control.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 1, ch. 3"
---

**Mean time to assemble (MTTA)** is the time from realizing a resource is
needed to that resource being engaged and ready to act. The central claim
built around it: asking "why did it break" (root-cause analysis) in the
first minutes of an incident is the wrong early question, because without
the right subject-matter experts present there is no data, and without data
there is no informed action. MTTA is singled out as **the only stage of
incident response an organization fully controls** — resolution itself
depends on how complex the underlying problem turns out to be, which is a
"wild card," but how fast the right people show up is a function of process
and readiness, not luck.

**Reflex time** is the related idea for individual dispatch decisions: the
gap between recognizing a need for a resource and that resource arriving.
The operating rule is "if you think you need it, call for it early" — it is
cheaper to dispatch a resource and release it unused than to wait for
certainty and lose time. This treats over-dispatching the same way the fire
service treats false alarms: an accepted cost of readiness, not a failure,
because an incident isn't classified a false alarm until after detection,
reporting, and investigation have actually happened.

A responder moves through **seven engagement states** as MTTA plays out:
available, dispatched, responding, on scene, assigned a task, staged (an
identified, ready participant not currently task-assigned — distinct from
merely lurking), and released back to available. The first four states are
where MTTA is won or lost; common time sinks are ambiguous availability,
weak [dispatch discipline](dispatch-vs-notification.md), and notification
tooling that automates a broken escalation policy rather than a sound one.

Because MTTA is the lever an organization actually controls, it is the
metric worth optimizing pre-incident — through clear on-call rosters,
rehearsed dispatch procedures (see [preparedness
drills](preparedness-drills.md)), and the kind of role clarity the
[incident response process framework](incident-response-process-framework.md)
evaluates under "Predictable" and "Repeatable."
