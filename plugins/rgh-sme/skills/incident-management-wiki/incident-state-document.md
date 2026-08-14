---
type: concept
title: Incident State Document
description: A single live document maintained throughout an active incident that separates fixed facts from evolving hypotheses so responders share one picture of the incident.
sources:
  - title: "Site Reliability Engineering"
    resource: "Site Reliability Engineering (Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy), Appendix C"
---

The **incident state document** is the artifact the [incident command
system](incident-command-system.md)'s central incident workspace is built
around — updated live, in place, rather than reconstructed from memory
afterward. It typically holds five sections:

- **Incident summary**: a short, current statement of the problem and status,
  rewritten as understanding improves rather than left as the initial guess.
- **Roles**: who is filling each ICS role right now (incident commander,
  operational lead, communications lead), so a responder joining mid-incident
  can immediately see who to report to and who owns what.
- **Impact summary**: quantified current user impact — percentage of traffic
  affected, error rates, which services — kept current so severity and
  communications decisions are grounded in numbers rather than impression.
- **Timeline**: a chronological log of events, hypotheses considered, and
  actions taken, written as they happen rather than reconstructed afterward.
  This running log is what a [blameless postmortem](blameless-postmortems.md)
  is later built from, which is why decisions belong in the document itself
  and not only spoken aloud in a call.
- **Active hypotheses and action items**: what's currently being
  investigated or tried, with an owner attached to each, so two responders
  don't unknowingly duplicate or contradict each other's work.

Separating "what we know" (summary, impact) from "what we're trying" (active
hypotheses) matters most for a document that is being edited live by several
people at once: it keeps a half-confirmed theory from being read as settled
fact by someone glancing at the document mid-incident, which is the same
failure mode [emergency response triage](emergency-response-triage.md) warns
against when it insists on mitigating a *possible* cause rather than waiting
for a confirmed one — the document has to make that distinction visible, not
just the responders' heads.
