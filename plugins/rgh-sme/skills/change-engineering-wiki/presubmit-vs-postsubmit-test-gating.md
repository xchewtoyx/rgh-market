---
type: concept
title: Presubmit vs Postsubmit Test Gating
description: >
  Run only fast, reliable tests before merge; accept broader coverage and
  occasional rollbacks after merge, because exhaustive presubmit blocks
  productivity and fights mid-air collisions.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
---

# Presubmit vs Postsubmit Test Gating

Given the goal of catching defects as early as possible, running every test
on presubmit is tempting — but at scale it fails for three reasons:

1. **Cost and productivity** — waiting for exhaustive tests on every
   submission is severely disruptive; presubmit must stay non-exhaustive
   (scoped runs, failure-prediction models) to keep throughput.
2. **Flakiness cost** — blocking engineers on failures unrelated to their
   change (unstable or flaky tests) is expensive; unreliable tests must not
   run on presubmit.
3. **Mid-air collisions** — while presubmit runs, the repo may change
   underneath the tested revision; two compatible changes can fail together
   even when each passes alone — common at large scale.

**Rule of thumb:** only **fast, reliable tests on presubmit**; accept some
coverage loss before merge and catch gaps on post-submit, with rollbacks
when needed. Post-submit can tolerate longer runtimes and some instability
if failure-management mechanisms exist. Presubmit tests are typically scoped
to the project under change and run concurrently.

Most teams restrict presubmit to small (unit) tests; larger-scoped tests on
presubmit vary by team — [hermetic testing](build-quality-in.md) reduces
their instability, or large tests may be allowed to flake on presubmit but
disabled aggressively when they start failing.

Empirically at Google, a change passing a fast presubmit subset has 95%+
likelihood of passing the rest of the suite — enough to integrate
optimistically so others can build on it, with post-submit continuous build
and [build cop rollback discipline](build-cop-rollback-discipline.md)
catching the remainder. Average presubmit wait can stay around minutes
when run in the background, trading exhaustive pre-merge verification for
throughput without abandoning recovery discipline.

This gating strategy is what makes [continuous build green head vs true
head](green-head-vs-true-head.md) workable: presubmit gives quick signal;
post-submit continuous build gives the authoritative green cut.
