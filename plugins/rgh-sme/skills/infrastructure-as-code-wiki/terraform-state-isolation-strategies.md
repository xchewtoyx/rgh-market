---
type: concept
title: Terraform State Isolation Strategies
description: Two ways to split a large Terraform codebase into multiple, independently-blast-radius-limited state files — workspaces and file-layout isolation — and how isolated states share data.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 3"
---

Keeping all of an organization's infrastructure in a single [Terraform state file](terraform-state-file.md) creates the same [blast radius](blast-radius.md) problem as a [monolithic stack](monolithic-stack-antipattern.md): a mistake anywhere can reach everything. Terraform offers two ways to isolate state.

**Workspaces** (`terraform workspace new/select/list/show`) keep multiple named state files under the same backend, all generated from identical HCL code. This is lightweight, but has real limits for anything long-lived: since every workspace shares the same code, environment-specific differences need conditional expressions rather than being structurally separate; a single backend location typically has one set of access permissions covering every workspace, making it hard to restrict who can touch production specifically; and it's easy to forget which workspace is currently selected and run a destructive command against the wrong one. Workspaces suit short-lived, throwaway, or feature-branch test environments, not permanent environment separation.

**File layout isolation** (the recommended default) organizes code into separate directories per environment and per component — for example `stage/vpc`, `stage/data-stores/mysql`, `prod/vpc`, `prod/data-stores/mysql` — each with its own state file at its own backend key. This strictly limits blast radius to one component in one environment, allows genuinely different IAM permissions per directory/key (so, for instance, most engineers can have no access to the `prod` key at all), and forces environment differences to be explicit in separate files rather than hidden behind conditionals on a workspace name. This is Terraform's concrete implementation of the general [reusable stack](reusable-stack-pattern.md) and [environment-as-stacks](environment-vs-stack.md) ideas.

Once state is split this way, components need an explicit way to read values published by another isolated state — the `terraform_remote_state` data source fetches another state file's outputs read-only, Terraform's specific implementation of the [stack data lookup pattern](stack-data-lookup-pattern.md) for [discovering cross-stack dependencies](resource-matching-pattern.md). [Terragrunt's `dependency` blocks](terragrunt-dry-environments.md) offer a more ergonomic alternative to `terraform_remote_state` for wiring isolated states together.
