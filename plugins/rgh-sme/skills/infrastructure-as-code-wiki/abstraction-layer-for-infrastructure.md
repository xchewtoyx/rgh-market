---
type: concept
title: Abstraction Layer for Infrastructure
description: A set of reusable, composable stack components that let teams work with higher-level infrastructure concepts instead of assembling low-level platform resources directly, without hiding the underlying implementation from those who need to see it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 16"
---

An abstraction layer provides a simplified interface to lower-level infrastructure resources, so that people focused on a higher-level task — an application team defining an environment with a server, database, and message-queue access — don't need to personally assemble every routing rule and permission an infrastructure specialist would. Even teams with the skills to work at the low level benefit from an abstraction layer, since it separates concerns and lets each person focus at the level of detail relevant to their task, while still being able to drill down into the underlying components when they need to extend or debug them.

An abstraction layer's components are usually built with a [low-level infrastructure language](low-level-vs-high-level-infrastructure-languages.md) underneath, but exposed through a [high-level language](low-level-vs-high-level-infrastructure-languages.md) that specifies application-runtime requirements. Simple, largely static cases can be served by [facade](facade-module-pattern.md) or [bundle modules](bundle-module-pattern.md); layers that need to flex meaningfully by use case are usually built from [infrastructure domain entities](infrastructure-domain-entity-pattern.md) written in an imperative language.

An abstraction layer can emerge organically as teams build libraries piecemeal, but it benefits from an explicit, higher-level design so its components fit together as a coherent system rather than a loose grab-bag — this is one of the things a "toolmaker" role, as distinct from a "builder" or "user" role, is often responsible for in a team's [workflow](team-workflow-effectiveness.md).
