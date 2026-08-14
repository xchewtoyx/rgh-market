---
type: concept
title: Integration Hell
description: >
  The prolonged, painful period at the end of a release cycle where long-lived,
  divergent branches are merged all at once, producing large merge conflicts,
  broken builds, and hard-to-isolate bugs.
sources:
  - title: Continuous Delivery
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 3"
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook (Kim, Humble, Debois, Willis, Forsgren), ch. 11"
---

# Integration Hell

Integration hell is what happens when integration is treated as a discrete,
deferred activity instead of a continuous one: developers work for an extended
period on separate branches, and when it's finally time to ship, all of those
branches have to be merged and made to work together at once. Because the
divergence has been accumulating for weeks or months, the resulting merge
conflicts are large, the interactions between changes are unfamiliar to
everyone, and defects introduced by the merge itself are hard to attribute to
any single change.

This is the direct consequence of skipping
[trunk-based development](trunk-based-development.md): the fix is not to
merge more carefully, but to integrate continuously (see
[continuous integration](continuous-integration.md)) so there is never a large
backlog of divergence to resolve in the first place. This is also an instance
of the general principle to
[bring the pain forward](bring-the-pain-forward.md) — integration is painful
in proportion to how long it's deferred, so doing it constantly in small
increments keeps it cheap.

## A subtler cost: reluctance to refactor

Beyond the direct cost of resolving conflicts, painful merging makes teams
reluctant to refactor at all, since a refactor touching shared code is more
likely to collide with everyone else's in-flight branches. This is
particularly damaging because the code most in need of refactoring — code
with dependencies reaching throughout the codebase — is also exactly the code
whose branches are most likely to conflict, so the parts of the system that
most need improvement become the parts least likely to get it. Left
unaddressed, this is how technical debt compounds: each avoided refactor
makes the next change slightly harder, which makes refactoring slightly more
avoided.
