---
type: concept
title: Requirements Pyramid (Needs, Features, Requirements)
description: >
  Business needs, features, and detailed software requirements form a
  layered abstraction, with "feature" as the mediating layer that
  translates a raw problem-domain need into something a solution-domain
  requirement can be written against.
sources:
  - title: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise"
    resource: "Agile Software Requirements: Lean Requirements Practices for Teams, Programs, and the Enterprise (Dean Leffingwell), ch. 13"
---

Needs, features, and requirements sit at three distinct layers of
abstraction, and treating them as interchangeable is a common source of
confusion in a requirements document:

- **Needs** (problem domain) — the raw business problem or opportunity,
  stated independent of any solution.
- **Features** — the mediating layer, bridging problem domain and solution
  domain. A feature is coarse enough to be meaningful to a business
  stakeholder (people have an intuitive, everyday sense of what a
  "feature" is — spell-check-as-you-type is a feature of a word
  processor) but concrete enough to decompose into implementable work.
- **Software requirements** (solution domain) — the detailed, individually
  specifiable and testable statements a feature decomposes into, such as a
  [functional requirement](functional-requirement.md) or [user
  story](user-story.md).

At larger scale, two further layers sit above "need" without changing the
pyramid's underlying logic. An **investment theme** states a strategic
direction the enterprise is committing resources to (e.g., "personalize
the product"), coarser than any single need and, unlike a
[prioritized](requirements-prioritization.md) backlog item, funded as an
ongoing percentage of resources rather than addressed in priority order —
a theme that's quietly underfunded over time is a strategic failure even
if every individual backlog item still gets prioritized correctly. An
**epic** is the large, customer-facing initiative that instantiates a
theme's value, still coarse enough to only describe who's impacted and
what capability is implied, not yet decomposed into features. Both a
theme and an epic are, deliberately, not directly testable the way a
[story](user-story.md) is — they're only verified indirectly, through the
features and stories they eventually decompose into. That indirection is
a feature of the pyramid, not a gap in it: demanding a fit criterion at
the theme or epic level would force premature precision on something that
is supposed to stay a coarse statement of intent until it's actually
elaborated.

A feature can optionally be expressed in the same user-voice form as a
story ("As a writer, I can get automatic notification of spelling errors
as I write so that I can correct them immediately") — this doesn't change
its layer in the pyramid, it's still a feature, just written at a coarser
grain than the stories it will eventually decompose into. The pyramid's
practical use is diagnostic: if a document element can't be cleanly placed
at one of these three layers, that's usually a sign it's conflating a
need with the feature meant to satisfy it, or a feature with one of the
requirements underneath it, rather than a sign the pyramid doesn't apply.
See the [Vision document](vision-document.md) for the artifact that
captures the top of this pyramid at program scale.
