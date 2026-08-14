---
type: concept
title: Implicit vs Explicit Revision Creation
description: >
  Two strategies for when a new resource revision is created — API-driven
  snapshots on change versus client-triggered snapshot methods.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

An API can create revisions **implicitly** (the service decides when to
snapshot) or **explicitly** (the client calls a custom method to snapshot
current state). Both are valid; pick one strategy and apply it consistently
across all revisable resources — mixing strategies without strong
justification and clear documentation confuses clients.

Regardless of strategy, populate `revisionId` at initial resource creation.
Records without a revision id are not true revisions and break downstream
patterns.

**Implicit** creation is most common: typically a new revision on every data
change (Google Docs, GitHub issue history). Variants include schedule-based
(one revision per day if changed), skip-based (every Nth modification), or
milestone-based (only when specific fields change or a named custom method
runs, such as `PublishBlogPost()`). No universal rule — product constraints
decide. Default toward keeping more revisions rather than fewer; the
simplest default is a new revision on every modification.

**Explicit** creation exposes a custom method (for example
`CreateMessageRevision`) that snapshots on demand. The request needs only
the resource id; the service assigns a random revision id and
`revisionCreateTime` at persistence time.
