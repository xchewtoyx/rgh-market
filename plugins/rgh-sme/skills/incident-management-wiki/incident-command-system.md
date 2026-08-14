---
type: concept
title: Incident Command System
description: A flexible incident management framework that uses explicit role separation to coordinate response under stress.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 14"
  - title: "Building Secure and Reliable Systems"
    resource: "Building Secure and Reliable Systems (Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield), ch. 17"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren), ch. 19"
  - title: "The Site Reliability Workbook"
    resource:
      "The Site Reliability Workbook: Practical Ways to Implement SRE (Betsy
      Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen
      Thorne), ch. 9"
  - title: "Team Topologies"
    resource: "Team Topologies, Second Edition (Matthew Skelton, Manuel Pais), ch. 5"
  - title: "Incident Management for Operations"
    resource: "Incident Management for Operations (Rob Schnepp, Ron Vidal, Chris Hawley), ch. 2, ch. 4"
---

The **Incident Command System (ICS)** coordinates incident response by separating strategic leadership from tactical technical execution:
* **Incident Commander (IC)**: Leads the response, sets overall strategy, assigns roles, and coordinates leads. The IC does *not* execute technical fixes.
* **Operational Lead (OL)**: Manages technical mitigation, directs debugging teams, and executes runbooks.
* **Communications Lead (CL)**: Handles internal and external communications, updates status pages, and manages notifications.
* **Remediation Lead (RL)**: Formulates the cleanup and recovery plan while the investigation is ongoing.
* **Liaison Officer (LNO)**: A role designated to handle incoming inquiries and shield primary responders from blunt-end executive interruptions — see [liaison officer role](liaison-officer-role.md) for how it functions as the IC's dedicated communication channel to another group.
* **Group Leader (GL)**: When several responders from the same function (e.g., three database engineers) join, the IC can appoint one as Group Leader, move that group to its own channel, and require only the GL to report back — this is how [span of control](span-of-control.md) stays manageable as an incident grows.
* **Scribe / Situational Status (SitStat)**: Documents responders, timeline, assignments, and actions taken as the incident unfolds — the record a later [after action review](after-action-review.md) is built from. As a supportive rather than problem-solving function, the scribe role doesn't count against the IC's own span of control.
* **Plans Group**: On large or complex incidents, a group of SMEs assigned to war-game alternative resolution paths (Plan B, C, D) while listening to — but not interrupting — the current plan's execution.

### Incident Management Workflows
ICS relies on clear handoff protocols during multi-hour outages (limiting shifts to 12 hours to prevent fatigue) and maintaining a central incident workspace (chat room and a live [incident state document](incident-state-document.md)). Responders should establish **parallel workstreams** running uninterrupted between scheduled status updates, ensuring that specialists can focus on debugging without interruption. For incidents that run long, rotating the IC and responders on a shorter cycle (e.g., every 4 hours) keeps decision-making sharp with rested people and fresh perspective, distinct from the outer 12-hour shift-handoff boundary. Decisions should always be recorded in the incident channel itself (not just spoken aloud), since that record becomes the timeline a [blameless postmortem](blameless-postmortems.md) is built from.

ICS must be declared early when system behavior is uncertain, and formally de-escalated once the system stabilizes. Modern incident management frameworks (such as CSG's post-2/4 outage model, developed in collaboration with Adaptive Capacity Labs) highlight that having a clearly authorized incident commander with unambiguous decision authority is essential for stabilizing complex failures. See [early incident declaration](early-incident-declaration.md) for why declaring promptly matters more than declaring with certainty.

Readiness pays off before an incident starts: pick and practice the incident communication channel in advance so no IC has to decide this mid-incident, pre-draft status-update templates, and maintain a standing contact list for "all hands on deck" escalations — see [extended "all hands on deck" response mode](extended-all-hands-response-mode.md) for how to run that kind of escalation without it becoming permanent. Keep stakeholders proactively informed during response — silence reads as "nothing is being done" and invites people to fill the gap with their own assumptions.

See [decentralized crisis response](decentralized-crisis-response.md) for why the IC's role should stay coordinating and logistical rather than becoming a bottleneck that frontline responders wait on for every decision.

### Team ownership and cross-team swarming

Day-to-day support should stay aligned to whichever team owns the affected
stream, rather than living in a separate, centralized support org — this
keeps each team accountable for the operability of what it builds. But when
an incident's blast radius crosses stream boundaries, the response should
form a dynamic, ad hoc "swarm" pulling in members from every affected
team's support function, rather than trying to force the incident through
any single team's normal chain. This also has a training benefit: including
less-experienced frontline responders in a cross-team swarm exposes them to
knowledge they'd otherwise only pick up much later. Whether an incident
needs this kind of swarm — versus staying within one team's normal
response — is itself a quick, useful triage question to ask before
assigning an incident commander.

### Assigning the Incident Commander
When a single team's ownership is unclear, assign the IC role to whoever has
the clearest visibility into customer impact, not necessarily whoever owns
the affected component — that team can see the blast radius most directly
and is best placed to coordinate the others. When multiple teams must
coordinate under one IC and a piece of cross-team work has no obvious owner
(e.g., an action that touches several teams' systems), the IC should
explicitly delegate a named coordinator for it rather than leaving it
ambiguous.

### The Three Cs
Most incident-response failures trace back to a breakdown in one of three
basic functions: **Coordinate** (keeping responders working the right
problems without duplicating or blocking each other), **Communicate**
(keeping the IC, responders, and stakeholders informed as the incident
evolves), and **Control** (maintaining a clear line of command so decisions
get made and don't stall). Diagnosing a struggling incident response often
means asking which of the three broke down.
