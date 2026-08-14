---
type: concept
title: Live Knowledge Transfer Techniques
description: Structured collaborative sessions that transfer tacit system knowledge during a handover more reliably than written documentation alone.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 10"
---

Written documentation is easily misread or misunderstood — the same message reliably produces multiple different interpretations across different readers. For the tacit knowledge that matters most during a handover (the reasoning behind a decision, the gotchas an operator would otherwise rediscover the hard way), live collaborative sessions transfer this kind of knowledge more reliably than a document one person wrote and another later reads cold.

## Techniques

- **Pairing / mob programming**: The outgoing and incoming owners work through real tasks together at the same keyboard (pairing) or as a full group (mobbing), so tacit knowledge surfaces naturally in context rather than needing to be anticipated and written down in advance.
- **Three Amigos**: A short structured conversation bringing together a business/product perspective, a development perspective, and a testing perspective on a specific piece of functionality before it's built or before it's handed off, surfacing gaps that any single perspective would miss.
- **Event Storming**: A collaborative, workshop-style mapping of a system's events, commands, and domain boundaries, done as a group exercise rather than read from a diagram — the shared act of building the map transfers understanding that a finished diagram alone doesn't.
- **Dedicated knowledge-transfer sessions**: Time explicitly set aside (not squeezed into an unrelated meeting) for the outgoing owner to walk the incoming owner through the system, prioritizing questions the incoming owner raises over a pre-scripted agenda.
- **Guided tours**: A live, narrated walkthrough of the running system or codebase led by someone who knows it, rather than a document describing it — lets the incoming owner ask "what's that" in the moment instead of trying to reconstruct the same understanding from prose later. For a written, reusable version of this that outlives the live session, see [Guided Tours and Sightseeing Maps](guided-tours-and-sightseeing-maps.md).
- **Decision log walkthroughs**: Reviewing the record of past significant decisions together with the person who made them, so the incoming owner gets the reasoning behind a choice, not just the choice itself — this is what makes a decision log useful for handover rather than just an audit trail.
- [Telling the Story of the System](telling-the-story-of-the-system.md): A structured, incremental exercise where someone explains the architecture starting from only the essential concepts, forcing a separation of what matters from what's merely expedient detail.

## Sequencing: Understanding Before Artifacts

A handover works best when it proceeds through these live techniques first — conversation, debrief, guided code discussion, decision log review, guided tour — and only then moves to written artifacts. Shared understanding built through live interaction gives the incoming owner the context needed to actually make sense of the written documentation afterward; handed a stack of documents with no live grounding first, they have no way to judge what's central versus incidental.

## When to Prefer These Over Writing More Documentation

These techniques are most valuable for exactly the knowledge that's hardest to write down well: reasoning that depends on context, judgment calls that don't reduce to a rule, and the kind of "here's what actually happens" detail that only comes up when someone tries to do the task. Reserve written documentation for what genuinely needs to persist and be looked up later — see [Just-in-Time Documentation Triggers](just-in-time-documentation-triggers.md) for deciding when a piece of knowledge has proven itself worth writing down permanently.

For a more front-loaded alternative when the same expertise needs to be captured once and reused across many future hires rather than transferred to a single incoming owner, see [Cognitive Task Analysis for Capturing Tacit Expertise](cognitive-task-analysis-for-tacit-expertise.md).
