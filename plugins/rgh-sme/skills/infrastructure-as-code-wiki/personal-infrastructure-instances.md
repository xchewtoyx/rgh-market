---
type: concept
title: Personal Infrastructure Instances
description: Giving each person working on infrastructure code their own disposable instance to test changes against before pushing, so pipeline feedback isn't the first signal a change might be broken.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 20"
  - title: Ansible for DevOps
    resource: "Ansible for DevOps (Jeff Geerling), ch. 2"
---

Testing a code change before pushing it to the shared repository is both faster than waiting for a full pipeline run and kinder to the rest of the team, since it avoids breaking a shared build with an untested change. Doing this safely for online tests (see [offline vs online stack testing](test-fixtures-for-infrastructure-stacks.md)) requires giving each person their own instance to experiment against, since sharing a "dev" instance across multiple people applying locally-edited code reproduces the same conflicts described in [applying code from a centralized service](applying-code-from-a-centralized-service.md).

Three things make personal instances practical: people need to be able to spin up and tear down their own instance of whatever they're working on, which depends on keeping infrastructure pieces small enough to provision quickly on their own — the same [coupling and cohesion](infrastructure-component-coupling-and-cohesion.md) discipline that [test fixtures](test-fixtures-for-infrastructure-stacks.md) rely on; and everyone should use the exact same tools and scripts to apply and test their personal instance that the shared pipeline uses, so a personal test is actually representative of what the pipeline will do.

Some teams centrally manage even personal instances — each person pushes to a personal branch that a central service applies to their own instance, keeping the instance's code visible and its infrastructure recoverable by someone else even when its owner is unavailable, addressing the same "who tears this down while I'm on vacation" problem that untracked local instances create.

A lightweight, fully local variant of the same idea pairs a server configuration tool with a local VM manager (for example, Ansible with Vagrant and VirtualBox): every developer runs the same server-configuration code against a throwaway local VM before pushing, gets a full apply-and-verify cycle in seconds with zero shared-infrastructure cost, and can destroy and rebuild the VM from scratch as often as needed with no risk to anyone else's work. This is explicitly framed, in the tool's own literature, as applying test-driven-development discipline to infrastructure — iterating locally against a disposable instance rather than making unreviewed, undocumented changes directly against a shared or production server (a practice nicknamed "cowboy coding," the operational-scale version of the [reproducibility principle](reproducibility-principle.md)'s central complaint). It only stays representative of the shared pipeline's behavior if the local VM runs the same server-configuration code, tool version, and provisioning entry point that the pipeline itself uses — otherwise a local "pass" doesn't actually predict a pipeline "pass."
