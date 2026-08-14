---
type: concept
title: Review Comment Resolution Conventions
description: >
  Structured conventions for unresolved vs. optional comments, batch publishing,
  and tracking whose turn it is to act — so review threads stay checkable.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 21"
---
# Review Comment Resolution Conventions

Review tools work best when comment status maps cleanly to verification obligations:

- **Unresolved comments** block commit until the author addresses them (by code change or reply) and marks them resolved.
- **Optional or informational comments** may be acknowledged without code change but still document reviewer intent.
- **Batch publishing** lets reviewers finish reading the whole change before comments go live, avoiding piecemeal partial feedback mid-read.

Scoring systems that require **zero unresolved comments** plus at least one LGTM and sufficient approvals make commit eligibility objectively checkable. Deliberately positive-only approval signals (LGTM/Approval) tie negative feedback to concrete, fixable threads rather than opaque thumbs-down ratings.

## Attention Set: Whose Turn
Turn-based review needs a visible **attention set** — who the change is blocked on now. Automatic updates when comments publish (with manual override) replace ad hoc chat about "whose turn" and make stalled reviews auditable.

## Trust-Based Soft Requirements
Some conventions rely on trust: authors may mark minor comments resolved without mandatory re-review; unresolved-comment counts are a soft requirement authors can clear after reply. That speeds timezone-separated teams but assumes professional norms — see [charitable interpretation in review](charitable-interpretation-in-review.md).

## Verification Action

When auditing a merged change, enumerate **open vs. resolved** threads at commit time. Commit with unresolved substantive threads, or emergency force-commit with post-hoc review only, weakens the audit trail — see [pre-commit peer review](pre-commit-peer-review.md) and [verification accounting](verification-accounting.md).
