---
type: concept
title: Formatting for Scanning
description: >
  Most readers scan a page rather than read it fully — one estimate puts
  it at under a third of the words, in an F-shaped pattern — so
  headings, short paragraphs, lists, and callouts have to carry
  structure that dense prose won't survive being skimmed.
sources:
  - title: "Docs for Developers: An Engineer's Field Guide to Technical Writing"
    resource: "Docs for Developers (Bhatti, Corleissen, Lambourne, Nunez, Waterhouse), ch. 3"
---

Readers arrive at a documentation page looking for an answer, not to read it end to end — one commonly cited estimate puts actual word-by-word reading at under a third of a page's content, following a rough F-shaped scan pattern (heavy attention at the top, decreasing attention down the left edge, less and less read across each line). This has direct formatting consequences, not just a general reminder to "be concise":

- **Headings** function as signposts and as search-result destinations at once — they should be brief, specific, unique within the page, worded consistently with each other, and lead with the most important information rather than burying it at the end of the heading.
- **Paragraphs** carry context but are slow to scan compared to lists or headings; keep them short, roughly five sentences or fewer, and put whatever answers "will this help me?" as early in the page as possible so a scanning reader can decide to keep reading or move on.
- **Procedures** belong in numbered lists that state the desired result and the starting state up front, give exactly one action per step, and end with a verification step the reader can check against — effectively a unit test for the instructions themselves, catching the case where the steps are individually correct but don't actually produce the promised outcome.
- **Unordered lists** are for related, non-sequential information, organized in whatever order helps the reader most (not just the order items came to mind); split any list that grows past roughly ten items into a smaller structure.
- **Callouts** interrupt the reader's flow, so they need to be reserved for cases that justify the interruption: warnings for danger or irreversible loss, cautions for unexpected but non-catastrophic consequences, and notes for genuinely useful adjacent information that isn't part of the main task. A friction log (see [documentation research artifacts](documentation-research-artifacts.md)) is a direct source for where callouts actually belong, rather than guessing.

If a page keeps resisting this kind of formatting — if it can't be broken into short paragraphs, clean lists, and a few well-placed headings without losing coherence — that's often a sign the page is trying to serve more than one goal and should be split, the same diagnosis as an unfocused title (see [drafting from an outline](drafting-with-outline-first.md)).

This scannability discipline assumes the material genuinely compresses without losing what matters. Where the underlying finding is complex or high-stakes and its credibility depends on caveats, magnitudes, or a chain of reasoning, compressing it into headings and bullets can silently discard exactly that material — see [bullet-point compression hides technical nuance](bullet-point-compression-hides-technical-nuance.md) for when to choose a fuller format instead.
