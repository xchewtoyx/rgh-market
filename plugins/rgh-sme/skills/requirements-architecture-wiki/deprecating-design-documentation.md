---
type: concept
title: Deprecating Design Documentation
description: >
  Design documentation has an expected lifespan tied to its usefulness,
  not permanence; recognizing when a system and its documentation can no
  longer be trusted is a deliberate call, not a default to avoid making.
sources:
  - title: Living Documentation
    resource: "Living Documentation: Continuous Knowledge Sharing by Design (Cyrille Martraire), ch. 11, ch. 14"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

Documentation should not be treated as a goal in itself, or as a way to
procrastinate on the underlying design work. Some documentation is
deliberately **biodegradable**: written to help while a decision is being
made or understood, and expected to disappear once it no longer serves
that purpose. Not every design artifact is meant to outlive the project
phase that produced it, and keeping it around past that point — updating a
stale design doc out of habit rather than need — costs maintenance effort
for no remaining benefit.

At the far end of that same spectrum is **documentation bankruptcy**: the
state where an application and its existing documentation can no longer be
trusted as a usable explanation of the system, and the application has
effectively become "fossilized knowledge" to be studied like archaeology —
you cannot assume any particular surviving detail still reflects current
intent. Recognizing this state, and deciding whether to invest in
recovering documentation or accept the loss, is a deliberate choice a team
has to make explicitly; treating a bankrupt system's stale docs as still
authoritative by default is worse than admitting the debt.

**Freshness metadata** makes stale docs visible before they mislead: record
last review date and owner in machine-readable form (e.g., a `freshness`
block with `owner` and `reviewed` fields), with automated reminders when
a document hasn't been touched within a defined interval. Attaching an
explicit owner increases adoption — updating the review date under source
control requires a review, which keeps owners honest. When a document is
obsolete, remove it or mark it clearly (pointing to a replacement); even
a prominent "this no longer works" note from a non-owner beats silent
authoritative rot. See [requirement revisit
triggers](requirement-revisit-triggers.md) for when stable requirements
themselves need revalidation.

Both cases point at the same underlying principle as [architecture
documentation rules](architecture-documentation-rules.md)'s "keep it
current, not necessarily exhaustive": documentation that can't be kept
current should be retired rather than left to mislead. See [bubble context
for legacy architecture](bubble-context-for-legacy-architecture.md) for a
technique specifically for documenting a target design while the legacy
system it's replacing is still in this state.
