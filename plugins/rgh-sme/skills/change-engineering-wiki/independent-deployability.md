---
type: concept
title: Independent Deployability
description: >
  The ability to deploy and release an individual service on demand,
  independently of other services it depends on, which is the architectural
  precondition for safe progressive delivery.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 5"
---

# Independent Deployability

Independent deployability is the capability of a loosely coupled
architecture to deploy and release an individual service on demand, without
requiring synchronized deployment of other services it depends on. Empirical
DORA data ties two architectural anti-patterns to low delivery performance:
custom software outsourced to third parties, and systems that must be
deployed simultaneously as a single monolithic block.

It matters for change engineering because every progressive-delivery
technique — [canary release](canary-release.md),
[blue-green deployment](blue-green-deployment.md),
[rolling deployment](rolling-deployment.md) — depends on being able to run
two versions of *one* service side by side without forcing a coordinated,
fleet-wide cutover. A system that can only be deployed as one indivisible
unit cannot canary: there is no smaller unit to route a fraction of traffic
to.

Independent deployability is what makes [working in small batches](working-in-small-batches.md)
possible at the service level, not just at the code-change level — a team
can ship its own small batches on its own schedule only if it isn't blocked
on coordinating a joint release with every service it talks to.

Not every cross-service dependency can be architected away, though — for
the changes that still cross a shared boundary despite independent
deployability, see [communication checklist for cross-team
changes](communication-checklist-for-cross-team-changes.md) for the
process-level backstop. For components that are genuinely too tightly
coupled to decouple at all, see [release atomicity and tuple
testing](release-atomicity-tuple-testing.md) for the fallback of testing
and deploying a named version combination as a single atomic unit.
