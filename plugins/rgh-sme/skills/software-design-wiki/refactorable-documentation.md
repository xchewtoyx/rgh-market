---
type: concept
title: Prefer Documentation Forms That Refactoring Tools Keep in Sync
description: >
  Documentation expressed as code — names, types, tests — gets updated
  automatically whenever a refactoring tool touches the identifiers it
  depends on; documentation expressed as disconnected prose has to be kept
  in sync by hand and drifts whenever that discipline lapses.
sources:
  - title: Living Documentation
    resource: "Living Documentation (Martraire), ch. 8"
---

[Keeping comments from going stale](keeping-comments-current.md) is a
discipline problem for prose comments specifically: nothing connects a
comment's text to the code it describes, so keeping them in sync depends
entirely on a developer noticing and manually updating it. A different, more
durable answer is choosing documentation *forms* that a development tool's
refactoring support will update automatically as a side effect of ordinary
code changes, rather than relying on human discipline to keep a
disconnected artifact current.

Code, types, and tests are refactorable in this sense: a rename tool
propagates a renamed identifier everywhere it's referenced; a type's
constraints stay checked by the compiler on every build, not just at the
moment someone wrote a comment about them; a test's assertions are
re-verified on every run. All three participate in ordinary change
workflows the same way the production code itself does. Plain prose in a
separate wiki page or design document does not — nothing forces it to
change when the code it describes changes, so it silently diverges the
moment the code moves on without it.

This reframes several existing techniques as instances of one underlying
principle — pick documentation whose truth is enforced by tooling, not by
memory:

- [Types over comments](replace-primitive-with-object.md): a type's
  constraints are compiler-checked on every build; a comment claiming the
  same constraint is checked by nobody unless a human happens to reread it.
- Composed methods with intention-revealing names (see [naming as
  documentation](naming-as-documentation.md)) push documentation into an
  identifier that a rename refactoring will propagate everywhere it's
  used, rather than into prose sitting beside a name that can drift out of
  sync with it.
- [Characterization tests](characterization-tests.md) and [self-testing
  code](self-testing-code.md) document actual behavior in a form that's
  re-verified automatically every run, rather than asserted once in prose
  and never rechecked.

Diagrams-as-code and plain-text diagram formats extend the same idea to
non-textual documentation: kept in source control and expressed as text, a
diagram diffs cleanly alongside the code change that motivated it and can
be updated using the same refactoring tools, unlike a diagram trapped in a
binary drawing-tool format that has no relationship to the code at all.
