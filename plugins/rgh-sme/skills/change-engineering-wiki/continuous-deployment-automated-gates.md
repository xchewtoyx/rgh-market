---
type: concept
title: Continuous Deployment Automated Gates
description: >
  Turn the informal human hunches that make an operator hesitate to push
  ("not during financial close", "not while the build is flaky") into
  explicit, automatable gate conditions rather than relying on inconsistent
  manual veto.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Continuous Deployment Automated Gates

Under [continuous deployment](continuous-deployment-vs-continuous-delivery.md),
every release that passes the pipeline goes to production with no human in
the loop — which raises an obvious worry: experienced operators often have
a "gut feeling" veto they'd normally exercise (skip the push during
financial close, be wary right after a run of broken builds suggesting a
stressed team). These hunches are real signals, not superstition, but the
right response is to convert each one into an explicit, automated gate
condition rather than leaving it to inconsistent human judgment — an
automated check runs identically every time regardless of who is on
vacation, tired, or in a bad mood.

Concrete conditions worth automating as gates on an otherwise-automatic
pipeline:

- **Build health** — block pushes if too many of the last N builds failed,
  as a proxy for a rushed or stressed development process.
- **Change size** — block or require extra approval for a change whose
  diff or blast radius is anomalously large relative to normal; see
  [change-size gating](change-size-gating.md).
- **Test comprehensiveness and reproducibility** — gate on code-coverage
  thresholds, and detect and gate on flaky tests via repeated or randomized
  test runs, since a flaky suite is a source of false confidence.
- **Production health** — require zero outstanding monitoring alerts
  before allowing a new push to land on top of an already-degraded system.
- **Schedule permission** — a maintained list of freeze dates (see
  [change freeze triggers](change-freeze-triggers.md)) blocks non-essential
  pushes during known-risky windows.
- **Oncall awareness** — avoid paging a sleeping oncall engineer; genuinely
  hard across follow-the-sun, multi-shift teams where no single hour has
  everyone awake.
- **Manual stop** — a defined, low-ceremony way for a specific list of
  people to halt automated pushes instantly, without needing to justify it
  as a formal emergency — the software equivalent of an assembly line's
  andon cord.
- **Push conflicts and intentional soak delays** — serialize deploys across
  interdependent services, and deliberately pause between pushes long
  enough to observe stability, since pushing too rapidly makes it hard to
  attribute a new symptom to the specific change that caused it.
- **Resource contention** — pause pushes under low disk space, high load,
  or insufficient spare replica capacity to safely absorb one more
  drained node.

The underlying claim is that automating these checks is *safer* than
leaving them to individual judgment, precisely because automation applies
every single time with total consistency — a memory-leak-shaped regression
is a case where automated detection reliably outperforms human vigilance,
which lapses even when a warning is already visible. This is a different
mechanism from [manual approval release gates](manual-approval-release-gates.md):
that pattern keeps a human explicitly in the loop for high-stakes stage
boundaries; this pattern is about removing the human from a loop that
doesn't need one, once the underlying judgment can be made mechanical.
