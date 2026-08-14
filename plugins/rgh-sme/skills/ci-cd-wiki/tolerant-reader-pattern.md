---
type: concept
title: Tolerant Reader Pattern
description: >
  API and message consumers should ignore unknown or unexpected fields rather
  than failing on them, so a producer can add new fields without that change
  becoming a breaking one for existing consumers.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd ed. (Nygard), ch. 14"
---

# Tolerant Reader Pattern

Named for Postel's Law ("be conservative in what you send, liberal in what
you accept"). A consumer of an API response, event payload, or message that
strictly validates the exact shape it expects — rejecting anything with an
extra or unrecognized field — turns every additive change on the producer
side into a breaking change for that consumer, even though the change didn't
remove or alter anything the consumer actually uses. Building consumers to
ignore unknown fields instead means a producer can add new fields (new
JSON properties, new optional parameters, new response data) freely, without
needing to coordinate a simultaneous release with every consumer.

## Why this matters for independent deployability

This is a precondition for [independent deployability](independent-deployability.md):
a producer can only release a purely additive change on its own schedule if
every consumer already tolerates additive changes. Consumers that behave this
way turn "add a new field" into a genuinely non-breaking change; consumers
that don't turn every producer release into a de facto coordinated
multi-service release, defeating the point of splitting services apart in
the first place.

This complements, rather than replaces, explicit versioning for changes that
really are breaking — see
[API version coexistence](api-version-coexistence.md) for how to handle
those.
