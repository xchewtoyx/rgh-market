---
type: concept
title: Landing Pages as Traffic Cops
description: >
  A landing page's only job is to state its purpose and route readers
  to the right next page — any content that does more than link onward
  belongs on a destination page instead.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

Team and product landing pages degrade easily into a pile of "read this first!" links, mixed customer and team information, and half-written overviews — partly because they are cumbersome to maintain and only get fixed when someone is already desperate. The fix is strict scope: **a landing page states its purpose and contains links to other pages.** If something on the landing page is doing more than routing traffic, it is not doing its job; move that content to a page with a single, substantive purpose.

When link volume grows past a screen or two, break the page up by taxonomy or section rather than accumulating an endless scroll. **Do not serve both a product's customers and its owning team from one landing page** — what maintainers need (process, on-call, internal design history) differs from what API users need (getting started, reference, support). Give each audience its own entry point. This is a specialization of the general rule to [keep each page focused on one purpose](organizing-documentation-by-user-goals.md); landing pages fail most often when they try to be conceptual overviews, tutorials, and team wikis at once.
