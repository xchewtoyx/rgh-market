---
type: concept
title: Change Assurance Mechanisms by Tooling
description: The concrete evidence a tool or deployment model can actually give you about a change's effect before it lands — a reviewable plan, an idempotent dry-run, or replace-not-mutate with trivial rollback — versus giving you none.
sources:
  - title: Terraform Up & Running
    resource: "Terraform: Up & Running, 3rd Edition (Yevgeniy Brikman), ch. 2"
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 1, ch. 9"
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 12"
---

Different tools and deployment models give fundamentally different kinds of evidence about what a change will actually do before it's applied. When deciding how much manual gatekeeping a change needs — see the [infrastructure change taxonomy](infrastructure-change-taxonomy.md) — the assurance mechanism actually available is as important as how routine the change looks, because a "routine-looking" change with no real preview mechanism is a worse candidate for an unattended pipeline than it appears.

**Reviewable plan/diff (provisioning tools).** Terraform's `terraform plan` (and equivalents in CloudFormation, Pulumi) inspects current state, computes a dependency graph, and prints exactly what it will create, update in place, or destroy before anything happens. This is a genuine preview of the actual operations that would run — a human or an automated policy check can veto it before `apply`. It's the strongest assurance mechanism covered here because it's specific to the change at hand, not a general property of the tool.

**Idempotent convergence plus dry-run (declarative configuration management).** [Idempotent](idempotent-infrastructure-code.md) tools like Ansible, Chef, and Puppet give a weaker but still real guarantee: reapplying converges toward the same declared state regardless of starting point, so a run that reports no changes is itself evidence nothing has drifted. Most of these tools also support a check/diff mode that reports what *would* change without actually changing anything — a dry-run in the same spirit as a Terraform plan, though generally coarser, since it's evaluated task-by-task rather than as a single dependency-aware graph. [Testing declarative infrastructure code](testing-declarative-infrastructure-code.md) covers how to turn this dry-run capability, and the run-twice-expect-zero-changes idempotence check, into an actual pass/fail test rather than something inspected by eye.

**Immutable replace-not-mutate (baked images).** A [baked server image](baking-vs-frying-server-configuration.md) or an [immutable server](immutable-server-pattern.md) gives a different kind of assurance entirely: not a preview of the change, but a guarantee about what happens if the change is wrong. Because the new version is a whole new instance built and tested before it takes any live traffic, and the old instance stays intact until cutover, rollback is trivial — swap traffic back to what was already known-good, via [blue-green infrastructure change](blue-green-infrastructure-change.md) or [rolling infrastructure updates](rolling-infrastructure-updates.md). The cost is that this assurance is bought with image build time (commonly 10–60 minutes), so it doesn't suit changes that need to land in seconds.

**Mutable in-place application (fried config, ad hoc scripts).** At the weak end, applying imperative scripts or ad hoc commands directly to a running instance gives no preview and no cheap rollback: the only way to know what happened is to have already applied it, and undoing it means writing and running another change, not switching back to something already proven. This is also the profile most prone to [configuration drift](configuration-drift.md) if applied inconsistently across a fleet — [continuous configuration synchronization](continuous-configuration-synchronization-pattern.md) is what turns this weak-assurance mechanism into a self-correcting one, at the cost of applying changes on a schedule rather than getting a preview beforehand.

Matching these against the [change taxonomy](infrastructure-change-taxonomy.md): a change with a reviewable plan and a small, well-understood [blast radius](blast-radius.md) is a reasonable candidate for continuous deployment even without a human gate, because the plan itself is the safety check. A change whose only tooling gives no preview and no cheap rollback warrants a human gate — a "normal" change — regardless of how routine it otherwise looks, precisely because nothing else is standing in for that missing assurance.
