---
type: concept
title: Escalation as a Resource Request
description: Reframing "escalation" from a management-approval or non-responsive-on-call problem into a request for more or different resources as an incident's conditions change.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 4"
---

IT organizations commonly use "escalation" for two different situations:
taking a decision to a higher-ranking manager, and paging a secondary
on-call because the primary didn't respond in time. The source argues both
uses obscure a more useful definition borrowed from the fire service:
**escalation is a request for more or different resources as conditions
change** — "fire has spread to the second floor, dispatch a second alarm."

Under this framing, the second common IT usage (a non-responsive primary
on-call) isn't really an escalation at all — it's a [mean time to
assemble](mean-time-to-assemble.md) failure, the one part of incident
response an organization is supposed to fully control. Treating "the
primary didn't answer" as a routine escalation path normalizes an
accountability gap that a well-run readiness system shouldn't have in the
first place; the fix belongs in a manager conversation about on-call
commitment, not in the incident's escalation policy.

Reframed this way, escalation becomes a proactive [incident
commander](incident-command-system.md) tool for scaling the response to
match the incident — raising severity, pulling in a disaster-recovery team,
or activating [Unified Command](unified-command.md) — rather than a
reactive fallback for when the on-call chain breaks down.
