---
type: concept
title: Avoid Duplicated Documentation
description: >
  Duplicated comments are harder to find and update consistently than a
  single comment at the most natural anchor point, referenced from
  everywhere else that needs it.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 16"
---

If a design decision is documented in only one place, there's only one
place to keep in sync — this is a maintenance-focused instance of
[information hiding](information-hiding.md), applied to documentation
itself. For information relevant across multiple usage sites, attach the
full explanation to the single most natural anchor point — document tricky
behavior of a variable in the comment next to its *declaration*, since that's
where developers investigating unexpected behavior around it are most likely
to look first — rather than repeating it at every use site.

When no single obvious anchor exists, fall back to a
[design-notes file](cross-module-design-decisions.md), or pick whichever
available location is best and have every other dependent site carry a short
pointer comment back to it ("See the comment in xyz for an explanation of the
code below"). Pointer references have a self-healing property duplicated
copies lack: if the master comment moves or is deleted, a dangling pointer
becomes immediately, visibly broken — developers find nothing at the named
location and can use version-control history to locate what happened —
whereas duplicated copies can silently drift apart with no signal that any of
them has gone stale.

The same discipline extends outward in two directions. Within a codebase,
don't re-explain another module's internal behavior at a call site (a
comment before a method call summarizing what the called method does) —
readers should consult that method's own [interface comment](interface-documentation.md)
instead, and IDE tooling already surfaces it nearly frictionlessly.
Outside the codebase, don't re-explain something already thoroughly
documented elsewhere — implementing HTTP doesn't require re-describing the
HTTP protocol in your own comments; link to an existing authoritative
reference instead. The actual goal is making documentation *findable*, which
doesn't require personally authoring every copy of it.
