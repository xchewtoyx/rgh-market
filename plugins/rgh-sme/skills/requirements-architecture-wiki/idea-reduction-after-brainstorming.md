---
type: concept
title: Idea Reduction After Brainstorming
description: >
  A brainstormed idea set needs a separate, structured reduction pass —
  pruning, then a shared-understanding check, then a vote — before it can
  be prioritized, or the resulting ranking is built on mismatched
  assumptions about what each idea even means.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 12"
---

Generation and reduction are separate steps in
[brainstorming](requirements-elicitation-techniques.md), and skipping
straight from a raw idea list to a vote produces an untrustworthy ranking,
because participants are voting on their own private interpretation of
each one-line idea rather than a shared one. The reduction sequence:

1. **Pruning** — the facilitator revisits each idea briefly, seeking group
   concurrence that it's basically valid. No one should defend an idea out
   of authorship; anyone can support or challenge any idea regardless of
   who wrote it.
2. **Shared understanding** — each surviving idea's original submitter
   gives a one-sentence restatement of it, so every participant is voting
   on the same understood idea rather than whatever they individually
   imagined the card meant.
3. **Prioritization** — not always necessary (sometimes generation and
   pruning alone are the goal), but usually needed since no team can build
   everything anyone thought of. Two lightweight voting mechanisms:
   - **Cumulative voting ("the $100 test")** — each participant is given a
     fixed budget (e.g., $100 of notional currency) to distribute across
     the surviving ideas however they see fit, concentrating their budget
     on what matters most to them rather than casting one vote per idea.
   - **Weighted-category voting** — each participant sorts ideas into
     critical / important / useful buckets; votes are then weighted
     (e.g., critical ×9, important ×3, useful ×1) and summed. The skew is
     deliberate: it ensures a small number of ideas someone considers
     critical aren't drowned out by a larger number of ideas everyone
     rates merely useful.

Both voting techniques feed a rough, session-level ranking meant to narrow
a large idea set down to a workable candidate list — a separate, coarser
exercise from the deliberate multi-factor judgment used once those
candidates become actual backlog items; see [requirements
prioritization](requirements-prioritization.md) for that later, more
rigorous pass.
