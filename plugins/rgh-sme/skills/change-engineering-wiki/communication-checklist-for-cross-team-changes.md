---
type: concept
title: Communication Checklist for Cross-Team Changes
description: >
  For a change that touches a system shared across specialist teams, an
  explicit checklist of who must be consulted before implementation catches
  the risk that a purely technical checklist cannot.
sources:
  - title: "The Checklist Manifesto: How to Get Things Right"
    resource: "The Checklist Manifesto (Gawande), ch. 3"
---

# Communication Checklist for Cross-Team Changes

Not every change risk is a missed technical step; some are a missed
conversation. When a system is built and operated by multiple specialist
teams, each with narrow but deep expertise, a locally sound change can be
globally unsafe in a way no individual team can see from inside their own
domain — because the risk lives in the interaction between two teams'
work, not inside either team's part of it.

The failure mode this guards against: a team makes a substitution or
change that looks like a routine, within-scope decision from where they
sit, without a mandated check-in with the team(s) whose systems the change
actually affects. In the canonical case (a structural engineering
disaster in modern building construction), a contractor swapped welded
joints for bolted ones to cut cost — a change that seemed like a
same-spec substitution — without running it past the engineer who owned
the load calculations for the whole structure. The building came within
one bad storm of catastrophic failure before the gap was caught, entirely
by accident, months later.

The fix is a **communication checklist**: distinct from a checklist that
verifies technical steps within one team's control (`automation-engineering`'s
territory), a communication checklist specifies *who must talk to whom,
and when*, whenever a change crosses a boundary between specialist
domains. It doesn't tell anyone what the
right technical answer is — it forces the conversation that surfaces
whether there even *is* a cross-domain risk, decentralizing the judgment
call to the people who understand each side rather than assuming any one
team can see the whole picture.

This is the process-level counterpart to
[independent deployability](independent-deployability.md): independent
deployability reduces how often teams *need* to coordinate a change by
architecting the boundary out of the critical path; a communication
checklist is what catches the risk on the changes that still cross a
shared boundary despite that effort, because not every dependency between
services can be architected away.
