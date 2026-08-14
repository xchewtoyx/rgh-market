---
type: concept
title: Write for the Reader, Not the Writer
description: >
  A shortcut that saves the writer a few minutes but costs every future
  reader more than that to decode is a bad trade nearly every time —
  the side that's outnumbered should be the one who spends the effort.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 18"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 12"
---

A generic, reusable container — bundling two values together and retrieving them as "the first one" and "the second one" — is faster to write than defining a small, purpose-built structure with named, documented fields for the same two values. It's also worse for every reader who encounters it afterward, because "the first one" and "the second one" carry no meaning on their own; a reader has to trace back to wherever the container was built just to learn what it actually holds. The convenience is real, but it's entirely one-sided: it's paid once by the writer and re-paid, in full, by every subsequent reader who touches the result.

Documentation amplifies that asymmetry: you write a document once, but it may be read hundreds or thousands of times, so even a small per-reader cost dominates the author's one-time savings. Unlike tests, documentation's benefits are downstream and do not accrue immediately to the author — which is one reason it is undervalued — but the reader-side return is what justifies the work. Explaining an API also clarifies whether the API is well designed: if you cannot explain and define it cleanly, the design probably is not finished yet.

This is the general shape of a whole class of shortcuts: whatever is fastest to produce in the moment is not automatically the version that costs the least overall, because the writer is one person writing it once and the readers are potentially many people reading it many times. The maxim this justifies is blunt but reliable: **write for ease of reading, not ease of writing.** When a choice trades a small amount of extra writer effort now for a real reduction in reader effort later — a named structure instead of an anonymous pair, a spelled-out label instead of an ambiguous abbreviation, an extra sentence of context instead of relying on the reader to infer it — take the trade. The few extra minutes spent up front are reliably cheaper than the cumulative cost of every reader independently doing the decoding work the writer skipped.

This connects directly to why [precise naming](precise-and-consistent-naming.md) and [comments completing the interface](comments-complete-the-interface.md) are worth their upfront cost at all: both are instances of the same trade, spending a little writer time to save a much larger amount of aggregate reader time. It's also the same asymmetry [the curse of knowledge](curse-of-knowledge-and-audience-research.md) describes from the opposite angle — the writer, who already knows what something means, systematically underestimates how much that convenience shortcut actually costs the reader who doesn't.
