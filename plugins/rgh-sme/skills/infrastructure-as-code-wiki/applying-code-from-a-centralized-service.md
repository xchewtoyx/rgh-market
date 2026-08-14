---
type: concept
title: Applying Code from a Centralized Service
description: Why infrastructure code for any shared instance should always be applied by a single central service rather than from individual team members' workstations.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 20"
---

Running a stack tool from a local workstation is fine for a personal test instance nobody else uses, but it's a source of real problems for any shared instance — a delivery environment or production. If someone applies locally-edited code before pushing it to the shared repository, nobody else has access to the version now running; if they don't push immediately, the next person to apply code (with an older version they pulled and edited) silently reverts the first person's change, and untangling what actually happened becomes confusing fast. Notably, a stack tool's built-in locking (such as Terraform's state locking) does not prevent this — locking only stops two people applying *simultaneously*, not two people applying *different, divergent versions of the code* one after another.

The fix is that code for any given shared instance should always be applied from the same place — not by designating one person's workstation (a risky single point of failure), but by using a central service that pulls code from the source or artifact repository and applies it, imposing a clear, controlled, and auditable record of which version was applied when. This is exactly the role an [infrastructure delivery pipeline](infrastructure-delivery-pipeline.md) plays; using a central service also forces genuine end-to-end automation, since there's no workstation to quietly do a manual pre- or post-step on.

[Personal infrastructure instances](personal-infrastructure-instances.md) are the deliberate exception: applying code locally is safe and useful there precisely because nobody else depends on that instance.
