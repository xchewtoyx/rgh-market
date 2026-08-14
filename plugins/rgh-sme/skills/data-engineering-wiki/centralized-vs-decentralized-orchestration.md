---
type: concept
title: Centralized vs. Decentralized Orchestration Ownership
description: >
  Whether one shared orchestrator coordinates every team's pipelines or each
  team runs its own, and the gatekeeping-vs-coordination-cost trade-off
  between them.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 9"
---

Once an organization has multiple teams each building pipelines, someone has
to decide whether [orchestration](orchestration-vs-scheduling.md) is one
shared platform or many independent ones:

- **Centralized orchestration** puts every team's pipelines in one shared
  orchestrator. Coordination is easy — one team can directly depend on
  another team's task completing — but it concentrates risk: one poorly
  written DAG failing or hanging can bring down processing and serving
  organization-wide, not just for the team that wrote it. This is only safe
  with real gatekeeping discipline — automated DAG testing and deployment
  standards (see [pipelines as code](pipelines-as-code.md)) — high enough
  that the shared platform doesn't become the single point of failure for
  every team's work at once.
- **Decentralized orchestration** lets each team manage its own pipeline
  flows independently, which reduces that blast radius and lets teams move
  at their own pace. The cost shifts to cross-team coordination: teams can no
  longer simply trigger another team's tasks within one shared DAG and
  instead have to pass messages or poll across system boundaries, which is
  slower and more error-prone to build correctly.

Neither is a free win — centralization trades autonomy for coordination ease
and concentrates failure risk; decentralization trades coordination ease for
autonomy and isolated failure domains. Where a centralized platform is
chosen, natural ownership tends to fall to whichever team has the most
holistic cross-lifecycle view (often a dedicated DataOps team, or the team
closest to serving), since that team is best positioned to enforce the
gatekeeping standards the model depends on.
