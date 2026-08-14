---
type: concept
title: Span of Control
description: The practical limit — roughly 5 to 7 people — on how many responders one person can effectively manage during an incident, and how to preserve it as an incident grows.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 4"
---

**Span of control** is the maximum number of people one person can
effectively manage at once — a norm of roughly 5 to 7, not an absolute
limit. It exists because humans have finite capacity to track simultaneous
conversations and tasks under stress; a channel with thirty unstructured
participants degrades into noise and wastes time no one can recover.

The technique for preserving span of control as an incident scales is
functional grouping: when one function grows past a manageable size (say,
five database engineers joining), the [incident
commander](incident-command-system.md) appoints a group leader for that
function, moves the group to its own channel, and requires only the group
leader to report back — the group's members return to only the group
leader, not the IC directly. This is the same mechanism [Unified
Command](unified-command.md) uses at a larger scale, where each business
unit's group leader reports through the IC to the Unified Command Leader.

A few supporting roles are deliberately exempt from counting against span
of control because they're supportive rather than problem-solving:
[scribe/SitStat](incident-command-system.md), [liaison
officer](liaison-officer-role.md), and the Plans group. This lets an
incident's org chart grow considerably wider without the commander's own
direct span growing past the point of effectiveness. Naming positions by
function rather than by person (Database, not "Alice") also matters here —
the org chart holds steady even as the specific person filling a role
changes through [transfer of command](transfer-of-command.md) or shift
rotation.

The authors argue for practicing this structure even on trivial incidents,
not reserving it for major ones, because the skill is built through
repetition — if a command structure is only invoked under real pressure,
the muscle memory isn't there when it matters most.
