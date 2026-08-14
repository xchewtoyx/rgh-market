---
type: concept
title: Characterization Baseline as a Verification Oracle
description: A baseline captured directly from a system's actual current output is valid evidence for detecting future drift, even though it is not evidence the behavior is correct.
sources:
  - title: "Working Effectively with Legacy Code"
    resource: "Working Effectively with Legacy Code (Michael C. Feathers), ch. 13"
---

# Characterization Baseline as a Verification Oracle

Two different questions get asked of the same check, and conflating them causes reviewers to either trust a check too much or dismiss it as worthless: **"is this behavior correct?"** and **"has this behavior changed?"** A correctness check needs an independent standard (a specification, a domain expert, a known-right answer) to compare against. A **characterization baseline** needs neither — it is built by observing whatever the system's actual current output happens to be, and its only job is to notice when that output later diverges.

## Capturing a baseline

1. Assert a value you know or suspect is wrong (a placeholder, deliberately incorrect).
2. Run the check and read the actual value it reports back.
3. Replace the placeholder assertion with that observed value.

The resulting check now documents current behavior precisely, whether or not that behavior is desirable — it becomes valid evidence for "this changed" even though it was never evidence for "this is right."

## Why "we're just enshrining a bug" misses the point

A baseline captured this way invites the objection that it proves nothing, since it was built from the system's own output rather than an independent standard. The objection conflates the two questions above: the baseline was never offered as evidence of correctness, only as evidence of consistency — a way to know, cheaply and repeatably, whether behavior drifted from a documented starting point, which is otherwise only knowable by re-deriving the system's behavior from scratch (reading code, mentally tracing values) every single time. See [verification oracles](verification-oracles.md), which lists a historical baseline as one of several oracle types — this note gives the deeper justification for why an oracle built from nothing but the system's own prior output is still a legitimate one for its specific purpose.

## Do not discard a suspicious baseline

If a captured baseline looks wrong once observed, do not quietly drop it or "fix" it before recording it — record it as-is and flag it separately as suspect, then investigate. Silently omitting a suspicious observation removes exactly the evidence a future investigation would need, and it can quietly convert an already-known risk into an invisible one.

The same tension shows up at system scale in [parallel-run parity verification](parallel-run-parity-verification.md): a legacy system used as the reference oracle for a replacement's behavior may itself be the "suspicious baseline," and the fix is the same — record and account for the known defect explicitly rather than letting the mismatch either block a valid migration or silently redefine correctness as "matches the bug."
