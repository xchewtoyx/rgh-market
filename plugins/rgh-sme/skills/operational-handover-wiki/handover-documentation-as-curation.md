---
type: concept
title: Handover Documentation as Curation
description: Approaching handover documentation as selecting and arranging existing knowledge for people who weren't present, adding only what's genuinely missing, rather than authoring a new account from scratch.
sources:
  - title: "Living Documentation"
    resource: "Living Documentation (Martraire), ch. 5"
---

By the time a handover happens, most of the knowledge a new owner needs already exists somewhere — in code, commit history, tickets, existing docs, and the heads of people who were there. Producing good handover material doesn't mean writing it all again from a blank page. It means acting as a curator: select the pieces of existing material that matter, arrange them into a route a newcomer can follow, and add only the connective tissue that's genuinely missing — the same posture an exhibition preparer takes toward an existing collection, not that of an author inventing new content.

## What This Changes in Practice

- **Start from an inventory, not a draft**: before writing anything new, identify what already documents the system — READMEs, design docs, dashboards, past incident write-ups, the code itself — and treat the handover task as selecting and connecting these, not replacing them.
- **Add only the gaps**: write new material specifically for what the existing artifacts don't cover, rather than re-explaining what a linked source already explains well. This keeps the handover document itself small and keeps it from drifting out of sync with the sources it would otherwise duplicate.
- **Curate for someone who wasn't there**: judge the selection and arrangement by whether it lets a newcomer make sense of the system, not by whether it's a complete archive — deliberately allocate the incoming owner's limited attention toward the material that will orient them fastest.
- **Serve posterity, not just the immediate transfer**: material curated this way should remain useful to the person after the incoming owner too, not just answer today's handover — this favors linking to durable existing sources over transient summaries.

For a concrete curated format that puts this into practice, see [Guided Tours and Sightseeing Maps](guided-tours-and-sightseeing-maps.md). For deciding which of the missing pieces are actually worth writing down permanently rather than explained live, see [Just-in-Time Documentation Triggers](just-in-time-documentation-triggers.md).
