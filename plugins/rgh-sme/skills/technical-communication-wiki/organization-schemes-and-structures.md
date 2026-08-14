---
type: concept
title: Organization Schemes and Structures
description: >
  Content can be organized by an exact scheme (alphabetical, chronological)
  that suits readers who already know what they want, or an ambiguous
  scheme (topical, task-based, audience-based) that supports browsing —
  and mixing the two inside one structure destroys the reader's mental
  model.
sources:
  - title: "Information Architecture: For the Web and Beyond, Fourth Edition"
    resource: "Information Architecture (Rosenfeld, Morville, Arango), ch. 6"
---

Organizing a body of content means choosing a **scheme** — the shared characteristic used to group items — and a **structure** — the relationships between those groups. **Exact schemes** (alphabetical, chronological, geographic) divide content into well-defined, mutually exclusive categories and work well when a reader already knows the specific item they want and just needs to locate it. **Ambiguous schemes** (topical, task-based, audience-based, metaphor-based, or some hybrid of these) group content by looser, more interpretive similarity, and support browsing and associative discovery for a reader who can't yet articulate exactly what they're looking for — but because they're interpretive, they need real user testing and ongoing maintenance to stay usable, unlike an exact scheme whose correctness is close to mechanical.

A shallow hybrid — surfacing a few high-priority tasks or topics as an addition to a primary scheme — can work well, but deeply blending two different schemes into one structure tends to destroy the reader's mental model rather than serve two audiences at once; keep genuinely distinct organizational schemes visibly separate from each other rather than merging them.

The three primary structures for relating groups to each other are hierarchy, database/relational structure, and hypertext. **Hierarchy** is the most familiar to readers, but has to balance breadth against depth — a reader can tolerate more choices at once (breadth) more easily than more levels to descend through (depth) up to a point, but there's no universal rule for exactly where that point is; test rather than apply a fixed link-count limit, and use deliberate cross-listing where one item genuinely belongs in more than one branch. **Database-style structure**, built on consistent metadata, supports dynamic search, filtering, and generated links that a fixed hierarchy can't. **Hypertext** — flexible, associative links between related items — is valuable but provides no orienting context of its own, so it normally works best layered on top of a hierarchy rather than replacing one; a reader who arrives via a hypertext link with no surrounding hierarchy has no way to tell where they are. A cohesive, well-built information structure typically mixes exact and ambiguous schemes and hierarchical, database, and contextual structures suited to each of its subdomains, rather than forcing one uniform scheme across genuinely different kinds of content. See [organizing documentation by user goals](organizing-documentation-by-user-goals.md) for the same discipline applied specifically to a technical documentation set, and [imposing logical order on groupings](imposing-logical-order-on-groupings.md) for the equivalent ordering discipline within a single document rather than across a whole content set.
