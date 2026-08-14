---
type: concept
title: Ensuring Consistency Across a Team
description: >
  Consistency erodes naturally as more people work on a codebase over more
  time; keeping it intact takes documenting conventions, backing them with
  automated enforcement, and defaulting to whatever precedent already exists
  rather than introducing a new approach.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 17"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 10"
---

One group can be unaware of another's conventions, and newcomers unknowingly
both violate existing conventions and introduce new, conflicting ones — so
[consistency](consistency-as-a-design-tool.md) needs active maintenance, not
just an initial decision.

**Document** the most important overall conventions somewhere genuinely
visible (a prominent wiki page, borrowing an existing published style guide
as a starting point rather than authoring from scratch — see [style guides as
design conventions](style-guides-as-design-conventions.md)), and actively
encourage newcomers to read it and veterans to revisit it periodically. For
narrower, code-local conventions — a specific [invariant](invariants.md) — 
document them right in the relevant code; an unwritten convention is one
nobody else can be expected to follow.

**Enforce** with automated tooling, since even well-documented conventions
are hard for people to remember consistently on their own; a pre-commit
checker works especially well for low-level syntactic rules — at scale,
[style guide rule process and enforcement](style-guide-rule-process-and-enforcement.md)
strongly prefers automated tooling over engineer memory. A worked
example: a project with mixed Unix/Windows developers hit recurring pain from
inconsistent line endings, where a cross-platform edit could silently rewrite
every line ending in a file and bury the real diff. A documented "LF only"
convention wasn't reliably followed because not every developer's tooling
respected it, and every new hire re-triggered the problem. An automated
pre-commit script that rejected — and could repair — any file containing the
wrong line ending instantly eliminated the problem and doubled as informal
onboarding for new developers. Code review is a second enforcement and
education channel: the more nitpicky reviewers are about conventions, the
faster the whole team internalizes them.

**"When in Rome..."** is the single most important convention-following
rule: on entering a new file, look at how the surrounding code is already
structured and match it, even for conventions never formally written down
anywhere. Before making a design decision, ask whether a similar decision was
likely already made elsewhere in the project, find that precedent, and
follow it.

**Don't change existing conventions** just because you have a marginally
better idea — the value of consistency itself almost always outweighs the
value of any one approach being slightly better. Two gating questions before
overriding a convention: do you have genuinely new information that wasn't
available when the existing convention was set, and is the new approach
enough of an improvement to justify retrofitting *every* existing use of the
old one? Only proceed if the answer to both is yes, and apply the change
thoroughly enough that no trace of the old convention remains — any leftover
mixture risks other developers unknowingly reviving the old pattern later,
having never learned the new one. Revisiting settled conventions is rarely a
good use of developer time.
