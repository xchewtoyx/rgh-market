---
type: concept
title: Canary Infrastructure Rollout
description: Applying an infrastructure change to a small subset of a large fleet first and watching it before widening, as a deployment-safety net rather than a substitute for pre-production testing.
sources:
  - title: The Practice of Cloud System Administration
    resource: "The Practice of Cloud System Administration (Limoncelli, Chalup, Hogan), ch. 11"
---

A canary rollout is the large-fleet variant of a [rolling infrastructure update](rolling-infrastructure-updates.md): rather than updating one node at a time in strict sequence — which for a fleet of hundreds or thousands of nodes would take too long to be practical — the change is applied to a very small group first (as few as one node), watched for a short window since most problems surface within the first few minutes, and then widened in progressively larger steps (for example, one node, then one percent of the fleet, then the rest) as long as it keeps "surviving." A failed canary halts the rollout immediately; the small number of already-updated nodes are rolled back or simply removed from service, leaving the rest of the fleet on the known-good version.

The purpose of a canary is easy to misread as a form of testing, but it is a deployment-safety mechanism, not a substitute for one. A failing test in a [progressive testing](progressive-testing-for-infrastructure.md) pipeline is a success — a bad change was caught before it could reach anything live. A failing canary is closer to a process failure: it means a defect that pre-production testing should have caught made it all the way to production infrastructure, and it should happen rarely enough that each occurrence justifies pausing further rollouts to find and close the specific test gap that let it through, rather than treating canarying as an acceptable place to discover problems. A canary environment that quietly becomes the place real correctness testing happens — for example, because production has come to differ from the test environment in ways nobody has gone back and reconciled — is a sign that [testing infrastructure in production](testing-infrastructure-in-production.md) has drifted from a deliberate complement to pre-production testing into an unplanned replacement for it.
