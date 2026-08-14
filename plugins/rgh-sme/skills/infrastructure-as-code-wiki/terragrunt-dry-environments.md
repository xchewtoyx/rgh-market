---
type: concept
title: "Terragrunt: DRY Environment Configuration"
description: A wrapper tool that generates repeated Terraform boilerplate (backend config, dependency wiring) from a small root configuration, avoiding the code duplication plain HCL forces across environment directories.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 10"
---

Isolating Terraform state [by file layout](terraform-state-isolation-strategies.md) — separate directories per environment and component — solves blast radius, but in plain HCL it means copy-pasting near-identical `backend` blocks, provider configuration, and dependency wiring into every one of those directories, which is exactly the duplication the [copy-paste environments antipattern](copy-paste-environments-antipattern.md) warns about, just at the configuration-boilerplate level rather than the whole-stack level.

Terragrunt (an open-source wrapper from Gruntwork) removes this duplication. A single root `terragrunt.hcl` generates a consistent backend configuration (bucket, key, lock table) dynamically for every subdirectory based on its position in the file tree, rather than that block being repeated by hand in each one. Each environment/component directory then holds a small `terragrunt.hcl` that just points at a specific versioned module (`source = "...//services/hello-world-app?ref=v0.0.7"`, the same [semantic versioning and promotion](terraform-module-versioning-and-promotion.md) discipline as plain Terraform modules) and supplies its `inputs`. Terragrunt's `dependency` blocks replace the more brittle `terraform_remote_state` data source for reading another component's outputs, and `terragrunt run-all apply` walks the whole directory tree and applies components in the correct dependency order automatically.

Terragrunt is a concrete tool implementing the [wrapper stack pattern](wrapper-stack-pattern.md) — each environment/component directory is a thin wrapper project that only sets parameters and points at a shared, versioned module, exactly the shape that pattern describes, with Terragrunt providing the machinery to keep that wrapping DRY instead of copy-pasted.
