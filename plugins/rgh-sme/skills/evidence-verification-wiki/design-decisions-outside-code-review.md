---
type: concept
title: Design Decisions Outside Code Review
description: >
  Using code review to verify implementation against settled design, not to reopen
  architecture or API decisions that belong in earlier review forums.
sources:
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright, eds.), ch. 9"
---
# Design Decisions Outside Code Review

Code review verifies that a proposed implementation is appropriate **given decisions already made** — not that the underlying design should have been chosen. Re-debating settled architecture, API shape, or product direction inside a diff review mixes two different verification questions: "Is this the right approach?" versus "Does this change correctly implement the agreed approach?"

Research, design communication, design proposals, API reviews, and prototypes should happen **before** substantial new code is written. Code review then checks comprehension, correctness, maintainability, and standards — not substitute for those upstream forums.

## Code as Liability Context
Code is a maintenance liability even when necessary — duplicated utility code can cost more than no code at all because every copy must stay synchronized. That economic fact supports doing design and reuse investigation upstream rather than discovering architectural mismatch late in a line-by-line review.

## Verification Action

When a review thread shows fundamental design disagreement, check whether a prior design/API review record exists. If not, the dispute may indicate a missing upstream verification step rather than a code-review failure. Flag documents that treat code-review LGTM as evidence that architecture was validated when only implementation fidelity was at issue — see [claim scope calibration](claim-scope-calibration.md).
