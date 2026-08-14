---
type: concept
title: Scenario for a Business Use Case
description: >
  A scenario is a step-by-step narrative of how a business use case plays
  out — normal flow, exception flows, and pre/postconditions — that
  bridges an abstract requirement and a concrete, checkable understanding
  of it.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 6"
---

A scenario is a step-by-step narrative describing how a [business use
case](business-event-and-use-case.md) is actually carried out. It exists
to bridge an abstract requirement statement and a concrete enough
description that a stakeholder can confirm "yes, that's what should
happen" or "no, that's wrong" — see [requirements discovery vs.
gathering](requirements-discovery-vs-gathering.md) for why concrete
walkthroughs surface understanding that abstract descriptions don't.

A scenario has a **normal flow** (the happy path, written as a simple
numbered sequence), **exception flows** (specific handling for each
identified error or unexpected condition, numbered against the step they
branch from), and explicit **preconditions** and **postconditions** (the
state required before the scenario can start, and the state reached when
it successfully completes). Storyboards, wireframes, and use-case or
activity diagrams are common supporting notations for walking a scenario
with a stakeholder.

A useful further distinction within scenario-writing is **essential**
versus **implementation** scenarios: an essential scenario describes pure
business intent independent of technology ("verify driver identity"), an
implementation scenario describes the technology-specific execution
("driver scans RFID badge on cab scanner"). Writing the essential version
first is the same discipline as [essence of the business
work](essence-of-the-business-work.md) applied at scenario granularity —
it keeps the scenario from silently becoming a specification of a
particular solution before the requirement itself has been agreed. See
[executable specification](executable-specification.md) for scenarios
written precisely enough to run as automated acceptance tests rather than
only as a walkthrough narrative.
