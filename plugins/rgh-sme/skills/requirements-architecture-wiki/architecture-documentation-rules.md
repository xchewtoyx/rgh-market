---
type: concept
title: Architecture Documentation Rules
description: >
  Seven working rules for architecture documentation as a whole — write
  for the reader, avoid ambiguity, use a standard organization, record
  rationale, and keep it current without needing to be exhaustive.
sources:
  - title: Documenting Software Architectures
    resource: "Documenting Software Architectures: Views and Beyond (Clements, Bachmann, Bass, Garlan), Prologue"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

Seven rules apply across any architecture documentation, regardless of
which [view](view-and-viewpoint.md) is being produced: write for the
reader, not for yourself; avoid repetition (state each fact once, in the
place a reader looking for it would check); avoid ambiguity; use a
standard organization so a reader familiar with the scheme can find things
without being told where each time; record rationale, not only the
resulting structure; keep the documentation current, but not necessarily
exhaustive — currency matters more than completeness; and review it for
fitness of the stakeholders' actual purpose, not for its own sake.

Open with the questions readers need answered before the how-to: **WHO**
(audience), **WHAT** (this document's single purpose — material that does
not fit belongs elsewhere; see [documentation type by
purpose](documentation-type-by-purpose.md)), **WHEN** (created or last
reviewed), **WHERE** (canonical location under version control), and
**WHY** (expected takeaway). Stating WHAT and WHY up front is the check
for whether the body stayed focused. Redundancy is acceptable in
documentation: summarize the key point first, then make the detailed case —
a buried conclusion in a wall of text is easy to miss.

The rule most often broken in practice is explaining notation — especially
what an arrow means — rather than assuming the reader already knows.
Diagrams that look like standard UML or informal boxes-and-arrows invite
readers to bring their own assumptions about what a line means; a legend
or textual explanation is what actually fixes the meaning, regardless of
how conventional the notation looks. See [connector
semantics](connector-semantics.md) for the specific case of connector
arrows, and [descriptive completeness](descriptive-completeness.md) for
what "not necessarily exhaustive" should still cover.

"Keep it current, not necessarily exhaustive" is a direct statement of
priority: documentation that is accurate but incomplete is more useful
than documentation that was once complete but has since gone stale. See
[deprecating design documentation](deprecating-design-documentation.md)
for what to do when currency can no longer be maintained at all.
