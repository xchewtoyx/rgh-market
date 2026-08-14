---
type: concept
title: Build Quality In
description: >
  Detect and fix defects at the point of origin instead of relying on
  downstream inspection, so that changes entering the pipeline are already
  low-risk rather than being filtered late.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Build Quality In

Build quality in is Deming's third management point applied to software
delivery: cease dependence on mass downstream inspection (a late-stage QA
gate, a change approval board) and instead detect and fix defects
immediately at the point where they originate.

This is a precondition for shipping faster without raising
[change failure rate](change-failure-rate.md) — it's the mechanism behind
the [speed-stability trade-off myth](speed-stability-tradeoff-myth.md).
Teams that increase deployment tempo without building quality in (reliable
automated tests owned by the people writing the code, not a downstream gate)
see change failure rate rise, because they've removed the manual filter
without replacing it with an earlier one.

It works together with [working in small batches](working-in-small-batches.md):
small batches make it feasible to verify a change thoroughly at commit time,
and thorough commit-time verification is what makes small, frequent batches
safe rather than merely fast.

Continuous integration's core guarantee is **verifiable, timely proof**
that a change is good to progress — not hoping contributors are careful.
Each integration into a testing scenario is a feedback loop; the cost of a
bug grows almost exponentially the later it is caught (triage by someone
unfamiliar with the change, author context reload, impact on others).
CI encourages stacking fast loops — local edit-compile-debug,
[presubmit vs postsubmit test gating](presubmit-vs-postsubmit-test-gating.md),
staging integration, [canary release](canary-release.md), dogfood, then
external users — so defects surface in the cheapest loop that can catch
them.

Feedback must be **accessible and actionable** — unified reporting where
anyone can look up a build or test run with history of when targets began
failing; flake classification so engineers aren't blocked debugging known
flakes; failure messages that embed deep links into logs (e.g., construct a
search URL for a failing entity ID) rather than requiring manual log
archaeology. Readable test output effectively automates understanding of
feedback.

Building CI is expensive but largely a cost **shifted left** — compared
against production firefighting that stresses users and engineers, earlier
detection is preferable even when resources are constrained.

Pipeline **visibility and feedback** (chat notifications, status badges,
inline PR check results, stored coverage artifacts) make CI outcomes
actionable without digging through raw logs — part of the same accessible
feedback requirement.
