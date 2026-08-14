---
type: concept
title: API Design Recurring Trade-offs
description: >
  Five recurring endpoint and contract dimensions — specificity, granularity,
  richness, freshness, and stability — that designers balance on every API surface.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 1"
---

API designs differ along recurring axes. None has a universal winner — context and
[architecturally significant API requirements](architecturally-significant-api-requirements.md)
pick the point on each spectrum:

| Trade-off | One pole | Other pole |
| --- | --- | --- |
| Endpoint scope | One general, reusable surface | Many specialized endpoints |
| Operation grain | Fine-grained (match, split backend capability) | Coarse-grained (aggregate, match client task) |
| Operation count | Few rich, self-contained operations | Many narrow, chatty calls |
| Data freshness | Stale-but-available reads | Strong correctness / consistency |
| Contract change rate | Stable, backward-compatible evolution | Fast-moving, extensible surface |

Freshness choices interact with integration style: polling versus event-driven or
streaming updates, and command/query separation. Stability choices interact with
[backward compatibility policy](backward-compatibility-policy.md) and
[versioning strategy trade-offs](versioning-strategy-tradeoffs.md).

[Endpoint operation design challenges](endpoint-operation-design-challenges.md)
applies these forces to concrete endpoint and operation placement; [remote API domain model](remote-api-domain-model.md)
names **granularity** and **coupling** as the abstract pair behind many rows.
