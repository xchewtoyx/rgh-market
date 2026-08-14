---
type: concept
title: Andon Cord Discipline
description: >
  Treating any deployment-pipeline break as an event that halts new work
  until fixed — echoing the Toyota Andon cord — because a broken pipeline
  left unfixed compounds into unreliable tests, abandoned commits, and a
  return to big-bang releases.
sources:
  - title: The DevOps Handbook (2nd ed.)
    resource: "The DevOps Handbook: How to Create World-Class Agility, Reliability, and Security in Technology Organizations (Kim, Humble, Debois, Willis, Forsgren), ch. 10"
---

# Andon Cord Discipline

Named for the Toyota Production System practice of giving any assembly-line
worker the authority to stop the whole line the moment they spot a defect.
Applied to a [deployment pipeline](deployment-pipeline.md): any change that
breaks the build or tests blocks new work from proceeding until it's fixed,
and anyone can pull the cord — at minimum by notifying the team; some teams
configure version control to physically block further commits until the
[commit stage](commit-stage.md) is green again. Any team member should be
empowered to roll back a bad commit to restore green, not just the person who
introduced it (this is why understanding the rollback process well enough to
execute it under pressure — see
[rollback and roll-forward](rollback-and-roll-forward.md) — matters as a
team-wide skill, not a specialist one).

## The failure cascade without it

If the cord isn't pulled: someone breaks the build and it isn't fixed; more
commits land on top of the broken state, and their own new failures go
unseen underneath the existing one; the accumulated noise makes the test
suite feel unreliable, so people stop bothering to write new tests ("why
bother, we can't even get the current ones to run"). The end state is
functionally indistinguishable from having no automated testing at all —
deployments become unpredictable, problems surface in production, and the
team lands back in a large, unplanned stabilization phase. This is the same
degenerative loop [integration hell](integration-hell.md) describes, applied
specifically to test-suite trust rather than branch divergence.

## Differentiated response by stage

A [commit stage](commit-stage.md) break stops everyone, because it's fast to
fix and blocks the entire team's flow. A break discovered at a later,
slower stage ([automated acceptance testing](automated-acceptance-testing.md),
[nonfunctional test gate](nonfunctional-test-gate.md)) doesn't need to halt
all new work — a dedicated on-call person fixes the specific problem, and
critically, backfills a faster test that would have caught it earlier next
time (see
[write a regression test for every production bug](regression-test-for-every-bug.md)).

## Why this is the harder half

Building the automated test/build infrastructure is a purely technical
problem. Making the team actually stop and fix a break immediately, every
time, without exceptions creeping in under deadline pressure, is a behavioral
and cultural one — and is reported as the harder of the two to sustain.
