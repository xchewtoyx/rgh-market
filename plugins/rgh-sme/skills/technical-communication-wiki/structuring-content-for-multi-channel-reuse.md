---
type: concept
title: Structuring Content for Multi-Channel Reuse
description: >
  Plan content as small, structured chunks tied to a defined type rather
  than as one bespoke document per channel, so the same underlying
  content can be assembled into a website, an app, a voice response, or
  any future format without being rewritten for each.
sources:
  - title: "Designing Connected Content: Plan and Model Digital Products for Today and Tomorrow"
    resource: "Designing Connected Content (Mike Atherton, Carrie Hane), ch. 1, 3, 7"
---

Content written as a single unstructured block — a page authored in one big body field — looks fine to a human reader but is opaque to everything else: it can't be selectively reused, its pieces can't be individually updated, and adapting it for a different device or format means manually rewriting it rather than reassembling it. The alternative is to design content as small **chunks**, each holding one well-defined piece of a larger topic (a title, a description, a single fact), tagged with what it is and how it relates to other chunks. A **display template**, chosen per audience or channel, then pulls together whichever subset of chunks that context actually needs — a detailed reference page might show everything, a smaller-screen or voice representation might show only three or four of the same underlying chunks. This is the practical mechanism behind "create once, publish everywhere": a correction made once to a chunk propagates to every representation that uses it, instead of requiring the same fix to be hunted down and repeated across every channel-specific copy.

Deciding structure before deciding presentation — content, then interface, in that order — is a deliberate sequencing choice, not an incidental one: interface design changes fastest and most often, so committing to it first locks a document's structure to the needs of whatever medium happened to be designed first. Planning the underlying content structure independent of any one interface is what makes the same content genuinely portable to a format that didn't exist yet when the content was written.

**Finding the right chunk size** is a judgment call with real failure modes on both ends. Too large, and a chunk stops being focused enough to reuse on its own — it drags in material a given context doesn't need. Too small, and reassembling chunks into something coherent becomes expensive and the fragments lose their own sense on the page (over-chopped video, sliced into individual shots, becomes "moving wallpaper" rather than usable footage). The useful middle — sometimes called the **minimum reusable unit** — is the smallest chunk that is still self-contained enough to make sense as a standalone piece. A practical checklist for whether something is a good chunk: does it correspond to one well-defined piece of information; does it make sense (or at least isn't confusing) read in isolation; does it work across the different contexts it needs to appear in, or does it have a context-appropriate equivalent (an audio track plus a transcript, say); and does it provide genuinely useful supporting context wherever else it's reused. See [choosing documentation types](choosing-documentation-types.md) for the parallel discipline of matching a whole document's type to a reader's need, applied here one level down, to the pieces a document is composed from.
