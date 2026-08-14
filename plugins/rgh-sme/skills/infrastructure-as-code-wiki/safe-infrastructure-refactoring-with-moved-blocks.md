---
type: concept
title: Safe Infrastructure Refactoring with Moved Blocks
description: Recording a resource rename or relocation explicitly in code so a stack tool updates its state bookkeeping without destroying and recreating the real underlying resource.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 5"
---

Simply renaming a resource's identifier in code (`aws_security_group.instance` to `aws_security_group.cluster_instance`) looks like a harmless refactor, but a stack tool has no way to know the old and new names refer to the same real object — it sees the old name disappear and a new one appear, and plans to destroy the former and create the latter, which is disruptive or outright dangerous for anything stateful or in active use.

Terraform's `moved` block (1.1+) declares this rename explicitly in code (`moved { from = aws_security_group.instance, to = aws_security_group.cluster_instance }`), so `terraform apply` updates only the [state file's](terraform-state-file.md) internal mapping between code identifier and real resource — no resource is actually created, changed, or destroyed. This replaces the older, manual, out-of-band `terraform state mv` CLI command with something declared in version-controlled code, so the refactor's history travels with the codebase rather than living only in someone's shell history.

This is a narrower, code-native alternative to the general [infrastructure surgery technique](infrastructure-surgery-technique.md) — both edit a stack tool's bookkeeping rather than real infrastructure, but a `moved` block is declarative, reviewable, and safely repeatable, while raw state surgery is an imperative, non-idempotent, manual last resort.
