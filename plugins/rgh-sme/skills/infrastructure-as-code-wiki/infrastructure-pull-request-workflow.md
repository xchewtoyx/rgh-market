---
type: concept
title: Infrastructure Pull Request Workflow
description: Reviewing a Terraform plan's diff as a pull-request comment before merge, so a human approves the actual computed change rather than just the source diff.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 10"
---

A common infrastructure delivery workflow runs `terraform plan` automatically when a pull request is opened, posts the resulting diff of additions, modifications, and deletions as a comment on the PR, and requires a human to review that plan diff — not just the source code diff — before merge triggers `terraform apply`. This matters because a small source code change can produce a large or unexpected infrastructure diff (a renamed argument that forces a resource replacement, say), so reviewing the *computed* plan catches risks that reviewing only the HCL text would miss; it's a specific implementation of the general practice of [previewing changes](test-fixtures-for-infrastructure-stacks.md) before applying them.

A specific security risk this workflow needs to guard against: a CI system holding permanent, broad cloud credentials (an `AdministratorAccess`-equivalent) is a severe target, since a compromised CI plugin or dependency can leak those credentials and do arbitrary damage. Mitigations include short-lived OIDC-federated credentials scoped to the specific repository and branch running the job (the CI-side version of [authenticating Terraform to a cloud provider](authenticating-and-passing-secrets-in-terraform.md)), isolating the workers that actually hold apply permissions from the general-purpose CI orchestrator, and using a tool like Atlantis to enforce per-pull-request state locking so concurrent plans and applies from different PRs can't race each other.

This workflow is a concrete Terraform-ecosystem instance of the general [infrastructure delivery pipeline](infrastructure-delivery-pipeline.md) and [governance in a pipeline-based workflow](governance-in-pipeline-based-workflow.md) — the pull request and its plan comment serve as the pipeline's approval stage.
