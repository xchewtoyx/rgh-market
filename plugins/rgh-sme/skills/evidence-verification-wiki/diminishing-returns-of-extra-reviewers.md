---
type: concept
title: Diminishing Returns of Extra Reviewers
description: >
  The first independent reviewer adds the most verification value; each additional
  reviewer adds less while coordination cost grows quickly.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Diminishing Returns of Extra Reviewers

Requiring many reviewers feels safer but often buys little extra assurance. Empirically at Google, **the first LGTM is by far the most valuable**; subsequent LGTMs add much less than teams expect while slowing the process. Most changes use exactly one primary reviewer; wider CC lists provide optional visibility without requiring unanimous sign-off.

When multiple reviewers are warranted, they should cover **different aspects** of the same change (correctness vs. ownership vs. readability — see [separated review approval roles](separated-review-approval-roles.md)) rather than duplicating the same line-by-line pass.

## Verification Action

Do not treat "reviewed by five people" as five times the evidence of "reviewed by one careful peer" unless each reviewer had a distinct mandated role. Redundant reviewers can create an illusion of thoroughness without proportional scrutiny — especially on oversized changes — see [review batch size effect](review-batch-size-effect.md).
