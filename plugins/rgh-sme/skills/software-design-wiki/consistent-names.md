---
type: concept
title: Consistent Names
description: >
  Pick one name for a given recurring purpose and use it everywhere that
  purpose recurs, so a reader who learns what the name means once can
  safely transfer that understanding everywhere else they see it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 14"
---

Once a reader has learned what a name means in one context, consistency lets
them safely transfer that understanding to every other place they see it,
cutting [cognitive load](cognitive-load.md) the same way reusing a
well-known class does. Genuine consistency requires three things:

1. Always use the chosen common name for its designated purpose.
2. Never reuse that name for anything else.
3. Keep the purpose narrow enough that every variable sharing the name
   genuinely behaves the same way.

Requirement 3 is exactly what the [`block` naming bug](naming-as-documentation.md)
violated — the name's "purpose" was defined too broadly, spanning two
different behaviors, which produced a false assumption and a six-month bug
hunt.

When multiple variables of the same conceptual kind coexist (a copy
operation needing both a source and a destination block number), keep the
shared base name but add a distinguishing prefix: `srcFileBlock` /
`dstFileBlock`. The same discipline extends to loop variables: if using
`i`/`j` for loop counters, always use `i` for the outermost loop and `j` for
a nested one, so readers can make instant, reliable assumptions about loop
nesting just from the variable name. See
[inconsistent abbreviations break consistent naming](abbreviation-consistency.md)
for a common, easy-to-miss way this discipline slips.
