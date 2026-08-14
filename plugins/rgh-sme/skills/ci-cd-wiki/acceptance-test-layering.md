---
type: concept
title: Acceptance Test Layering (Specification / Driver / SUT)
description: >
  Separating an acceptance test's business-domain specification from the
  technical driver that executes it against the system under test, so a UI or
  protocol change requires updating only the driver layer, not every scenario.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 8"
---

# Acceptance Test Layering (Specification / Driver / SUT)

A three-layer architecture keeps
[automated acceptance tests](automated-acceptance-testing.md) from becoming
brittle as the application's UI or protocols evolve:

1. **Specification layer**: scenarios written purely in business-domain
   language (e.g. Cucumber feature files, FitNesse tables). No UI details
   (XPaths, button IDs, URLs) or technical protocol details appear here at
   all.
2. **Application driver layer**: a technical abstraction (e.g. the Page
   Object pattern for UIs, an HTTP REST client for APIs) that translates
   domain actions from the specification layer into concrete calls against
   the running system.
3. **System under test (SUT)**: the deployed application in a realistic QA
   environment, with test databases and mocked external integrations.

## Why the split matters

When the UI changes, only the driver layer needs updating — the
business-language specifications above it are untouched, because they never
referenced UI details in the first place. This is what lets acceptance-test
suites survive years of UI rework without a full rewrite, and what makes the
specification layer trustworthy as living documentation: it describes
behavior, not implementation, so it stays accurate even as implementation
changes.
