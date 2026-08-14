---
type: concept
title: Techniques for Obvious Code
description: >
  Good names and consistency are the most important tools for obviousness,
  followed by judicious whitespace to make code's structure visually
  scannable, with comments as the fallback for whatever remains nonobvious.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 18"
---

The two most important techniques for [obvious code](code-obviousness.md)
are covered in depth elsewhere: [precise, meaningful names](precise-names.md)
reduce the need to read code just to infer meaning, and
[consistency](consistency-as-a-design-tool.md) lets readers safely reuse
prior knowledge without re-analysis.

**Judicious whitespace** is a smaller but real lever. Compare a cramped
parameter-documentation block with all blank lines squeezed out — hard to
tell where one description ends and the next begins — against the same
content with proper line breaks and indentation, where the structure becomes
immediately scannable. Blank lines separating a method's major logical
blocks work especially well when paired with a leading comment on the first
line after each blank; the blank line makes the comment, and thus the block
boundary, more visually salient. Whitespace *within* a single statement
matters too — `for(int pass=1;pass>=0&&!empty;pass--)` is harder to parse at
a glance than `for (int pass = 1; pass >= 0 && !empty; pass--)`.

**Comments as a fallback**: when nonobvious code genuinely can't be avoided,
comments must compensate by supplying exactly the missing information — which
requires actively imagining what a reader is likely to find confusing and
addressing that specific gap, rather than commenting generically.
