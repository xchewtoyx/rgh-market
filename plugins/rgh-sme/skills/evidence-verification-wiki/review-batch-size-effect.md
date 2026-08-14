---
type: concept
title: Review Batch Size Effect
description: Reviewer thoroughness degrades non-linearly as the size of a single reviewed unit grows, so a reviewable submission should be kept small rather than comprehensive.
sources:
  - title: "The DevOps Handbook, 2nd Edition"
    resource: "The DevOps Handbook, 2nd Edition (Kim, Humble, Debois, Willis, Forsgren), ch. 18"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---

# Review Batch Size Effect

The risk that a reviewer misses a real problem does not scale linearly with the size of what they're asked to review — it scales much faster. A ten-line change reviewed carefully might surface ten issues; the same reviewer asked to review a five-hundred-line change is far more likely to skim it and say "looks good," even though the larger change objectively contains more opportunity for error. Past some size, a review stops being an independent check and becomes a formality — the reviewer's name attached to something they didn't actually verify.

## Why Size Breaks Review Quality
- **Working-memory limits**: a reviewer can hold only so many interacting pieces of a change in mind at once; beyond that, they either skim or reconstruct a plausible mental model that may not match what's actually there.
- **Time pressure compounds the effect**: a large review request usually arrives with the same implicit time budget as a small one, so the reviewer's actual attention-per-line falls sharply as the request grows.
- **Diminishing accountability per unit**: when a reviewer signs off on a large bundled submission, no single part of it feels like "their" responsibility — approval becomes a single up-or-down gate on the whole bundle rather than a considered judgment on each piece within it.

At Google, keeping changes near **200 lines or fewer** is the dominant practice for keeping review nimble; roughly **35% of changes touch a single file**, and most receive one primary reviewer — sizes far above that norm should trigger scrutiny that the review was real, not rubber-stamped.

## Verification Action
- When asked to review something large and monolithic (a big document revision, an omnibus change, a bundle of unrelated edits), treat the size itself as a red flag before evaluating content — ask whether it can be split into independently reviewable pieces first.
- When designing a review process (for documents, code, or any claim-bearing artifact), keep the unit that goes to a reviewer at once small enough that a careful read is actually feasible in the time a reviewer will realistically spend — don't rely on reviewer diligence to compensate for an oversized submission.
- Treat a pattern of fast approvals on large submissions as a symptom of rubber-stamping, not evidence that the large submissions were unusually clean — see [charitable interpretation in review](charitable-interpretation-in-review.md) for the adjacent failure mode of assuming good faith substitutes for actually checking.
- This complements, rather than replaces, checklist-based review: even a well-designed [verification checklist](verification-checklist-design.md) degrades in effectiveness if the unit it's applied to is too large for a reviewer to hold in mind while working through it.
