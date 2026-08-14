---
type: concept
title: Weighted Category Vote
description: >
  Sort each option into a critical/important/useful tier per
  voter, then multiply tier counts by deliberately skewed
  weights so critical needs dominate the final ranking.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements (Dean Leffingwell), ch. 12"
---

When many stakeholders each need to weigh in on many candidate
options (a workshop-scale prioritization, not a small group
narrowing a handful of options), ask each voter to place every
option into one of three tiers — critical, important, or useful
— rather than rank or score it directly. Then aggregate by
multiplying the vote count in each tier by a deliberately
skewed weight, for example critical × 9, important × 3, useful
× 1, and sum per option to produce the final ranking.

The multipliers are chosen specifically so that critical votes
dominate: an option a few voters call critical should outrank
one many voters call merely useful, because the point of the
exercise is to surface every stakeholder's non-negotiable needs,
not to average sentiment. This is an explicit, visible weighting
scheme the group agrees to before voting — which is what
separates it from the failure mode
[multi-lens-comparison-without-false-precision](multi-lens-comparison-without-false-precision.md)
warns against: a composite score manufacturing false objectivity
out of hidden judgment calls. Here the judgment (critical needs
should dominate) is stated up front as the scheme's explicit
purpose, and the tiering itself — critical vs. important vs.
useful — is still each voter's own qualitative call, not a
disguised numeric rating.
