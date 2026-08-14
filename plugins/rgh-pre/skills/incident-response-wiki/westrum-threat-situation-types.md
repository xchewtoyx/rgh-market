---
type: concept
title: Westrum Threat Situation Types
description: >
  Three classes of threat — regular, irregular, and unexampled — that set
  how much pre-scripted procedure versus improvisation an acute response
  can rely on.
sources:
  - title: "Resilience Engineering: Concepts and Precepts"
    resource: "Resilience Engineering: Concepts and Precepts (Hollnagel, Woods, Leveson, Eds.), Chapter 5 (Westrum)"
---

Resilience is a family of capabilities, not one skill. Westrum's typology
sorts threats by predictability (whether events of this type are routine
enough to standardise), disruptive potential, and origin (internal versus
external). The situation class tells an agent how much runbook exists
before the acute phase.

**Situation I — Regular threat.** Occurs often enough for algorithmic
response. Least alarming when predictable, internal, low disruption (e.g.
medication errors managed by safeguards). More disturbing when predictable
and external (recurring bombings with rehearsed hospital resource shifts;
earthquake drills). [Crisis rehearsal](crisis-rehearsal.md) and standard
procedures dominate.

**Situation II — Irregular threat.** A one-off instance of a understood
category — too many low-probability event types to script each, but the
class is conceivable (Apollo 13, a mass-casualty attack on a forward
operating base with improvised ambulances and ORs in conference rooms).
Improvisation within known bounds; self-organisation and monitoring matter.
Maps to the abnormal region of [operational mode envelopes](operational-mode-envelopes.md).

**Situation III — Unexampled event.** Requires a shift in mental framework,
not mere scale-up. No advance algorithm; outcome depends on basic qualities
— self-organisation, monitoring, novel response formulation (9/11, Chernobyl,
catastrophic institutional collapse from stacked latent failures). Maps to
the emergency open region; [sacrificing decisions](sacrificing-decisions.md)
and [defence in depth tactical retreat](defence-in-depth-tactical-retreat.md)
may be all that exists.

**Time axis (independent).** Westrum separates resilience meanings across
the timeline:

- Foresee and avoid (requisite imagination, faint signals, learning from
  experience — preventive, mostly outside incident-response charter)
- **Cope with ongoing trouble** — defences, adaptive resilience, monitoring,
  removing latent pathogens during the event
- **Repair after catastrophe** — rebound; see [post-incident
  recovery](post-incident-recovery.md)

Having one capability does not imply the others. An organisation expert at
Situation I recovery may fail Situation III recognition — see [resilience
state transitions](resilience-state-transitions.md) for transition
requirements once the situation class is named.
