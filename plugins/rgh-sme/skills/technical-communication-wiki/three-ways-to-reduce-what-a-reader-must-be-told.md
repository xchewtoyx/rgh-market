---
type: concept
title: Three Ways to Reduce What a Reader Must Be Told
description: >
  In order of preference — eliminate the need for a piece of
  information entirely, let the reader's existing knowledge of
  convention supply it for free, or, only when neither is possible,
  state it explicitly.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 18"
---

Any piece of information a reader needs but doesn't already have has to come from somewhere, and there are exactly three sources, worth reaching for in this order because each one is progressively more expensive than the last.

**First, eliminate the need for it.** The cheapest fix for a reader needing to know something is restructuring the material so they don't need to know it at all — folding a special case into the normal flow so there's no exception to explain, or simplifying a structure so a distinction that used to matter no longer does. This is the best option specifically because it removes the burden completely rather than relocating it to a different, still-costly channel.

**Second, let convention supply it for free.** If eliminating the information isn't possible, the next-cheapest source is whatever the reader already knows from established convention or genre expectation — a familiar structure, a standard term, a near-universal pattern for how this kind of document or artifact usually behaves. Conforming to an expectation the reader already carries means they don't have to learn anything new specifically for this piece of work; violating one, on the other hand, doesn't just cost the explanation you'd have needed anyway — it costs *more*, because a reader who expects the conventional behavior and gets something else will act confidently on a wrong assumption before discovering their error, exactly the way [the curse of knowledge](curse-of-knowledge-and-audience-research.md) describes an author's own blind spot. A departure from strong convention needs deliberate, explicit flagging at the point where the reader would otherwise assume the default — the more universal the convention being broken, the more directly the deviation needs to be called out, not left to a footnote the reader has no reason to go looking for.

**Third, state it explicitly.** Whatever can't be eliminated and isn't already covered by convention has to actually be written down — a precise name, a well-placed comment or annotation, a sentence of context — because a reader has no other way to get information that isn't already visible or already expected. This is the most expensive of the three options in aggregate, since it's the one where every reader pays the reading cost every time, which is exactly why it should be the fallback rather than the default: reach for it only after checking whether the first two options could have removed the need for it altogether.
