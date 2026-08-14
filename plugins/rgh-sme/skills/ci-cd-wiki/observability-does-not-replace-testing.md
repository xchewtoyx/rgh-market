---
type: concept
title: Observability Does Not Replace Pre-Deployment Testing
description: >
  Investing in production observability does not reduce the need for
  automated pre-deployment testing — distributed-system complexity makes
  catching defects before deployment more important, not less, even with
  excellent runtime instrumentation.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Observability Does Not Replace Pre-Deployment Testing

A tempting but mistaken inference: "we have excellent production
observability now, so we can afford to test less before deploying." The
argument against it: production incidents remain costly and hard to debug
even with excellent instrumentation, and the complexity that comes with
distributed systems makes pre-deployment correctness testing of individual
services *more* valuable, not less — observability tells you something went
wrong and helps you find where, but it doesn't prevent the wrongness from
reaching users in the first place. Without automated testing, as Gary Gruver
put it, "the more code we write, the more time and money is required to test
our code" manually — an unscalable model regardless of how good the
observability stack is.

The two capabilities are complementary, not substitutes: the
[deployment pipeline](deployment-pipeline.md)'s test gates
([commit stage](commit-stage.md),
[automated acceptance testing](automated-acceptance-testing.md),
[nonfunctional test gate](nonfunctional-test-gate.md)) exist to catch what
can be caught before release; observability exists to catch and diagnose
whatever gets through anyway. Cutting investment in one because the other
improved trades a cheap, fast feedback loop for an expensive, slow one.
