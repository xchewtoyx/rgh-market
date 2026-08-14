---
type: concept
title: Seekers Versus Stumblers
description: >
  Seekers know what they want and scan for a match; stumblers have only
  a vague goal and need orienting overviews — reference material should
  optimize consistency for seekers, introductions and TL;DRs for stumblers.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Audience analysis is not only *who* reads a document but *how* they encounter it. Two reader modes show up constantly:

**Seekers** already know roughly what they need and are checking whether this page or API is the right one. For them, **consistency is the key device** — reference comments, function listings, and API pages that follow the same format let a reader scan vertically and decide relevance fast (see [scan-friendly function comments](scan-friendly-function-comments.md)).

**Stumblers** have only a vague idea of what they want. For them, **clarity at the threshold matters** — overviews at the top of a file or page, explicit statements of purpose, and TL;DR flags that say when a document is *not* for this reader so they can leave without wading in.

The same documentation set usually needs to serve both modes: seekers deep in reference material, stumblers at landing pages and introductions. See [landing pages as traffic cops](landing-pages-as-traffic-cops.md) for routing stumblers, and [organization schemes and structures](organization-schemes-and-structures.md) for exact versus ambiguous browse paths.
