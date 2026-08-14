---
type: concept
title: Crew Resource Management
description: A commercial-aviation practice of deliberately flattening hierarchy during an active emergency so any team member can raise a safety concern regardless of rank.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), ch. 33"
  - title: "The Checklist Manifesto"
    resource: "The Checklist Manifesto: How to Get Things Right (Atul Gawande), ch. 5, ch. 7, ch. 8"
---

**Crew Resource Management (CRM)** originated in commercial aviation after
accident investigations found that junior crew members had noticed problems
but deferred to a captain's authority instead of speaking up. CRM
deliberately flattens the hierarchy during an emergency: any crew member,
regardless of rank, is expected — and trained — to voice a safety concern,
and senior figures are trained to invite and act on that input rather than
treat it as a challenge to their authority.

The same dynamic threatens incident response: a junior responder who
notices a problem with the [incident commander](incident-command-system.md)'s
plan may stay quiet out of deference, even when speaking up would shorten
the outage. Building CRM-like norms — explicitly inviting dissent,
rewarding it when it happens, and training the behavior before an incident
rather than hoping for it in the moment — turns [chronic unease](chronic-unease.md)
from an individual disposition into a team-level practice that functions
under real time pressure.

### A concrete mechanism: who calls the checklist

CRM's hierarchy-flattening can be built into a process, not just hoped for
as a norm. Aviation's "pilot not flying" convention has one pilot fly the
aircraft while the other runs the checklist and monitors — deliberately
separating execution from verification. The WHO Safe Surgery Checklist
adopted the same structural move: the circulating nurse, not the lead
surgeon, is designated to initiate and run the checklist. Assigning that
role to someone other than the most senior person in the room removes the
need for a junior team member to *interrupt* authority in order to invoke
a safety check — the check is already theirs to run. The equivalent move
in incident response is deciding, before an incident, who is authorized to
call for a pause or invoke a [runbook](runbooks-and-checklists.md) step
regardless of who else is in the room.

Early trials of structured pre-briefings found the same team effect outside
aviation: a Johns Hopkins pilot raised the share of surgical staff who felt
their team "functioned as a well-coordinated unit" from 68% to 92% in three
months, and a larger Kaiser Southern California rollout across 3,500
operations dropped OR nurse turnover from 23% to 7% and caught concrete
near-misses (a mislabeled drug vial, a procedure planned for the wrong
patient) that no individual checklist item was specifically designed to
catch — they surfaced because the team was talking to each other at a
mandatory checkpoint.

Two contrasting aviation cases show the stakes. At Tenerife in 1977, the
deadliest accident in aviation history, a captain disregarded an ambiguous
air-traffic-control clearance and his own second officer's audible doubt —
the second officer had never come to believe he had standing to *halt* the
captain, and 583 people died. By contrast, when Captain Sullenberger and
First Officer Skiles ditched US Airways Flight 1549 in the Hudson River in
2009, they had never flown together before that trip; a short structured
pre-flight briefing (introductions, plans, contingencies) turned two
strangers into a functioning crew within minutes, well before the birds hit
the engines. That kind of team formation — done deliberately, before a
crisis, not improvised during one — is exactly what [preparedness
drills](preparedness-drills.md) and pre-established incident roles are for.
