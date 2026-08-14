---
type: concept
title: Shift-Left Security
description: >
  Moving security expertise into design time and automated pipelines
  instead of a downstream manual gate is what lets security scale past
  the infosec-to-developer staffing ratio.
sources:
  - title: Accelerate
    resource:
      "Accelerate: The Science of Lean Software and DevOps (Forsgren,
      Humble, Kim), ch. 6"
---

# Shift-Left Security

A typical organization staffs roughly one infosec specialist per ten
infrastructure engineers per hundred developers (Wickett 2014). A security
model built around infosec as a gatekeeper at the end of the delivery
lifecycle — manually inspecting each change before it ships — cannot scale
against that ratio once delivery tempo rises to multiple deploys per day:
the queue either throttles delivery to a crawl or gets routed around
entirely, and the review happens too late to change the design cheaply
anyway.

Shifting left means moving security work to where it's cheap and where the
scarce specialists can act as multipliers instead of bottlenecks:

- **Design time**: infosec participates in feature design and threat
  modeling while the design is still a document, per
  [security design review](security-design-review.md) — the earliest and
  cheapest point to change course.
- **Build time**: instead of reviewing every change by hand, infosec builds
  pre-approved libraries, frameworks, and templates so secure code is what
  developers write by default — see
  [secure-by-construction frameworks](secure-by-construction-frameworks.md).
- **CI time**: security checks run as automated pipeline steps rather than
  a human sign-off — [static analysis](static-analysis-for-security.md)
  and [testing for security](testing-for-security.md) catch what manual
  review used to gate on, at every commit instead of once before release.
- **Runtime**: making live attack telemetry visible to every engineer, not
  only security specialists, pulls the same shift-left effect forward
  into production — see
  [security telemetry visibility](security-telemetry-visibility.md).

This reallocates the specialists: instead of personally inspecting every
change, they build the guardrails and automation that make the default
path secure, then spend their time on the design-level judgment calls that
automation can't make. The empirical payoff tracks the reallocation:
organizations that build security into daily work this way spend roughly
half as much time remediating security issues as organizations that defer
security to a downstream audit.

This is a scaling argument, not just a process preference — the same logic
that justifies [secure-by-construction frameworks](secure-by-construction-frameworks.md)
and early [design review](security-design-review.md) as *why* those
practices exist, rather than restating what each does mechanically.
