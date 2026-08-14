---
type: concept
title: Environment Drift
description: >
  The silent divergence in configuration, OS patches, libraries, or settings
  between development, testing, staging, and production environments as they
  age, which invalidates the confidence earlier pipeline stages were meant to provide.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 1, 2"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 11"
---

# Environment Drift

Environments drift when their configuration is allowed to change outside of
version-controlled automation — the classic cause is
[snowflake servers](snowflake-server.md) accumulating manual, unrecorded
tweaks. Once environments have drifted apart, a build passing tests in one
environment (e.g. QA) says less and less about whether it will work in
another (e.g. production), which undermines the entire premise of the
[deployment pipeline](deployment-pipeline.md): that passing each gate
increases genuine confidence in production-readiness.

The structural fix is to provision every environment from the same
version-controlled automation every time — see
[idempotent provisioning](idempotent-provisioning.md) and
[phoenix server](phoenix-server.md) — so environments cannot silently diverge
because there is no persistent, hand-edited state for them to diverge in.

## Automation lag: apply on a schedule, not just on change

A related, more direct prevention: the longer it's been since automation was
last applied to an environment, the more likely the next run is to fail —
because unrelated drift (dependency changes, tool upgrades, an
un-folded-back manual fix) accumulates the whole time nothing runs. Applying
automation only when its own code changes leaves that gap unbounded. Running
it continuously or on a fixed schedule, even when nothing has changed,
keeps the gap small enough that failures are rare and, when they do happen,
easy to diagnose because little else could have changed since the last
successful run. This is the mechanism behind GitOps-style continuous
reconciliation, and complements the dry-run detection below rather than
replacing it.

## Detecting drift automatically

Beyond preventing drift structurally, it can be detected directly: run
provisioning automation in a dry-run/check mode on a schedule against live
environments — applying nothing, but reporting anything that *would* change
if it ran for real. Any reported difference means the live environment has
diverged from its version-controlled definition, whether from an
unauthorized manual change or a latent bug. This gives an explicit, automated
signal for drift instead of waiting to discover it indirectly, the way the
original [snowflake server](snowflake-server.md) problem usually surfaces —
as a mysterious deployment failure with no obvious cause.
