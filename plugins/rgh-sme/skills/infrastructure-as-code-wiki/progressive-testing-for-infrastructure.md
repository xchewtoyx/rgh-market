---
type: concept
title: Progressive Testing for Infrastructure
description: Running infrastructure test suites in a sequence from fast, narrow-scoped, offline checks toward slower, broad, online checks, so failures surface at the smallest possible scope.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 8, ch. 9"
---

Progressive testing runs multiple test suites in a deliberate sequence: faster tests with a narrower scope and fewer dependencies first, then tests that add more integrated components and platform dependencies. When a broadly-scoped test fails, there's a large surface of components and dependencies to investigate, so the goal is to catch any given risk at the earliest, narrowest-scoped stage that can feasibly catch it — see [offline and online stack test stages](test-fixtures-for-infrastructure-stacks.md) for the specific offline/online split this maps onto in an [infrastructure delivery pipeline](infrastructure-delivery-pipeline.md).

The classic *test pyramid* (many fast unit tests, fewer integration tests, fewest end-to-end tests) was devised for application code and translates awkwardly to declarative infrastructure: most low-level stack code is too coarse-grained for unit testing and depends on the platform to mean anything, and [testing declarative code](testing-declarative-infrastructure-code.md) usually has low value at that grain. The result tends to look more like a diamond — relatively few offline/unit-level tests, a bulk of mid-level integration tests, and few full end-to-end tests — unless the codebase leans heavily on imperative libraries (see the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md)), which reintroduces enough variable behavior to make the pyramid shape relevant again.

The *Swiss cheese model* offers a complementary way to think about a whole progressive suite: any one layer of testing has gaps, like holes in a slice of cheese, but stacking several layers means no hole should go all the way through. The point isn't to catch every risk at the earliest possible layer at all costs, only to be sure it's caught *somewhere* in the overall model — testing should be driven by risk, not by mechanically fitting every check into a formula. Avoid duplicating the same check at multiple layers; a check that belongs to a narrow-scoped stage shouldn't be repeated in a broader one. See also [testing infrastructure in production](testing-infrastructure-in-production.md) for the risks progressive pre-production testing cannot cover at all.
