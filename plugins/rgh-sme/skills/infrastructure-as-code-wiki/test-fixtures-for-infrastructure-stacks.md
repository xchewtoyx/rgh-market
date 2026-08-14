---
type: concept
title: Test Fixtures for Infrastructure Stacks
description: Using purpose-built infrastructure — test doubles standing in for a stack's upstream or downstream dependencies — to test a stack in isolation, without needing running instances of every stack it depends on.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 9"
---

Many [stacks](infrastructure-stack.md) depend on resources created by other stacks — a shared networking stack that an application stack's servers attach to. A test fixture is additional infrastructure created purely to support testing a stack on its own, standing in for a dependency so you don't need a full instance of every stack it touches. A dependency is *upstream* if the stack under test consumes resources from it, or *downstream* if other stacks consume resources from the stack under test; the stack providing resources is the *provider*, the one consuming them is the *consumer* — the same stack can be both, depending on direction.

For an upstream dependency, a fixture typically means creating just the specific resource needed (an address block) rather than a full instance of the provider stack, which usually carries extra production-only concerns (auditing, stricter policies) that are unnecessary overhead for a test and would also couple the test to the provider stack's own release cadence. For a downstream dependency, the fixture is typically a minimal consumer (for example, a bare container instance) placed where a real consumer would sit, so the provider stack's outcomes — can this segment actually route traffic where it should — can be verified without a full real consumer.

If a component can't be cleanly isolated with a fixture, that's a signal about the design, not the tests: dependencies that are hardcoded or too tangled to isolate indicate the components are too tightly coupled, and the fix is usually to refactor toward the loose coupling described in [drawing boundaries between infrastructure components](drawing-boundaries-between-infrastructure-components.md), not to give up on isolating the test. Test fixtures are what makes [progressive testing](progressive-testing-for-infrastructure.md)'s early, narrow-scoped stages possible at all, and they underpin [dependency injection for infrastructure](dependency-injection-for-infrastructure.md), which decouples a stack's definition code from however its dependencies get discovered.
