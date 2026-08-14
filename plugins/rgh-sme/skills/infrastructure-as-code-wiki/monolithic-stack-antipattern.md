---
type: concept
title: "Antipattern: Monolithic Stack"
description: An infrastructure stack that has grown to include too many unrelated elements, making changes to it slow, risky, and hard to coordinate across the people who need to work on it.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

A monolithic stack is an [infrastructure stack](infrastructure-stack.md) that includes so many elements that it becomes difficult to maintain. It's usually not deliberate: the simplest way to add a new element is to add it to the existing project, and a single stack is genuinely simpler to manage while a system is small.

Symptoms that a stack has become a monolith: it's hard to understand how its pieces fit together; new people take a long time to learn its codebase; debugging problems in it is hard; changes to it frequently cause problems; and disproportionate time goes into managing the complexity of the stack rather than using it. The clearest tell is how many people routinely work on changes to it at once — the more common that multiple people (or worse, multiple teams) are working on the same stack simultaneously, the more time goes into coordinating conflicting changes, and the more likely the team resorts to long-lived feature branches, which in turn slow down CI and erode build discipline.

The underlying cost is [blast radius](blast-radius.md): a larger stack means more can go wrong with any given change, the impact of a failure is broader, and provisioning and updating the whole thing is slower — all of which push teams toward larger, less frequent changes and rising technical debt, the opposite of what [optimizing for continuous change](optimizing-infrastructure-for-continuous-change.md) calls for.

The antidote is splitting the stack using one of the sizing patterns on the spectrum away from monolith — the [application group stack](application-group-stack-pattern.md), [service stack](service-stack-pattern.md), or [micro stack](micro-stack-pattern.md) pattern — chosen according to [how you draw boundaries between infrastructure components](drawing-boundaries-between-infrastructure-components.md).
