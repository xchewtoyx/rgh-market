---
type: concept
title: Higher-Level Comments
description: >
  The other way to avoid restating code is to step up a level of
  abstraction, omitting detail to convey overall intent — the same skill as
  abstraction itself, applied to commenting, and harder to write than
  precision-adding comments.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Common for comments inside method bodies and for top-level interface
comments. A bad comment inside a loop over active RPCs ("If there is a
LOADING readRpc using the same session as PKHash pointed to by assignPos, and
the last PKHash in that readRPC is smaller than current assigning PKHash,
then we put assigning PKHash into that readRPC") just re-describes the `if`
condition in prose without ever stating the code's actual purpose. Replaced
with "Try to append the current key hash onto an existing RPC to the desired
server that hasn't been sent yet" — no low-level detail at all, but a reader
can infer almost the entire loop's structure from that one sentence, and
gains a basis for judging whether the code actually does what it claims to.

The self-interrogation technique for writing these: "What is this code
trying to do? What is the simplest thing you can say that explains
everything in the code? What is the most important thing about this code?"
This is harder to write than a [precision-adding comment](precision-adding-comments.md)
because it requires a real shift in thinking style: engineers are naturally
detail-oriented (a real asset elsewhere), but a good higher-level comment
requires stepping back to identify which few things matter most and ignoring
the rest — literally the same skill as
[abstraction](abstraction.md) itself, applied to commenting.

A good higher-level comment can do two jobs at once: a "what" (the abstract
description of the block's action) and a "why" or "how we get here"
(explaining the circumstances that lead to this code running). The
"why"/"how we get here" framing is especially useful for documenting when and
why a method tends to get invoked, particularly for methods only called in
unusual circumstances.

Higher-level comments are also inherently more durable than
[precision-adding](precision-adding-comments.md) ones, since they don't
encode implementation specifics — small code-level edits are less likely to
invalidate them, and only genuine changes in overall *behavior* require an
update. This doesn't make precise, detailed comments unnecessary; both are
still needed in their respective places. But it means the comments that are
already most valuable to readers, because they don't just restate the code,
also happen to be the cheapest to keep accurate over time — a rare case where
"better for readers" and "cheaper to maintain" point the same direction. See
[keeping comments from going stale](keeping-comments-current.md) for the rest
of that maintenance discipline.
