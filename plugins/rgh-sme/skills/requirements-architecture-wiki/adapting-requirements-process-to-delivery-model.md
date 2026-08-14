---
type: concept
title: Adapting the Requirements Process to Delivery Model
description: >
  The same requirements process changes its timing and granularity, not
  its substance, across agile, outsourced/COTS, legacy-modernization, and
  fast-track delivery.
sources:
  - title: Mastering the Requirements Process
    resource: "Mastering the Requirements Process: Getting Requirements Right (Suzanne Robertson, James Robertson), ch. 9, ch. 14"
---

Requirements discovery doesn't change substance across delivery models —
every model still needs discovered, [rationale](requirement-rationale.md)-backed,
[fit-criterion](fit-criterion.md)-verified requirements — but the timing
and granularity of discovery adapts:

- **Agile/iterative** — [project blastoff](project-blastoff.md) and work
  scoping happen once, up front, lightweight. [Business use
  cases](business-event-and-use-case.md) become epics; individual [atomic
  requirements](atomic-requirement-shell.md) and their fit criteria are
  discovered just-in-time, one or two sprints ahead of implementation,
  rather than all at once. The mapping is direct: work context and goal
  become the product vision and epic backlog, BUCs become feature
  themes/epics, atomic requirements become [user
  stories](user-story.md) ("as a [role], I want [action], so that
  [rationale]"), and fit criteria become acceptance criteria or definition
  of done.
- **Outsourced / off-the-shelf (COTS)** — weight shifts toward [non-functional
  requirements](non-functional-requirement.md), architectural constraints,
  and fit criteria, because these become the benchmarks used to evaluate
  competing vendor packages during RFP evaluation, rather than driving a
  from-scratch build.
- **Legacy modernization** — focus on extracting the essential business
  rules a legacy system encodes (see [essence of the business
  work](essence-of-the-business-work.md)) without also replicating its
  obsolete technical workarounds as if they were requirements.
- **Fast-track / accelerated** — prioritize the highest-risk,
  highest-value [business use cases](business-event-and-use-case.md)
  first, and do just-in-time analysis for the stable, low-risk remainder.

What stays constant across all four is the underlying [requirements
knowledge model](requirements-traceability.md) — goal, event, use case,
requirement, fit criterion — only the pacing of discovery against it
changes.
