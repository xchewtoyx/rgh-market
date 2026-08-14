---
type: concept
title: Author Deference in Technical Review
description: >
  In peer review, the author owns approach choices among equally valid options;
  the reviewer verifies comprehension and material defects, not personal taste.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Author Deference in Technical Review

Technical review works best when roles are clear: the **author** owns how a change is implemented among valid alternatives; the **reviewer** verifies that the change is understandable, meets standards, and does not introduce material defects.

## When to Suggest Alternatives
Reviewers should propose a different approach only when the author's choice is genuinely deficient — harder to understand, less correct, or less efficient in a way that matters — not because another style is equally plausible but preferred. If several approaches are equally valid, defer to the author's preference even when defects are found elsewhere; frame findings as learning opportunities rather than authority contests.

## Ask Before Assuming Error
Ask why something was done a certain way before assuming it is wrong. This keeps review focused on checkable claims about the artifact rather than inferred intent — aligned with [charitable interpretation in review](charitable-interpretation-in-review.md).

## Verification Action

When reading review threads cited as evidence of quality, distinguish **substantive defects found** from **style disagreements settled by deference**. A review record full of overridden stylistic nits is not the same verification signal as one that surfaced misunderstanding, missing tests, or maintainability risks.
