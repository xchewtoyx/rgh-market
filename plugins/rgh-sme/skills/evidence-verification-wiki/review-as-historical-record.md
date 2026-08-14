---
type: concept
title: Review as Historical Record
description: >
  Review artifacts preserve who approved what, why a change was made, and how
  decisions were discussed — enabling later independent verification ("code archaeology").
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9, 21"
---
# Review as Historical Record

Every reviewed change leaves a durable record: diffs, descriptions, comment threads, LGTM/approval bits, and post-commit follow-ups. That record supports **code archaeology** — later engineers (or auditors) reconstructing when a pattern was introduced, what alternatives were considered, and which reviewer attested to it.

## What Makes the Record Useful
A good change description states **what** changed and **why**, not merely "bug fix." Inline comments capture detail inappropriate for public APIs. If decisions evolve during review, the description should be updated so the archived thread matches what was actually committed. Review tools indexed by change state let future readers find the discussion that justified a line of code long after the original author moved on.

## Knowledge Transfer Side Effect
Review also spreads domain knowledge in the present: authors pick expert reviewers; reviewers leave FYI comments; both sides learn. But the historical record extends that transfer across time zones and turnover — the audit trail outlives any single conversation.

## Verification Action

When a claim rests on "we reviewed this in PR #…," trace the archived description and thread — not just the merge button. Missing rationale, unresolved threads marked away without reply, or post-hoc description edits without comment are weak audit trails — compare [verification accounting](verification-accounting.md) and [verification markup conventions](verification-markup-conventions.md).
