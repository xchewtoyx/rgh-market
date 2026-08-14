---
type: concept
title: Continuous Deployment vs. Continuous Delivery
description: >
  Continuous delivery guarantees every change is releasable on demand;
  continuous deployment additionally removes the human decision to actually
  push each releasable change to production.
sources:
  - title: "Continuous Delivery"
    resource: "Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation (Humble, Farley), ch. 10"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 25"
  - title: "Serverless Design Patterns and Best Practices"
    resource: "Serverless Design Patterns and Best Practices (Zambrano), ch. 9"
---

# Continuous Deployment vs. Continuous Delivery

**Continuous delivery** is the property that every change which passes the
[deployment pipeline](build-once-promote-artifact.md)'s automated gates is
proven to be in a releasable state — it *could* go to production right now,
on demand, with a single manual trigger. More concretely, continuous
delivery is the continuous assembling of [release
candidates](build-once-promote-artifact.md), followed by promotion and
testing of those candidates through a series of environments — sometimes
reaching production and sometimes not. **Continuous deployment** goes one
step further: every change that passes those same gates is pushed to
production automatically, with no manual trigger at all.

The difference is entirely about who or what pulls the trigger, not about
pipeline rigor — both models require the same automated build, test, and
verification confidence, because continuous deployment has no manual
checkpoint left to catch what the pipeline missed. Continuous deployment is
therefore a strictly stronger claim about the pipeline's trustworthiness: an
organization that isn't confident enough in its automated gates to let them
deploy unattended should stay at continuous delivery and keep the manual
release trigger, rather than automating past a safety margin it hasn't
earned.

**Continuous delivery** (in the broader sense) is also the practice of
automating so that fixing a bug and getting that fix safely to production
is as fast and handoff-free as possible — whether or not every merge
auto-deploys. Build the pipeline so [continuous deployment](continuous-deployment-vs-continuous-delivery.md)
*is possible*; enabling it remains a team choice, often via a [branch
gated deploy workflow](branch-gated-deploy-workflow.md).

[Decoupling deployment from release](decoupling-deployment-from-release.md)
is what makes continuous deployment tolerable even for user-facing changes
that need a business-controlled rollout: the code lands in production
automatically, but a flag or gated release step still controls when users
see it.

Much of continuous delivery's value comes from having the *structures* in
place — robust documented process, real-time user-satisfaction and
product-health metrics, coordinated launch policies — even when max cadence
isn't used every day. Prerequisites named in practice: binaries
configurable in production, configuration managed like code in version
control, and toolchain support for dry-run verification,
[rollback vs. roll-forward](rollback-vs-roll-forward.md), and reliable
patching.
