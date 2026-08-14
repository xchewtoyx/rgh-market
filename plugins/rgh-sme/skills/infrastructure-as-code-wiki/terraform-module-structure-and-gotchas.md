---
type: concept
title: Terraform Module Structure and Common Gotchas
description: The standard file layout for a Terraform module's input/output contract, and two easy-to-hit mistakes — relative file paths and inline resource blocks — that break reuse.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 4"
---

Any directory of `.tf` files is a Terraform module; the directory `terraform apply` is run from is the *root module*, and anything instantiated from it via a `module` block is a *child module*. A production-ready module keeps a clean contract: `variables.tf` declares typed, described inputs; `outputs.tf` publishes values a caller can reference (`module.name.output`); `main.tf` holds the resources and data sources; and `locals` hold internal intermediate values that shouldn't be part of the module's public interface at all — this input/output/locals split is Terraform's concrete version of the general principle of [treating stack modules as facades or bundles with a deliberate interface](facade-module-pattern.md) rather than exposing internals directly.

Two gotchas repeatedly bite module authors:

- **Relative file paths resolve against the root module's working directory, not the child module's own directory.** A module referencing `"user-data.sh"` breaks the moment it's called from a root module located somewhere else, because Terraform resolves that path relative to wherever `terraform apply` was actually run from. The fix is `path.module`, which always resolves to the current module's own directory (`path.root` and `path.cwd` are the analogous root-module and invocation-directory variants).
- **Inline resource blocks (like an `ingress`/`egress` block embedded in a security group resource) conflict with any attempt by a caller to attach separate standalone resources later** (such as `aws_security_group_rule`), because Terraform will keep overwriting the inline block on every apply. Preferring separate standalone resources over inline blocks keeps a module open for callers to extend, rather than locking its shape closed — a concrete instance of the general preference for [loosely coupled, composable infrastructure components](infrastructure-component-coupling-and-cohesion.md).

See [Terraform module versioning and promotion](terraform-module-versioning-and-promotion.md) for how a module's contract is versioned and rolled out once it's stable, and [production-grade Terraform module design](production-grade-infrastructure-checklist.md) for further conventions (an `examples/` directory, pinned dependency versions) that a module needs before it's ready for production use.
