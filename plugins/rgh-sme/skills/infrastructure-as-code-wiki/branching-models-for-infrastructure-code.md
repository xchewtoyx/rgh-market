---
type: concept
title: Branching Models for Infrastructure Code
description: The trade-off between short-lived feature branches with PR review and trunk-based development with frequent small merges, applied to infrastructure codebases specifically.
sources:
  - title: Infrastructure as Code Patterns and Practices
    resource: "Infrastructure as Code, Patterns and Practices (Rosemary Wang), ch. 7"
---

**Feature branching** isolates each change in a short-lived branch, with CI running against the branch and peer review happening on the pull request before it merges to the main line. This gives a clear isolation boundary for unverified work and a natural point for review, but a branch that lives too long accumulates merge drift against a moving main line, and the longer it lives, the more that drift compounds.

**Trunk-based development** has everyone merge small, frequent commits directly to the main line — the same [integration frequency](team-workflow-effectiveness.md) discipline that the [four key delivery metrics](four-key-delivery-metrics.md) research associates with higher-performing teams — guarding any incomplete work behind [feature flags](feature-toggles-for-infrastructure.md) or configuration parameters rather than an unmerged branch. This eliminates branch drift and merge debt entirely, but it depends on genuinely solid automated test coverage and a reliable sandbox environment, since there's no long-lived branch acting as a safety buffer between an author's work and the shared codebase.

Whichever model a team uses, peer review is most valuable when it's reserved for what automation genuinely can't check — system architecture, [blast radius](blast-radius.md), and dependency impact — with style, formatting, and syntax validation offloaded entirely to CI linters and static checks, so human reviewers aren't spending their attention on things a machine already caught. Pair programming (a driver and a navigator co-authoring the same change in real time) is a complementary, more immediate form of review that catches logic errors as code is written and spreads institutional knowledge of the codebase faster than after-the-fact code review does. [GitOps](gitops.md) is the delivery-side counterpart to these branching choices — however code gets merged, GitOps is specifically about the *main* branch being continuously and automatically reconciled against running infrastructure once a change lands there.
