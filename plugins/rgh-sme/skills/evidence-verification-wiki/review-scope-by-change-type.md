---
type: concept
title: Review Scope by Change Type
description: >
  Different change categories — greenfield, behavior change, bug fix, rollback,
  large-scale refactor — warrant different verification focus and review strictness.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Review Scope by Change Type

Not every change needs the same review questions. Matching scope to change type keeps review checkable:

## Greenfield / New Code
New projects should not surprise reviewers — design review precedes code review. The code review confirms implementation matches an **agreed** design (not re-litigating API shape), adequate tests (including endpoints that fail when assumptions change), ownership files, comments, and CI integration. This is where long-term maintainability matters most.

## Behavioral Changes and Optimizations
Ask whether the change is necessary and improves the codebase; deletions of dead code are often high-value. Behavioral changes need updated tests run through CI; optimizations may need benchmark evidence so reviewers can verify claims.

## Bug Fixes and Rollbacks
Bug fixes should stay **focused** — bundling unrelated edits enlarges review and complicates rollback. Reviewers should expect test updates that would have caught the bug. **Rollbacks** revert to a known state but still require their own review; because dependents adopt new code quickly, every change should stay small and atomic so rollback does not cascade — see [review batch size effect](review-batch-size-effect.md).

## Large-Scale Automated Changes (LSCs)
Machine-generated refactors may route to global approvers for low-risk patterns or to local owners for risky ones. Reviewers focus on local applicability, not re-debating the org-wide tool process already reviewed elsewhere — scope expansion requests that would stall hundreds of in-flight automated changes are disallowed.

## Verification Action

When a document cites "standard code review," ask **which change type** applied and whether the review questions matched it. A bug-fix review that re-opened greenfield design, or an LSC review that treated local nits as veto rights, indicates process mismatch rather than thorough verification.
