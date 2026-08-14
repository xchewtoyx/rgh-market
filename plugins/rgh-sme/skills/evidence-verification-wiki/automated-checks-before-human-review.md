---
type: concept
title: Automated Checks Before Human Review
description: >
  Running mechanical verifiers (tests, linters, static analysis) before a human
  reviewer sees a change so review effort focuses on substance, not formatting.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9, 21"
---
# Automated Checks Before Human Review

Human review is expensive and easy to waste on problems machines detect reliably. **Presubmit** hooks and snapshot-time analyzers run when a change is uploaded or mailed for review, blocking or flagging failures before a reviewer spends attention on formatting, style, or known bug patterns.

## Shift-Left Verification
Catching defects at review time is cheaper than after commit; catching them in automated presubmit is cheaper still. Authors who preview analyzer results while "wearing the reviewer's hat" reduce back-and-forth. Reviewers should focus on comprehension, design fit, and issues automation misses — not on issues a linter could have enforced.

## Verification Action

When a document cites human review as quality assurance, ask what **automated gates ran first** and whether they passed. A review that only caught mechanical issues a presubmit should have blocked is weak process evidence. Conversely, presubmit pass plus shallow human LGTM on a large change may still be insufficient — see [review batch size effect](review-batch-size-effect.md) and [code review comprehension priority](code-review-comprehension-priority.md).
