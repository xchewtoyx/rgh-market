---
type: concept
title: "Pattern: Service Stack"
description: Managing the infrastructure for each deployable application component in its own dedicated stack, aligning infrastructure boundaries to service boundaries.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 5"
---

The service stack pattern gives each application or service its own [infrastructure stack](infrastructure-stack.md), so the stack boundary matches the software boundary. This limits the [blast radius](blast-radius.md) of any change to the one service it belongs to, simplifies scheduling changes, and lets an autonomous service team own its infrastructure end to end — it pairs naturally with a microservices application architecture.

The trade-off is duplication: if every service stack provisions its own application server, networking, and similar boilerplate, that code — and the inconsistency risk that comes with duplicated code — is repeated across every stack. This is usually mitigated by sharing code through [modules](infrastructure-domain-specific-languages.md), accepting the coupling that shared modules introduce in exchange for less duplication.

Service stack sits between the [application group stack](application-group-stack-pattern.md) pattern (multiple services, one stack) and the [micro stack](micro-stack-pattern.md) pattern (one service, multiple stacks) on the sizing spectrum, and is a common target when breaking apart a [monolithic stack](monolithic-stack-antipattern.md).
