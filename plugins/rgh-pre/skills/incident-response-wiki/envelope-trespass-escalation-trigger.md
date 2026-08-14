---
type: concept
title: Envelope Trespass Escalation Trigger
description: >
  The pivotal in-moment decision that a situation has left the prepared
  response envelope and requires mobilising additional resources or expertise.
sources:
  - title: "Resilience Engineering in Practice: A Guidebook"
    resource: "Resilience Engineering in Practice (Hollnagel et al., Eds.), Chapter 3 (Cuvelier & Falzon)"
---

Before an acute episode, a practitioner can define an **envelope of
potential variability** — situations that may occur, with resources
prepared in advance. Two regions matter for incident response:

- **Potential situations** — the event type was envisaged beforehand; only
  timing was uncertain. Protocols, equipment, and drugs are ready; help
  may be pre-arranged. Adaptation stays inside the envelope.

- **Unthought-of situations** — the event's nature was not foreseen for
  this case, even if known to the field generally. Sense-making is lost or
  delayed; existing protocols may not apply; the operator may be "in
  difficulty."

Resilience at the boundary is not only detecting trespass but **deciding**
trespass has occurred. Calling a colleague for help is the observable sign
that the system has shifted from potential to unthought-of — a **pivotal
decision**, not a reflex. Practitioners weigh colleague availability, time
of day, what function the call would serve, and their own capacity to
continue holding an unstable-but-survivable state while diagnosing.

In unthought-of cases, two sequential challenges appear:

1. **Identify and understand** — trade-off between pursuing diagnosis while
   maintaining a survivable state versus acting on a working hypothesis
   without full understanding.

2. **Implement coping** — if protocols fail or the team cannot meet demands,
   choose between continuing an inefficient organisational protocol or
   acting beyond protocols under time pressure.

Most unthought-of recoveries in the studied near-misses involved calling
colleagues — the default [incident escalation
path](incident-escalation-path.md) when the prepared envelope no longer
fits. Reducing unthought-of situations upstream is controls-design work;
once trespass is recognised, escalation and [acute stabilisation
procedures](acute-stabilisation-procedures.md) are the runbook.
