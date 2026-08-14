---
type: concept
title: Synthesize Across Compared Alternatives
description: >
  Treat picking the best alternative as the second-best outcome of
  an options comparison — the best outcome is often a new option
  that combines the strongest features of several.
sources:
  - title: "A Philosophy of Software Design"
    resource: "A Philosophy of Software Design (John Ousterhout), ch. 11"
---

Once several genuinely different alternatives
(see [radically-different-alternatives](radically-different-alternatives.md))
have been compared, the default move is to declare a winner and move
on. That default leaves value on the table: the comparison itself
usually surfaces which specific feature of each alternative made it
strong, and those features are often combinable into a new option
that beats every alternative that was actually proposed. Selecting a
winner answers "which of these is best"; synthesizing answers the
more useful question, "given what we now understand, what should we
actually build" — and the two answers are not always the same
option.

**When no alternative is attractive, the comparison still isn't
wasted.** If every candidate on the table shares the same weakness,
that shared weakness is itself the design driver for the next
candidate — it tells you specifically what the next alternative
needs to fix, rather than leaving you to generate one blind. A
comparison that produces zero acceptable options has still narrowed
the search: it has ruled out an entire family of approaches and named
why, which is strictly more useful than not having run the comparison
at all.

This changes what a recommendation document should show its readers:
not just the surviving option and the rejected ones, but the specific
strength of each rejected option that the recommendation actually
kept — otherwise a reader who liked a losing alternative for one
particular reason has no way to see that the reason was heard and
incorporated rather than dismissed. This extends
[fair-treatment-of-objections](fair-treatment-of-objections.md):
fair treatment of an alternative includes checking whether it has
something worth keeping, not only whether it survives as a whole.
