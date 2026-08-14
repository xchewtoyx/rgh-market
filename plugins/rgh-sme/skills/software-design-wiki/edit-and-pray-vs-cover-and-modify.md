---
type: concept
title: Edit and Pray vs. Cover and Modify
description: >
  Changing code by editing carefully and then manually poking around for
  breakage is the unfortunate industry default; wrapping the code in tests
  first gives the same care access to fast, reliable feedback instead.
sources:
  - title: Working Effectively with Legacy Code
    resource: "Working Effectively with Legacy Code (Feathers), ch. 2"
---

**Edit and pray**: plan the change, understand the code as best you can,
make the edit, run the system and poke around to make sure nothing broke.
This is the unfortunate industry standard, and it superficially looks like
"working with care" — but care alone isn't sufficient. "I don't think any of
us would choose a surgeon who operated with a butter knife just because he
worked with care": safety requires the right tools and techniques, not just
diligence.

**Cover and modify**: work with a safety net of tests wrapped around the
code being changed — "a cloak that we put over code we are working on to
make sure that bad changes don't leak out." With good tests around a piece of
code, a change gets fast feedback on whether its effects were good or bad,
applying the same care but with far better information. This is the practical
alternative that the rest of this domain's dependency-breaking and testing
techniques exist to make possible even when
[tests don't already exist](legacy-code-definition.md). See
[regression testing as a software vise](regression-testing-as-a-software-vise.md)
for what that safety net looks like in practice.
