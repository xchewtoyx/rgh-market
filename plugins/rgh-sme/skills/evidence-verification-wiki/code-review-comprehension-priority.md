---
type: concept
title: Code Review Comprehension Priority
description: >
  Independent review primarily verifies that a change is understandable and
  maintainable by others, not that it matches the reviewer's preferred approach.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Code Review Comprehension Priority

At scale, the main value of code review is often **comprehension** — whether someone other than the author can understand and maintain the change — rather than catching every possible defect. Correctness matters, but automated tests and static analysis increasingly cover many correctness checks; human review still excels at asking "will anyone else understand this six months from now?"

## LGTM Criteria: Correctness Plus Comprehension
An LGTM ("looks good to me") attests both that the change appears to do what it claims and that it is understandable to a peer. Comprehension feedback should be treated seriously: if a reviewer asks a question, that question will likely recur for future readers — clearer structure or comments may be required even when the logic is already correct.

## Author Deference on Approach
Reviewers defer to authors on **approach** when several valid implementations exist. Alternatives should be suggested only when they materially improve comprehension (less complexity) or functionality (more efficiency). Holding out for a reviewer's preferred style when the author's approach is valid slows review without improving verification quality — see [author deference in technical review](author-deference-in-technical-review.md).

## Verification Action

When evaluating whether "code review happened," ask what the review actually checked. A review that only enforced stylistic preference or re-debated settled design (see [design decisions outside code review](design-decisions-outside-code-review.md)) is weaker evidence than one that tested comprehensibility and correctness against stated intent. Flag claims that treat review as proof of bug-freedom — [evidence triangulation](evidence-triangulation.md) still applies.
