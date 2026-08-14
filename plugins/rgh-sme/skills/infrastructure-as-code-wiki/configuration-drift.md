---
type: concept
title: Configuration Drift
description: The gradual divergence of infrastructure instances that were once identical, caused by manual changes or by automation applied inconsistently across instances.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 2"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 5"
---

Configuration drift is variation that accumulates over time across infrastructure instances that were originally built the same way. It happens when someone makes a manual change to one instance and not others, or when automation is applied selectively — updating some servers or stacks but not the rest of the fleet.

Drift is corrosive because it undermines confidence in automation: once instances diverge, applying shared code to all of them becomes riskier, because the code may have been tuned against the assumptions of one particular instance's now-nonstandard state. This creates the [automation fear spiral](automation-fear-spiral.md), where inconsistency causes people to avoid running automation unattended, which causes more inconsistency.

Drift is the direct enemy of the [reproducibility principle](reproducibility-principle.md) and of [minimizing variation](minimize-variation-principle.md) across a fleet. The main countermeasure is [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) — reapplying infrastructure code on a schedule regardless of whether it changed — or adopting [immutable servers](immutable-server-pattern.md), which sidestep drift by never modifying a running instance in place. A [snowflake system](snowflake-system.md) is the end state of unchecked drift: an instance nobody can confidently rebuild or change.

Tools with a dry-run or "check" mode give a way to detect drift without correcting it in the same step: running [idempotent](idempotent-infrastructure-code.md) convergence code against live infrastructure with changes suppressed reports exactly what *would* change if applied for real, which surfaces drift (manual intervention that diverged live state from the declared code) as a distinct, reviewable signal — separate from the everyday case of the code itself having legitimately changed since the last run. Run unattended and on a schedule, purely in dry-run mode, this becomes a lightweight drift-detection job in its own right, without committing to actually reconciling what it finds every time it runs.
