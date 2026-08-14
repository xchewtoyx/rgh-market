---
type: concept
title: Three Cases for Large-Scale Architecture Refactoring
description: >
  A large architectural change falls into one of three cases — fully
  incremental, occasionally interrupted, or genuinely non-incremental —
  and which case it is should be decided economically, not assumed.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 20"
---

An [architecture epic](architectural-runway.md) large enough to span
releases and teams doesn't automatically dictate its own implementation
strategy — there are three genuinely different cases, and documenting
which one applies (and why) is itself part of specifying the epic:

- **Case A — big, but incremental: the system always runs.** The
  best-case scenario: the change can be built and shipped in increments,
  the system stays releasable throughout, risk stays controlled, and
  work-in-process stays bounded. This is the default to aim for. The
  [strangler pattern](strangler-pattern-for-legacy-migration.md) is the
  concrete technique for landing a legacy-system replacement in this case
  rather than as a non-incremental rewrite.
- **Case B — big, but not entirely incremental: the system takes an
  occasional break.** The first response on landing here should be to
  stop and look for a way back to Case A — retrenching or redefining the
  epic, adding temporary stubs or [scaffolding](architectural-scaffolding.md),
  is usually worth the extra decomposition effort because of the lower
  risk and faster feedback it buys back. Sometimes, though, the economics
  genuinely favor breaking the system down for a bounded period, doing the
  refactor, and reassembling before the next release boundary — a
  legitimate choice, not a fallback of last resort, provided it doesn't
  jeopardize external release commitments even if it costs an internal
  one.
- **Case C — really big and not incremental: the system runs when needed;
  do no harm.** The hardest and rarest case, typical only of the largest
  legacy systems: even a single release cycle's worth of incremental
  redesign is impractical, a genuinely longer initiative is required, and
  the product must stay shippable the entire time regardless. This
  requires running the architectural initiative as a sustained,
  multi-release program alongside ordinary feature delivery, under an
  explicit "do no harm" constraint on everything else still shipping.

Deciding which case applies is an economic judgment, not a technical
default: weigh the [cost of delay](weighted-shortest-job-first.md) from a
missed release against the cost of slower incremental work, the risk of
carrying a long-lived divergent branch, or the added investment of
maintaining multiple parallel implementation options at once. Recording
which case was chosen, and the trade-off that decided it, is what a later
reader needs in order to tell whether the same reasoning still applies
once circumstances change — see [documenting
trade-offs](documenting-trade-offs.md).
