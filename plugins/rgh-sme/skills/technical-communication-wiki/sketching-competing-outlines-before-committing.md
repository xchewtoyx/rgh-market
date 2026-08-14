---
type: concept
title: Sketching Competing Outlines Before Committing
description: >
  A document's first structural idea is rarely its best one, so a hard
  structuring decision deserves two or three deliberately different
  outline sketches, compared before any is drafted into prose.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 11"
---

When a document's structure is genuinely hard to get right — competing candidate orderings, more than one plausible way to divide it into sections, an audience whose needs might be served several different ways — the instinct is to pick the first workable shape and start drafting prose around it. That instinct skips the cheapest part of the whole process: at the outline stage, a structure costs almost nothing to discard, while the same discovery made after paragraphs of prose have been written around it costs a rewrite. The fix is to sketch two or three genuinely different outlines for the same content before drafting any of them, the same way [drafting from an outline](drafting-with-outline-first.md) treats an outline as pseudocode specifically because it's cheap to rearrange.

The alternatives are only useful if they're **radically different** from each other, not minor variations on the same shape — a document ordered chronologically, one ordered by reader priority, and one built around a single central problem are different enough to actually teach something by contrast; three orderings that differ only in which paragraph comes second teach nothing. It's worth sketching a second outline even when the first already feels obviously right: articulating in a sentence or two *why* the alternative is worse than the first is often what turns a vague sense of "this structure feels right" into an explicit, checkable reason — and that reason is worth having before a stakeholder or reader asks for it later.

Evaluate each sketch against the same question that should have driven the choice in the first place: which shape serves the reader's actual patience and need to act, not which one was easiest to list out (see [matching document structure to reader patience](matching-document-structure-to-reader-patience.md)). The strongest outcome from comparing alternatives usually isn't picking one wholesale — it's noticing that two or three of them share the same underlying weakness (say, every candidate forces the reader to hold context from an early section to make sense of a late one) and using that shared flaw to drive a further structure that avoids it, rather than just choosing the least-bad of the original set.

This is worth the modest time cost specifically because structuring decisions compound: a document's shape, once drafted, is expensive to change, while comparing outline sketches for the same document might cost minutes against the hours the draft itself will take — cheap insurance for exactly the decision that's hardest to walk back later.
