---
type: concept
title: SLO Adoption Anti-Patterns
description: >
  Four recurring mistakes when rolling out SLOs across an organization —
  going too broad too fast, over-scoping the initial set, reviewing too
  rarely, and hiding results.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 6"
---

- **Too much too soon** — don't roll SLOs out to an entire org or product at
  once. Start with one product, ideally one "failure domain" (a tightly
  coupled set of things that fail together), to limit how many people need
  convincing up front.
- **Less is more** — start with just a few SLIs, a few SLOs, and exactly one
  [error budget policy](error-budget-policy.md) (see
  [feature freeze as a first error budget policy](feature-freeze-as-first-error-budget-policy.md));
  expand later once the basics are working. See also
  [SLO count and scope](slo-count-and-scope.md).
- **Review early, review often** — reevaluate targets monthly or even
  quarterly at first (are customers complaining more or less than expected
  relative to target?); stretch the review cadence to twice a year or yearly
  only once things are mature and dialed in.
- **Be completely transparent** — publish dashboards visible company-wide,
  including to executives, that clearly show SLIs, SLOs, the current error
  budget policy, and current performance; ideally also track release-
  velocity trends over time to demonstrate the promised feature-velocity
  payoff. See [SLO discoverability](slo-discoverability.md). Transparency supports a [generative culture](measurement-trust-and-generative-culture.md) where metrics are used for alignment rather than punishment.

Two objections worth having a ready answer for: "we're not Google" — the
approach works at any size/maturity, and if it's gotten too complicated for
your org, that's overengineering, not a sign SLOs don't apply; "we're not
smart enough" — the underlying math is basic arithmetic and light
statistics plus discipline, not a credibility barrier.
