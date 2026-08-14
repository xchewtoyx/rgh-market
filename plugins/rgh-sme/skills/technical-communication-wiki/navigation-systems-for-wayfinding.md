---
type: concept
title: Navigation Systems for Wayfinding
description: >
  Navigation has to answer four questions for a reader at any point in a
  document set — where am I, what else is here, where can I go, how do
  I get back — combining global, local, and contextual navigation rather
  than relying on any one of them alone.
sources:
  - title: "Information Architecture: For the Web and Beyond, Fourth Edition"
    resource: "Information Architecture (Rosenfeld, Morville, Arango), ch. 8"
---

Navigation exists to give a reader a sense of course, position, a way back, context, and comfort inside a body of content — not just links to click. A useful test of whether navigation actually works: drop a reader on a random page deep inside the content, with no path in from the top, and ask them to identify where they are, what section contains this page, and where they could go next. If they can't answer from the page's own navigation cues, the navigation has failed regardless of how complete the underlying content is. This "placemaking" requires a few concrete, checkable things to be present on every page: a persistent sense of overall identity, a visible position in the hierarchy, descriptively named destinations rather than generic ones ("more" or "details" tell a reader nothing), and some form of "you are here" indicator.

Well-built navigation normally combines three distinct kinds, embedded together rather than substituting for each other: **global navigation** gives site-wide access and orienting context from anywhere; **local navigation** covers the immediate subsection a reader is currently in, and can reasonably differ in structure from one subsection to another as long as that divergence is deliberate rather than arbitrary (an arbitrary difference between two similar sections disorients readers who expect consistency); **contextual navigation** surfaces editorially or algorithmically related material at the point where a reader would actually want it, supporting associative discovery the fixed hierarchy doesn't capture. Every page deep in a content set is a potential entry point for a reader arriving from a search engine or a shared link with no other context, so it should carry enough of all three kinds to reorient a reader who has never seen anything else in the set.

Hierarchy alone doesn't scale to every situation, and several supplemental systems fill the gaps it leaves: a sitemap reinforces the hierarchy and supports exploration for a reader who wants an overview; an alphabetical index lets a reader who already knows the specific term they want bypass the hierarchy entirely; and a short, self-contained guide can introduce a topic, audience, or task without requiring the reader to already understand the broader structure. Search functions as a form of navigation too — but it supplements rather than substitutes for a well-built navigational structure, and its absence or weakness shouldn't be papered over by adding a search box; see [organizing documentation by user goals](organizing-documentation-by-user-goals.md) for the related point that search behavior itself (the exact terms readers type, including their failed searches) is a direct source of evidence for where the navigation and labeling need to improve.
