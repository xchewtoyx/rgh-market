---
type: concept
title: Dedicated Function for Operational Learning
description: Assigning a specific team or role ownership of failure investigation and checklist/runbook revision, rather than leaving operational documentation to accumulate ad hoc.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 8"
  - title: "The DevOps Handbook"
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 19"
---

Assembling excellent individual components does not produce an excellent system — a car built from the world's best engine, brakes, suspension, and body from four different manufacturers is expensive junk, because no one owned making the parts work together. The same failure pattern shows up in operations: an organization can have skilled engineers, good individual runbooks, and thorough incident write-ups, and still have no institution responsible for turning those into a coherent, improving whole.

## The Missing Institutional Roles

Aviation avoids this gap by assigning specific, standing ownership to each of these functions. When taking over or maintaining a system long-term, check whether each of these roles exists and is actually staffed — not just whether the artifacts (runbooks, postmortems) exist:

- **Failure investigation**: A function equivalent to an accident-investigation board, whose job is specifically to determine root cause after operational failures — distinct from the team that experienced the failure and is busy remediating it.
- **Checklist/runbook design and dissemination**: A function equivalent to an airline's flight-operations group, whose job is to convert investigation findings into revised, distributed operational documentation — not leave each team to independently decide whether and how to update its own runbooks.
- **Outcome tracking**: Ongoing, month-to-month tracking of operational outcomes, so that whether the accumulated changes are actually improving reliability is measured rather than assumed.

## Make the Archive Itself Discoverable

The function needs more than a place to file postmortems — it needs those postmortems to be found again by someone who didn't write them. A wiki-page-per-incident archive that isn't searchable or taggable tends to accumulate write-only: teams see low returns on writing detailed retrospectives if no one before an incident thinks to check whether something similar happened previously. A searchable, centrally-indexed incident archive (tagged by system, severity, and symptom) makes "has this happened before" answerable in minutes rather than dependent on someone's memory — and observed practice is that easier-to-search tooling measurably increases how often teams bother writing retrospectives at all, particularly for the lower-severity incidents most likely to be skipped otherwise. Treat the archive's discoverability as part of the function's remit, not an afterthought to be solved once volume becomes unmanageable.

## Why This Matters for Handover

A handover is exactly the moment this gap becomes visible: a new team inherits the individual artifacts (runbooks, dashboards, postmortem archive) but not necessarily the standing function that keeps them current and coherent. If no one owns [postmortem-derived checklist items](postmortem-derived-checklist-items.md) as an ongoing process, the runbooks the new team receives are a snapshot that will start decaying immediately, with no mechanism to catch the decay. Confirm during handover who — which team or role — owns each of these three functions going forward, and make that ownership explicit rather than assumed.

This complements the mechanical maintenance practices in [Documentation Maintenance Workflows](documentation-maintenance-workflows.md) and the playbook-specific validation practices in [Playbook Maintenance Tension](playbook-maintenance-tension.md) — those describe what to do; this describes who is responsible for doing it.
