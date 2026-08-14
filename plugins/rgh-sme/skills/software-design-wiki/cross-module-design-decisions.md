---
type: concept
title: Documenting Cross-Module Design Decisions
description: >
  Some design decisions inevitably span multiple modules with no single
  natural home for their documentation; when a natural anchor point exists,
  put a checklist there, and when it doesn't, a dedicated design-notes file
  with pointer comments is a workable fallback.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 13"
---

Ideally every design decision would live inside one class's boundary, but
real systems have decisions spanning multiple modules — a network protocol
constrains both sender and receiver implementations, which may live in
entirely separate places. These cross-cutting decisions tend to be complex,
subtle, and disproportionately bug-prone, making good documentation
unusually valuable and unusually hard to place.

**Best case — a natural anchor point exists.** Adding a new status value to
an enum might require touching several separate files (an exception-mapping
table, a human-readable-message table), but if there's one place every
developer *must* visit to add a new value — the enum declaration itself — a
numbered checklist comment can live right there, at the point new values get
appended, spelling out every other file and step that also needs updating.

**Hard case — no natural anchor exists.** A concern like a distributed
system's "zombie server" handling (a server the cluster believes is dead but
which is actually still alive) can require coordinated code across several
interdependent modules with no single obvious home. Duplicating the
explanation at every dependent site is awkward and hard to keep synchronized
as the system evolves; parking it at just one of the dependent sites means
developers working at the others won't know to look there.

**Experimental fallback — a dedicated design-notes file.** A single central
file, organized into clearly labeled topic sections, holds the explanation;
every piece of code touching that concern carries a short pointer comment
(`// See "Zombies" in designNotes.`). This keeps a single authoritative,
genuinely discoverable copy, but it's physically distant from all the code
that depends on it, which risks the documentation silently drifting out of
sync as the system evolves — the opposite trade-off from
[keeping comments close to the code they describe](keeping-comments-current.md).
