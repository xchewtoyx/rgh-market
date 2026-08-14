---
type: concept
title: "Pattern: Bundle Module"
description: A declarative module that packages a cohesive collection of related infrastructure resources — centered on one core resource — behind a simplified interface.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 16"
---

A bundle module declares several related resources together — typically a core resource plus the supporting pieces it usually needs, such as a server cluster plus its load balancer and DNS entry — behind one simplified interface. It's the multi-resource extension of the [facade module pattern](facade-module-pattern.md): where a facade wraps one resource, a bundle wraps a cohesive group, capturing the knowledge of how those pieces get wired together for a recurring purpose and avoiding verbose, repeated boilerplate every time that purpose recurs.

Like a facade module, a bundle module fits a declarative language best when the resources it creates don't vary much between uses; if you find yourself needing the module to create meaningfully different resources depending on parameters, that's a sign to either split it into separate, narrower modules, or to switch to an imperative language and use the [infrastructure domain entity pattern](infrastructure-domain-entity-pattern.md) instead. The risk with a bundle module is provisioning more than a given caller actually needs — users need to understand what it creates and avoid reaching for it when it's overkill for their case.

A bundle module that's been stretched with conditionals to handle significantly divergent parameter combinations, rather than being kept to a fairly static set of resources, degrades into the [spaghetti module antipattern](spaghetti-module-antipattern.md).
