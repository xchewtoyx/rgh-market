---
type: concept
title: Minimize Variation Principle
description: The design principle that infrastructure is easier to manage when it is composed of fewer distinct types of pieces, since work grows with both the number of pieces and the number of different kinds of pieces.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 2"
---

As a system grows, the effort to understand, change, and fix it grows with the number of components — but it grows faster with the number of distinct *types* of components. It's easier to manage one hundred identical servers than five completely different ones, because each additional type of operating system, application runtime, database, or package version requires its own knowledge, tooling, and testing.

This complements the [reproducibility principle](reproducibility-principle.md): if you define one simple component and create many identical instances of it, that component is easy to understand, change, and fix — but only if every instance actually receives every change. Applying a change to some instances and not others is exactly how [configuration drift](configuration-drift.md) starts.

Common sources of unwanted variation include running multiple operating systems, application runtimes, or databases where one would do; running multiple versions of the same software; and letting package versions diverge across servers over time. Organizations must balance this against the legitimate need for different teams to choose technologies suited to their own needs — minimizing variation is a tension to manage deliberately, not an absolute rule.
