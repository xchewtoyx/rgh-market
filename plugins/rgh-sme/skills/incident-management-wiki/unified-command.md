---
type: concept
title: Unified Command
description: A meta layer above single-team incident command that lets multiple business units converge on one incident action plan when an incident's impact or decision needs cross organizational boundaries.
sources:
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 5"
---

**Unified Command (UC)** is a group of senior business and technology leaders
who converge on a single set of objectives and a single incident action
plan when an incident's impact or required decisions cut across multiple
business units ("kingdoms"). The framing: the [incident command
system](incident-command-system.md) manages people and teams *within* a
kingdom; UC manages *across* kingdoms. Not every organization needs it —
only ones where incidents routinely cross business-unit lines or carry
business impact beyond what a single [incident
commander](incident-command-system.md) can resolve alone.

UC activates typically for two reasons: multiple technically viable
resolution paths exist with different business consequences and someone
with business authority needs to pick between them (while the IC and
responders keep executing, not debating policy); or the incident needs
rapid decisions across the company, or with outside parties like customers
or regulators, faster than the normal chain of approval allows. Once
activated, the division of labor is explicit: **incident responders resolve
the technical problem, UC supports the incident commander, and — if UC
escalates further to a Tier 1 notification of the company's most senior
executives — those executives set policy and direction, not the fix
itself.** No layer in this structure ever takes independent action outside
the consolidated incident action plan.

Coordination runs on a repeating cycle nicknamed the **Planning Wheel**: the
IC sends a [CAN report](can-report.md) to the Unified Command Leader (UCL,
the person who leads the UC group when more than one person is convened);
the UCL decides whether to loop in the On-Call Executive (OCE) with the same
CAN-report structure; direction flows back down through the UCL to the IC;
that direction gets executed for an operational period; and the cycle
repeats with a fresh SitStat briefing. The wheel "spins as fast as it needs
to" — from minutes to weeks — depending on incident severity.

Structurally, activating UC changes the org chart: instead of the IC
managing SME resources directly, each involved business unit organizes its
own responders under its own group leader (see [span of
control](span-of-control.md)), who reports through the IC up to the UCL.
Information between the IC's technical channel and the UC group flows
through a dedicated [liaison officer](liaison-officer-role.md) rather than
merging the two channels, which keeps the technical bridge free of
strategic debate the IC has no bandwidth to also manage. As with the base
incident command system, UC's own effectiveness depends on pre-incident
setup — knowing in advance who the UCL and OCE are, how they're reached
24x7, and what triggers activation — rather than being improvised the first
time a cross-kingdom incident actually happens.
