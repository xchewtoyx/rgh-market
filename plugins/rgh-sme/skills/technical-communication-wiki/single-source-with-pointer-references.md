---
type: concept
title: Single Source With Pointer References
description: >
  When several places need the same explanation, write it once at
  whichever spot is the most natural anchor and point every other
  location back to it — a broken pointer fails loudly, where a
  duplicated copy fails silently by quietly drifting out of sync.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 13, ch. 16"
---

When the same explanation is genuinely needed in several places, the instinct to copy it into each one creates a maintenance trap: every copy is a separate thing to keep in sync, and nothing about a duplicated copy signals when it's fallen out of date with the others — they can silently diverge for a long time before anyone notices which version, if any, is still correct. The fix is to write the explanation exactly once, in whichever single place is the most natural home for it, and have every other location that needs it carry a short pointer back to that one place rather than its own copy of the content.

Finding the natural anchor is usually straightforward: attach the explanation to whatever a reader investigating the topic would check first — a declaration, a definition, the one place in a system every related change is guaranteed to pass through. Sometimes no single natural anchor exists at all, because the concept genuinely spans several unrelated places with no shared home; in that case, pick a dedicated location for the explanation (a single reference document or section) and have every dependent site point to it by name, rather than trying to force the explanation into one of the dependent sites where the others won't think to look.

The pointer approach has a structural advantage duplication can't match: if the master explanation moves, gets renamed, or is deleted, a stale pointer becomes immediately and visibly broken — a reader following it finds nothing, notices right away, and can track down what happened. A duplicated copy has no equivalent failure signal; it just keeps existing, quietly wrong, looking exactly as authoritative as it did before it drifted. This is the same logic behind [curating guides over duplicating content](curating-guides-over-duplicating-content.md) — pointing into authoritative material rather than restating it — applied one level down, to explanations that recur inside a single document set or codebase rather than to an entire external corpus.
