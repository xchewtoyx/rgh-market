---
type: concept
title: "Antipattern: Copy-Paste Environments"
description: Maintaining a separate, independently-copied stack source project for each environment instance, which avoids one stack's blast radius problem but reliably drifts environments apart over time.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 6"
---

Copy-paste environments use a completely separate infrastructure stack source code project for each environment instance (test, staging, production), with changes made by editing one environment's code and then copying the edit into each of the others in turn. It's an intuitive way to maintain multiple environments, and it does avoid the [multiple-environment stack antipattern](multiple-environment-stack-antipattern.md)'s shared blast radius — each environment can be freely broken and rebuilt without touching the others, and each can be customized easily.

The cost is that every change needs to be manually propagated to every copy and tested separately, since a change can work in one environment's copy but not another's — and in practice, propagation is missed or delayed, so copy-paste environments reliably drift into [configuration drift](configuration-drift.md), undermining the confidence that testing in one environment says anything about another.

The fix is the [reusable stack pattern](reusable-stack-pattern.md): a single stack project applied to multiple instances, so every environment is guaranteed to be running the same code rather than a hand-copied variant of it. Using environment branches in source control to hold each environment's variant is a variation of this same antipattern, since it still requires editing and merging a copy per environment; [continuously applying code](gitops.md) rather than editing it as part of promotion avoids that pitfall.
