---
type: concept
title: Design Document
description: >
  A design document records goals, implementation strategy, and key
  architectural decisions with trade-offs before major work begins, then
  serves as the baseline for a post-launch goal check.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 12"
---

A design document is the primary pre-implementation artifact for major
project work: written from a team-approved template, shared for
collaborative review (sometimes in a dedicated design meeting — code
review before code exists). Canonical templates prompt authors to address
cross-cutting concerns — security, internationalization, storage, privacy,
and similar — often reviewed by domain experts.

A good design document covers:

- **Goals** — what the project must achieve, linked to [requirements
  rationale](requirement-rationale.md) and [architecturally significant
  requirements](architecturally-significant-requirement.md) where they
  drive structure.
- **Implementation strategy** — how the team plans to reach those goals at
  a level sufficient for alignment, not full low-level specification.
- **Key [architectural decisions](architectural-decision-capture.md)** —
  each with its [documented trade-offs](documenting-trade-offs.md), not
  just the chosen option.
- **Alternative designs** — strong and weak points of options not chosen,
  so rationale survives the meeting where the decision was made.

Once approved, the document is both historical record and success
criterion: teams often re-read it before launch to check whether stated
goals still hold and whether the built system matches the documented
intent. That post-launch review is part of [requirements
traceability](requirements-traceability.md) — connecting what was promised
in design to what shipped.

Design documents belong in the [stable vs volatile
documentation](stable-vs-volatile-documentation.md) split as deliberately
authored prose tied to a project phase; collaborative drafts may live in
shared editors during discussion, but the approved record should move to
version control with clear ownership when the decision is final. Keep
implementation minutiae and API reference detail out of the design doc —
those belong in reference documentation and [interface
documentation](interface-documentation.md) respectively, mirroring the
separation between public interface and internal implementation in code.
