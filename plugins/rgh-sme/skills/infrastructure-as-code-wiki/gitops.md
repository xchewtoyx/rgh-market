---
type: concept
title: GitOps
description: A variation of Infrastructure as Code that treats a source branch as the continuously-reconciled source of truth for an environment, applying code by merging rather than by triggering discrete pipeline runs.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 8, ch. 20"
---

GitOps combines [defining everything as code](define-everything-as-code.md) with [continuously applying code](continuous-configuration-synchronization-pattern.md): rather than an explicit pipeline stage triggering an apply when code changes, a service continuously compares each environment against the code in its corresponding source branch and reconciles any difference — reducing [configuration drift](configuration-drift.md) by construction, since divergence is corrected automatically and frequently rather than only when someone happens to run the tool.

GitOps promotes code between environments by merging it to environment-specific branches, and it discourages packaging code into delivery artifacts (see [packaging infrastructure code as an artifact](organizing-infrastructure-repositories.md)) in favor of using the branch itself as the promoted unit. It doesn't prescribe a testing strategy — it's compatible with running a full [delivery pipeline](infrastructure-delivery-pipeline.md) ahead of the merge, but doesn't require one.

A common failure mode is adopting only the branches-per-environment half of GitOps without the continuous-synchronization half: without a service actively reconciling each branch against its environment, teams tend to fall back into ad hoc changes and the same drift the [copy-paste environments antipattern](copy-paste-environments-antipattern.md) produces, since editing code as part of "promoting" it to a branch reintroduces exactly the risk continuous synchronization exists to remove.
