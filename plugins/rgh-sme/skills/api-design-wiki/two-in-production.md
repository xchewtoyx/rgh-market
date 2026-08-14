---
type: concept
title: Two in Production
description: >
  A lifecycle policy keeping a bounded number of API versions deployed
  concurrently so clients migrate on their own schedule while provider effort
  stays capped.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

**Two in production** runs two (or **N in production**) [version identifiers](version-identifier.md)
side by side, retiring the oldest when a new major ships. Clients observe
changes on the prior version before cutover; providers make bolder breaking
changes in the new line without stranding everyone simultaneously.

Requires distinct version markers on the wire and in the
[API description](api-description.md)/[SLA](service-level-agreement-as-contract.md).
Redirect or reject traffic to retired versions (HTTP redirection is common).
Compatible patch-level updates within a major may replace in place per
[semantic versioning](semantic-versioning-api.md).

Unlike [limited lifetime guarantee](limited-lifetime-guarantee.md), removal
timing is tied to the **next** release — harder to plan in isolation unless
patterns combine. Layer [aggressive obsolescence](aggressive-obsolescence.md)
to force migration off one slot. An [experimental preview](experimental-preview.md)
may occupy one of the N slots.

Major bumps on long-running [processing resources](processing-resource.md) may
require migrating in-flight process instances, not just schema and code.
