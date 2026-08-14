---
type: concept
title: Claim Verification Triage
description: The practice of prioritizing checkable claims based on external dependencies, risk level, and ease of verification to optimize the review schedule.
sources:
  - title: "The Chicago Guide to Fact-Checking, Second Edition"
    resource: "The Chicago Guide to Fact-Checking, Second Edition (Brooke Borel), ch. 3"
---
# Claim Verification Triage

**Claim verification triage** is the practice of ordering verification tasks to maximize efficiency and meet deadlines. Since different claims require different verification methods, a reviewer should not simply check claims in the order they appear in the text. Triage presupposes the set of claims to check is already known; for the prior step of discovering claims a change could silently affect that nobody has yet identified as needing a check, see [effect propagation analysis for verification scope](effect-propagation-analysis-for-verification-scope.md).

## Triaging Priorities
1. **External People/System Dependencies (High Priority)**:
   - Identify claims that require contacting external experts, stakeholders, or running slow, resource-intensive tests/queries.
   - *Action*: Initiate outreach or launch long-running test suites immediately. Because external entities operate on their own schedules, contacting them first prevents verification from stalling near deadlines.
2. **High-Attention / High-Risk Claims**:
   - Flag claims that carry substantial legal, safety, or financial risk if wrong, as well as claims that the author explicitly notes as questionable (e.g., marked with `(CK)` — see [verification markup conventions](verification-markup-conventions.md)).
   - *Action*: Prepare specialized verification questions and compile supporting documentation early.
3. **Document-Based / Local Claims (Low Priority)**:
   - Identify claims that can be verified using local resources, public search engines, local database queries, or easily accessible documentation.
   - *Action*: Process these tasks in the background while waiting for responses from external experts or long-running tests.

## Triaging Steps
1. **First Pass Read**: Read the draft to grasp the context and flag potential [omissions](omission-detection.md).
2. **Mark the Claims**: Extract all [checkable claims](defining-checkable-claims.md).
3. **Group and Schedule**: Group claims by the source needed to verify them (e.g., Expert A, Database B, Reference Document C) and initiate the longest-lead-time tasks first.

## See Also
- [Defining Checkable Claims](defining-checkable-claims.md)
- [Verification Markup Conventions](verification-markup-conventions.md)
- [Omission Detection](omission-detection.md)
- [Correction Effort Asymmetry](correction-effort-asymmetry.md)
- [Precommitted Evaluation Criteria](precommitted-evaluation-criteria.md)
