---
type: concept
title: Selecting Content by Stakeholder Concerns
description: >
  Choose what a technical document covers by mapping each intended
  reader to their specific concerns and the questions or tasks they need
  the document to support, then covering the smallest set of content
  that answers all of them.
sources:
  - title: "Documenting Software Architectures: Views and Beyond"
    resource: "Documenting Software Architectures (Clements, Bachmann, Bass, Garlan), ch. 9"
---

A technical document's content should be driven by its readers' concerns, not by a fixed checklist of sections a document of that type is "supposed to" have. Different roles reading the same underlying system genuinely need different things from documentation about it — one stakeholder needs the decomposition and interfaces to build against, another needs behavior and failure modes to test against, another needs deployment and installation detail to operate it, another needs assignment and schedule information to manage it, and another needs context and capability to evaluate whether it does what they need at all. A single document trying to serve all of these audiences at once with one flat structure usually serves none of them well.

The selection method: list the actual stakeholders and, for each, their specific concerns and the questions or tasks they need to accomplish using the document; map each concern to the piece of content or type of view that would answer it; select the smallest set of content that covers every mapped concern, rather than defaulting to comprehensive coverage; prioritize and organize what's selected; and validate the resulting selection with the actual stakeholders before treating it as final, since concerns are easy to guess wrong from the writer's side. This mapping isn't a one-time exercise — revisit it as requirements and the audience itself change, since a document scoped correctly at launch can quietly become miscalibrated as its readership shifts.

The diagnostic for whether something is missing follows directly from this method: a gap is a real risk only if it leaves some stakeholder's concern uncovered, not merely because a topic that could theoretically be documented hasn't been. This reframes "what should this document cover" from an open-ended completeness question into a closed, checkable one — has every stated concern actually been mapped to content that answers it — which is a more tractable question to actually resolve. See [choosing documentation types](choosing-documentation-types.md) for the parallel technique of matching a document's *type* to what a reader needs from it, and [the curse of knowledge and audience research](curse-of-knowledge-and-audience-research.md) for how to find out what those concerns actually are in the first place.
