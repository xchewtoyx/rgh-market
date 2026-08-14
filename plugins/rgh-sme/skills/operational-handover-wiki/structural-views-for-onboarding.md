---
type: concept
title: Structural Views for Onboarding
description: A newcomer needs at least three different diagram types, not one, because each answers a different orientation question a single "architecture diagram" can't cover on its own.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 2"
---

A single architecture diagram cannot orient a new operator, because "how the system is built" splits into at least three genuinely different questions, each best answered by a different kind of view:

- **A module/decomposition view** answers "who owns what, and what's the project's team structure?" — it maps onto work assignment and is usually the closest thing to how the source tree and the team's org chart are organized.
- **A component-and-connector (runtime) view** answers "how does this actually operate — what talks to what while it's running, and where does data flow?" — this is what a newcomer needs to troubleshoot a live system, as opposed to reading its source.
- **An allocation/deployment view** answers "where does my piece actually run, and how does it get there?" — which processor, container, or environment a given element lands on, and how it's built/tested/deployed along the way.

## Why This Matters for Handover

A handover package that includes only one of these (commonly just the module/source-tree view, because it's the easiest to generate) leaves the incoming operator unable to answer the other two questions and forces them to reconstruct a runtime or deployment mental model by trial and error. Deciding which of the three a given onboarding document needs is itself part of scoping the document: a [guided tour](guided-tours-and-sightseeing-maps.md) through the source answers the module question; a [system baseline](system-baseline-for-troubleshooting.md) of normal runtime behavior answers the runtime question; a [runbook](runbook-checklist-design.md) typically encodes the deployment question (where things run, how to redeploy them). None of the three substitutes for the others, and a maintainer who has internalized only the module view but is handed a live incident is missing exactly the view they need at that moment.

This is a companion to [Telling the Story of the System](telling-the-story-of-the-system.md): the "story" exercise builds one shared narrative, but that narrative still has to draw on whichever of these three structural lenses the current question actually calls for. It also underlies [Tailoring Documentation to Recipient Role](tailoring-documentation-to-recipient-role.md): different recipients of a handover need different combinations of these views, not just different levels of detail on the same one.
