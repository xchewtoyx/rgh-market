---
type: concept
title: "Pattern: Resource Matching"
description: A consumer stack discovering a provider stack's resource by looking for infrastructure that matches a naming pattern, tag, or other identifying characteristic, rather than a hardcoded reference.
sources:
  - title: Infrastructure as Code
    resource: "Infrastructure as Code (Kief Morris), ch. 17"
---

Resource matching discovers a dependency across [stacks](infrastructure-stack.md) by looking for infrastructure that matches an expected name pattern, tag, or other attribute — for example, a consumer stack referencing `vlan-appserver-${ENVIRONMENT_NAME}`, relying on the provider stack having named its VLAN that way for each environment. This is a big improvement over hardcoding a specific resource identifier directly into consumer code, which creates very tight coupling and makes it impossible to test the consumer without a live instance of the exact provider.

It's straightforward to implement with most stack tools and languages, and it doesn't require the provider and consumer to use the same tool — a real advantage in larger organizations where different teams use different tooling, and it keeps the option open to adopt new tools later without breaking existing integrations. The trade-off is that the matching pattern itself becomes an implicit contract the moment a consumer relies on it: if the provider team changes the naming convention, every consumer depending on the old pattern breaks silently. Provider teams need to treat whatever matching pattern they expose as a genuine, communicated interface, not an implementation detail they're free to change.

Resource matching is one of three patterns for [discovering dependencies across stacks](stack-data-lookup-pattern.md) covered alongside [stack data lookup](stack-data-lookup-pattern.md) and [integration registry lookup](integration-registry-lookup-pattern.md); all three can be combined with [dependency injection](dependency-injection-for-infrastructure.md) to keep the discovery mechanism out of a stack's core definition code.
