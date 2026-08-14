---
type: concept
title: Trunk-Based Development
description: >
  Keeping the version-control branch topology flat — developers integrate to a
  single mainline via short-lived branches or feature toggles rather than
  long-lived feature branches — because long-lived branches defer integration
  and accumulate merge debt.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 2, 3, 14"
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 11"
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 16, 26"
---

# Trunk-Based Development

[Continuous integration](continuous-integration.md) requires a single canonical
stream of code (the mainline, or trunk) that represents the current state of
the application. Long-lived feature branches — lasting days, weeks, or months
— are directly antithetical to this: they defer integration until the branch
is merged, at which point all the divergence accumulated over its lifetime has
to be resolved at once.

The alternative is either:

- **Short-lived branches** (under a day), merged back to trunk before they can
  diverge meaningfully, or
- **Feature toggles**: incomplete or unreleased functionality is merged to
  trunk continuously but hidden behind a runtime flag until it's ready, so
  integration never waits on feature completeness.

Distributed version-control systems (Git, Mercurial) support local, offline
commits, but that doesn't change the requirement: developers must still push
to and integrate with the shared canonical mainline at least daily to actually
be doing continuous integration. Working locally on a long-lived unpushed
branch is the same anti-pattern with extra steps.

See [integration hell](integration-hell.md) for the failure mode this avoids
— the deferred-merge cost it names is sometimes called **merge debt**: cost
that grows non-linearly with how long a branch has been diverging and how
many files it touches.

## Branch-by-team anti-pattern

A variant of the same failure mode happens at organizational granularity
rather than per-feature: assigning separate branches to separate teams. This
defers *cross-team* integration to the end of a release cycle instead of
per-feature integration, producing the same [integration hell](integration-hell.md)
but with architectural friction between teams layered on top. The fix is the
same principle applied across team boundaries: every team integrates to the
same mainline continuously, not just internally within its own branch.

## Velocity is a team sport

At scale, the optimal workflow for many developers collaborating on one
product requires modular architecture and near-continuous integration at head —
**velocity is a team sport**. The antipattern as teams grow: a subteam branches
off to avoid stepping on others' feet, then struggles later with integration,
culprit-finding, and [integration hell](integration-hell.md). Google's
preference is developing at head in a shared codebase backed by CI testing,
automatic rollbacks, and culprit finding — not long-lived team branches.

Long-lived **dev branches** are a distinct anti-pattern — see
[long-lived dev branch anti pattern](long-lived-dev-branch-anti-pattern.md).
One organizational **source of truth** at trunk (or policy-designated branch)
is required so releases and dependency versions aren't negotiated ad hoc.

Two other patterns exist alongside pure trunk-based development for specific
purposes: [branch-for-release](release-branching-pattern.md) for
stabilizing an in-flight release without freezing mainline, and
[branch by abstraction](branch-by-abstraction.md) for large structural
changes that can't land as a single small commit.

## Trunk-based development vs. GitHub Flow

Concretely, high-performing internal teams keep branch lifespan under a day
and rarely more than a few active branches concurrently. GitHub Flow (a
pull-request-per-feature-branch model) is a reasonable fit for asynchronous
open-source contribution, where contributors aren't co-located in time and a
PR can legitimately sit open for a while — but it's a weaker fit for a
full-time internal engineering team optimizing for delivery performance,
where the same pattern tends to produce branches that live far longer than a
day.

## The empirical sub-practices that predict performance

DORA's State of DevOps research found trunk-based development specifically
predicts higher throughput, better stability, and better availability when a
team follows three concrete sub-practices — vaguer adherence ("we sort of do
trunk-based development") doesn't show the same effect:

- 3 or fewer active branches in the repository at any time.
- Merging to trunk at least daily.
- No code freezes and no separate integration phases.

This is called out as one of the more controversial practices in the field —
teams often resist it initially — but is also linked to higher job
satisfaction and lower burnout, on top of the delivery-performance effect,
likely because it removes the recurring dread of a large, high-stakes merge
event.
