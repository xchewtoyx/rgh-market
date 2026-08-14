---
type: concept
title: Keeping Comments From Going Stale
description: >
  Comments drifting out of date with the code is a real risk, but it needn't
  be a major practical problem, because large documentation-update needs
  only arise alongside large code changes — and the code change itself
  always takes longer than updating the comment.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 12"
---

The concern behind "comments get out of date and become misleading" is real,
but keeping documentation current doesn't require huge effort in practice:
you only need to touch a large amount of documentation when you make a large
code change, and that code change will always take longer than updating the
comment that describes it. Past some threshold of frequency, stale comments
make readers stop trusting *any* of the comments in a codebase, not just the
wrong ones — which is what makes the following techniques worth the
discipline.

**Physical proximity** is the core mitigating technique: the closer a
comment sits to the code it describes, the more likely a developer editing
that code will actually notice and update it; the farther apart they are, the
more likely staleness slips through unnoticed. In C/C++-style split
code/header files, put interface comments next to the method's
*implementation*, not just in the header — that's where a developer editing
the method's behavior will actually be looking, whereas a comment living only
in a header risks being missed during a body-only edit. The instinct to put
interface docs only in headers "so users don't need the code file" is solved
by tooling instead — documentation-extraction tools or IDE hover/autocomplete
— not by physical placement optimized for the wrong audience: documentation
should live wherever is most convenient for the people who maintain the code,
since tooling handles surfacing it to the people who merely use it.

For [implementation comments](implementation-comments.md) inside a method
body, don't front-load one big comment block at the top describing every
phase of a multi-phase method — scope each comment down to the narrowest
span of code it actually describes, with a phase-specific comment right
above that phase's first line. A short top-level roadmap comment naming the
phases is still valuable as an orienting overview, with the detail comments
living lower down, right where each phase begins.

The general corollary: **the farther a comment sits from its code, the more
abstract it should be** — see
[higher-level comments are more durable](higher-level-comments.md) — because
abstract, high-level statements are less likely to be invalidated by
small code-level changes than detailed ones would be, so distance and
abstraction level should scale together. Code review is a practical
mechanism for catching comments that have drifted out of sync with the code
they describe; see also
[avoiding duplicated documentation](avoid-comment-duplication.md) and
[checking the diff before committing](check-diffs-before-committing.md).

A complementary strategy sidesteps the discipline problem instead of
managing it: see [prefer documentation forms that refactoring tools keep in
sync](refactorable-documentation.md) for choosing documentation whose
truth is enforced by tooling — types, tests, names — rather than by
whether a developer remembered to update a comment.
