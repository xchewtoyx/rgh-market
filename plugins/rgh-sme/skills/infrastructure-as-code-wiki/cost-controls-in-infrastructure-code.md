---
type: concept
title: Cost Controls in Infrastructure Code
description: Embedding cost governance directly into infrastructure code and its pipeline — policy gates on resource sizing, automated cost estimation on pull requests, and TTL-tagged ephemeral environments — rather than treating cost as a separate, after-the-fact concern.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 12"
---

Cost governance can be built into the same automated checks that already enforce other policy on infrastructure code, rather than left to manual review or discovered after the fact on a monthly bill. Two pipeline-level techniques do this directly: a [policy-as-code](policy-as-code-for-infrastructure.md) test that inspects declared instance sizes against a catalog of cost data and hard-fails a plan that requests something over budget (say, any VM spec above a set vCPU ceiling); and an automated cost-estimation tool (such as Infracost) that parses a plan's diff, computes the resulting monthly cost delta, and posts it directly on the pull request, so a reviewer sees the financial impact of a change alongside its infrastructure impact before approving it — the cost analogue of the [plan-review pull request workflow](infrastructure-pull-request-workflow.md).

Several practices reduce ongoing waste specifically because infrastructure is defined and orchestrated as code: sweeping and terminating untagged or orphaned resources (unattached disks, unassociated floating IPs) that accumulated outside any tracked ownership; scheduling non-production environments to stop automatically outside business hours; right-sizing and autoscaling based on real utilization rather than static provisioning; and tagging ephemeral stacks with an expiry (`TTL`/`expire_date`) that an automated job uses to destroy them once they age out, rather than relying on someone remembering to tear a test environment down.

More structurally, provisioning [ephemeral, on-demand test environments](persistent-vs-ephemeral-test-stacks.md) per feature branch — created for CI, torn down immediately after — avoids the ongoing cost of maintaining persistent non-production environments at all; consolidating test infrastructure within a single availability zone and routing over private networking avoids unnecessary cross-zone or cross-region data egress fees; and [testing in production](testing-infrastructure-in-production.md) via feature flags, canary routing, and blue-green deployment reduces the need to maintain a full duplicate staging environment purely to validate changes before they reach real traffic.
