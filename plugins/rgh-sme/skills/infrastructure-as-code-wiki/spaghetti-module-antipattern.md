---
type: concept
title: "Antipattern: Spaghetti Module"
description: A module, written in a declarative language, so heavily parameterized with conditionals that it produces significantly different infrastructure depending on inputs and becomes hard to understand, test, or safely change.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 16"
---

A spaghetti module is configurable to the point that it produces significantly different results depending on the parameters passed to it, implemented with enough nested conditionals and switches that the code is hard to follow and reason about. It usually starts life as a well-intentioned [facade](facade-module-pattern.md) or [bundle module](bundle-module-pattern.md) that grew, one seemingly-reasonable extension at a time, to cover use cases that looked similar on the surface but actually diverged — for instance a module that decides between Java, .NET, or PHP application infrastructure, and optionally a database, all through switch statements, based on caller-supplied parameters.

This is the failure mode that most often results from trying to build an [infrastructure domain entity](infrastructure-domain-entity-pattern.md) using a declarative language rather than an imperative one — [declarative languages](declarative-vs-imperative-infrastructure-code.md) simply aren't a good fit for expressing meaningfully divergent logic, and forcing them to do so produces code that's hard to test (a direct sign, per the [testability rationale for good design](infrastructure-component-coupling-and-cohesion.md), that the module's coupling and cohesion have gone wrong) and hard to change safely.

The fix is usually to decompose the spaghetti module into several smaller, more focused modules — for example, splitting a single application-infrastructure module that branches on application type and optional database into a `java-application-servers` module and a separate `mysql-database` module, wired together where the caller actually needs both — or to rewrite the dynamic parts as an imperative library following the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md).
