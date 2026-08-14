---
type: concept
title: Curating Guides Over Duplicating Content
description: >
  When authoritative material already exists but is scattered or
  hard to approach, write a short guide that points into it — a
  sightseeing map or guided tour — rather than duplicating it into a
  new, separately maintained document.
sources:
  - title: Living Documentation
    resource: "Living Documentation (Cyrille Martraire), ch. 5"
---

When the underlying material a reader needs already exists — in source code, in a large reference corpus, in scattered authoritative documents — the temptation is to write a new document that re-explains it. That new document immediately becomes a second thing to keep in sync with the original, and it usually loses the sync battle. The alternative is to curate rather than duplicate: write something short that points a reader into the existing material, rather than restating that material's content.

Two useful shapes for this: a **sightseeing map** orients a newcomer by pointing out the significant places and how they relate to each other, without trying to be exhaustive — its job is orientation, not coverage. A **guided tour** goes further, giving a reader a purposeful route through existing material, explaining at each stop what to notice and why it matters, the way a human guide would walk someone through a place they don't yet know. Both stay "living" specifically by linking directly to the actual source rather than reproducing it, so they need only light, occasional refreshing as the source evolves — the guide is an interpretation layered over existing material, not a parallel copy of it.

This is a curation discipline as much as a writing one: deliberately selecting and arranging what already exists, adding only the connective explanation that's genuinely missing, rather than treating every fact as equally worth restating. It's also an explicit acknowledgment that reader attention is limited — a guide's value comes from choosing what to highlight, not from trying to cover everything the underlying material contains. See [maintaining and deprecating documentation](maintaining-and-deprecating-documentation.md) for the related failure mode this avoids — duplicate content silently drifting out of sync with its authoritative source — and [organizing documentation by user goals](organizing-documentation-by-user-goals.md) for the broader discipline of structuring a document set around what a reader is trying to do rather than around what already happens to exist. See [single source with pointer references](single-source-with-pointer-references.md) for the same point-rather-than-copy discipline applied one level down, to an explanation that recurs at several places inside one document set rather than to an entire external corpus.
