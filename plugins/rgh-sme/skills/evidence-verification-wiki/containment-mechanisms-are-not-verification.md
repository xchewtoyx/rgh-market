---
type: concept
title: Containment Mechanisms Are Not Verification
description: A safeguard designed to limit the blast radius of an undetected defect is a different thing from a check designed to detect the defect, and treating a clean pass of the former as evidence of correctness lets verification quietly erode.
sources:
  - title: "The Practice of Cloud System Administration"
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

# Containment Mechanisms Are Not Verification

A **canary deployment** — releasing a change to a small slice of production first and watching for trouble before releasing it everywhere — looks like a verification step: something is checked, and a clean result lets the rollout proceed. But its actual job is different from testing's: a canary exists to *limit the damage* of a defect that already escaped detection, by confining first exposure to a small, recoverable population, not to *establish* that the change is correct. A failing test is success — the verification process worked, catching a bad change before it shipped. A failing canary is a process failure: a defect that should have been caught earlier reached production at all, and only the canary's narrow blast radius kept it from being worse.

## Why the distinction matters

Conflating the two lets an organization's real verification coverage quietly decay while every dashboard still shows green. If canarying is treated as *the* verification step (rather than testing), teams stop asking whether the test environment still resembles production, because the canary's blast-radius protection continues to "work" — small failures get caught and contained — even as coverage gaps grow underneath it. The canary is answering "did this fail *visibly*, on the *first* few machines, in a way the built-in health checks would notice?" which is a much narrower claim than "does this change work correctly."

## Worked case: divergence hidden behind a working safety net

A team canaried every release into production for years, and treated the canary passing as their real confidence signal. Meanwhile, engineers built ad hoc production-only tooling that the separate, official test environment never exercised, and the test and production environments' hardware, kernel, and virtualization stack quietly drifted apart over time. None of this surfaced as a problem, because the canary kept "working" — until a production push broke specific virtual machines in a way that hadn't shown up in canary or test, discovered only after the rollout had already completed. The fix required a months-long project to rebuild the test environment to genuinely mirror production's exact combination of release, kernel, virtualization framework, and hardware — restoring testing as the actual verification mechanism, with canarying restored to its narrower role as a deployment-safety net behind it.

## Verification action

When a process relies on a deployment-time safety mechanism (canary, feature flag kill switch, automatic rollback trigger) as evidence that a change is correct, ask what the mechanism is actually built to detect, and how that detection surface compares to the full scope of the claim being relied on. A mechanism scoped to "does this crash or fail obvious health checks on a handful of machines in the first few minutes" is not evidence for "this change is correct" — only for the much narrower claim it actually tests. A near-zero failure rate on a containment mechanism should prompt investigation into whether the earlier, broader verification step it's supposed to sit behind is still doing real work, not be read as confirmation that everything upstream is fine.

## See Also
- [Verification Checkpoint Proximity](verification-checkpoint-proximity.md)
- [Test Oracle Self-Validation](test-oracle-self-validation.md)
- [Parallel-Run Parity Verification](parallel-run-parity-verification.md)
