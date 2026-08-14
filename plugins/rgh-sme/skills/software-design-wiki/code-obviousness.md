---
type: concept
title: Code Should Be Obvious
description: >
  Obvious code is code a reader can read quickly and with little conscious
  effort, whose meaning they will guess correctly on the first try — the
  direct prescription against obscurity, one of the two root causes of
  complexity.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 18"
---

[Obscurity](obscurity.md) is one of the two root causes of complexity;
writing obvious code is the direct countermeasure. Nonobvious code costs
readers extra time and effort and, worse, raises the odds of misunderstanding
and bugs. A useful corollary: obvious code needs fewer comments than
nonobvious code, since [comments](comments-describe-non-obvious-things.md)
exist specifically to compensate for what isn't obvious.

As with every other obviousness judgment in this wiki's source material,
"obvious" is judged by the reader, not the writer — it's inherently easier to
see nonobviousness in someone else's code than your own, which is why code
review is the practical mechanism for catching it: if a reviewer says
something isn't obvious, treat that as ground truth regardless of how clear
it seems to the author, and use the disagreement to learn what to write more
clearly next time.

See [techniques for obvious code](techniques-for-obvious-code.md) for what
makes code more obvious, [nonobvious code patterns](nonobvious-code-patterns.md)
for what to watch for and compensate against, and
[three strategies for supplying reader information](three-strategies-for-reader-information.md)
for the overall framework these fit into. "Reveal its intention" is the
second of [Kent Beck's four rules of simple
design](four-rules-of-simple-design.md), where it's ranked above removing
duplication or minimizing element count.
