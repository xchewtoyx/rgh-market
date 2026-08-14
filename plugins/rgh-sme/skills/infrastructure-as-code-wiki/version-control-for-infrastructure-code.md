---
type: concept
title: Version Control for Infrastructure Code
description: The specific benefits version-controlling infrastructure code provides — traceability, rollback, correlation, visibility, and actionability — and the rule against storing secrets in it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 4"
---

Once infrastructure is [defined as code](define-everything-as-code.md) in externalized files, putting that code into a version control system delivers benefits beyond simple backup:

- **Traceability** — a history of every change, who made it, and (given decent commit messages) why, invaluable when debugging.
- **Rollback** — the ability to restore exactly the prior state after a change breaks something.
- **Correlation** — tags and version numbers let you correlate changes across files and projects when tracing a problem.
- **Visibility** — everyone can see every committed change, giving the team situational awareness; someone may spot a missed consideration, or recognize a recent commit as the likely cause of an incident.
- **Actionability** — the VCS can trigger automation on every commit, which is what enables CI and CD pipelines to exist at all.

The one thing that must never go into version control is an unencrypted secret — passwords, keys, tokens. Even a private repository leaks secrets too easily through history, forks, and backups; leaked secrets in source code are one of the most common causes of security breaches. See [handling secrets in infrastructure code](handling-secrets-in-infrastructure-code.md) for the alternatives.

Version control is also the foundation for [GitOps](gitops.md), which treats a source branch as the single source of truth that infrastructure is continuously reconciled against.
