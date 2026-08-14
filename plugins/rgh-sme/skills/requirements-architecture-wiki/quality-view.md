---
type: concept
title: Quality View
description: >
  A quality view extracts and repackages the pieces of several structural
  views relevant to one cross-cutting concern — security, error handling,
  reliability — because that concern's stakeholder can't be served by any
  single module, component-and-connector, or allocation view alone.
sources:
  - title: Software Architecture in Practice
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 22"
---

[Module, component-and-connector, and allocation
views](architecture-as-structures-for-reasoning.md) are each organized
around one kind of structure, and they're excellent for constraining what
implementers build. Some stakeholder concerns don't fit that mold — a
security reviewer, for instance, needs security-relevant elements and
their communication paths regardless of which structural category each
one happens to live in, and that information is scattered awkwardly
across multiple structural views with otherwise-incompatible element
types.

A quality view is built for exactly this case: it extracts and repackages
the relevant fragments of the structural views around one specific
cross-cutting concern, rather than forcing that concern's stakeholder to
reconstruct it themselves from several unrelated diagrams. Common
examples: a **security view** (security-relevant components, their
communication, security data stores, and threat/vulnerability response
behavior); a **communications view** (all inter-component channels,
network paths, and QoS parameters, especially valuable for globally
distributed systems); an **exception/error-handling view** (how faults
are detected, reported, and resolved, supporting root-cause analysis); a
**reliability view** (replication and switchover mechanisms, transaction
integrity); and a **performance view** (traffic models, latency budgets).

A quality view is a fourth category alongside the three structural ones —
it exists because [choosing which views to
produce](choosing-architecture-views.md) is driven by stakeholder concerns
in the first place, and a concern that cuts across structures is still a
real stakeholder concern that deserves its own purpose-built
representation rather than being left implicit.
