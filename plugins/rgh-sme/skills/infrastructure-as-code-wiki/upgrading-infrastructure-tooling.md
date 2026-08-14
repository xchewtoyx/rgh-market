---
type: concept
title: Upgrading Infrastructure Tooling and State
description: How to sequence upgrades of an infrastructure engine, provider plugins, or a whole tool, depending on whether the upgrade is backward compatible or changes the state file's schema.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 13"
---

Before upgrading an infrastructure engine, provider plugin, or module version, reconcile any active [configuration drift](configuration-drift.md) first — an upgrade applied on top of an already-inconsistent system makes it much harder to tell which problems are caused by the upgrade versus pre-existing drift — pin every module, plugin, and engine version explicitly so the upgrade is a deliberate, single, reviewable step rather than a moving target, and make sure dependencies between modules are already decoupled via [dependency injection](dependency-injection-for-infrastructure.md) rather than hardcoded, so each module can be validated independently as the upgrade proceeds.

For an upgrade that stays **backward compatible** — the new tool version reads the existing state format fine — update high-level, dependent modules first and verify them, then move down to the low-level, foundational modules last, the reverse order of [extracting resources from a monolithic stack](extracting-resources-from-a-monolithic-stack.md) but following the same underlying logic: validate the parts with the most at stake (or, here, the parts likely to surface a problem soonest) before touching the harder-to-recover foundation.

For an upgrade with a **breaking state schema change**, where the new engine version can't simply read the old state, a **blue-green state strategy** is the safer path: stand up a parallel state file under the new engine version rather than upgrading the existing state in place, and migrate bottom-up — low-level resources first, then high-level resources that depend on them — decommissioning the old engine's state only once everything has moved across.

Migrating between entirely different tools follows the same shape, gated by whether the new tool can import existing resources: if it can (`terraform import`, `pulumi import`, and equivalents), import bottom-up from low-level to high-level resources into the new tool's state, verifying a zero-delta plan at each step before removing the old tool's configuration — essentially the [extracting resources from a monolith](extracting-resources-from-a-monolithic-stack.md) procedure applied across tools rather than within one. If the new tool can't import, fall back to a full [blue-green infrastructure change](blue-green-infrastructure-change.md): provision a parallel stack with the new tool, migrate any stateful data (see [data continuity strategies](data-continuity-strategies.md)), and decommission the old stack. Either way, unit and contract tests need rewriting for the new tool's language and state schema, but integration and end-to-end tests — which validate real cloud behavior rather than a specific tool's internals — should carry over unchanged.
