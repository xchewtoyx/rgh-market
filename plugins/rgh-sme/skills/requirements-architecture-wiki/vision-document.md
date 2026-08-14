---
type: concept
title: Vision Document
description: >
  A short, standing document stating why a product or program exists,
  what problem it solves, and what it must deliver — the artifact that
  replaces a big up-front spec as the thing development teams build
  toward.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 13"
---

Agile delivery drops the heavyweight up-front specification document, but
it doesn't drop the need for teams to know what they're building toward —
if anything, that need becomes more acute, since there's no large
requirements document left to fall back on. The Vision document is the
artifact that fills this gap: a standing statement, owned by product
management (since it flows from business and portfolio investment
strategy, not from the development team), answering why the product is
being built, what problem it solves, what features and benefits it
delivers and for whom, and what performance, reliability, and scalability
it must meet.

Its defining constraint is brevity: even for a large greenfield program,
a Vision document should stay in the 5-10 page range (20 pages as an
absolute ceiling), not because the underlying decisions are simple but
because a document teams won't actually read provides no more guidance
than no document at all. This makes it a different kind of artifact from
[Project Blastoff](project-blastoff.md)'s output — Blastoff fixes a
project's initial scope and constraints once, at inception; the Vision is
meant to be revisited and re-communicated on an ongoing basis as the
authoritative statement of intent for a running program.

A lighter-weight alternative some organizations use instead of a
standalone document: let an elaborated, prioritized feature backlog *be*
the Vision, communicated through a face-to-face briefing to the
development team rather than committed to a separate written artifact.
This trades a durable reference document for lower authoring overhead, and
depends on the briefing actually happening and being repeated as the
backlog changes — a risk a written Vision document doesn't carry.

The Vision sits above individual requirements in scope: see the
[requirements pyramid](requirements-pyramid.md) for how it relates to
features and to detailed software requirements underneath it.

A worked template's section order is itself informative about what a
Vision document is *for*: user description and environment (background
only — explicitly not itself a place to state requirements), stakeholders
and their degree of involvement, a product overview with a
features-vs-customer-benefit summary, the product features themselves, a
few [exemplary use cases](use-case-as-story-source.md) chosen for being
architecturally significant or representative of typical usage,
[non-functional requirements](non-functional-requirement.md), and finally
documentation requirements (user manual, online help) needed to support
the product once built. Background and user context come before any
feature is stated, and requirements proper come only after that context
is established — a Vision document that leads with a feature list before
explaining who needs it and why tends to read as a solution in search of
a justification.
