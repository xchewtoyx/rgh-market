---
type: concept
title: TALENT Diagnostic Framework
description: A six-dimension checklist — Training, Accountability, Leadership, Empowerment, Notification, Trust — for locating why a people-side failure happened during an incident response.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 6"
---

**TALENT** is a fast triage tool used during an [after action
review](after-action-review.md) to locate *why* a human-side failure
occurred, across six dimensions:

- **Training**: the most common root cause of response-side human error —
  but struggling with a genuinely novel problem isn't automatically a
  training gap; a real training gap looks like an [incident
  commander](incident-command-system.md) letting [span of
  control](span-of-control.md) balloon, or an untrained SME disrupting the
  channel.
- **Accountability**: failures cluster where no one is accountable to a
  specific person once the [peacetime/wartime](peacetime-wartime-mode-shift.md)
  switch happens — dispatch needs to be acknowledged and responded to with
  genuine urgency, not just technical SLA compliance.
- **Leadership**: a weak commander lets the incident slip into chaos through
  unclear objectives or timelines; this dimension also applies to executive
  performance during a [Unified Command](unified-command.md) activation, not
  only to the incident commander.
- **Empowerment**: responders need real authority to act at their level, not
  just the skill and knowledge to know what to do — a micromanaging
  commander or an under-authorized responder both slow the whole response.
- **Notification**: were pre-agreed SLAs and notification triggers (for
  customers, executives, business units) actually followed, defined in
  advance rather than improvised mid-incident?
- **Trust**: harder to observe directly, but worth probing for — did
  responders trust each other's competence, or did a senior person
  informally bypass the commander and seize control?

TALENT is meant as a filter, not an exhaustive audit: run the observed
failure through the six dimensions and the place to focus remediation is
usually apparent. The source explicitly frames this as diagnosing a
*process* failure, not an individual's fault, even when the proximate
trigger was one person's action — the same [blameless postmortem](blameless-postmortems.md)
posture applied specifically to the human-response half of an incident.
