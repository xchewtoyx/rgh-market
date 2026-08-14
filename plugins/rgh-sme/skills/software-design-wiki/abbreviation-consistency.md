---
type: concept
title: Inconsistent Abbreviations Break Consistent Naming
description: >
  An inconsistently applied abbreviation scheme across class or identifier
  names forces readers to guess, defeating the point of a naming
  convention even when each individual name looks reasonable.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 21"
---

Anecdote: a team abbreviated "manager"/"management" inconsistently across
class names (some as one suffix, some as a slightly different one) to the
point that guessing the correct suffix for an unfamiliar class name was
right barely half the time. This is a special case of
[consistent names](consistent-names.md): the underlying concept (a manager
class) was named consistently in spirit but not in the literal string used,
which is enough to defeat the benefit consistency is supposed to provide —
a reader can't reliably guess or autocomplete a name from the concept alone.
The fix isn't picking a "better" abbreviation, it's picking any one
abbreviation scheme and applying it everywhere without exception.
